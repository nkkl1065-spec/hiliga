

import os
import requests
import urllib.parse
from bs4 import BeautifulSoup
import time
import re
from pathlib import Path
import json
import threading
from concurrent.futures import ThreadPoolExecutor
import ssl
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import hashlib

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BrutalWebsiteCloner:
    def __init__(self, base_url, output_dir="cloned_website", max_workers=20):
        self.base_url = base_url.rstrip('/')
        self.domain = urllib.parse.urlparse(base_url).netloc
        self.output_dir = output_dir
        self.visited_urls = set()
        self.downloaded_files = set()
        self.failed_urls = set()
        self.all_found_urls = set()
        self.max_workers = max_workers
        
        # Create output directory
        Path(self.output_dir).mkdir(exist_ok=True)
        
        # Setup brutal session
        self.setup_brutal_session()
        
        # Setup Selenium for JS-heavy sites
        self.setup_selenium()
        
        self.lock = threading.Lock()
    
    def setup_brutal_session(self):
        """Setup session yang sangat agresif"""
        self.session = requests.Session()
        
        # Brutal headers to bypass security
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8,es;q=0.7,fr;q=0.6',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'Pragma': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': self.base_url,
            'Origin': self.base_url,
        })
        
        # Disable SSL verification
        self.session.verify = False
        
        # Setup adapters with retries
        adapter = requests.adapters.HTTPAdapter(
            max_retries=urllib3.util.Retry(
                total=5,
                backoff_factor=0.3,
                status_forcelist=[500, 502, 503, 504, 404, 403]
            )
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
    
    def setup_selenium(self):
        """Setup Selenium untuk bypass JS protection"""
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-web-security')
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')
            chrome_options.add_argument('--ignore-certificate-errors-spki-list')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-plugins')
            chrome_options.add_argument('--disable-images')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.selenium_available = True
            print("✅ Selenium WebDriver ready - JS bypass enabled")
        except Exception as e:
            print(f"⚠️ Selenium not available: {str(e)}")
            self.selenium_available = False
    
    def get_page_with_selenium(self, url):
        """Get page content using Selenium untuk bypass JS protection"""
        if not self.selenium_available:
            return None
            
        try:
            print(f"🔥 Using Selenium for: {url}")
            self.driver.get(url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Execute JS to reveal hidden content
            self.driver.execute_script("""
                // Trigger common JS events
                window.dispatchEvent(new Event('load'));
                window.dispatchEvent(new Event('DOMContentLoaded'));
                
                // Scroll to trigger lazy loading
                window.scrollTo(0, document.body.scrollHeight);
                
                // Click hidden elements
                var hiddenElements = document.querySelectorAll('[style*="display: none"], [style*="visibility: hidden"]');
                hiddenElements.forEach(function(el) {
                    el.style.display = 'block';
                    el.style.visibility = 'visible';
                });
            """)
            
            time.sleep(2)  # Wait for JS execution
            
            return self.driver.page_source
            
        except Exception as e:
            print(f"Selenium error for {url}: {str(e)}")
            return None
    
    def brutal_request(self, url, method='GET', **kwargs):
        """Request yang sangat brutal dengan multiple fallbacks"""
        methods = [
            # Method 1: Normal session
            lambda: self.session.request(method, url, timeout=30, **kwargs),
            
            # Method 2: Without SSL verification
            lambda: requests.request(method, url, verify=False, timeout=30, headers=self.session.headers, **kwargs),
            
            # Method 3: Different User-Agent
            lambda: requests.request(method, url, verify=False, timeout=30, headers={
                **self.session.headers,
                'User-Agent': 'curl/7.68.0'
            }, **kwargs),
            
            # Method 4: Mobile User-Agent
            lambda: requests.request(method, url, verify=False, timeout=30, headers={
                **self.session.headers,
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15'
            }, **kwargs),
            
            # Method 5: Googlebot
            lambda: requests.request(method, url, verify=False, timeout=30, headers={
                **self.session.headers,
                'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
            }, **kwargs),
        ]
        
        for i, method_func in enumerate(methods):
            try:
                response = method_func()
                if response.status_code == 200:
                    return response
                elif response.status_code in [301, 302, 303, 307, 308]:
                    # Follow redirects manually
                    redirect_url = response.headers.get('Location')
                    if redirect_url:
                        return self.brutal_request(redirect_url, method, **kwargs)
            except Exception as e:
                print(f"Method {i+1} failed for {url}: {str(e)}")
                continue
        
        # Last resort: Selenium
        if self.selenium_available:
            content = self.get_page_with_selenium(url)
            if content:
                # Create fake response object
                class FakeResponse:
                    def __init__(self, content):
                        self.content = content.encode('utf-8')
                        self.text = content
                        self.status_code = 200
                        self.headers = {'content-type': 'text/html'}
                
                return FakeResponse(content)
        
        return None
    
    def sanitize_filename(self, filename):
        """Sanitize filename dengan encoding yang aman"""
        # Remove/replace problematic characters
        filename = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', filename)
        filename = re.sub(r'[%]', '_', filename)
        
        # Handle unicode characters
        try:
            filename = filename.encode('ascii', 'ignore').decode('ascii')
        except:
            filename = base64.b64encode(filename.encode('utf-8')).decode('ascii')[:50]
        
        return filename[:200]
    
    def get_local_path(self, url):
        """Get local path dengan handling yang lebih robust"""
        try:
            parsed = urllib.parse.urlparse(url)
            path = urllib.parse.unquote(parsed.path.lstrip('/'))
            
            # Handle query parameters
            if parsed.query:
                query_hash = hashlib.md5(parsed.query.encode()).hexdigest()[:8]
                if path:
                    name, ext = os.path.splitext(path)
                    path = f"{name}_{query_hash}{ext}"
                else:
                    path = f"index_{query_hash}.html"
            
            if not path or path.endswith('/'):
                path += 'index.html'
            elif '.' not in os.path.basename(path):
                # Detect file type from URL pattern
                if any(keyword in path.lower() for keyword in ['css', 'style']):
                    path += '.css'
                elif any(keyword in path.lower() for keyword in ['js', 'script']):
                    path += '.js'
                elif any(keyword in path.lower() for keyword in ['img', 'image', 'pic']):
                    path += '.jpg'
                else:
                    path += '/index.html'
            
            # Sanitize path components
            path_parts = path.split('/')
            path_parts = [self.sanitize_filename(part) for part in path_parts if part]
            clean_path = '/'.join(path_parts)
            
            return os.path.join(self.output_dir, clean_path)
            
        except Exception as e:
            # Fallback: use URL hash as filename
            url_hash = hashlib.md5(url.encode()).hexdigest()
            return os.path.join(self.output_dir, f"file_{url_hash}.html")
    
    def extract_all_urls_brutal(self, content, base_url):
        """Extract URLs dengan cara yang sangat brutal"""
        found_urls = set()
        
        try:
            # 1. BeautifulSoup extraction
            soup = BeautifulSoup(content, 'html.parser')
            
            # All possible URL attributes
            url_selectors = [
                ('*', 'href'), ('*', 'src'), ('*', 'data-src'), ('*', 'data-original'),
                ('*', 'data-lazy'), ('*', 'data-url'), ('*', 'data-href'),
                ('*', 'action'), ('*', 'formaction'), ('*', 'poster'),
                ('*', 'background'), ('*', 'cite'), ('*', 'longdesc'),
                ('*', 'profile'), ('*', 'usemap'), ('*', 'classid'),
                ('*', 'data'), ('*', 'archive'), ('*', 'codebase')
            ]
            
            for tag, attr in url_selectors:
                for element in soup.find_all(attrs={attr: True}):
                    value = element.get(attr)
                    if value:
                        # Handle srcset
                        if 'srcset' in attr.lower():
                            urls = re.findall(r'(\S+)', value)
                            for u in urls:
                                if not u.endswith(('w', 'x')) and '.' in u:
                                    found_urls.add(urllib.parse.urljoin(base_url, u))
                        else:
                            found_urls.add(urllib.parse.urljoin(base_url, value))
            
            # 2. Regex patterns untuk semua kemungkinan URL
            url_patterns = [
                # Standard URLs
                r'(?:href|src|action|data-src|data-original)=["\']([^"\']+)["\']',
                # CSS URLs
                r'url\s*\(\s*["\']?([^"\']+)["\']?\s*\)',
                # JavaScript URLs
                r'["\']([^"\']*\.(?:html|htm|php|asp|aspx|jsp|css|js|json|xml|txt)(?:\?[^"\']*)?)["\']',
                # Image URLs
                r'["\']([^"\']*\.(?:jpg|jpeg|png|gif|bmp|svg|webp|ico|tiff)(?:\?[^"\']*)?)["\']',
                # Media URLs
                r'["\']([^"\']*\.(?:mp4|avi|mov|wmv|flv|webm|mp3|wav|ogg|pdf)(?:\?[^"\']*)?)["\']',
                # Path-like strings
                r'["\']([/][^"\']{2,})["\']',
                # Protocol-relative URLs
                r'["\']([//][^"\']+)["\']',
                # Relative paths
                r'["\']([^"\']*[/][^"\']*\.[\w]+)["\']',
            ]
            
            for pattern in url_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    if match and not match.startswith(('data:', 'javascript:', 'mailto:', 'tel:')):
                        full_url = urllib.parse.urljoin(base_url, match)
                        found_urls.add(full_url)
            
            # 3. Extract dari JSON embedded
            json_pattern = r'<script[^>]*>.*?({.*?}|\\[.*?\\]).*?</script>'
            json_matches = re.findall(json_pattern, content, re.DOTALL | re.IGNORECASE)
            for json_str in json_matches:
                try:
                    # Try to extract URLs from JSON-like strings
                    url_in_json = re.findall(r'["\']([^"\']*\.[\w]+(?:\?[^"\']*)?)["\']', json_str)
                    for url in url_in_json:
                        if '.' in url and not url.startswith(('data:', 'javascript:')):
                            found_urls.add(urllib.parse.urljoin(base_url, url))
                except:
                    pass
            
            # 4. Extract dari inline styles
            style_pattern = r'style=["\']([^"\']*)["\']'
            style_matches = re.findall(style_pattern, content, re.IGNORECASE)
            for style in style_matches:
                css_urls = re.findall(r'url\s*\(\s*["\']?([^"\']+)["\']?\s*\)', style)
                for css_url in css_urls:
                    found_urls.add(urllib.parse.urljoin(base_url, css_url))
            
        except Exception as e:
            print(f"Error extracting URLs: {str(e)}")
        
        return found_urls
    
    def discover_hidden_paths(self):
        """Discover hidden paths dengan brute force"""
        print("🔍 Discovering hidden paths...")
        
        common_paths = [
            # Standard paths
            '/', '/index.html', '/index.php', '/home.html', '/main.html',
            '/sitemap.xml', '/sitemap_index.xml', '/robots.txt', '/favicon.ico',
            
            # Asset directories
            '/css/', '/js/', '/images/', '/img/', '/assets/', '/static/',
            '/media/', '/files/', '/uploads/', '/download/', '/downloads/',
            
            # Common pages
            '/about/', '/contact/', '/blog/', '/news/', '/products/', '/services/',
            '/gallery/', '/portfolio/', '/team/', '/careers/', '/help/', '/faq/',
            
            # Admin and system
            '/admin/', '/administrator/', '/wp-admin/', '/wp-content/', '/wp-includes/',
            '/api/', '/ajax/', '/json/', '/xml/', '/rss/', '/feed/',
            
            # Hidden files
            '/.htaccess', '/.env', '/config.php', '/config.json', '/settings.json',
            '/backup/', '/tmp/', '/temp/', '/cache/', '/logs/',
            
            # Common file extensions
            '/style.css', '/main.css', '/app.css', '/bootstrap.css',
            '/script.js', '/main.js', '/app.js', '/jquery.js',
        ]
        
        # Add numbered variations
        for i in range(1, 11):
            common_paths.extend([
                f'/page{i}.html', f'/post{i}.html', f'/article{i}.html',
                f'/image{i}.jpg', f'/photo{i}.jpg', f'/pic{i}.jpg',
            ])
        
        found_urls = set()
        
        def check_path(path):
            test_url = self.base_url + path
            try:
                response = self.brutal_request(test_url, method='HEAD')
                if response and response.status_code == 200:
                    found_urls.add(test_url)
                    print(f"✅ Found: {test_url}")
                    return test_url
            except:
                pass
            return None
        
        # Use threading for faster discovery
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(check_path, path) for path in common_paths]
            for future in futures:
                try:
                    result = future.result(timeout=5)
                except:
                    pass
        
        return found_urls
    
    def download_file_brutal(self, url):
        """Download file dengan cara yang sangat brutal"""
        if url in self.downloaded_files:
            return True
        
        with self.lock:
            if url in self.downloaded_files:
                return True
            self.downloaded_files.add(url)
        
        try:
            print(f"🔥 Downloading: {url}")
            
            response = self.brutal_request(url)
            if not response:
                raise Exception("All brutal methods failed")
            
            local_path = self.get_local_path(url)
            
            # Create directory
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            # Determine content type
            content_type = response.headers.get('content-type', '').lower()
            
            if 'text' in content_type or 'html' in content_type or 'css' in content_type or 'javascript' in content_type:
                # Text-based files
                try:
                    content = response.text
                except:
                    content = response.content.decode('utf-8', errors='ignore')
                
                # Extract more URLs from content
                if hasattr(self, 'extraction_phase') and self.extraction_phase:
                    new_urls = self.extract_all_urls_brutal(content, url)
                    with self.lock:
                        self.all_found_urls.update(new_urls)
                
                # Post-process content
                if 'html' in content_type:
                    content = self.post_process_html_content(content, url)
                elif 'css' in content_type:
                    content = self.post_process_css_content(content, url)
                
                with open(local_path, 'w', encoding='utf-8', errors='ignore') as f:
                    f.write(content)
            else:
                # Binary files
                with open(local_path, 'wb') as f:
                    f.write(response.content)
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to download {url}: {str(e)}")
            with self.lock:
                self.failed_urls.add(url)
            return False
    
    def post_process_html_content(self, content, original_url):
        """Post-process HTML content"""
        try:
            soup = BeautifulSoup(content, 'html.parser')
            
            # Update all links to relative
            selectors = [
                ('a', 'href'), ('img', 'src'), ('link', 'href'), ('script', 'src'),
                ('iframe', 'src'), ('embed', 'src'), ('object', 'data'),
                ('source', 'src'), ('video', 'src'), ('audio', 'src'),
                ('form', 'action'), ('area', 'href'), ('input', 'src')
            ]
            
            for tag_name, attr in selectors:
                for element in soup.find_all(tag_name):
                    url = element.get(attr)
                    if url and self.is_same_domain(urllib.parse.urljoin(original_url, url)):
                        # Convert to relative path
                        full_url = urllib.parse.urljoin(original_url, url)
                        try:
                            local_path = self.get_local_path(full_url)
                            current_path = self.get_local_path(original_url)
                            rel_path = os.path.relpath(local_path, os.path.dirname(current_path))
                            element[attr] = rel_path.replace(os.sep, '/')
                        except:
                            pass
            
            return str(soup)
        except:
            return content
    
    def post_process_css_content(self, content, original_url):
        """Post-process CSS content"""
        try:
            def replace_url(match):
                url = match.group(1).strip('\'"')
                if not url.startswith(('http://', 'https://', 'data:', '//')):
                    full_url = urllib.parse.urljoin(original_url, url)
                    if self.is_same_domain(full_url):
                        try:
                            local_path = self.get_local_path(full_url)
                            current_path = self.get_local_path(original_url)
                            rel_path = os.path.relpath(local_path, os.path.dirname(current_path))
                            return f'url("{rel_path.replace(os.sep, "/")}")'
                        except:
                            pass
                return match.group(0)
            
            return re.sub(r'url\s*\(\s*["\']?([^"\']+)["\']?\s*\)', replace_url, content)
        except:
            return content
    
    def is_same_domain(self, url):
        """Check if URL is same domain"""
        try:
            parsed = urllib.parse.urlparse(url)
            return (parsed.netloc == self.domain or 
                   parsed.netloc == '' or 
                   parsed.netloc.endswith('.' + self.domain) or
                   self.domain.endswith('.' + parsed.netloc))
        except:
            return False
    
    def brutal_crawl_and_discover(self):
        """Brutal crawling dan discovery"""
        print("🔥 Phase 1: Brutal URL Discovery")
        
        self.extraction_phase = True
        
        # Start with base URL
        to_crawl = {self.base_url}
        crawled = set()
        
        # Discover hidden paths
        hidden_urls = self.discover_hidden_paths()
        to_crawl.update(hidden_urls)
        
        # Multi-level crawling
        max_depth = 10
        current_depth = 0
        
        while to_crawl and current_depth < max_depth:
            current_batch = list(to_crawl - crawled)[:100]
            to_crawl -= set(current_batch)
            crawled.update(current_batch)
            
            print(f"🕷️ Crawling depth {current_depth + 1}, batch: {len(current_batch)}")
            
            def crawl_url(url):
                if not self.is_same_domain(url):
                    return set()
                
                try:
                    response = self.brutal_request(url)
                    if response:
                        content = response.text if hasattr(response, 'text') else response.content.decode('utf-8', errors='ignore')
                        return self.extract_all_urls_brutal(content, url)
                except:
                    pass
                return set()
            
            # Parallel crawling
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = [executor.submit(crawl_url, url) for url in current_batch]
                for future in futures:
                    try:
                        discovered = future.result(timeout=30)
                        valid_urls = {u for u in discovered if self.is_same_domain(u)}
                        to_crawl.update(valid_urls)
                        self.all_found_urls.update(valid_urls)
                    except:
                        pass
            
            current_depth += 1
        
        self.all_found_urls.update(crawled)
        self.extraction_phase = False
        
        print(f"🎯 Discovery complete! Found {len(self.all_found_urls)} URLs")
    
    def brutal_download_all(self):
        """Download semua dengan brutal force"""
        print("🔥 Phase 2: Brutal Mass Download")
        
        valid_urls = [url for url in self.all_found_urls if self.is_same_domain(url)]
        
        print(f"📥 Starting brutal download of {len(valid_urls)} files...")
        
        # Parallel download dengan banyak workers
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for url in valid_urls:
                future = executor.submit(self.download_file_brutal, url)
                futures.append((url, future))
            
            completed = 0
            for url, future in futures:
                try:
                    future.result(timeout=60)
                    completed += 1
                    if completed % 5 == 0:
                        print(f"📊 Progress: {completed}/{len(valid_urls)}")
                except:
                    pass
    
    def start_brutal_cloning(self):
        """Start brutal cloning process"""
        print("🔥" * 20)
        print("🔥 BRUTAL WEBSITE CLONER ACTIVATED 🔥")
        print("🔥" * 20)
        print(f"🎯 Target: {self.base_url}")
        print(f"📁 Output: {self.output_dir}")
        print(f"⚡ Workers: {self.max_workers}")
        print("🔥" * 20)
        
        start_time = time.time()
        
        try:
            # Phase 1: Brutal Discovery
            self.brutal_crawl_and_discover()
            
            # Phase 2: Brutal Download
            self.brutal_download_all()
            
            # Phase 3: Retry failures
            if self.failed_urls:
                print(f"🔄 Retrying {len(self.failed_urls)} failed downloads...")
                failed_copy = list(self.failed_urls)
                self.failed_urls.clear()
                
                for url in failed_copy:
                    time.sleep(0.5)
                    self.download_file_brutal(url)
            
            # Generate summary
            self.generate_brutal_summary()
            
        except KeyboardInterrupt:
            print("\n🛑 Brutal cloning interrupted!")
        except Exception as e:
            print(f"💥 Brutal error: {str(e)}")
        finally:
            if hasattr(self, 'driver'):
                try:
                    self.driver.quit()
                except:
                    pass
        
        end_time = time.time()
        duration = end_time - start_time
        
        print("\n" + "🔥" * 50)
        print("🎉 BRUTAL CLONING COMPLETED! 🎉")
        print(f"⏱️ Duration: {duration:.2f} seconds")
        print(f"🔍 URLs discovered: {len(self.all_found_urls)}")
        print(f"📥 Files downloaded: {len(self.downloaded_files)}")
        print(f"❌ Failed downloads: {len(self.failed_urls)}")
        print(f"📁 Output: {os.path.abspath(self.output_dir)}")
        print("🔥" * 50)
    
    def generate_brutal_summary(self):
        """Generate summary files"""
        try:
            # Save all discovered URLs
            with open(os.path.join(self.output_dir, 'all_discovered_urls.txt'), 'w') as f:
                for url in sorted(self.all_found_urls):
                    f.write(url + '\n')
            
            # Save failed URLs
            if self.failed_urls:
                with open(os.path.join(self.output_dir, 'failed_urls.txt'), 'w') as f:
                    for url in sorted(self.failed_urls):
                        f.write(url + '\n')
            
            # Generate index
            html_files = []
            for root, dirs, files in os.walk(self.output_dir):
                for file in files:
                    if file.endswith(('.html', '.htm')):
                        rel_path = os.path.relpath(os.path.join(root, file), self.output_dir)
                        html_files.append(rel_path.replace(os.sep, '/'))
            
            index_html = f"""<!DOCTYPE html>
<html><head><title>Brutal Clone - {self.domain}</title>
<style>body{{font-family:Arial;margin:40px;}}h1{{color:#d32f2f;}}
.stats{{background:#f5f5f5;padding:20px;margin:20px 0;border-radius:5px;}}
a{{color:#1976d2;text-decoration:none;}}a:hover{{text-decoration:underline;}}
</style></head><body>
<h1>🔥 Brutal Clone: {self.domain}</h1>
<div class="stats">
<h3>Clone Statistics:</h3>
<p><strong>URLs discovered:</strong> {len(self.all_found_urls)}</p>
<p><strong>Files downloaded:</strong> {len(self.downloaded_files)}</p>
<p><strong>HTML pages:</strong> {len(html_files)}</p>
<p><strong>Failed downloads:</strong> {len(self.failed_urls)}</p>
</div>
<h2>Available Pages:</h2><ul>"""
            
            for html_file in sorted(html_files):
                               index_html += f'<li><a href="{html_file}">{html_file}</a></li>\n'
            
            index_html += """</ul></body></html>"""
            
            with open(os.path.join(self.output_dir, 'brutal_index.html'), 'w', encoding='utf-8') as f:
                f.write(index_html)
                
        except Exception as e:
            print(f"Error generating summary: {str(e)}")

def main():
    print("🔥" * 60)
    print("🔥" + " " * 20 + "BRUTAL WEBSITE CLONER" + " " * 20 + "🔥")
    print("🔥" + " " * 15 + "BYPASS SEMUA PROTEKSI & KEAMANAN" + " " * 15 + "🔥")
    print("🔥" * 60)
    print()
    
    # Input URL
    url = input("🎯 Masukkan URL target: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Input folder output
    output_dir = input("📁 Nama folder output (Enter = auto): ").strip()
    if not output_dir:
        domain = urllib.parse.urlparse(url).netloc
        output_dir = f"brutal_clone_{domain.replace('.', '_')}"
    
    # Input workers
    try:
        workers = int(input("⚡ Jumlah workers (Enter = 30): ").strip() or "30")
    except:
        workers = 30
    
    print(f"\n🔥 MEMULAI BRUTAL CLONING...")
    print(f"🎯 Target: {url}")
    print(f"📁 Output: {output_dir}")
    print(f"⚡ Workers: {workers}")
    print("🔥 Mode: BYPASS ALL SECURITY")
    print("\n⚠️  Tekan Ctrl+C untuk menghentikan\n")
    
    # Start brutal cloning
    cloner = BrutalWebsiteCloner(url, output_dir, workers)
    cloner.start_brutal_cloning()

if __name__ == "__main__":
    main()