# This will reside on the clients machine,
# allowing them to communicate with the server-side script

import socket

#connecting to eustis3
def start_client(server_ip='eustis3.eecs.ucf.edu', port=5234):
    # create the TCP IP sockeet
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to da server
    client_socket.connect((server_ip, port))
    print(f"Connected with server on {server_ip}:{port}")

    while True:
        # take input
        math_expression = input("Enter a math question (e.g., 20+10=): ")

        # ewww, math, send it off...
        client_socket.sendall(math_expression.encode('utf-8'))

        # dividing by 0 is a cheat code in the universe, 
        # but sv_cheats is set to 0 and protected by admin..
        if math_expression == "0/0=":
            break

        # mmmmm, doughnuts..
        result = client_socket.recv(1024).decode('utf-8')
        print(f"Answer from server: {result}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client(port=5234) 
    # grrrr

#    |    _________
#    |   /  mmmmm, \
#    |   \doughnuts/   _
#    |        O      _//\-\
#    |         O    /      \
#   _|_         o  /       |
#  /   \         (.(.) /|\/
# |  0  |         (___    ,)
#  \___/          /   \   \
#      _          \o  /   |
#    _( \_         _| _____\
#   (___  \_______/\_/______\
#   (___         /    /    \|
#   (___________/     |____||
#              /      |    ||
#             /_______|    |_\
#             \      _|    | /
#              |    (_     \/
#              | \__  | | | |
#              |    \ |_|_|_|
#              |     |     |
#              |     |     |
#              |     |     |
#              |_____|_____|
#              |_____|_____|
#             /     /      |