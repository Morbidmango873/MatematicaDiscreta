## Francsico Hauch Cardos, Henrique De conti, Arthur Cappellazi

with open("teste.txt",'r') as f:
   lines = f.readlines()

operacoes = int(lines[0])
operacoes = operacoes*3+1
u = 'U\n'
Inter = 'I\n'
d = 'D\n'
c = 'C\n'

## União

for x in range(1,operacoes):

        if lines[x] == u:
            lines[x+1] = lines[x+1].replace("\n","")
            s1 = lines[x+1].split(",",)
            lines[x + 2] = lines[x + 2].replace("\n", "")
            s2 = lines[x+2].split(",",)

            print("União")
            print("Conjunto 1",s1)
            for dis in range(len(s2)):
                s1.append(s2[dis])
            se1 = set(s1)
            print("Conjunto 2",s2)
            print("A união dos conjuntos", se1)

##intersecção

        if lines[x] == Inter:
            lines[x + 1] = lines[x + 1].replace("\n", "")
            s1 = lines[x + 1].split(",", )
            lines[x + 2] = lines[x + 2].replace("\n", "")
            s2 = lines[x + 2].split(",", )

            print("Interseção")
            print("Conjunto 1", s1)
            print("Conjunto 2", s2)
            print(set(s1).intersection(s2))


## Diferença

        if lines[x] == d:
            lines[x + 1] = lines[x + 1].replace("\n", "")
            s1 = lines[x + 1].split(",", )
            lines[x + 2] = lines[x + 2].replace("\n", "")
            s2 = lines[x + 2].split(",", )

            print("Diferença")
            print("Conjunto 1", s1)
            print("Conjunto 2", s2)
            print(set(s1).difference(s2))

## Plano Cartesiano

        if lines[x] == c:
            lines[x + 1] = lines[x + 1].replace("\n", "")
            s1 = lines[x + 1].split(",", )
            lines[x + 2] = lines[x + 2].replace("\n", "")
            s2 = lines[x + 2].split(",", )
            se1 = []
            se2 = []




            print("Plano Carteziano")
            print("Conjunto 1", s1)
            print("Conjunto 2", s2)
            for t in range(len(s1)):
                for y in range(len(s2)):
                    print(s1[t],"x",s2[y])











