import os
os.system("clear")
from dataclasses import dataclass


@dataclass
class Autor:
    nome: str
    blibiografia: str

@dataclass 
class Livro:
    titulo: str
    ano: int
    autor: Autor
    
    def exibindo_detalhes(self):
        print(f"Titulo: {self.titulo}\n ano: {self.ano}\n Autor: {self.autor.nome}")
         
print(f"= solicitando dados para o usuario =")  

livro = Livro(
    titulo = input("Digite o titulo do livro: "),
    ano = int(input("Digite o ano do livro: ")),
    autor = Autor(
       nome = input("Digite o nome do autor: "),
       blibiografia = input("Digite as informaçoes de blibiografia do autor: ")
    )
)       
print("\n= Exibindo dados =")
