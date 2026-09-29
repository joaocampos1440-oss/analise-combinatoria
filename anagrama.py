from collections import Counter

palavra = input('Digite uma palavra: ')

contagem = Counter(palavra)

for letras in contagem.items():
    numero = letras

print(numero)
for letras, vezes in contagem.items():
    print(f"'{letras}' apareceu {vezes} vez(es)")

   #if letras > 1: