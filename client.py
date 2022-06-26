import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 21       # FTP Control Port 

class FtpClient():

    def __init__(self, client):
       self.client = client                 # Control connection
       self.logged = False                  # User logged or not
       self.cmd = None                      # Command used
       self.client_data_conn = None         # Data connection
       self.connect()

    #---------------------------------#
    ## FTP Connection/Authentication ##
    #---------------------------------#

    def connect(self):
        # Connect user to Control Connection
        self.client.connect((HOST, PORT))

    def send_auth(self):
        # Send authorization information when server requests for it (username/password)
        ack_username = self.recv_control_message()
        print(ack_username)
        username = input("").encode("utf-8")
        self.client.sendall(username)

        ack_password = self.recv_control_message()
        print(ack_password)
        password = input("").encode("utf-8")
        self.client.sendall(password)

        access = self.recv_control_message()
        print(access[4:])

        # Status 230 - User successfuly logged
        # Status 430 - Invalid username/password
        if access[:3] == "230":
            return True
        elif access[:3] == "430":
            return False

    #--------------------------#
    ## FTP Control Connection ##
    #--------------------------#

    def start_control_conn(self):
        # Start Ccontrol Connection
        welcome_msg = self.recv_control_message()
        print(welcome_msg)

        self.logged = self.send_auth() 
        if not self.logged:
            return
        
        # Main loop to send commands
        while True:
            self.cmd = input("Enter command: ").strip().upper()
            self.send_cmd()
            if self.cmd == "STOR":
                self.STOR()
            elif self.cmd == "QUIT":
                self.client.close()
                break

    def send_cmd(self):
        # Send commands to server
        self.client.sendall((self.cmd).encode("utf-8"))

    def recv_control_message(self):
        # Recieve basic communication messages from server
        return client.recv(1024).decode("utf-8")


    #-----------------------#
    ## FTP Data Connection ##
    #-----------------------#

    def start_data_conn(self):
        # When command is sent and data wants to be transfered
        # Start a data connection socket and bind to same IP on port 20
        self.client_data_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_data_conn.connect((HOST, 20))
        print("Starting Data Connection")

    def close_data_conn(self):
        # When data transfer complete
        # Close socket
        print("Closing Data Connection")
        self.client_data_conn.close()
        
    #----------------#
    ## FTP Commands ##
    #----------------#

    def STOR(self):
        # Command for storing file to server
        self.start_data_conn()

        # Send filename
        filename = input("Filename: ")
        self.client_data_conn.sendall(filename.encode("utf-8"))

        # Open and read files. Send in batches of 1024 bytes
        file = open(f"{filename}", "rb")
        print("Sending")

        data = file.read(1024)
        while data:
            self.client_data_conn.sendall(data)
            data = file.read(1024)
        
        print("Finised sending")
        # Send a flag for file completely read
        self.client_data_conn.sendall(b"DONE")
            
        file.close()
        self.close_data_conn()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    c = FtpClient(client)
    c.start_control_conn()
    

    

