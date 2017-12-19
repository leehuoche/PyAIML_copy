
#coding=utf-8
import sys
sys.path.insert(0, "../")
from bottle import route ,run, request
import aiml




# The Kernel object is the public interface to
# the AIML interpreter.
#k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
#k.learn("cn-startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
#k.respond("load aiml cn")

# Loop forever, reading user input from the command
# line and printing responses.
#while True: print k.respond(raw_input("> "))

def res_aiml(ques):
    k=aiml.Kernel()
    k.learn("cn-startup.xml")
    k.respond("load aiml cn")
    return k.respond(ques)

@route('/login')
def login():
        return '''
        <html>
        <head>
        <body>
        <h1 style="text-align: center"> 你好，我是你的好朋友阿明。快来跟我说说话吧</h1>
        <form action="/login"  method="post">
          请讲:<input name="username"  type="text"/>
        
          <input value="说完话点我一下"  type="submit"/>
                                          
        </form>
        </body>
        </html>
          '''


                                    
@route('/login',method='POST')
def do_login():
    username=request.forms.get('username')
    #password=request.forms.get('password')
    
    ans=res_aiml(username)

    print (type(ans))
                                                                                                        
    return '<p>YOU: %s</p>  <p> 阿明 %s </p>'  %(username,ans)
                                                             
run (host='localhost',port=8080,debug=True)

