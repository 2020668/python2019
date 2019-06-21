import socket
def main():
     udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
     udp_socket.sendto(b"hahahahaha",("192.168.43.113",8080))
     udp_socket.close()

if __name__ == " __main__":
    main()


