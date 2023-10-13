import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    operation = input("Enter operation (Random/Add/Subtract): ")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    request = f"{operation};{num1};{num2}"
    client.send(request.encode())

    response = client.recv(1024).decode()
    print(f"Server response: {response}")

    client.close()

if __name__ == "__main__":
    main()
