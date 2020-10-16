import socket
from time import sleep
import codecs

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
    irc.send(b'PRIVMSG candy :!ep3\r\n')

    while 1:

        #Get answer
        response = irc.recv(7000).decode('utf-8')
        print(response)

        #Do the magic
        delimiter = response[1:].find(':')
        answer = codecs.encode(response[delimiter+2:], "rot_13")
        print(answer)

        #Send answer
        irc.send(('PRIVMSG candy :!ep3 -rep '+str(answer)+'\r\n').encode())

        #Get password
        password = irc.recv(7000).decode('utf-8')
        print(password)
        break
        


main()
    