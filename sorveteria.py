sabores = {
    'Baunilha': 2.50,
    'Chocolate': 3.00,
    'Morango': 2.75,
    'Limão': 2.25,
    'Flocos': 4.50,
    'Açaí': 7.00,
    'Ninho Trufado': 5.50,
    'Maracujá': 3.75,
}

print("Olá, essa é a Master Sorvets !")
print("Esses são nossos sabores disponíveis : ")
for sabor in sabores:
    print("- " + sabor)

sabor_escolhido = input("Qual sabor você escolhe ? ")

if sabor_escolhido not in sabores:
    print("Desculpa, não temos esse sabor.")
    exit()

quantidade = int(input("Quantos deseja comprar ? "))

if quantidade <= 0:
    print("Impossivel essa quantidade.")
    exit()

preco_sorvete = sabores[sabor_escolhido]
preco_total = preco_sorvete * quantidade


#2f igual a duas casas decimal dps da virgula
print(f"Valor total: R${preco_total:.2f}")


valor_pago = float(input("Troco para quanto ?"))

if valor_pago < preco_total:
    print("Esta faltando.")
    exit()

troco = valor_pago - preco_total

print(f"Seu troco é de R${troco:.2f}")
print("Espero que goste !")
print("PROOOOXIMO")

