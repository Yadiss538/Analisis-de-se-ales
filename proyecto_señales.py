import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de parámetros de tiempo
# Tiempo continuo (simulado con muchos puntos)
t = np.linspace(0, 2, 1000) 
# Tiempo discreto (valores enteros secuenciales o muestras espaciadas)
n = np.arange(0, 25)        

# 2. Creación de las señales (Onda senoidal como ejemplo base)
# Señal Continua: fluida en el dominio del tiempo
senal_continua = np.sin(2 * np.pi * 1 * t)

# Señal Discreta: valores definidos únicamente en instantes enteros
# Para que sea periódica en tiempo discreto usamos una frecuencia adecuada
senal_discreta = np.sin(0.25 * np.pi * n)

# 3. Configuración de las gráficas para la presentación visual
plt.figure(figsize=(10, 6))

# Subgráfica 1: Representación de Señal Continua
plt.subplot(2, 1, 1)
plt.plot(t, senal_continua, color='blue', linewidth=2)
plt.title('Señal Continua en el Dominio del Tiempo x(t)', fontsize=12)
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')
plt.grid(True)

# Subgráfica 2: Representación de Señal Discreta
plt.subplot(2, 1, 2)|

# Ajustar espacio entre gráficas
plt.tight_layout()

# Mostrar el resultado final en pantalla
plt.show()