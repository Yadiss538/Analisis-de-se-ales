import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de parámetros (Punto 2.1 del maestro)
fs = 1000  # Frecuencia de muestreo
T = 1.0    # Tiempo total
t = np.linspace(0, T, int(fs * T), endpoint=False)

# 2. Generación de la señal senoidal (Ejemplo)
frecuencia_fundamental = 5 
senal = np.sin(2 * np.pi * frecuencia_fundamental * t)

# 3. Cálculo de la Transformada de Fourier (Punto 2.2 del maestro)
# fft() en Python convierte la señal al dominio de la frecuencia
fft_resultado = np.fft.fft(senal)
frecuencias = np.fft.fftfreq(len(senal), 1/fs)

# 4. Graficación de magnitud y fase (Punto 2.3 del maestro)
plt.figure(figsize=(10, 6))

# Magnitud
plt.subplot(2, 1, 1)
plt.plot(frecuencias[:len(frecuencias)//2], np.abs(fft_resultado)[:len(frecuencias)//2])
plt.title("Magnitud del espectro (FFT)")
plt.grid(True)

# Fase
plt.subplot(2, 1, 2)
plt.plot(frecuencias[:len(frecuencias)//2], np.angle(fft_resultado)[:len(frecuencias)//2])
plt.title("Fase del espectro")
plt.grid(True)

plt.tight_layout()
plt.show()