import socket
import time
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 21       # FTP Control Port 
curr_server_dir = os.path.abspath('./Server')

admin_username = "Test"
admin_password = "123"

def logger(func, code, msg):
    logmsg = time.strftime(f"%Y-%m-%d %H:%M:%S [{code}] {func}: {msg}")
    print(logmsg)

class FtpServer():
    def __init__(self, conn, addr):
        self.curr_server_dir = curr_server_dir
        self.control_conn = conn                    # Control connection
        self.addr = addr                            # Control connection IP

        self.data_sock = None                       # Data connection socket
        self.data_conn = None                       # Data connection
        self.data_addr = None                       # Data connection IP

    #----------------------#
    ## FTP Authentication ##
    #----------------------#
    
    def request_auth(self):
        # Send commands to enter username/password

        self.control_conn.sendall(b"Enter username:")
        username = self.control_conn.recv(1024).decode("utf-8")

        self.control_conn.sendall(b"Enter Password:")
        password = self.control_conn.recv(1024).decode("utf-8")

        # Check if username/password are correct
        if username == admin_username and password == admin_password:
            self.control_conn.sendall(f"230 Greetings {username}".encode("utf-8"))
            logger("request_auth", 230, f"Client {username} has connected")
            return True
        else:
            self.control_conn.sendall(f"430 Incorrect username or password".encode("utf-8"))
            logger("request_auth", 430, "Access denied")
            return False

    #--------------------------#
    ## FTP Control Connection ##
    #--------------------------#

    def start_control_conn(self):
        # Start control connection
        self.send_control_msg("Welcome to the server!\n")

        # Check if user is authenticated
        accepted = self.request_auth()
        if not accepted:
            return

        # Main loop to listen for commands
        while True:
            cmd = self.recv_control_msg()
            if cmd == "STOR":
                self.STOR()
            elif cmd == "QUIT":
                self.QUIT()
                break
            else:
                logger("start_control_conn", 502, "Invalid command")
                break

    def send_control_msg(self, msg):
        # Sending control messages
        self.control_conn.sendall(msg.encode("utf-8"))

    def recv_control_msg(self):
        # Recieving commands from user
        return self.control_conn.recv(1024).decode("utf-8")

    #-----------------------#
    ## FTP Data Connection ##
    #-----------------------#

    def start_data_conn(self):
        # When user uses a command to transfer data
        # Start a new socket and bind to same IP on port 20
        self.data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data_sock.bind((HOST, 20))
        self.data_sock.listen(1)
        self.data_conn, self.data_addr = self.data_sock.accept()
        logger("start_control_conn", 225, "Data connection open")

    def close_data_conn(self):
        # When data transfer is finished
        # Close socket
        logger("close_data_conn", 226, "Data connection closed")
        self.data_addr = None
        self.data_conn.close()

    #----------------#
    ## FTP Commands ##
    #----------------#

    def QUIT(self):
        # User disconnects from server
        # Close control connection socket  
        logger("QUIT", 426, "Client has disconnected")
        self.control_conn.close()
        self.addr = None

    def STOR(self):
        # Stores file into server
        # Start data connection
        self.start_data_conn()

        # Request for file name and open file in write binary
        filename = self.data_conn.recv(1024).decode("utf-8")
        up_file = open(f"Server/{filename}", "wb")  
        
        # Keep writing data until user finishes sending file
        # [FLAG] - DONE - File completely sent by user
        while True:
            data = self.data_conn.recv(1024)
            if data == b"DONE":
                break
            up_file.write(data)
        
        logger("STOR", 250, "File stored successfully")
        up_file.close()
        self.close_data_conn()

def start_listening():
    # Socket listening over Ipv4 using TCP
    # Control connection socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    logger("start_listening", 220, "Server started for user")
    
    while True:
        conn, addr = sock.accept()  
        ftp_conn = FtpServer(conn, addr)
        ftp_conn.start_control_conn()

if __name__ == "__main__":
    start_listening()

