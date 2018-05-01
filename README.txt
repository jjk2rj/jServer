README

Server -
The server listens for connections and receives 
data transfers through a socket that is up to 4096
in size.

Server Arugments:
	1. Optional port number 
		If no port number is provided, default port number is 2345 

Client -
	The client connects to the desired server ands
	sends the files to the server in 4096 byte chunks,	
	The client will then display the hash followed by the file name.

Client Arguments:
	1. Port number - Optional 
		-p <port number>
	2. IP address
	2. Hashing algorithm 
		The following algorithms will be accepted:
		sha1, sha256, sha512, and md5
	3. File names
		At least one file name is required
		Separate multiple files with a ' '

Example: 
	./hashclient -p 7777 127.0.0.1 sha1 hello.txt

Instructions: 
1. Run the Server 
2. Run the Client