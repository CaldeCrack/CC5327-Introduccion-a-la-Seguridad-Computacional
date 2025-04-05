import socket

# We connect to a (host,port) tuple
import utils

CONNECTION_ADDR_A = ("cc5327.hackerlab.cl", 5312)
CONNECTION_ADDR_B = ("cc5327.hackerlab.cl", 5313)

if __name__ == "__main__":
    sock_input_A, sock_output_A = utils.create_socket(CONNECTION_ADDR_A)
    sock_input_B, sock_output_B = utils.create_socket(CONNECTION_ADDR_B)
    while True:
        try:
            # Read a message from standard input
            response = input("send a message: ")
            # You need to use encode() method to send a string as bytes.
            print("[Client] \"{}\"".format(response))
            resp = utils.send_message(sock_input_A, sock_output_A, response)
            print(f"[Server] {resp}")
            # Wait for a response and disconnect.
            desencrypted = utils.send_message(sock_input_B, sock_output_B, resp)
            print(f"[Desencrypted] {desencrypted}")
        except Exception as e:
            print(e)
            print("Closing...")
            input.close()
            break
