import re

cpf_regex = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
nome_regex = r'^[A-Za-z]+(?:\s[A-Za-z]+)+$' # Verifica se o nome só tem letra e que contenha pelo menos um sobrenome

def verifica_cpf(cpf: str) -> bool:
    return re.fullmatch(cpf_regex, cpf) is not None

def verifica_nome(nome: str) -> bool:
    return re.fullmatch(nome_regex, nome) is not None