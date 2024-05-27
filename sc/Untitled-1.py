import socket
def startsv():
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind(('127.0.0.1',2000))
        soc.listen(4)
        while True:
            print('all working')
            client_socket, adress = soc.accept()
            data = client_socket.recv(1024).decode('utf-8')
            #print(data)
            
            cont = loadp(data)
            client_socket.send(cont)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        soc.close()
        print('shut')


def loadp(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    with open('ht'+path,'rb') as file:
        response = file.read()
    return HDRS.encode('utf-8') + response


if __name__ == '__main__':
    startsv()