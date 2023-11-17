import socket
import sys


OPTION_MANUAL = "01"
OPTION_PADRAO = "02"
OPTION_COMPLETO = "03"
OPTION_ENTRY = ["01", "02", "03"]

linha = "-" * 78

def scan():
    try:
        print("01 - ESCÂNER MANUAL")
        print("02 - ESCÂNER PADRÃO")
        print("03 - ESCÂNER COMPLETO")
        print(linha)
        entry = input("[+] SELECIONE O TIPO DE SCAN: ")
        print(linha)
        if entry == OPTION_MANUAL:
            host = input("[+] DIGITE O HOST: ")
            print(linha)
            ports = input("[+] DIGITE AS PORTAS: ")
            for port in ports.split(" "):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((host, int(port)))
                if result == 0:
                    print("[+] PORTA {} ABERTA.".format(port))
                    print(linha)
                else:
                    print("[+] PORTA {} FECHADA.".format(port))
                    print(linha)
                sock.close()
        elif entry == OPTION_PADRAO:
            host = input("[+] DIGITE O HOST: ")
            print(linha)
            for port in range(1, 1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((host, port))
                if result == 0:
                    print("[+] PORTA {} ABERTA.".format(port))
                    print(linha)
                else:
                    print("[+] PORTA {} FECHADA.".format(port))
                    print(linha)
                sock.close()
        elif entry == OPTION_COMPLETO:
            host = input("[+] DIGITE O HOST: ")
            print(linha)
            for port in range(1, 65535):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((host, port))
                if result == 0:
                    print("[+] PORTA {} ABERTA.".format(port))
                    print(linha)
                else:
                    print("[+] PORTA {} FECHADA.".format(port))
                    print(linha)
                sock.close()
        elif entry != OPTION_ENTRY:
            print("[+] MODO DE USO - ESCOLHA ENTRE: 01, 02, 03")
            print(linha)
            sys.exit()
        else:
            print(linha)
            print("[+] OCORREU UM ERRO INESPERADO.")
            print(linha)
            sys.exit()
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
