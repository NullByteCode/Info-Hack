import sys

import whois

linha = "-" * 78

def get_whois():
    try:
        print("MODO DE USO: www.teste.com")
        print(linha)
        url = input("DIGITE A URL: ")
        print(linha)
        who = whois.whois(url)
        print(who)
        sys.exit()
    except KeyboardInterrupt:
        print(linha)
        print("ENCERRANDO O PROGRAMA.")
        print(linha)
        sys.exit()
