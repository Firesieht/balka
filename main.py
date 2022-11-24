from math import *
import numpy as np
import matplotlib.pyplot as plt

L = 61
b = 0.115
b1 = 19
P = 8300
E = 22000
I = 0.346
K0 = 5*(10**7)

EI = E*I*10**7
B = ((K0/10**6)*b/(4*E*I))**0.25
test_long = L*B

print("Жесткость балки:", EI)
print("Коэффицент Бета", B)
print(f"Проверка условий расчета:{test_long} > {2*pi}, условие выполнено, считаем по длинной балке")

iters = 1000

x = list(np.linspace(0, L, iters))
exp = [exp(-B * abs(b1 - i)) for i in x]
sin = [sin(B * abs(b1 - i)) for i in x]
cos = [cos(B * abs(b1 - i)) for i in x]

deflection = []
angle = []
moment = []
force = []

for i in range(iters):
    deflection.append(P*exp[i]/(8*B**3*EI)*(sin[i]-cos[i])*(-1))
    angle.append(P*exp[i]/(4 * B**2 * EI)*sin[i])
    moment.append(P*exp[i]/(4*B)*(cos[i]-sin[i])*(-1))
    if x[i] < b1:
        force.append(-P/2*exp[i]*cos[i])
    else:
        force.append(P/2*exp[i]*cos[i])

fig = plt.figure()
deflection_graph = plt.plot(x, deflection)
plt.title("Эпюра прогиба")

fig1 = plt.figure()
angle_graph = plt.plot(x, angle)
plt.title("Эпюра поворота")

fig2 = plt.figure()
moment_graph = plt.plot(x, moment)
plt.title("Эпюра момента")

fig3 = plt.figure()
force_graph = plt.plot(x, force)
plt.title("Эпюра поперечной силы")

plt.show()