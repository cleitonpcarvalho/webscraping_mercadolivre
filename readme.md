# Cotação de Produtos no Mercado Livre com Webscraping

## 🚀 Sobre o Projeto

Este projeto tem como objetivo realizar a **cotação de produtos** no **Mercado Livre** e gerar uma planilha em formato **Excel** (.xlsx) contendo o **nome do produto**, o **preço** e o **link** do produto. É uma ferramenta simples e eficiente para quem deseja comparar preços de diferentes vendedores de um mesmo produto na plataforma.

## 💡 Funcionalidades

- **Busca personalizada**: O usuário pode pesquisar qualquer produto disponível no Mercado Livre.
- **Extração de dados**: Coleta automaticamente informações como nome, preço e link do produto.
- **Exportação para Excel**: Gera uma planilha Excel com os dados coletados, facilitando a visualização e o uso dos resultados.

## 📦 Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- `requests`: Para realizar as requisições HTTP ao Mercado Livre.
- `beautifulsoup4`: Para fazer o parsing e extração de dados do HTML.
- `openpyxl`: Para gerar o arquivo Excel.

Você pode instalar essas dependências usando o **pip**. Execute o seguinte comando no terminal:

```bash
pip install requests beautifulsoup4 openpyxl
```

## 📝 Como Usar

1. **Clone este repositório** ou baixe o código fonte.
2. **Instale as dependências** (conforme explicado acima).
3. **Execute o script**:

```bash
python nome_do_arquivo.py
```

4. **Digite o nome do produto** quando solicitado. O código buscará automaticamente os resultados no Mercado Livre.
5. O script gerará um arquivo **Excel** com as informações encontradas.

O arquivo será salvo com o nome `Cotação de [nome_do_produto].xlsx`.

## ⚙️ Como Funciona

### 🧑‍💻 Função `buscar_html(busca)`

Esta função recebe o nome do produto como argumento, cria a URL de busca para o Mercado Livre, e faz uma requisição HTTP para obter o HTML da página de resultados.

- **Entrada**: Nome do produto (por exemplo, "smartphone").
- **Saída**: O código HTML da página de resultados de busca do Mercado Livre ou `None` em caso de erro.

### 🔍 Função `parser_html(html)`

Recebe o HTML da página e utiliza o **BeautifulSoup** para extrair as informações de nome, preço e link dos produtos. A função retorna uma lista com essas informações para cada produto encontrado.

- **Entrada**: Código HTML da página.
- **Saída**: Lista de tuplas contendo o nome, o preço e o link
