from exercicios import Inventario
import pytest

def test_adicionar_produto_novo():
    adc=Inventario()
    adc.adicionar_produto("Martelo", 10)
    adc.adicionar_produto("Faca", 20)
    resultado_obtido= adc.lista_estoque
    resultado_esperado= [{"produto": "Martelo", "quantidade": 10},{"produto":"Faca", "quantidade":20}]

    assert resultado_obtido== resultado_esperado

def test_adicionar_produto_existente():
    adc=Inventario()
    adc.adicionar_produto("Martelo", 10)
    adc.adicionar_produto("Martelo", 20)
    adc.adicionar_produto("Martelo", 10)
    
    resultado_obtido= adc.lista_estoque
    resultado_esperado= [{"produto": "Martelo", "quantidade": 40}]
    assert resultado_obtido== resultado_esperado


def test_remover_produto():
    rem=Inventario()
    rem.adicionar_produto("Martelo", 10)
    rem.adicionar_produto("Faca", 20)

    rem.remover_produto("Martelo")  

    resultado_obtido= rem.lista_estoque
    resultado_esperado= [{"produto":"Faca", "quantidade":20}]

    assert resultado_obtido== resultado_esperado

def test_remover_produto_ValueError():
    rem=Inventario()
    rem.adicionar_produto("Martelo", 10)
    rem.adicionar_produto("Faca", 20)
    with pytest.raises(ValueError) as r:
        rem.remover_produto("Relogio")
    assert "Produto não encontrado" in str(r.value)

def test_vender_item():
    adc=Inventario()

    adc.adicionar_produto("Martelo", 10)
    adc.adicionar_produto("Faca", 20)        

    adc.vender_item("Martelo", 5)

    resultado_obtido= adc.lista_estoque
    resultado_esperado=[{"produto": "Martelo" , "quantidade": 5},{"produto": "Faca" , "quantidade": 20}]

    
    assert resultado_obtido== resultado_esperado

def test_vender_item_ValueError():
    adc=Inventario()

    adc.adicionar_produto("Martelo", 10)
    adc.adicionar_produto("Faca", 20)        
    with pytest.raises(ValueError) as v:
        adc.vender_item("Relogio", 5)
    assert "Produto não encontrado" in str(v.value)


def test_vender_item_quantidade_insuficiente():
    adc = Inventario()
    adc.adicionar_produto("Martelo", 5)

    with pytest.raises(ValueError) as exc:
        adc.vender_item("Martelo", 10)
    assert "Quantidade indisponível" in str(exc.value)