import socket
from time import sleep
import base64

def main():

    #Variables
    HOST = "irc.root-me.org"
    PORT = 6667

    #Create IRC socket
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to host
    irc.connect((HOST, PORT))
    print('Connected to: ' + HOST + ':' + str(PORT))

    #Send IRC mandatory commands
    sleep(1)
    irc.send(b'NICK Hacat\r\n')
    sleep(1)
    irc.send(b'PASS HAHA\r\n')
    sleep(1)
    irc.send(b'USER Hacat irc.root-me.org root-me :BOT1\r\n')
    sleep(1)

    #Connect to channel
    irc.send(b'JOIN #root-me_challenge\r\n')
    sleep(2)

    #Empty the bin !!!
    while 1:
        useless_info = irc.recv(7000).decode('utf-8')
        break

    #Send message to candy 
    irc.send(b'PRIVMSG candy :!ep2\r\n')

    while 1:

        #Get answer
        response = irc.recv(7000).decode('utf-8')
        print(response)

        #Do the math
        delimiter = response[1:].find(':')
        answer = base64.b64decode(response[delimiter+2:])
        print(answer)

        #Send answer
        irc.send(('PRIVMSG candy :!ep2 -rep '+str(answer)+'\r\n').encode())

        #Get password
        password = irc.recv(7000).decode('utf-8')
        print(password)
        break
        


main()
    