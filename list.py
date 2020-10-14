list = []
resp = "s"

while resp == "s":
    name=[]
    name.append(input("Name: "))
    name.append(input("Age: "))
    list.append(name)

    resp = input("Digite s para inserir mais: ")

for n in list:
    print("Name: ", n[0])
    print("Idade: ", n[1])
