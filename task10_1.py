pets = {}


def formatAge(age):
    strAge = str(age)
    lastNum = int(strAge[len(strAge) - 1])

    l1 = [5, 6, 7, 8, 9, 0]
    l2 = [2, 3, 4]

    if 5 <= age % 100 <= 20:
        return f'{age} лет'
    elif lastNum in l1:
        return f'{age} лет'
    elif lastNum in l2:
        return f'{age} года'
    else:
        return f'{age} год'
     
def printData(data, nickname):
     print(f'Это {data["species"]} по кличке "{nickname}". Возраст питомца: {formatAge(data["age"])}. Имя владельца: {data["owner"]}')
formatAge(14)

while True:
    print('Введите команду(create/get/get_all/exit):')
    cmd = input().strip().lower()
    if cmd == "create":
        newPet = {}
        species = input('Введите породу питомца: ')
        nickname = input('Введите кличку питомца: ')
        age = int(input('Введите возраст питомца: '))



        owner = input('Имя владельца питомца: ')
        newPet['species'] = species
        newPet['age'] = age
        newPet['owner'] = owner
        
        pets[nickname] = newPet
    elif cmd == "get":
        getnickname = input('Введите кличку питомца: ')
        
        if not getnickname in pets:
            print(f"{getnickname} не найден в списке")
            continue

        else:
            petData = pets[getnickname]
            printData(petData, getnickname)

    elif cmd == "get_all":
        for k in pets.keys():
            petData = pets[k]
            printData(petData, k)
    elif cmd == "exit":
        print("Программа завершена")
        break
    


