import math

a = float(input())
b = float(input())
c = float(input())
h = float(input())
r = float(input())
l = float(input())

d = input("wybierz pole figury której chcesz obliczyć: ")

if d == "a":
    print(f"{6}*{a}*{a} = {6*a*a}")
elif d== "b":
    print(f"{2}*{a}*{b}+{2}*{a}*{c}+{2}*{b}*{c}={2*a*b+2*a*c+2*b*c}")
elif d== "d":
    print(f"{a}*{b}+{2}*{a}*{c}+{2}*{b}*{c}={a*b+2*a*c + 2*b*c}")
elif d== "c":
     print(f"{4}*{math.pi}*{r}*{r} = {4*math.pi*r*r}")
elif d== "e":
    print(f"{a}*{a} = {a*a}")
elif d== "f":
    print(f"{a}*{b} = {a*b}")
elif d== "g":
    print(f"{2}*{math.pi}*{r}*{r}+{2}*{math.pi}*{r}*{h} = {2*math.pi*r*r+2*math.pi*r*h}")
elif d== "h":
    print(f"{math.pi}*{r}*{r}+{math.pi}*{r}*{l} = {math.pi*r*r+math.pi*r*l}")
elif d== "i":
    print(f"{4}*{math.pi}*{r}*{r} = {4*math.pi*r*r}")
elif d== "j":
    print(f"{a}*{h} = {a*h}")
elif d== "k":
    print(f"{1/2}*{a}*{h} = {1/2*a*h}")
elif d== "l":
    print(f"{a}*{h} = {a*h}")
elif d== "m":
    print(f"{a}+{b}+{c} = {a+b+c}")
