# Cadastro produtos
Automação para cadastro de produtos em site
# 🤖 Automação de Cadastro de Produtos com PyAutoGUI

Projeto de automação (RPA) desenvolvido em Python para automatizar o processo de login e o cadastro em lote de produtos em uma plataforma web a partir de uma base de dados local em arquivo CSV.

---

## 📌 Funcionalidades

- **Abertura automática do navegador:** Inicializa o Microsoft Edge e navega até a URL da aplicação de cadastro.
- **Login automático:** Preenche as credenciais de acesso e submete o formulário de login.
- **Importação de dados:** Faz a leitura da tabela de produtos (`Produtos.csv`) utilizando a biblioteca `pandas`.
- **Cadastro em lote:** Itera sobre as linhas da planilha preenchendo automaticamente os campos:
  - Código
  - Marca
  - Tipo
  - Categoria
  - Preço unitário
  - Custo
  - Observações (quando existentes)
- **Submissão contínua:** Envia os dados e reinicia o cursor/foco para o próximo registro até finalizar toda a base.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** (versão 3.10 ou superior recomendada)
- **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Biblioteca para controle programático de teclado e mouse.
- **[Pandas](https://pandas.pydata.org/):** Leitura, manipulação e análise de dados em formato tabular.

---

## 📋 Pré-requisitos

1. Ter o **Python** instalado em seu computador.
2. Manter o arquivo `Produtos.csv` no mesmo diretório do script principal.
3. Instalar as dependências do projeto.

---

## 🚀 Como Executar

### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
