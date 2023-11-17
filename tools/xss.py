import sys

import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

linha = "-" * 78

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = [{"type": input_tag.get("type", "text"), "name": input_tag.get("name")} for input_tag in form.find_all("input")]
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    data = {input_tag["name"]: value if input_tag["type"] in ["text", "search"] else input_tag.get("value") for input_tag in form_details["inputs"] if input_tag.get("name")}
    print(f"[+] ENVIANDO CARGA MALICIOSA PARA: {target_url}")
    print(linha)
    print(f"[+] DADOS: {data}")
    print(linha)
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)


def scan_xss():
    url = input("[+]DIGITE A URL QUE DESEJA ENCANEAR PARA XSS: ")
    print(linha)
    forms = get_all_forms(url)
    print(f"[+] DETECTADO {len(forms)} FORMULÁRIO EM: {url}.")
    print(linha)
    js_script = "<script>alert('Hello')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        response = submit_form(form_details, url, js_script).content.decode()
        if js_script in response:
            print(f"[+] XSS DETECTADO EM: {url}")
            print(linha)
            is_vulnerable = True
    if not is_vulnerable:
        print("[+] VULNERABILIDADE XSS NÃO ENCONTRADA.")
        print(linha)
    sys.exit()
