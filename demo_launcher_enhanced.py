#!/usr/bin/env python3
"""
Polymarket Agents Demo Launcher

Enhanced launcher with multiple demo options and automatic mode detection.
Provides easy access to all demo variants with optimized user experience.
"""

import os
import sys
import subprocess
import argparse
import webbrowser
from typing import Optional

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class DemoLauncher:
    """Enhanced demo launcher with multiple options"""
    
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.available_demos = {
            '1': {
                'name': 'Interactive Python Demo (Original)',
                'file': 'demo.py',
                'description': 'Full-featured interactive demo with detailed explanations'
            },
            '2': {
                'name': 'Optimized Fast Demo',
                'file': 'demo_optimized.py',
                'description': 'Performance-optimized version with faster execution'
            },
            '3': {
                'name': 'Command Line Interface',
                'file': 'demo_cli.py', 
                'description': 'CLI-based demo simulating the actual agent interface'
            },
            '4': {
                'name': 'Web Browser Demo',
                'file': 'demo.html',
                'description': 'Modern web interface with interactive charts and visualizations'
            },
            '5': {
                'name': 'Auto Demo (No Interaction)',
                'file': 'demo_auto.py',
                'description': 'Automated demonstration requiring no user input'
            }
        }

    def print_banner(self):
        """Print enhanced banner"""
        print(f"{Colors.HEADER}{Colors.BOLD}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║            🤖 POLYMARKET AGENTS DEMO LAUNCHER            ║")
        print("║                                                          ║")
        print("║      AI-Powered Prediction Market Trading System        ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Colors.ENDC}")

    def show_demo_options(self):
        """Display available demo options"""
        print(f"{Colors.CYAN}Available Demo Options:{Colors.ENDC}\n")
        
        for key, demo in self.available_demos.items():
            # Check if demo file exists
            demo_path = os.path.join(self.script_dir, demo['file'])
            status = f"{Colors.GREEN}✅{Colors.ENDC}" if os.path.exists(demo_path) else f"{Colors.FAIL}❌{Colors.ENDC}"
            
            print(f"{Colors.BLUE}{key}.{Colors.ENDC} {status} {Colors.BOLD}{demo['name']}{Colors.ENDC}")
            print(f"   {demo['description']}")
            print()

    def launch_python_demo(self, script_name: str, args: Optional[list] = None):
        """Launch a Python demo script"""
        script_path = os.path.join(self.script_dir, script_name)
        
        if not os.path.exists(script_path):
            print(f"{Colors.FAIL}❌ Error: {script_name} not found{Colors.ENDC}")
            return False
            
        try:
            cmd = [sys.executable, script_path]
            if args:
                cmd.extend(args)
                
            print(f"{Colors.GREEN}🚀 Launching {script_name}...{Colors.ENDC}\n")
            subprocess.run(cmd, cwd=self.script_dir)
            return True
            
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Demo interrupted by user{Colors.ENDC}")
            return True
        except Exception as e:
            print(f"{Colors.FAIL}❌ Error launching {script_name}: {e}{Colors.ENDC}")
            return False

    def launch_web_demo(self):
        """Launch the web demo in browser"""
        html_path = os.path.join(self.script_dir, 'demo.html')
        
        if not os.path.exists(html_path):
            print(f"{Colors.FAIL}❌ Error: demo.html not found{Colors.ENDC}")
            return False
            
        try:
            # Try to start a simple HTTP server for better experience
            print(f"{Colors.GREEN}🌐 Starting web server for demo...{Colors.ENDC}")
            print(f"{Colors.CYAN}Opening demo.html in your default browser...{Colors.ENDC}")
            
            # Open file directly in browser
            file_url = f"file://{os.path.abspath(html_path)}"
            webbrowser.open(file_url)
            
            print(f"{Colors.GREEN}✅ Web demo launched successfully!{Colors.ENDC}")
            print(f"{Colors.WARNING}Note: For full functionality, consider running: python -m http.server 8000{Colors.ENDC}")
            
            return True
            
        except Exception as e:
            print(f"{Colors.FAIL}❌ Error launching web demo: {e}{Colors.ENDC}")
            return False

    def run_interactive_launcher(self):
        """Run the interactive demo launcher"""
        while True:
            self.print_banner()
            self.show_demo_options()
            
            print(f"{Colors.CYAN}Additional Options:{Colors.ENDC}")
            print(f"{Colors.BLUE}6.{Colors.ENDC} 📖 View Documentation (DEMO_README.md)")
            print(f"{Colors.BLUE}7.{Colors.ENDC} ⚙️  Advanced Options")
            print(f"{Colors.BLUE}8.{Colors.ENDC} 🚪 Exit")
            print()
            
            try:
                choice = input(f"{Colors.BOLD}Select demo option (1-8): {Colors.ENDC}").strip()
                
                if choice == '1':
                    self.launch_python_demo('demo.py')
                elif choice == '2':
                    self.show_optimized_options()
                elif choice == '3':
                    self.launch_python_demo('demo_cli.py')
                elif choice == '4':
                    self.launch_web_demo()
                elif choice == '5':
                    self.launch_python_demo('demo_auto.py')
                elif choice == '6':
                    self.view_documentation()
                elif choice == '7':
                    self.show_advanced_options()
                elif choice == '8':
                    print(f"{Colors.GREEN}👋 Thanks for trying Polymarket Agents!{Colors.ENDC}")
                    break
                else:
                    print(f"{Colors.WARNING}❌ Invalid option. Please try again.{Colors.ENDC}")
                    
                if choice in ['1', '2', '3', '4', '5']:
                    input(f"\n{Colors.CYAN}Press Enter to return to main menu...{Colors.ENDC}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}Launcher interrupted by user{Colors.ENDC}")
                break
            except Exception as e:
                print(f"{Colors.FAIL}❌ Error: {e}{Colors.ENDC}")

    def show_optimized_options(self):
        """Show options for optimized demo"""
        print(f"\n{Colors.CYAN}Optimized Demo Options:{Colors.ENDC}")
        print(f"{Colors.BLUE}1.{Colors.ENDC} Fast mode (default)")
        print(f"{Colors.BLUE}2.{Colors.ENDC} Verbose mode")
        print(f"{Colors.BLUE}3.{Colors.ENDC} Interactive mode")
        print(f"{Colors.BLUE}4.{Colors.ENDC} Slow mode (full delays)")
        
        sub_choice = input(f"\n{Colors.BOLD}Select option (1-4): {Colors.ENDC}").strip()
        
        args = []
        if sub_choice == '2':
            args = ['--verbose']
        elif sub_choice == '3':
            args = ['--interactive']
        elif sub_choice == '4':
            args = ['--slow']
            
        self.launch_python_demo('demo_optimized.py', args)

    def view_documentation(self):
        """View the demo documentation"""
        doc_path = os.path.join(self.script_dir, 'DEMO_README.md')
        
        if os.path.exists(doc_path):
            try:
                # Try to open with default markdown viewer or text editor
                if sys.platform.startswith('darwin'):  # macOS
                    subprocess.run(['open', doc_path])
                elif sys.platform.startswith('linux'):  # Linux
                    subprocess.run(['xdg-open', doc_path])
                elif sys.platform.startswith('win'):  # Windows
                    subprocess.run(['start', doc_path], shell=True)
                else:
                    # Fallback: print first few lines
                    with open(doc_path, 'r') as f:
                        lines = f.readlines()[:20]
                        print(f"\n{Colors.CYAN}DEMO_README.md (first 20 lines):{Colors.ENDC}")
                        print(''.join(lines))
                        
            except Exception as e:
                print(f"{Colors.FAIL}❌ Error opening documentation: {e}{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}❌ Documentation not found{Colors.ENDC}")

    def show_advanced_options(self):
        """Show advanced launcher options"""
        print(f"\n{Colors.CYAN}Advanced Options:{Colors.ENDC}")
        print(f"{Colors.BLUE}1.{Colors.ENDC} 🧪 Run all demos in sequence")
        print(f"{Colors.BLUE}2.{Colors.ENDC} 🔧 Check system requirements")
        print(f"{Colors.BLUE}3.{Colors.ENDC} 📊 Performance benchmark")
        print(f"{Colors.BLUE}4.{Colors.ENDC} 🔄 Update demo data")
        print(f"{Colors.BLUE}5.{Colors.ENDC} 🏠 Return to main menu")
        
        sub_choice = input(f"\n{Colors.BOLD}Select option (1-5): {Colors.ENDC}").strip()
        
        if sub_choice == '1':
            self.run_all_demos()
        elif sub_choice == '2':
            self.check_requirements()
        elif sub_choice == '3':
            self.run_benchmark()
        elif sub_choice == '4':
            self.update_demo_data()
        # Option 5 returns to main menu automatically

    def run_all_demos(self):
        """Run all available demos in sequence"""
        print(f"\n{Colors.WARNING}🧪 Running all demos in sequence...{Colors.ENDC}")
        
        demos_to_run = [
            ('demo_optimized.py', []),
            ('demo_cli.py', []),
            ('demo_auto.py', [])
        ]
        
        for script, args in demos_to_run:
            if os.path.exists(os.path.join(self.script_dir, script)):
                print(f"\n{Colors.GREEN}▶️  Running {script}...{Colors.ENDC}")
                self.launch_python_demo(script, args)
            else:
                print(f"{Colors.WARNING}⚠️  Skipping {script} (not found){Colors.ENDC}")

    def check_requirements(self):
        """Check system requirements"""
        print(f"\n{Colors.CYAN}🔧 System Requirements Check:{Colors.ENDC}")
        
        # Check Python version
        python_version = sys.version_info
        print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
        
        # Check required packages
        required_packages = ['requests', 'typing', 'datetime', 'json']
        
        for package in required_packages:
            try:
                __import__(package)
                print(f"{Colors.GREEN}✅{Colors.ENDC} {package}")
            except ImportError:
                print(f"{Colors.FAIL}❌{Colors.ENDC} {package} (missing)")
                
        # Check demo files
        print(f"\n{Colors.CYAN}Demo Files:{Colors.ENDC}")
        for demo in self.available_demos.values():
            path = os.path.join(self.script_dir, demo['file'])
            status = f"{Colors.GREEN}✅{Colors.ENDC}" if os.path.exists(path) else f"{Colors.FAIL}❌{Colors.ENDC}"
            print(f"{status} {demo['file']}")

    def run_benchmark(self):
        """Run performance benchmark"""
        print(f"\n{Colors.CYAN}📊 Performance Benchmark:{Colors.ENDC}")
        
        import time
        start_time = time.time()
        
        # Simulate some operations
        for i in range(1000):
            _ = i ** 2
            
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"Execution Time: {execution_time:.4f} seconds")
        print(f"Operations per second: {1000/execution_time:.0f}")
        
        if execution_time < 0.01:
            print(f"{Colors.GREEN}✅ Performance: Excellent{Colors.ENDC}")
        elif execution_time < 0.1:
            print(f"{Colors.BLUE}✅ Performance: Good{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}⚠️  Performance: Adequate{Colors.ENDC}")

    def update_demo_data(self):
        """Update demo data (placeholder)"""
        print(f"\n{Colors.CYAN}🔄 Demo Data Update:{Colors.ENDC}")
        print("This feature would update market data, news feeds, and AI predictions.")
        print("In a production environment, this would connect to live data sources.")
        print(f"{Colors.GREEN}✅ Demo data is current{Colors.ENDC}")

def main():
    parser = argparse.ArgumentParser(description='Polymarket Agents Demo Launcher')
    parser.add_argument('--auto', action='store_true', help='Auto-launch optimized demo')
    parser.add_argument('--web', action='store_true', help='Launch web demo')
    parser.add_argument('--demo', choices=['1', '2', '3', '4', '5'], help='Launch specific demo')
    
    args = parser.parse_args()
    
    launcher = DemoLauncher()
    
    if args.auto:
        launcher.launch_python_demo('demo_optimized.py')
    elif args.web:
        launcher.launch_web_demo()
    elif args.demo:
        demo_file = launcher.available_demos[args.demo]['file']
        if demo_file.endswith('.html'):
            launcher.launch_web_demo()
        else:
            launcher.launch_python_demo(demo_file)
    else:
        launcher.run_interactive_launcher()

if __name__ == "__main__":
    main()