import math
alph = ['а','б','в','г','д','е',
     'ё','ж','з','и','й','к',
     'л','м','н','о','п','р',
     'с','т','у','ф','х','ц',
     'ч','ш','щ','ъ','ы','ь','э','ю','я']
alpB = ['А','Б','В','Г','Д','Е',
     'Ё','Ж','З','И','Й','К',
     'Л','М','Н','О','П','Р',
     'С','Т','У','Ф','Х','Ц',
     'Ч','Ш', 'Щ','Ъ','Ы','Ь','Э','Ю','Я']

const = int(32)
newstr = ""
print("кодировать - введите 0; декодировать - введите 1")
key = int(input())
if key==0:
    print ("введите строку на русском языке")
    inp = str(input())
    print ("введите ROT")
    
    rot = int(input())
    for i in range(len(inp)):
        for j in range(len(alph)):
            if inp[i] == alph[j]:
                num = (rot + j)%33
                new = alph[num]
                break
            elif (inp[i] == alpB[j]):
                num = (rot + j) % 33
                new = alpB[num]
                break
            else:
                new = inp[i]
        newstr = newstr + new
    print(newstr)

if key==1:
    print("введите ROT")
    rot = int(input())
    print("введите строку на русском языке")
    inp = str(input())

    for i in range(len(inp)):
        for j in range(len(alph)):
            if inp[i] == alph[j]:
                num = j - rot%33
                if num<0:
                    num = (33 - num)%33

                new = alph[num]

                break
            elif (inp[i] == alpB[j]):
                num = j - rot % 33
                if num < 0:
                    num = (33 - num)%33
                new = alpB[num]
                break
            else:
                new = inp[i]
        newstr = newstr + new
    print(newstr)

