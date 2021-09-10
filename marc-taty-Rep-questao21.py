x = int( input("Digite um valor inteiro: ") )
ehprimo = True

for d in range(2, x): #[2, ..., x-1] x = 7 -> [2, 3, 4, 5, 6]
    if x % d == 0:                   #x = 8 -> [2, 3, 4, 5, 6, 7]
        ehprimo = False              #x = 25 -> [2, 3, 4, 5, ..., 24]
        break

if ehprimo:
    print("O valor %d é primo!" % x)
else:
    print("O valor %d não é primo!" % x)
