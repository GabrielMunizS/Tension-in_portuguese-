# Importando as bibliotecas necessárias
import math as mt
import numpy as np
import pylab as pt

# Dados de entrada
VRMS = float(input("Digite a tensão em RMS (VRMS): "))
f = float(input("Digite a frequência em hertz (Hz): "))
X = float(input("Digite o valor da fase em graus (X°): "))

# Cálculos e conversões
teta = mt.radians(X)
w = 2*mt.pi*f
T = (1/f) # Período (s)
Vp = mt.sqrt(2)*VRMS # Tensão de pico (V)
Vpp = 2*Vp # Tensão de pico a pico (V)

# Gerando o gráfico da onda
tempo = np.arange(0,0.0101,0.0001) # Valores de tempo (s)
tensao_inst = [] # Valores de tensão instantânea

for i in range(len(tempo)):
  t = tempo[i] # Tempo (s)
  Vinst = Vp*mt.sin(w*t + teta)
  tensao_inst.append(Vinst)

  if t == 0:
    V0 = Vinst
  elif t == T/4:
    V1 = Vinst
  elif t == T/2:
    V2 = Vinst
  elif t == T*3/4:
    V3 = Vinst
  elif t == T:
    V4 = Vinst

pt.plot(tempo,tensao_inst,"b-")
pt.title("Gráfico da tensão pelo tempo")
pt.xlabel("Tempo (s)")
pt.ylabel("Tensão(V)")
pt.axhline(0, color="black")
pt.axvline(0, color="black")

# Imprimindo os resultados em tela
print()
print(f"Valor de pico = {Vp:.2f}V")
print(f"Valor de pico a pico = {Vpp:.2f}V")
print(f";Valor do período = {T*1000:.2f}ms")
print(f"Valor da tensão instantânea no inicio do gráfico = {V0:.2f}V")
