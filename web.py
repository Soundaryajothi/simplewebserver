from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
    <title>Top Software Companies</title>
</head>
<body>
    <h1>Top Software Companies</h1>
    <ul>
        <li>GOOGLE</li>
        <li>MICROSCOFT</li>
        <li>APPLE</li>
        <li>TCS</li>
        <li>WIPRO</li>
        <li>INFOSYS</li>
    </ul>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()