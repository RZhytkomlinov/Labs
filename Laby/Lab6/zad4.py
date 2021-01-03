def DzielnikiWlasciwe(a):
  wynik = []
  for i in range(1, a // 2 + 1):
    if (a % i == 0):
      wynik.append(i)
  return wynik