import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 21       # FTP Control Port 

class FtpClient():

    def __init__(self, client):
       self.client = client
       self.connect()

    def connect(self):
        """
        Connect user to Control Connection
        """
        self.client.connect((HOST, PORT))

    def start_control_conn(self):
        """
        Start Ccontrol Connection
        """
        welcome_msg = self.recv_message()
        print(welcome_msg)
        self.send_auth()

    def send_auth(self):
        """
        Send authorization information when server requests for it (username/password)
        """
        ack_username = self.recv_message()
        print(ack_username)
        username = input("").encode("utf-8")
        self.client.sendall(username)

        ack_password = self.recv_message()
        print(ack_password)
        password = input("").encode("utf-8")
        self.client.sendall(password)

        access = self.recv_message()
        print(access)

    def recv_message(self):
        """
        Quick function to recieve messages and convert to string
        Mostly used for communcation messages, such as welcome and authorization

        Returns:
            str: Message recieved from server
        """
        return client.recv(1024).decode("utf-8")
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    c = FtpClient(client)
    c.start_control_conn()
    

    

