import re

def nome_valido(nome):
        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ'\"\s]+$"

        return re.match(pattern, nome)
