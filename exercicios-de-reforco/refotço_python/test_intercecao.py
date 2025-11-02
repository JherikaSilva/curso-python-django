from intercecao import intercecao
import random


def test_saida_funcao_intercecao(mocker):
    resultados_random = [5, 3, 3, 4, 1, 5]
    # resultado tem que ser [5]
    mock = mocker.patch("random.randint", side_effect=resultados_random)

    list1 = []
    list2 = []
    for _ in range(3):
        list1.append(random.randint(1, 5))  # [5,3,1]
        list2.append(random.randint(1, 5))  # [3,4,5]

    assert intercecao(list1, list2) == [3, 5]
    assert mock.call_count == 6