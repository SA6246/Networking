from socket import *
import os
import sys
import struct
import time
import select
import binascii


ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 1
# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exercise

def checksum(string):
# In this function we make the checksum of our packet
    csum = 0
    print("1") 
    

    countTo = (len(string) // 2) * 2
    count = 0


    while count < countTo:
        thisVal = (string[count + 1]) * 256 + (string[count])
        csum += thisVal
        csum &= 0xffffffff
        count += 2


    if countTo < len(string):
        csum += (string[len(string) - 1])
        csum &= 0xffffffff


    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def build_packet():
    #Fill in start
    # In the sendOnePing() method of the ICMP Ping exercise ,firstly the header of our
    # packet to be sent was made, secondly the checksum was appended to the header and
    # then finally the complete packet was sent to the destination.
    myChecksum = 0
    ID = os.getpid() & 0xFFFF
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    myChecksum = checksum(header + data)

    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network  byte order
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    

    # Make the header in a similar way to the ping exercise.
    # Append checksum to the header.


    # Dont send the packet yet , just return the final packet in this function.
    #Fill in end


    # So the function ending should look like this
    packet = header + data
    return packet


def get_route(hostname):
    timeLeft = TIMEOUT
    tracelist1 = [] #This is your list to use when iterating through each trace 
    tracelist2 = [] #This is your list to contain all traces
    timeLeft = 1


    for ttl in range(1,MAX_HOPS):
        for tries in range(TRIES):
            destAddr = gethostbyname(hostname)


            #Fill in start
            icmp = getprotobyname("icmp")
            mySocket = socket(AF_INET, SOCK_RAW, icmp)
            # Make a raw socket named mySocket
            #Fill in end


            mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)
            try:
                d = build_packet()
                mySocket.sendto(d, (hostname, 0))
                t = time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)
                if whatReady[0] == []: # Timeout
                    print("here")
                    tracelist1.append(str(ttl) + " * * * Request timed out.")
                    #Fill in start
                    tracelist2.append(list(tracelist1))
                    tracelist1.clear()
                    #You should add the list above to your all traces list
                    #Fill in end
                recvPacket, addr = mySocket.recvfrom(1024)
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect
                
                if timeLeft <= 0:
                    print("here1")
                    tracelist1.append(str(ttl) + " * * * Request timed out.")
                    #Fill in start
                    tracelist2.append(list(tracelist1))
                    tracelist1.clear()
                    #You should add the list above to your all traces list
                    #Fill in end
            except timeout:
                print("herex")
                continue


            else:
                #Fill in start
                #Fetch the icmp type from the IP packet
                
                headerICMP = recvPacket[20:28]
                i, c, csum, pidv, seq = struct.unpack("bbHHh", headerICMP)
                types = i

                #Fill in end
                try: #try to fetch the hostname
                    #Fill in start
                    
                    dest_hostname = gethostbyaddr(addr[0])[0]
                   
                    #Fill in end
                except herror:   #if the host does not provide a hostname
                        #Fill in start
                    dest_hostname = "hostname not returnable"
                    #Fill in end


                if types == 11:
                    #print("here2")
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 +
                    bytes])[0]
                    #Fill in start
                   
                    message3 = " * * * Time Exceeded."
                    tracelist1.append(str(ttl)+ message3)
                    tracelist2.append(list(tracelist1))
                    tracelist1.clear()
                    #You should add your responses to your lists here.
                    #Fill in end
                elif types == 3:
                    #print("here2")
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    #Fill in start
                    message4 = " * * * Destination Unreachable."
                    tracelist1.append(str(ttl)+ message4)
                    tracelist2.append(list(tracelist1))
                    tracelist1.clear()
                    #You should add your responses to your lists here 
                    #Fill in end
                elif types == 0:
                    print("here3")
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    #Fill in start
                    totaltime = round((timeReceived - timeSent)*1000,2)
                    totaltimestr = str(totaltime) + "ms"
                    whitespace = ", "
                    tracelist1.append(str(ttl) + whitespace + totaltimestr + whitespace + str(addr[0])+ whitespace + dest_hostname)
                    tracelist2.append(list(tracelist1))
                    tracelist1.clear()
                    print(tracelist2)
                    return tracelist2
                    #You should add your responses to your lists here and return your list if your destination IP is met
                    #Fill in end
                else:
                    print("here4")
                    #Fill in start
                    #If there is an exception/error to your if statements, you should append that to your list here
                    tracelist2.append(list(str(ttl) + " ERROR"))
                    tracelist1.clear()
                    break

            finally:
                mySocket.close()

            #print(tracelist2)
            return tracelist2
            


if __name__ == '__main__':
  K = get_route("www.bing.com")
  print(K)

    
