import customtkinter as ctk
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from tkinter import messagebox

# ========== Funções ==========
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
        messagebox.showerror("Erro de conexão", f"Erro ao buscar HTML: {e}")
        return None

def parser_html(html):
    soup = BeautifulSoup(html, "html.parser")
    produtos_nome = soup.find_all("a", class_="poly-component__title")
    produtos_precos = soup.find_all("span", class_="andes-money-amount andes-money-amount--cents-superscript")
    links = soup.find_all("a", class_="poly-component__title")

    produtos = zip(produtos_nome, produtos_precos, links)
    return list(produtos)

def gerar_planilha(pesquisa, busca):
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

        nome_arquivo = f"Cotação de {busca}.xlsx"
        wb.save(nome_arquivo)
        messagebox.showinfo("Sucesso", f"Planilha gerada: {nome_arquivo}")
    else:
        messagebox.showwarning("Aviso", "Nenhum dado encontrado para gerar o arquivo.")

def iniciar_busca():
    busca = entrada.get().strip()
    if not busca:
        messagebox.showwarning("Campo vazio", "Digite o nome de um produto.")
        return

    status_label.configure(text="Buscando, aguarde...")
    app.update()

    html = buscar_html(busca)
    if html:
        pesquisa = parser_html(html)
        if pesquisa:
            gerar_planilha(pesquisa, busca)
        else:
            messagebox.showinfo("Resultado", "Nenhum produto encontrado.")
    status_label.configure(text="")

# ========== Interface Moderna ==========
ctk.set_appearance_mode("light")  # "dark" ou "light"
ctk.set_default_color_theme("blue")  # azul padrão

app = ctk.CTk()
app.title("Cotação Mercado Livre")
app.geometry("450x250")
app.resizable(False, False)

# Cores
COR_AZUL = "#105EDD"
COR_BRANCO = "#FFFFFF"
COR_PRETO = "#000000"

# Fundo branco
app.configure(fg_color=COR_BRANCO)

frame = ctk.CTkFrame(app, fg_color=COR_BRANCO)
frame.pack(padx=20, pady=20, fill="both", expand=True)

titulo = ctk.CTkLabel(frame, text="Cotação Mercado Livre", font=("Arial", 18, "bold"), text_color=COR_PRETO)
titulo.pack(pady=(0, 10))

entrada = ctk.CTkEntry(frame, width=300, height=35, placeholder_text="Digite o nome do produto", font=("Arial", 12))
entrada.pack(pady=10)
entrada.focus()

botao = ctk.CTkButton(
    frame,
    text="Pesquisar",
    command=iniciar_busca,
    width=150,
    height=40,
    corner_radius=20,
    fg_color=COR_AZUL,
    hover_color="#0d4ccc",
    font=("Arial", 12, "bold"),
    text_color=COR_BRANCO
)
botao.pack(pady=10)

status_label = ctk.CTkLabel(frame, text="", font=("Arial", 10), text_color=COR_PRETO)
status_label.pack(pady=(5, 0))

app.mainloop()
