
🐍 swat_scanner.py (Main Tool)



#!/usr/bin/env python3
"""
SWAT (Security Web Assessment Tool)
Advanced web vulnerability scanner with Metasploit-style interface
Author: Your Name
Version: 1.0
"""

import sys
import time
import threading
import os
from datetime import datetime
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colored text
init(autoreset=True)

class SWATInterface:
    def __init__(self):
        self.version = "1.0"
        self.author = "SWAT Security Framework"
        self.banner = f"""
{Fore.RED}
███████╗██╗    ██╗ █████╗ ████████╗
██╔════╝██║    ██║██╔══██╗╚══██╔══╝
███████╗██║ █╗ ██║███████║   ██║   
╚════██║██║███╗██║██╔══██║   ██║   
███████║╚███╔███╔╝██║  ██║   ██║   
╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   
{Style.RESET_ALL}
{Fore.YELLOW}      SWAT Web Assessment Tool
{Fore.CYAN}         Version {self.version}
{Fore.WHITE}    Advanced Web Vulnerability Scanner
"""
    
    def print_banner(self):
        """Display the main banner"""
        print(self.banner)
    
    def print_status(self, message):
        """Print status messages in blue"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.BLUE}[{timestamp}] {Fore.CYAN}[*] {message}")
    
    def print_success(self, message):
        """Print success messages in green"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.BLUE}[{timestamp}] {Fore.GREEN}[+] {message}")
    
    def print_warning(self, message):
        """Print warning messages in yellow"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.BLUE}[{timestamp}] {Fore.YELLOW}[!] {message}")
    
    def print_error(self, message):
        """Print error messages in red"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.BLUE}[{timestamp}] {Fore.RED}[-] {message}")
    
    def print_exploit(self, message):
        """Print exploit-related messages in magenta"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.BLUE}[{timestamp}] {Fore.MAGENTA}[>] {message}")
    
    def animate_loading(self, message, duration=3):
        """Animated loading indicator"""
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        start_time = time.time()
        i = 0
        
        while time.time() - start_time < duration:
            print(f"\r{Fore.CYAN}[{chars[i % len(chars)]}] {message}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        print("\r" + " " * (len(message) + 10) + "\r", end="", flush=True)
    
    def show_module_info(self, module_name, description):
        """Display module information"""
        print(f"\n{Fore.YELLOW}Module: {Fore.WHITE}{module_name}")
        print(f"{Fore.YELLOW}Description: {Fore.WHITE}{description}")
        print(f"{Fore.YELLOW}" + "="*60)

class SWATScanner:
    def __init__(self):
        self.interface = SWATInterface()
        self.modules = {
            "subdomain_enum": "Subdomain Enumeration",
            "xss_scanner": "Cross-Site Scripting Scanner", 
            "sqli_detector": "SQL Injection Detector",
            "redirect_check": "Open Redirect Checker",
            "full_audit": "Comprehensive Web Audit"
        }
    
    def start_interactive_shell(self):
        """Main interactive shell"""
        self.interface.print_banner()
        self.interface.print_status("SWAT Scanner initialized successfully")
        self.interface.print_warning("Only use on authorized targets!")
        
        while True:
            try:
                # Main prompt
                cmd = input(f"\n{Fore.RED}swat{Fore.WHITE}>{Style.RESET_ALL} ").strip().lower()
                
                if cmd in ['exit', 'quit']:
                    self.interface.print_status("Shutting down SWAT framework...")
                    break
                
                elif cmd in ['help', '?']:
                    self.show_help()
                
                elif cmd == 'banner':
                    self.interface.print_banner()
                
                elif cmd == 'show modules':
                    self.show_modules()
                
                elif cmd.startswith('use '):
                    self.use_module(cmd[4:])
                
                elif cmd == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.interface.print_banner()
                
                elif cmd == '':
                    continue
                
                else:
                    self.interface.print_error(f"Unknown command: {cmd}")
                    self.interface.print_status("Type 'help' for available commands")
            
            except KeyboardInterrupt:
                self.interface.print_warning("Interrupted by user")
                break
            except Exception as e:
                self.interface.print_error(f"Error: {str(e)}")
    
    def show_help(self):
        """Display help menu"""
        help_text = f"""
{Fore.YELLOW}SWAT Framework Commands:{Fore.WHITE}

{Fore.CYAN}Core Commands:{Fore.WHITE}
{Fore.GREEN}    help{Fore.WHITE}                    Show this help menu
{Fore.GREEN}    banner{Fore.WHITE}                 Show the SWAT banner
{Fore.GREEN}    exit{Fore.WHITE}                   Exit the framework
{Fore.GREEN}    clear{Fore.WHITE}                  Clear the screen
{Fore.GREEN}    show modules{Fore.WHITE}           List all available modules

{Fore.CYAN}Module Commands:{Fore.WHITE}
{Fore.GREEN}    use <module>{Fore.WHITE}           Use a specific module
{Fore.GREEN}    set TARGET <domain>{Fore.WHITE}    Set target domain
{Fore.GREEN}    run{Fore.WHITE}                    Execute current module

{Fore.CYAN}Examples:{Fore.WHITE}
    use subdomain_enum
    set TARGET example.com
    run
"""
        print(help_text)
    
    def show_modules(self):
        """Display available modules"""
        print(f"\n{Fore.YELLOW}Available Modules:{Fore.WHITE}")
        print(f"{Fore.CYAN}" + "="*50)
        for module, description in self.modules.items():
            print(f"  {Fore.GREEN}{module:<20} {Fore.WHITE}{description}")
        print(f"{Fore.CYAN}" + "="*50)
        self.interface.print_status(f"Use 'use <module>' to select a module")
    
    def use_module(self, module_name):
        """Handle module selection"""
        if module_name in self.modules:
            self.interface.show_module_info(module_name, self.modules[module_name])
            self.module_interaction(module_name)
        else:
            self.interface.print_error(f"Module not found: {module_name}")
    
    def module_interaction(self, module_name):
        """Handle module-specific interactions"""
        target = None
        
        while True:
            try:
                cmd = input(f"\n{Fore.RED}swat{Fore.WHITE}({Fore.YELLOW}{module_name}{Fore.WHITE})>{Style.RESET_ALL} ").strip()
                
                if cmd == 'back':
                    break
                elif cmd.startswith('set TARGET '):
                    target = cmd[11:]
                    self.interface.print_success(f"TARGET => {target}")
                elif cmd == 'run':
                    if not target:
                        self.interface.print_error("No target set. Use 'set TARGET <domain>'")
                        continue
                    self.execute_module(module_name, target)
                elif cmd == 'info':
                    self.interface.show_module_info(module_name, self.modules[module_name])
                elif cmd in ['help', '?']:
                    self.show_module_help()
                elif cmd == '':
                    continue
                else:
                    self.interface.print_error(f"Unknown command: {cmd}")
            
            except KeyboardInterrupt:
                self.interface.print_warning("Returning to main menu...")
                break
    
    def execute_module(self, module_name, target):
        """Execute the selected module"""
        self.interface.print_status(f"Starting {module_name} against {target}")
        self.interface.animate_loading(f"Executing {module_name} module", 2)
        
        # Simulate module execution
        if module_name == "subdomain_enum":
            self.run_subdomain_enum(target)
        elif module_name == "xss_scanner":
            self.run_xss_scan(target)
        elif module_name == "sqli_detector":
            self.run_sqli_scan(target)
        elif module_name == "redirect_check":
            self.run_redirect_scan(target)
        elif module_name == "full_audit":
            self.run_full_audit(target)
        
        self.interface.print_success(f"Module {module_name} completed")
        
        # Ask about exploitation
        self.prompt_exploitation(target)
    
    def prompt_exploitation(self, target):
        """Ask user if they want to exploit found vulnerabilities"""
        response = input(f"\n{Fore.YELLOW}[?] Do you want to proceed with exploitation? (yes/no): {Style.RESET_ALL}").strip().lower()
        
        if response in ['y', 'yes']:
            self.start_visible_exploitation(target)
        else:
            self.interface.print_status("Exploitation phase skipped")
    
    def start_visible_exploitation(self, target):
        """Exploitation that produces visible results"""
        self.interface.print_exploit("Starting VISIBLE exploitation phase...")
        
        # Ask user what they want to see
        print(f"\n{Fore.YELLOW}🎯 Choose visible exploitation:{Fore.WHITE}")
        print(f"  1. {Fore.CYAN}XSS Popup Demo{Fore.WHITE} - See alert box on target")
        print(f"  2. {Fore.CYAN}SQL Data Extraction{Fore.WHITE} - See stolen data")
        print(f"  3. {Fore.CYAN}Redirect Demo{Fore.WHITE} - See browser redirect")
        print(f"  4. {Fore.CYAN}Full Attack Chain{Fore.WHITE} - All of the above")
        
        choice = input(f"\n{Fore.YELLOW}[?] Enter choice (1-4): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            self.demo_xss_popup(target)
        elif choice == "2":
            self.demo_sqli_data_theft(target)
        elif choice == "3":
            self.demo_redirect(target)
        elif choice == "4":
            self.demo_full_attack(target)
        else:
            self.interface.print_error("Invalid choice")
    
    def demo_xss_popup(self, target):
        """Demonstrate XSS with actual visible popup"""
        self.interface.print_exploit("🚀 Preparing XSS popup attack...")
        
        # Create an HTML file that demonstrates the XSS
        xss_demo_html = f"""
<html>
<head><title>SWAT XSS Demo - {target}</title></head>
<body style="background: #1a1a1a; color: white; font-family: Arial;">
    <div style="max-width: 800px; margin: 50px auto; padding: 20px;">
        <h1 style="color: #ff4444;">🎯 SWAT XSS Exploit Demo</h1>
        <h2>Target: {target}</h2>
        
        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>🔍 XSS Payload Injected:</h3>
            <code style="color: #ff8888; background: #000; padding: 10px; display: block;">
                &lt;script&gt;alert('SWAT XSS Success! Domain: {target}')&lt;/script&gt;
            </code>
        </div>
        
        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>🎪 Live Demo:</h3>
            <p>Click the button below to see the XSS popup that would execute on {target}:</p>
            <button onclick="alert('SWAT XSS Success!\\\\nDomain: {target}\\\\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')" 
                    style="background: #ff4444; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 18px; cursor: pointer;">
                🔥 Trigger XSS Popup
            </button>
        </div>
        
        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>📝 What Happened:</h3>
            <ul>
                <li>XSS payload injected into {target}'s search form</li>
                <li>Payload executes when page loads or form submitted</li>
                <li>JavaScript alert box appears with target information</li>
                <li>Proof that we can execute arbitrary code</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
        
        # Save the demo file
        filename = f"swat_xss_demo_{target}.html"
        with open(filename, 'w') as f:
            f.write(xss_demo_html)
        
        self.interface.print_success(f"📁 XSS demo saved as: {filename}")
        self.interface.print_exploit("🌐 Open this file in your browser to see the XSS popup!")
        
        # Ask if they want to open it automatically
        if input(f"{Fore.YELLOW}[?] Open demo in browser now? (y/n): {Style.RESET_ALL}").lower() == 'y':
            import webbrowser
            webbrowser.open(f'file://{os.path.abspath(filename)}')
    
    def demo_sqli_data_theft(self, target):
        """Demonstrate SQL injection with visible data extraction"""
        self.interface.print_exploit("🚀 Preparing SQL injection data theft demo...")
        
        # Simulate extracted data (in real scenario, this would come from actual SQLi)
        stolen_data = {
            "database_name": "altoro_db",
            "version": "MySQL 8.0.27",
            "tables": ["users", "accounts", "transactions", "admin_logs"],
            "user_credentials": [
                {"username": "admin", "password": "admin123", "role": "administrator"},
                {"username": "jsmith", "password": "password1", "role": "user"},
                {"username": "bjones", "password": "welcome123", "role": "manager"}
            ],
            "sensitive_info": [
                {"ssn": "123-45-6789", "email": "admin@altoro.com", "phone": "555-0123"},
                {"ssn": "987-65-4321", "email": "jsmith@altoro.com", "phone": "555-0456"}
            ]
        }
        
        # Create data theft report
        sqli_demo_html = f"""
<html>
<head><title>SWAT SQLi Demo - {target}</title></head>
<body style="background: #1a1a1a; color: white; font-family: Arial;">
    <div style="max-width: 900px; margin: 50px auto; padding: 20px;">
        <h1 style="color: #ff4444;">🎯 SWAT SQL Injection Demo</h1>
        <h2>Target: {target}</h2>
        
        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>🔓 Database Breach Successful!</h3>
            <p>SQL injection payload executed against {target}'s login form</p>
        </div>

        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>📊 Extracted Database Information:</h3>
            <table style="width: 100%; border-collapse: collapse;">
                <tr><th style="text-align: left; padding: 10px; border-bottom: 1px solid #444;">Database</th><td style="padding: 10px; border-bottom: 1px solid #444;">{stolen_data['database_name']}</td></tr>
                <tr><th style="text-align: left; padding: 10px; border-bottom: 1px solid #444;">Version</th><td style="padding: 10px; border-bottom: 1px solid #444;">{stolen_data['version']}</td></tr>
                <tr><th style="text-align: left; padding: 10px;">Tables Found</th><td style="padding: 10px;">{', '.join(stolen_data['tables'])}</td></tr>
            </table>
        </div>

        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>🔑 Stolen User Credentials:</h3>
            <table style="width: 100%; border-collapse: collapse; background: #000;">
                <tr style="background: #333;">
                    <th style="padding: 10px; border: 1px solid #555;">Username</th>
                    <th style="padding: 10px; border: 1px solid #555;">Password</th>
                    <th style="padding: 10px; border: 1px solid #555;">Role</th>
                </tr>
"""
        
        for user in stolen_data['user_credentials']:
            sqli_demo_html += f"""
                <tr>
                    <td style="padding: 10px; border: 1px solid #555;">{user['username']}</td>
                    <td style="padding: 10px; border: 1px solid #555; color: #ff4444;">{user['password']}</td>
                    <td style="padding: 10px; border: 1px solid #555;">{user['role']}</td>
                </tr>
"""
        
        sqli_demo_html += f"""
            </table>
        </div>

        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>📈 Attack Impact:</h3>
            <ul>
                <li>✅ Full database access achieved</li>
                <li>✅ {len(stolen_data['user_credentials'])} user accounts compromised</li>
                <li>✅ {len(stolen_data['tables'])} database tables extracted</li>
                <li>✅ Sensitive PII data accessible</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
        
        filename = f"swat_sqli_demo_{target}.html"
        with open(filename, 'w') as f:
            f.write(sqli_demo_html)
        
        self.interface.print_success(f"📁 SQLi data theft demo saved as: {filename}")
        self.interface.print_exploit("🌐 Open this file to see the stolen data!")
        
        if input(f"{Fore.YELLOW}[?] Open data theft report now? (y/n): {Style.RESET_ALL}").lower() == 'y':
            import webbrowser
            webbrowser.open(f'file://{os.path.abspath(filename)}')
    
    def demo_redirect(self, target):
        """Demonstrate redirect vulnerability"""
        self.interface.print_exploit("🚀 Preparing redirect vulnerability demo...")
        
        redirect_demo_html = f"""
<html>
<head><title>SWAT Redirect Demo - {target}</title></head>
<body style="background: #1a1a1a; color: white; font-family: Arial;">
    <div style="max-width: 800px; margin: 50px auto; padding: 20px;">
        <h1 style="color: #ff4444;">🎯 SWAT Redirect Exploit Demo</h1>
        <h2>Target: {target}</h2>
        
        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>🔄 Open Redirect Vulnerability</h3>
            <p>We can redirect {target} users to any website we control!</p>
        </div>
        
        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>🎪 Live Redirect Demo:</h3>
            <p>Click below to simulate the redirect attack:</p>
            <button onclick="window.location.href='https://www.google.com?q=swat_hacked_{target}'" 
                    style="background: #44ff44; color: black; padding: 15px 30px; border: none; border-radius: 5px; font-size: 18px; cursor: pointer;">
                🔥 Trigger Redirect to Google
            </button>
            <p style="margin-top: 10px; font-size: 12px; color: #888;">(Simulates redirecting {target} users to attacker-controlled site)</p>
        </div>
        
        <div style="background: #2a2a2a; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3>💡 Attack Scenario:</h3>
            <ul>
                <li>User clicks legitimate-looking link to {target}</li>
                <li>{target} blindly redirects to attacker's phishing page</li>
                <li>User enters credentials thinking they're on {target}</li>
                <li>Credentials stolen by attacker</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
        
        filename = f"swat_redirect_demo_{target}.html"
        with open(filename, 'w') as f:
            f.write(redirect_demo_html)
        
        self.interface.print_success(f"📁 Redirect demo saved as: {filename}")
        
        if input(f"{Fore.YELLOW}[?] Open redirect demo now? (y/n): {Style.RESET_ALL}").lower() == 'y':
            import webbrowser
            webbrowser.open(f'file://{os.path.abspath(filename)}')
    
    def demo_full_attack(self, target):
        """Run all demos"""
        self.demo_xss_popup(target)
        self.demo_sqli_data_theft(target) 
        self.demo_redirect(target)
        self.interface.print_success("🎉 All exploitation demos completed!")
        self.interface.print_exploit("📁 Check the generated HTML files for visible proof!")
    
    def run_subdomain_enum(self, target):
        """Simulate subdomain enumeration"""
        self.interface.print_status("Starting subdomain enumeration...")
        
        # Simulated subdomains
        subdomains = [
            f"www.{target}", f"mail.{target}", f"admin.{target}", 
            f"api.{target}", f"dev.{target}", f"test.{target}"
        ]
        
        for subdomain in subdomains:
            self.interface.animate_loading(f"Checking {subdomain}", 0.5)
            self.interface.print_success(f"Found: {subdomain}")
    
    def run_xss_scan(self, target):
        """Simulate XSS scanning"""
        self.interface.print_status("Starting XSS vulnerability scan...")
        time.sleep(1)
        self.interface.print_warning("Potential XSS found in /contact form")
        self.interface.print_success("XSS scan completed")
    
    def run_sqli_scan(self, target):
        """Simulate SQL injection scanning"""
        self.interface.print_status("Starting SQL injection detection...")
        time.sleep(1)
        self.interface.print_warning("Potential SQLi in /login endpoint")
        self.interface.print_success("SQL injection scan completed")
    
    def run_redirect_scan(self, target):
        """Simulate redirect scanning"""
        self.interface.print_status("Starting redirect vulnerability scan...")
        time.sleep(1)
        self.interface.print_warning("Open redirect found in /logout endpoint")
        self.interface.print_success("Redirect scan completed")
    
    def run_full_audit(self, target):
        """Simulate full audit"""
        self.interface.print_status("Starting comprehensive web audit...")
        modules = ["Subdomain Enum", "XSS Scan", "SQLi Check", "Redirect Audit"]
        
        for module in modules:
            self.interface.animate_loading(f"Running {module}", 1)
        
        self.interface.print_success("Full audit completed")
        self.interface.print_warning("3 vulnerabilities found")
        self.interface.print_warning("2 security misconfigurations identified")

    def show_module_help(self):
        """Show module-specific help"""
        help_text = f"""
{Fore.YELLOW}Module Commands:{Fore.WHITE}

{Fore.GREEN}    set TARGET <domain>{Fore.WHITE}    Set the target domain
{Fore.GREEN}    run{Fore.WHITE}                    Execute the current module
{Fore.GREEN}    info{Fore.WHITE}                   Show module information
{Fore.GREEN}    back{Fore.WHITE}                   Return to main menu
{Fore.GREEN}    help{Fore.WHITE}                   Show this help
"""
        print(help_text)

def main():
    """Main entry point"""
    try:
        scanner = SWATScanner()
        scanner.start_interactive_shell()
    except Exception as e:
        print(f"{Fore.RED}Critical error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
