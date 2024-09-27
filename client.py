# This will reside on the clients machine,
# allowing them to communicate with the server-side script

import socket

def start_client(server_ip='eustis3.eecs.ucf.edu', port=5234):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, port))
    print(f"Connected with server on {server_ip}:{port}")

    while True:
        # Get user input
        math_expression = input("Enter a math question (e.g., 20+10=): ")

        # Send the input to the server
        client_socket.sendall(math_expression.encode('utf-8'))

        # If the input is '0/0=', break and close the connection
        if math_expression == "0/0=":
            break

        # Receive and print the response from the server
        result = client_socket.recv(1024).decode('utf-8')
        print(f"Answer from server: {result}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client(port=5234)  # Ensure port is the same as the server
