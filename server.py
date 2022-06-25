import socket
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 21       # FTP Control Port 
curr_server_dir = os.path.abspath('./Server')

admin_username = "Test"
admin_password = "123"

class FtpServer():
    def __init__(self, conn, addr):
        self.curr_server_dir = curr_server_dir
        self.control_conn = conn
        self.addr = addr
        self.data_conn = None

    def request_auth(self):
        """
        Checks if user username/password is correct

        Returns:
            Boolean: True if successfully authenticated, otherwise False
        """
        self.control_conn.sendall(b"Enter username:")
        username = self.control_conn.recv(1024).decode("utf-8")
        self.control_conn.sendall(b"Enter Password:")
        password = self.control_conn.recv(1024).decode("utf-8")

        if username == admin_username and password == admin_password:
            self.control_conn.sendall(f"Greetings {username}".encode("utf-8"))
            return True
        else:
            self.control_conn.sendall(f"Access Denied".encode("utf-8"))
            return False
       
    def start_control_conn(self):
        """
        Start Ccontrol Connection
        """
        self.control_conn.sendall(b"Welcome to the server!\n")
        accepted = self.request_auth()
        if not accepted:
            return

def start_listening():
    # Socket listening over Ipv4 using TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    print("Server is listening...")
    
    while True:
        conn, addr = sock.accept()  
        ftp_conn = FtpServer(conn, addr)
        ftp_conn.start_control_conn()

if __name__ == "__main__":
    start_listening()

