s1 = input("s1: ")
s2 = input("s2: ")

ts1 = len(s1)
ts2 = len(s2)

print("%s: %i caractere(s)" % (s1, ts1))
print("%s: %i caractere(s)" % (s2, ts2))

if ts1 == ts2:
    print("Possuem o mesmo tamanho!")
    if s1 == s2:
        print("Possuem o mesmo conteúdo!")
    else:
        print("O conteúdo é diferente!")
else:
    print("O tamanho e o conteúdo são diferentes!")



