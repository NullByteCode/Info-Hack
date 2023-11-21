import sys

from tools.banner import grabbing
from tools.dnsresolver import resolver
from tools.portscan import scan
from tools.dirbrute import bruteforce
from tools.whois import get_whois
from tools.xss import scan_xss

linha = "-" * 78

logo= """
██╗███╗   ██╗███████╗ ██████╗       ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║████╗  ██║██╔════╝██╔═══██╗      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██║██╔██╗ ██║█████╗  ██║   ██║█████╗███████║███████║██║     █████╔╝
██║██║╚██╗██║██╔══╝  ██║   ██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗
██║██║ ╚████║██║     ╚██████╔╝      ██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

                  [✔] Developed by: SAYKE - ISL [✔]
                        [✔] Version 1.0.1 [✔]
            [✔] https://github.com/NullByteCode/Info-Hack [✔]
"""

OPTIONS = {
    "01": scan,
    "02": scan_xss,
    "03": resolver,
    "04": grabbing,
    "05": get_whois,
    "06": bruteforce,
    "00": sys.exit,
}


def menu_opcoes():
    print(linha)
    print(logo)
    print(linha)
    print("01 - ESCÂNER DE PORTAS")
    print("02 - ESCÂNER DE XSS")
    print("03 - RESOLVER O DNS")
    print("04 - COLETA DE BANNER")
    print("05 - INFORMAÇÕES WHOIS")
    print("06 - DESCOBERTA DE DIRETÓRIOS")
    print("00 - SAIR DO PROGRAMA")
    print(linha)


def obter_entrada_usuario():
    while True:
        entry = input("[+] SELECIONE A OPÇÃO: ")
        print(linha)
        if entry in OPTIONS:
            return entry
        else:
            print("OPÇÃO ONVÁLIDA, TENTE NOVAMENTE.")


def main():
    try:
        while True:
            menu_opcoes()
            entry = obter_entrada_usuario()
            if entry == "00":
                print(f"SAINDO!!!\n{linha}")
                sys.exit()
            OPTIONS[entry]()
    except KeyboardInterrupt:
        print("\n", end='')
        print(linha)
        print("ENCERRANDO O PROGRAMA.")
        print(linha)
        sys.exit()


if __name__ == "__main__":
    main()
