import http.server
import webbrowser
import os
import signal
import sys

PORT = 3546

def server_report(report_path):
    report_dir = os.path.dirname(os.path.abspath(report_path))
    report_file = os.path.basename(report_path)
    os.chdir(report_dir)

    handler = http.server.SimpleHTTPRequestHandler

    server = http.server.HTTPServer(("", PORT), handler)

    url = f"http://localhost:{PORT}/{report_file}"
    webbrowser.open(url)

    print(f"\n Report ready at {url}")
    print("Press CTRL + C to shutdown the server \n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n Server Shutdown")
        server.server_close()
        sys.exit(0)
