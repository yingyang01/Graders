from math import sqrt
def mosteller(w, h):
    return sqrt(w*h)/60

def du_bois(w, h):
    return 0.007184*w**0.425*h**0.725

def fujimoto(w, h):
    return 0.008883*w**0.444*h**0.663

def main():
    w = float(input())
    h = float(input())
    print("Mosteller = {mosteller}\nDu Bois = {du_bois}\nFujimoto = {fujimoto}".format(mosteller = round(mosteller(w, h), 5), du_bois = round(du_bois(w, h), 5), fujimoto = round(fujimoto(w, h), 5)))

exec(input())