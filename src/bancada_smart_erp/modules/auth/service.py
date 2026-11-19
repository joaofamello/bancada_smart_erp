from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from bancada_smart_erp.database.models import Usuario

@dataclass(frozen=True)
class UsuarioAutenticado:
    id: int
    nome: str
    email: str
    nivel_acesso: str

def autorizar_usuario(
        db: Session,
        email: str | None,
        google_sub: str | None,
        email_verificado: bool,
) -> UsuarioAutenticado | None:
    """Confere se a conta Google pode usar o sistema."""
    email = (email or "").strip().lower()
    if not email or not google_sub or not email_verificado:
        return None

    usuario = db.scalar(select(Usuario).where(Usuario.email == email))
    if usuario is None or not usuario.ativo:
        return None
    elif usuario.google_sub != google_sub:
        return None

    return UsuarioAutenticado(
        id=usuario.id,
        nome=usuario.nome,
        email=usuario.email,
        nivel_acesso=usuario.nivel_acesso,
    )

