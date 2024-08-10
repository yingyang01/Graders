from math import sqrt, log10
w = float(input())
h = float(input())
print("{Mosteller}\n{Haycock}\n{Boyd}".format(Mosteller = sqrt(w*h)/60, Haycock = 0.024265*w**0.5378*h**0.3964, Boyd = 0.0333*w**(0.6157-0.0188*log10(w))*h**0.3))
