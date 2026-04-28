#!/usr/bin/env python3
"""
BiasGuard - Simple HTTP Server
Run this to host the project locally for demo purposes
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for potential API integration
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              🛡️  BiasGuard - AI Bias Detection            ║
║                                                            ║
║              Server running at:                           ║
║              http://localhost:{PORT}                       ║
║                                                            ║
║              Press Ctrl+C to stop                         ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)

        # Open browser automatically
        webbrowser.open(f'http://localhost:{PORT}')

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped. Thank you for using BiasGuard!")

if __name__ == "__main__":
    main()
