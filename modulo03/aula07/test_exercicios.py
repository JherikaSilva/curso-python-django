from exercicios import Inventario
import pytest

def test_adicionar_produto():
    adc=Inventario()

    resultado_obtido= adc.adicionar_produto("Martelo", 10)
    resultado_esperado= [{"Martelo":10}]

    assert resultado_obtido== resultado_esperado


