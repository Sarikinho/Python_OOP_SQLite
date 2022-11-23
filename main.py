#Importar nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
sardeiro = Pessoa(1, "Henrique da Costa Sardeiro")
print (sardeiro)

#Quero mostrar somente o nome
print(sardeiro.nome)