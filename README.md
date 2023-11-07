# EX01 Developing a Simple Webserver
## Date: 07.10.2023

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```


## OUTPUT:

![Alt text](<Screenshot 2023-11-01 062722.png>)
![Alt text](<Screenshot 2023-11-01 062733.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
