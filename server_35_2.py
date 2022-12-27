import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break


            def ceaser_code(sentence, value):
                try:
                    sentence = sentence.decode('utf-8')
                    value = int(value)
                    word_list = list(sentence)
                    encrypt_list = []
                    for letter in word_list:
                        encrypt = ord(letter)
                        if 90 >= encrypt >= 65:
                            encrypt_value = encrypt + value
                            if encrypt_value > 90:
                                res = (encrypt_value - 90) + 64
                                encrypt_list.append(chr(res))
                            else:
                                encrypt_list.append(chr(encrypt_value))
                        elif 122 >= encrypt >= 97:
                            encrypt_value = encrypt + value
                            if encrypt_value > 122:
                                res = (encrypt_value - 122) + 96
                                encrypt_list.append(chr(res))
                            else:
                                encrypt_list.append(chr(encrypt_value))
                        else:
                            encrypt_list.append(chr(encrypt))
                    result = ''.join(encrypt_list)
                    return result.encode('utf-8')

                except Exception:
                    return "Sorry"


            res = ceaser_code(data, 5)
            conn.sendall(res)
