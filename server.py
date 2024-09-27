# Alexander Lokhanov 9/27/24

# This script will be server-side,
# conducting math calculations

import socket

def process_math_expression(expression):
    try:
        # ewww, whats thats two line thingy, lets remove it
        expression = expression[:-1]
        result = eval(expression) #isnt eval insecure?
        return str(result)
    except Exception as e:
        return "Input error. Re-type the math question again."

def start_server(host='0.0.0.0', port=5234):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # binding the server (consentually ofc) ;D
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")

    # my hearing is bad, hopefully this works
    server_socket.listen(1)

    # We take those...
    conn, addr = server_socket.accept()
    print(f"Connected by client on {addr}")

    while True:
        # Receive the data (math expression) from the client
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Received question: '{data}'")

        # SV_CHEATS == 0. Cheating (dividing by 0) is not allowed! talk to the admin, tough luck...
        if data == "0/0=":
            print("Received question '0/0='; end the server program")
            conn.sendall("User input ends; end the client program".encode('utf-8'))
            break

        # lemme think and imma get back to you
        result = process_math_expression(data)
        print(f"Sending back answer: {result}")
        conn.sendall(result.encode('utf-8'))

    # close connection
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server(port=5234)

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