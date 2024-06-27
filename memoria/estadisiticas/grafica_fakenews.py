import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
nombre_archivo = 'est.xlsx'  # Reemplaza 'datos.xlsx' con el nombre de tu archivo Excel
dataframe = pd.read_excel(nombre_archivo)

# Convertir la columna 'Semana' a formato de fecha
dataframe['Semana'] = pd.to_datetime(dataframe['Semana'])

# Crear la gráfica de líneas con una línea continua
plt.figure(figsize=(10, 5))
plt.plot(dataframe['Semana'], dataframe['Popularidad'], linestyle='-', color='blue')
plt.title('Evolución del término "Fake News"')
plt.xlabel('Fecha')
plt.ylabel('Popularidad')
plt.grid(True)

# Ajustar los límites del eje x para que se ajusten al rango de fechas mostrado
plt.xlim(dataframe['Semana'].min(), dataframe['Semana'].max())

plt.tight_layout()
plt.show()
