Claro, Cleiton! Aqui está seu `README.md` **atualizado**, com:

* Explicação da nova **interface moderna com `customtkinter`**
* Comando atualizado de execução com `app.py`
* Link para o **vídeo no YouTube**
* Correção da URL de clonagem
* Ajustes de clareza e organização visual

---

````markdown
# Scraper de Cotação de Produtos no Mercado Livre 🛒📊

Bem-vindo ao repositório do scraper de cotação de produtos no Mercado Livre! Este projeto automatiza a busca de preços de produtos na plataforma e gera uma **planilha Excel** com os dados encontrados. Agora com uma interface gráfica **moderna e intuitiva** usando `customtkinter`.

## 🎯 Objetivo

O app permite que você:

- Digite o nome de um produto
- Consulte automaticamente os preços no Mercado Livre
- Gere uma planilha `.xlsx` com os seguintes dados:
  - ✅ Nome do produto
  - ✅ Preço
  - ✅ Link para o anúncio

## ✨ Tecnologias Utilizadas

- `requests`: Requisições HTTP
- `BeautifulSoup`: Extração e parsing do HTML
- `openpyxl`: Geração de planilhas Excel
- `customtkinter`: Interface gráfica moderna com bordas arredondadas e tema azul

---

## 💻 Interface Moderna

O projeto conta com uma interface gráfica responsiva:

- Campo para digitar o nome do produto
- Botão estilizado em azul com cantos arredondados
- Mensagens visuais de carregamento e conclusão

📺 **Veja o projeto funcionando no YouTube:**  
👉 [https://www.youtube.com/watch?v=PYpRjSfytJ4](https://www.youtube.com/watch?v=PYpRjSfytJ4)

---

## 🚀 Como Usar

### 1. Clone o repositório:

```bash
git clone https://github.com/cleitonpcarvalho/webscraping_mercadolivre.git
cd webscraping_mercadolivre
````

### 2. Crie e ative o ambiente virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou, se preferir:

```bash
pip install requests beautifulsoup4 openpyxl customtkinter
```

### 4. Execute a aplicação com interface:

```bash
python3 app.py
```

---

## 📦 Exemplo de Planilha Gerada

| **Nome**                  | **Preço** | **Link**                                |
| ------------------------- | --------- | --------------------------------------- |
| Notebook Dell Inspiron 15 | R\$ 2.499 | [Link](https://www.mercadolivre.com.br) |
| Notebook Acer Aspire 5    | R\$ 2.199 | [Link](https://www.mercadolivre.com.br) |

---

## 🧠 Estrutura do Código

### 🔍 `buscar_html(busca)`

Responsável por buscar o HTML da página de resultados do Mercado Livre.

### 🔎 `parser_html(html)`

Usa BeautifulSoup para extrair os nomes, preços e links dos produtos listados.

### 📥 `gerar_planilha(pesquisa, busca)`

Gera e salva a planilha Excel com os dados coletados.

### 🖥️ `app.py`

Contém a interface gráfica desenvolvida com `customtkinter`.

---

## ⚠️ Possíveis Erros

* **Erro de conexão**: problema com a internet ou mudança na estrutura do site.
* **Nenhum produto encontrado**: caso o nome pesquisado não retorne resultados válidos.

---

## 🤝 Contribua

Achou um bug ou tem sugestões de melhoria?
Abra uma [issue](https://github.com/cleitonpcarvalho/webscraping_mercadolivre/issues) ou envie um pull request!

---

Feito com 💙 por [Cleiton Carvalho](https://github.com/cleitonpcarvalho)

```

---

```
