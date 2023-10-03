import os

# Caminho para o arquivo da planilha
arquivo_planilha = os.path.join(os.getcwd(), "planilha.json")

# Criação do servidor Flask
app = Flask(__name__)

# Leitura da planilha de dados
with open(arquivo_planilha, "r") as f:
    dados = json.load(f)

# Retorno da planilha em JSON
@app.route("/index")
def index():
    return json.dumps(dados)

# Execução do servidor Flask
app.run(host="0.0.0.0", port=8080)