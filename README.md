# Networking - Computer Networking Assignment 3

## Lab 3: SMTP Lab
 
By the end of this lab, you will have acquired a better understanding of SMTP protocol. You will also gain experience in implementing a standard protocol using Python.

Your task is to develop a simple mail client that sends email to any recipient. Your client will need to connect to a mail server, dialogue with the mail server using the SMTP protocol, and send an email message to the mail server. Python provides a module, called smtplib, which has built-in methods to send mail using SMTP protocol. However, you will not be using this module in this lab, because it hides the details of SMTP and socket programming. 

In order to limit spam, some mail servers do not accept TCP connections from arbitrary sources. For the experiment described below, you may want to try connecting both to your university mail server and to a popular Webmail server, such as an AOL mail server. To connect to the university mail server, you will need to use NYU’s VPN. You may also try making your connection both from your home and from your university campus.

## Code
Below you will find the skeleton code for the client. You are to complete the skeleton code. The places where you need to fill in code are marked with #Fill in start and #Fill in end. Each place may require one or more lines of code. 

## Additional Notes
In some cases, the receiving mail server might classify your email as junk. Make sure that you check your junk/spam folder when you look for the email sent from your client.

## What to Hand In
Use your GitHub repository to upload the complete code for the SMTP mail client. Make sure you follow the SMTP protocol for non-encrypted communication. In this assignment, GradeScope will use a local SMTP server to grade the assignment. Please make sure to use port 1025 and mail server address 127.0.0.1 to receive full credit.
Note: Comment out all the print statements in your code, otherwise gradescope will fail to autograde your assignment.
 
Skeleton Python Code for the Web Server
 ```
from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

```



#FAQ
Q: I am getting the following error in gradescope: 
```“cp: cannot stat '/autograder/submission/solution.py': No such file or directory”```
A: If you are submitting a python solution, all python submissions must have the filename titled “solution.py” (minus the quotation marks). Make sure your file meets this naming requirement.

Recommended Textbook Reference
Chapter 2: 2.3.1 SMTP
(Non-textbook reference) rfc2821
(Non-textbook reference) How to setup NYU VPN (required to communicate with NYU SMTP server)

Most Common issues
SMTP commands do not follow requirements documented in the RFC referenced above
SMTP commands are case-inconsistent or all lowercase (reference RFC 2821 for requirements)
Not establishing socket connection properly
Reference to read - python docs
Not encoding or decoding properly
Incorrect port or server address


