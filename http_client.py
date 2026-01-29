from socket import * 
import ssl # Added for SSL encryption

server_name = 'gaia.cs.umass.edu' 
server_port = 443 # Changed from 80 to 443 for HTTPS

# 1. Create a TCP socket (IPv4) 
client_socket = socket(AF_INET, SOCK_STREAM) 

# 2. Wrap socket with SSL
context = ssl.create_default_context()
secure_socket = context.wrap_socket(client_socket, server_hostname=server_name)

# 3. Connect to the server
secure_socket.connect((server_name, server_port))

# 4. Prepare the HTTP request 
request = "GET /kurose_ross/interactive/index.php HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n" 

# 5. Send the request 
secure_socket.send(request.encode()) 

# 6. Receive the response  
response = secure_socket.recv(4096) 

# 7. Decode and print the result 
print(response.decode()) 

# 8. Close the connection 
secure_socket.close() 