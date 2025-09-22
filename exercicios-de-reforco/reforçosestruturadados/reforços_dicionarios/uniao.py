"""Crie dois dicionários. Crie um terceiro dicionário que seja a união
dos dois primeiros. Se uma chave existir em ambos, use o valor do segundo dicionário.
"""

dicio_1={"ameixa":"fruta", "morango":"fruta", "melancia":"fruta", "abobora": "verdura"}
dicio_2={"banana": "fruta", "chuchu":"verdura", "abobora": "fruta"}
dicio_3={**dicio_1, **dicio_2}

print(dicio_3)