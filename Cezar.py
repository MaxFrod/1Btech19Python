# funkcja ord() - zwraca kod ascii danego
# funkcja chr() - zwraca znak danego kodu ascii
# znaki ASCII od A-Z mają kody 65-90 !!!
# print(ord("Z"))

# print(chr(69))

# wypicać pętlą range alfabet
# for i in range(65,91):
#   print(chr(i), end="")
#   print()
# jak słowo rozbić na litery

# napis = "POLSKA"
# print(len(napis)) # zwraca długość napisu
# print(napis[0])
# print(napis[1])
# print(napis[2])
# print(napis[3])
# print(napis[4])
# print(napis[5])

# napisz kody ASCII  literek napisu
# napis = "POLSKA"
# for i in range(len(napis)):
#   print(chr(ord(napis[i])+3))
# ///// print(chr(65 + (ord(napis[i])-65+3) % 26))