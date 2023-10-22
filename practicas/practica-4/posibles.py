with open('rockyou.txt', 'r', encoding='latin1') as f:
    diccionario = f.readlines()


posibles = []

for i in diccionario:
    if i[0] == "p" and len(i) == 12:
        posibles.append(i)

with open("posiblesCriptonianos.txt", "w") as f:
    for contra in posibles:
        # write each item on a new line
        f.write(contra)
    print('Done')
