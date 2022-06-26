# Transfer

FTP server for transfering files. Goal is to allow transfering files from mobile device to computer using FTP Protocol.

## Running

Clone project, run server and client seperatly

```bash
git clone https://github.com/DeepP2667/Transfer.git
```

```python
python server.py
python client.py
```

## FTP Commands (WIP)

QUIT - Disconnects client from server  
STOR - Stores file in server (Currently only works when given a file in the same directory)

## Helpful Links

[FTP Protocol](https://datatracker.ietf.org/doc/html/rfc959)  
[FTP Status Codes](https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes)  
[FTP Commands](https://en.wikipedia.org/wiki/List_of_FTP_commands)
