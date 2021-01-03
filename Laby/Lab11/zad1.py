w = 3 #szerokość pokoju
l = 5 #długość pokoju
h = 2.5 #wysokość pokoju
S = w+l + 2*(h+l) + 2*(w+h)
print(float(S))
d_h = 2   #drzwi
d_w = 0.8
w_h = 1.4  #okno
w_w = 1.1
d_S = d_h*d_w
w_S = w_h*w_w
S_nowe = S - d_S - w_S
print(S_nowe)