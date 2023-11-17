import socket
import sys

linha = "-" * 78

def resolver():
    try:
        print("MODO DE USO: www.teste.com")
        print(linha)
        host = input("DIGITE O HOST: ")
        print(linha)
        print(host, ">>>>>>>>>>>", socket.gethostbyname(host))
        print(linha)
        sys.exit()
    except KeyboardInterrupt:
        print(linha)
        print("ENCERRANDO O PROGRAMA.")
        print(linha)
        sys.exit()
    except socket.gaierror:
        print(linha)
        print("O HOST NÃO PODE SER RESOLVIDO.")
        print(linha)
        sys.exit()
    except socket.timeout:
        print(linha)
        print("A CONEXÃO EXPIROU.")
        print(linha)
        sys.exit()
    except socket.error:
        print(linha)
        print("NÃO FOI POSSÍVEL CONECTAR-SE AO SERVIDOR.")
        print(linha)
        sys.exit()
