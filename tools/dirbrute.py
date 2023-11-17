import sys

import requests

linha = "-" * 78

def bruteforce():
    try:
        print("[+] MODO DE USO: teste.com")
        print(linha)
        with open("tools/diretorios.txt") as file:
            url = input("[+] DIGITE A URL: ")
            if not url.startswith("https://"):
                url = "https://" + url
            for diretorio in file:
                diretorio = diretorio.strip()
                url_final = "{}/{}".format(url, diretorio)
                response = requests.get(url_final)
                code = response.status_code
                if code == 200:
                    print(linha)
                    print("[+] DIRETÓRIO ENCONTRADO: {}".format(url_final))
                elif code != 200:
                    print(linha)
                    print("[+] DIRETÓRIO NÃO ENCONTRADO.")
                else:
                    print(linha)
                    print("[+] OCORREU UM ERRO INESPERADO.")
                    print(linha)
                    sys.exit()
    except requests.ConnectionError:
        print(linha)
        print("[+] OCORREU UM ERRO DE CONEXÃO.")
        print(linha)
        sys.exit()
    except requests.Timeout:
        print(linha)
        print("[+] A REQUISIÇÃO EXCEDEU O TEMPO LIMITE.")
        print(linha)
        sys.exit()
    except requests.HTTPError:
        print(linha)
        print("[+] OCORREU UM ERRO DE HTTP.")
        print(linha)
        sys.exit()
    except KeyboardInterrupt:
        print(linha)
        print("[+] ENCERRANDO O PROGRAMA.")
        print(linha)
        sys.exit()
