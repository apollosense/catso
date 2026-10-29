import http.server,json,os
import socketserver
import random
from http.server import SimpleHTTPRequestHandler

PORT=6969
f = "bloops.txt"
n=0
if os.path.exists(f) :
    try:
     n=int(open(f).read().strip())
    except:
        n = 0

def save():
    open(f,'w').write(str(n))

class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/count':
            self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers()
            self.wfile.write(json.dumps({'n':n}).encode())
        else:
            return SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
      global n
      if self.path == "/bloop":
            n=n+1
            save()
            print(random.choice(["bloop","blop","BLOOP","boop"]), n)
            self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers()
            self.wfile.write(json.dumps({"n":n}).encode())
      else:
          self.send_response(404);self.end_headers()
    def log_message(self, *a):pass

#def meow():
#    print('meow')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address=True
print('catso on http://localhost:'+str(PORT))
with socketserver.TCPServer(("",PORT),H) as s:
    s.serve_forever()
