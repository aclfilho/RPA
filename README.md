Tecnologias Utilizadas
Python
  Selenium(automação web)
  Pandas(mmanipulaçãod e dados)
Micrsoft Edge WebDriver(navegador)

Estrutura do Projeto
Automacao
│── RPA.py                # Script principal de automação
│── cotacoes.xlsx          # Arquivo gerado com as cotações
│── README.md              # Documentação do projeto
│── requirements.txt       # Dependências do projeto

1- Instalar e Executar
git clone https://github.com/seu-usuario/Automacao_Cotacoes.git
cd Automacao_Cotacoes

2- Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

3 - Instale as dependencias
pip install -r requirements.txt

4 - Execute o script
python RPA.py
