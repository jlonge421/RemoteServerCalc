# This script will be server-side,
# conducting math calculations

import socket

def process_math_expression(expression):
    try:
        # Removing the '=' at the end
        expression = expression[:-1]
        # Evaluate the mathematical expression
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Input error. Re-type the math question again."

def start_server(host='0.0.0.0', port=5001):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")

    # Listen for incoming connections
    server_socket.listen(1)

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by client on {addr}")

    while True:
        # Receive the data (math expression) from the client
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Received question: '{data}'")

        # Check if the user input is '0/0=' to terminate the server
        if data == "0/0=":
            print("Received question '0/0='; end the server program")
            conn.sendall("User input ends; end the client program".encode('utf-8'))
            break

        # Process the mathematical expression and send the result back
        result = process_math_expression(data)
        print(f"Sending back answer: {result}")
        conn.sendall(result.encode('utf-8'))

    # Close the connection
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server(port=5001)  # Ensure port is between 1024 and 65535
