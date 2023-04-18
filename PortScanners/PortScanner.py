import socket
import sys
from datetime import datetime

startingTime = 0

def scanner():
    print("-" * 40)
    print("Scanning Target : ", HOST)
    print("Scanning started at: ", str(datetime.now()))
    startingTime = datetime.now()
    print("-" * 40)
    try:
        for port in range(1, 500):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.001)

            sonuc = s.connect_ex((HOST, port))
            if sonuc == 0:
                print("Port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n Exitting program!")
    except socket.gaierror:
        print("\n Host colud not be resolved")
    finally:
        print("Scanning time:", datetime.now() - startingTime)

if len(sys.argv) == 2:
    HOST = socket.gethostbyname(sys.argv[1])
    scanner()
else:
    print("Invalid argument of value")