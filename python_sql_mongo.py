import os
import sqlalchemy.orm as sa

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho para o banco de dados SQLite
arquivo_banco = os.path.join(os.getcwd(), "banco.sqlite")

# Criação da engine de conexão
engine = create_engine(f"sqlite:///{arquivo_banco}")

# Criação do mapper base
Base = declarative_base()

# Criação das classes de modelo
class Cliente(Base):
    __tablename__ = "clientes"

    id = sa.Column(sa.Integer, primary_key=True)
    nome = sa.Column(sa.String(255), nullable=False)
    idade = sa.Column(sa.Integer, nullable=False)

class Conta(Base):
    __tablename__ = "contas"

    id = sa.Column(sa.Integer, primary_key=True)
    numero = sa.Column(sa.String(255), nullable=False)
    saldo = sa.Column(sa.Float, nullable=False)
    cliente_id = sa.Column(sa.Integer, sa.ForeignKey("clientes.id"))

# Criação da sessão de banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de dados
cliente1 = Cliente(nome="Fulano", idade=30)
cliente2 = Cliente(nome="Beltrano", idade=25)

conta1 = Conta(numero="1234-5678-9012-3456", saldo=1000.0, cliente=cliente1)
conta2 = Conta(numero="9876-5432-1098-7654", saldo=500.0, cliente=cliente2)

session.add(cliente1)
session.add(cliente2)
session.add(conta1)
session.add(conta2)

session.commit()

# Recuperação de dados
clientes = session.query(Cliente).all()

for cliente in clientes:
    print(cliente.nome, cliente.idade)

contas = session.query(Conta).all()

for conta in contas:
    print(conta.numero, conta.saldo, conta.cliente.nome)
