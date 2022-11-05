frutas=['maçã','uva','morango','tomate','cereja']

print(frutas)
escolha = input("Escolha uma fruta da lista: ")
if escolha.lower() in frutas:
    print("A fruta que você escolheu foi:",escolha)
else:
    print("A fruta não está na lista")

print("===============================")
print("===============================")
print("===============================")

print(frutas)

substituicao = str(input("Escolha a fruta que deseja substituir: "))
frutas.remove(substituicao.lower())

nova_fruta = input("Digite o nome da fruta que deseja adicionar: ")
nova_fruta.lower()
frutas.append(nova_fruta)
print("A nova lista de frutas vai ser:")
print(frutas)


