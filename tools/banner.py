import socket
import sys

linha = "-" * 78

def grabbing():
    try:
        print("[+] MODO DE USO: 192.168.0.1, 22")
        print(linha)
        ip = input("[+] DIGITE O HOST: ")
        print(linha)
        porta = input("[+] DIGITE A PORTA ")
        print(linha)
        meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        meusocket.connect((ip, porta))
        banner = meusocket.recv(1024)
        print(banner)
        meusocket.close()
    except KeyboardInterrupt:
        print(linha)
        print("[+] ENCERRANDO O PROGRAMA.")
        print(linha)
        sys.exit()
    except socket.gaierror:
        print(linha)
        print("[+] O HOST NÃO PODE SER RESOLVIDO.")
        print(linha)
        sys.exit()
    except socket.timeout:
        print(linha)
        print("[+] A CONEXÃO EXPIROU.")
        print(linha)
        sys.exit()
    except socket.error:
        print(linha)
        print("[+] NÃO FOI POSSÍVEL CONECTAR-SE AO SERVIDOR.")
        print(linha)
        sys.exit()
