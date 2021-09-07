from os import closerange
from socket import *


def smtp_client(port = 1025, mailserver = '127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    
    clientSocket = socket(AF_INET,SOCK_STREAM) #create Socket
    clientSocket.connect((mailserver,port)) #pass in as a tuple (str,int)
    # Fill in end
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
       # print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    MailingSender = "MAIL FROM:<Alice>\r\n"
    clientSocket.send(MailingSender.encode())
    recv2 = clientSocket.recv(1024)
    recv2 = recv2.decode()
    #print(recv2)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    MailRec = "RCPT FROM:<BOB>\r\n"
    clientSocket(MailRec.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()
    #print(recv3)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    Datuh = "DATA\r\n"
    clientSocket(Datuh.encode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv4.decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    Quittin = "QUIT\r\n"
    clientSocket(Quittin.encode())
    recv5 = clientSocket.recv(1024)
    recv5 = recv5.decode()
    # Fill in end
    clientSocket.close()

#if __name__ == '__main__':
 #   smtp_client(1025, '127.0.0.1')
