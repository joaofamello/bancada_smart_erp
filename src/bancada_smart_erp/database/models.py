from sqlalchemy import Column, DateTime, Boolean, BigInteger, String, Text, Enum, func, ForeignKey
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