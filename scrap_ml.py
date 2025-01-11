import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


def buscar_html(busca):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    busca_ifem = busca.replace(" ", "-")
    busca_perct = busca.replace(" ", "%20")
    url = f"https://lista.mercadolivre.com.br/{busca_ifem}#D[A:{busca_perct}]"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Erro ao buscar HTML: {e}")
        return None


def parser_html(html):
    soup = BeautifulSoup(html, "html.parser")
    produtos_nome = soup.find_all("a", class_="poly-component__title")
    produtos_precos = soup.find_all("span", class_="andes-money-amount andes-money-amount--cents-superscript")
    links = soup.find_all("a", class_="poly-component__title")
    
    produtos = zip(produtos_nome, produtos_precos, links)
    return list(produtos)


def gerar_planilha(pesquisa):
    if pesquisa:
        wb = Workbook()
        sheet = wb.active
        sheet["A1"] = "Nome"
        sheet["B1"] = "Preço"
        sheet["C1"] = "Link"  

        for linha, (nome, preco, link) in enumerate(pesquisa, start=2):
            sheet[f"A{linha}"] = nome.text.strip()
            sheet[f"B{linha}"] = preco.text.strip()
            sheet[f"C{linha}"].hyperlink = link['href'] if 'href' in link.attrs else ""

        wb.save(f"Cotação de {busca}.xlsx")
        print("Arquivo gerado com sucesso!")
    else:
        print("Não foi possível gerar o arquivo!")


busca = input("Digite o nome do produto: ")

codigo_html = buscar_html(busca)

if codigo_html:
    pesquisa = parser_html(codigo_html)
    if pesquisa:
        gerar_planilha(pesquisa)
    else:
        print("Nenhum dado foi encontrado.")
else:
    print("Erro ao buscar HTML.")
