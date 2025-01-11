```markdown
# 🛍️ **Scraper de Cotação de Produtos no Mercado Livre** 🛒

Bem-vindo ao repositório do scraper de cotação de produtos no Mercado Livre! Aqui você vai encontrar um código simples mas poderoso que busca informações sobre preços de produtos e gera uma planilha Excel com esses dados. O script utiliza **Python**, **BeautifulSoup** para parsing HTML, **requests** para fazer requisições HTTP e **openpyxl** para criar a planilha.

## 🚀 **Objetivo**

O objetivo deste projeto é automatizar a busca por preços de produtos no Mercado Livre e gerar uma planilha Excel com os seguintes dados:
- Nome do produto
- Preço do produto
- Link do produto

Com esse scraper, você pode facilmente comparar preços de vários produtos diretamente na plataforma!

## 🔧 **Tecnologias Utilizadas**

- **requests**: Para realizar requisições HTTP e obter o conteúdo das páginas web.
- **BeautifulSoup**: Para fazer parsing do HTML e extrair as informações relevantes.
- **openpyxl**: Para criar e manipular a planilha Excel.

## ⚙️ **Como Funciona?**

1. O código começa pedindo ao usuário o nome de um produto.
2. A partir do nome do produto, ele busca o HTML da página de resultados do Mercado Livre.
3. O HTML é então analisado, e os dados dos produtos são extraídos: nome, preço e link.
4. Esses dados são organizados e salvos em uma planilha Excel com três colunas: **Nome**, **Preço** e **Link**.
5. Ao final, o arquivo gerado é salvo com o nome `Cotação de [produto].xlsx`.

## 📦 **Requisitos**

Antes de rodar o código, você precisa ter as bibliotecas necessárias instaladas. Você pode instalá-las com o seguinte comando:

```bash
pip install requests beautifulsoup4 openpyxl
```

## 📝 **Exemplo de Uso**

1. Clone o repositório para sua máquina local:
   
   ```bash
   git clone https://github.com/SeuUsuario/scraper-mercadolivre.git
   cd scraper-mercadolivre
   ```

2. Execute o script:

   ```bash
   python scraper_mercadolivre.py
   ```

3. O script irá pedir para você digitar o nome do produto que deseja pesquisar. Exemplo:

   ```
   Digite o nome do produto: notebook
   ```

4. Após a execução, será gerado um arquivo Excel com as cotações dos produtos encontrados.

   - O arquivo gerado terá o nome: `Cotação de notebook.xlsx`

## 📊 **Exemplo de Planilha Gerada**

A planilha gerada será organizada da seguinte forma:

| **Nome**                  | **Preço** | **Link**                                                |
|---------------------------|-----------|---------------------------------------------------------|
| Notebook Dell Inspiron 15  | R$ 2.499  | [Link](https://www.mercadolivre.com.br)                  |
| Notebook Acer Aspire 5     | R$ 2.199  | [Link](https://www.mercadolivre.com.br)                  |

## 🧑‍💻 **Como o Código Funciona**

### 1. **Buscar HTML do Mercado Livre**

A função `buscar_html(busca)` realiza uma requisição para o Mercado Livre, utilizando o nome do produto informado pelo usuário.

- **Objetivo**: Obter o conteúdo HTML da página de resultados.
- **Tecnologia usada**: `requests.get()`

```python
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
```

### 2. **Parser do HTML**

A função `parser_html(html)` usa o BeautifulSoup para analisar o HTML e extrair os dados dos produtos: nome, preço e link.

- **Objetivo**: Extrair dados relevantes do HTML.
- **Tecnologia usada**: `BeautifulSoup`

```python
def parser_html(html):
    soup = BeautifulSoup(html, "html.parser")
    produtos_nome = soup.find_all("a", class_="poly-component__title")
    produtos_precos = soup.find_all("span", class_="andes-money-amount andes-money-amount--cents-superscript")
    links = soup.find_all("a", class_="poly-component__title")
    
    produtos = zip(produtos_nome, produtos_precos, links)
    return list(produtos)
```

### 3. **Gerar Planilha Excel**

A função `gerar_planilha(pesquisa)` pega os dados extraídos e cria uma planilha Excel com três colunas: **Nome**, **Preço** e **Link**.

- **Objetivo**: Gerar e salvar uma planilha Excel.
- **Tecnologia usada**: `openpyxl`

```python
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
```

## ⚠️ **Erros Possíveis**

1. **Erro de Conexão**: Caso o Mercado Livre esteja fora do ar ou a URL não seja encontrada.
2. **Erro ao Gerar Planilha**: Se não houver dados suficientes para gerar a planilha.

## 🤖 **Sobre o Código**

O código foi desenvolvido para ser simples, eficiente e funcional. Ele utiliza técnicas de web scraping para extrair informações úteis de uma plataforma popular, permitindo comparar preços de produtos de maneira rápida e prática. E o melhor: tudo é armazenado em um arquivo Excel, facilitando a análise posterior.

## 💡 **Contribua!**

Se você tiver sugestões ou melhorias para este projeto, fique à vontade para abrir uma **issue** ou fazer um **pull request**!

---

Feito com 💙 por [Seu Nome](https://github.com/cleitonpcarvalho)
```
