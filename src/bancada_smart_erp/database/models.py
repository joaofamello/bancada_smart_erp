from sqlalchemy import Column, DateTime, Boolean, Integer, BigInteger, String, Text, Enum, func, ForeignKey, Float
from bancada_smart_erp.database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    NIVEL_ACESSO = Enum("admin", "operador", name="nivel_acesso_enum")

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    email = Column("email", String, unique=True, nullable=False)
    google_sub = Column("google_sub", String, unique=True, nullable=False)
    nome = Column("nome", String, nullable=False)
    nivel_acesso = Column(NIVEL_ACESSO, default="operador", nullable=False)
    ativo = Column("ativo", Boolean, nullable=False, default=True)
    criado_em = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    criado_por = Column(BigInteger, ForeignKey("usuarios.id"), nullable=True)

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    cpf = Column("cpf", String, nullable=False)
    telefone = Column("telefone", String, nullable=False)
    endereco = Column("endereco", Text, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False, default=True)
    criado_em = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    criado_por = Column(BigInteger, ForeignKey("usuarios.id"), nullable=True)

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    razao_social = Column("razao_social", String, nullable=False)
    cnpj = Column("cnpj", String, nullable=False)
    telefone = Column("telefone", String, nullable=False)
    email = Column("email", String, nullable=False)
    endereco = Column("endereco", Text, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False, default=True)
    criado_em = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    criado_por = Column(BigInteger, ForeignKey("usuarios.id"), nullable=True)

class Marca(Base):
    __tablename__ = "marcas"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)

class ModeloCelular(Base):
    __tablename__ = "modelos_celulares"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    marca_id = Column("marca_id", BigInteger, ForeignKey("marcas.id"), nullable=False)

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)

class Servico(Base):
    __tablename__ = "servicos"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    preco_padrao = Column("preco_padrao", Float, nullable=False, default=0.0)
    ativo = Column("ativo", Boolean, nullable=False, default=True)

class TipoDefeito(Base):
    __tablename__ = "tipos_defeitos"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)

class Produto(Base):
    __tablename__ = "produtos"

    TIPO_PRODUTO = Enum("aparelho", "acessorio", "peca", name="tipo_produto_enum")

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    tipo = Column("tipo", TIPO_PRODUTO, nullable=False)
    nome = Column("nome", String, nullable=False)
    categoria_id = Column("categoria_id", BigInteger, ForeignKey("categorias.id"), nullable=False)
    preco_venda = Column("preco_venda", Float, nullable=False, default=0.0)
    custo_medio = Column("custo_medio", Float, nullable=False, default=0.0)
    estoque_atual = Column("estoque_atual", Integer, nullable=False, default=0)
    estoque_minimo = Column("estoque_minimo", Integer, nullable=False, default=0)
    ativo = Column("ativo", Boolean, default=True, nullable=False)
    criado_em = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    criado_por = Column(BigInteger, ForeignKey("usuarios.id"), nullable=True)
