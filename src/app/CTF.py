import socket

def main():
    host = '0.0.0.0'  # Listen on all network interfaces
    port = 200

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening...")

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            message = '53776174694354467b596f755f476f745f69747d'  # Hex for "SwatiCTF{You_Got_it}"
            # Convert hex to decimal numbers ASCII codes
            decimals = ' '.join(str(int(message[i:i+2], 16)) for i in range(0, len(message), 2))
            conn.sendall(decimals.encode() + b'\n')
            conn.close()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
