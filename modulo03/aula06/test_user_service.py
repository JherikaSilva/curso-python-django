import pytest
from database import DatabaseConnection
from user_service import UserService
from user_model import UserModel

@pytest.fixture
def conexao_db_limpa():
    """Cria um DB temporário (:memory:) e garante o fechamento (Teardown)."""

    conexao = DatabaseConnection(db_name=":memory:")

    yield conexao  
    
    conexao.fechar()



@pytest.fixture
def user_service(conexao_db_limpa):
    """Monta o UserService, INJETANDO a Conexao limpa."""
   
    return UserService(db_conn=conexao_db_limpa)

def test_safe_user(user_service):

    email = "jherika@gmail"
    nome = "JherikaSilva"
    perfil = "Diretoria"

  
    ok= user_service.user_model.create_user("12345_hash", email, nome, perfil)
    assert ok

    resultado_obtido = user_service._safe_user_data(ok)

    resultado_esperado = {
        "email": email,
        'nome_completo': nome,
        'perfil_acesso': perfil,
    }

    assert resultado_obtido == resultado_esperado