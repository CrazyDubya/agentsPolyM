#!/usr/bin/env python3
"""
Polymarket Agents Demo Launcher

Choose which demo mode to run:
1. Automated Demo - Runs automatically with no interaction
2. Interactive Demo - Full interactive experience
3. CLI Demo - Command-line interface
4. Web Demo - Open web interface
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def print_header():
    print("="*60)
    print("🤖 POLYMARKET AGENTS - DEMO LAUNCHER")
    print("="*60)
    print("Choose your demo experience:")
    print()

def print_options():
    options = [
        ("1", "🚀 Automated Demo", "Runs complete demo automatically (recommended for first viewing)"),
        ("2", "🎮 Interactive Demo", "Full interactive experience with user input"),
        ("3", "💻 CLI Demo", "Command-line interface with all features"),
        ("4", "🌐 Web Demo", "Open web-based interface in browser"),
        ("5", "📖 Documentation", "Open demo documentation"),
        ("6", "❌ Exit", "Exit the launcher")
    ]
    
    for num, title, desc in options:
        print(f"{num}. {title}")
        print(f"   {desc}")
        print()

def run_automated_demo():
    print("🚀 Starting Automated Demo...")
    try:
        subprocess.run([sys.executable, "demo_auto.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running automated demo: {e}")
    except FileNotFoundError:
        print("Error: demo_auto.py not found!")

def run_interactive_demo():
    print("🎮 Starting Interactive Demo...")
    try:
        subprocess.run([sys.executable, "demo.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running interactive demo: {e}")
    except FileNotFoundError:
        print("Error: demo.py not found!")

def run_cli_demo():
    print("💻 Starting CLI Demo...")
    try:
        subprocess.run([sys.executable, "demo_cli.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running CLI demo: {e}")
    except FileNotFoundError:
        print("Error: demo_cli.py not found!")

def run_web_demo():
    print("🌐 Opening Web Demo...")
    demo_html = Path("demo.html")
    
    if demo_html.exists():
        try:
            # Try to start a simple HTTP server
            import http.server
            import socketserver
            import threading
            
            PORT = 8000
            
            class Handler(http.server.SimpleHTTPRequestHandler):
                def log_message(self, format, *args):
                    pass  # Suppress server logs
            
            def start_server():
                with socketserver.TCPServer(("", PORT), Handler) as httpd:
                    httpd.serve_forever()
            
            # Start server in background
            server_thread = threading.Thread(target=start_server, daemon=True)
            server_thread.start()
            
            # Open browser
            url = f"http://localhost:{PORT}/demo.html"
            webbrowser.open(url)
            
            print(f"✅ Web demo opened at: {url}")
            print("Press Ctrl+C to stop the server")
            
            # Keep the main thread alive
            try:
                while True:
                    import time
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n🛑 Server stopped")
                
        except Exception as e:
            print(f"Error starting web server: {e}")
            print("You can also open demo.html directly in your browser")
    else:
        print("Error: demo.html not found!")

def open_documentation():
    print("📖 Opening Documentation...")
    doc_file = Path("DEMO_README.md")
    
    if doc_file.exists():
        try:
            # Try to open with default markdown viewer or text editor
            if sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', str(doc_file)])
            elif sys.platform.startswith('win'):    # Windows
                subprocess.run(['start', str(doc_file)], shell=True)
            else:  # Linux
                subprocess.run(['xdg-open', str(doc_file)])
            
            print("✅ Documentation opened")
        except Exception as e:
            print(f"Could not open documentation automatically: {e}")
            print(f"Please manually open: {doc_file}")
    else:
        print("Error: DEMO_README.md not found!")

def main():
    while True:
        print_header()
        print_options()
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                run_automated_demo()
            elif choice == "2":
                run_interactive_demo()
            elif choice == "3":
                run_cli_demo()
            elif choice == "4":
                run_web_demo()
            elif choice == "5":
                open_documentation()
            elif choice == "6":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter a number 1-6.")
                
            input("\nPress Enter to return to menu...")
            print("\n" * 3)  # Clear screen
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()