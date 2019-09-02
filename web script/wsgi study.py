#coding:utf-8

import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

body = '''socket test <h1> wsgi study</h1>'''
response_params = ['Content-Type: html; charset=utf-8',body]
response = '\r\n'.join(response_params)

print(response)

def handle_connection(conn,addr):
	request =b""
	while EOL1 not in request and EOL2 not in request:
		request = request + conn.recv(1024)
		print(request)
		conn.send(response.encode())
		conn.close
def main():
	serversk =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serversk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)0.0
	serversk.bind(('127.0.0.1',8000))
	serversk.listen(5)


	try:
		while True:

			conn,address = serversk.accept()
			handle_connection(conn,address)

	finally:
			serversk.close()

if __name__ == '__main__':
	main()

