#!/usr/bin/env python3
import http.server
import os
import io
import urllib

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve upload form
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"""
            <html><body>
            <h2>Upload File</h2>
            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="file"><br><br>
                <input type="submit" value="Upload">
            </form>
            </body></html>
        """)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)

        # Extract filename
        header = self.headers['Content-Type']
        boundary = header.split("boundary=")[1].encode()
        parts = data.split(b'--' + boundary)

        for part in parts:
            if b'Content-Disposition' in part and b'filename=' in part:
                # Get filename
                header_str = part.split(b'\r\n')[1].decode()
                filename = header_str.split('filename="')[1].split('"')[0]

                # File content starts after blank line
                file_data = part.split(b'\r\n\r\n')[1].rsplit(b'\r\n', 1)[0]

                with open(filename, "wb") as f:
                    f.write(file_data)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Upload successful!\n")
                return

        self.send_response(400)
        self.end_headers()
        self.wfile.write(b"Upload failed.")

if __name__ == "__main__":
    server = http.server.HTTPServer(('0.0.0.0', 8000), UploadHandler)
    print("🚀 Upload server running on http://0.0.0.0:8000")
    server.serve_forever()
