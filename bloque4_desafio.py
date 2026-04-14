import pandas as pd
import matplotlib.pyplot as plt
datos = {
'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
'turno': ['manana','tarde','noche','manana','tarde','noche','manana','tarde'],
'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
df = pd.DataFrame(datos)
df['estado'] = df['temperatura'].apply(lambda t: 'critico' if t > 90 else 'normal')
print(df)
print(df['estado'].value_counts())

promedio_eficiencia = df.groupby('reactor')['eficiencia'].mean()
colores=['green' if reactor == 'R1'else 'blue' if reactor =='R2' else 'orange' for reactor in promedio_eficiencia.index]
plt.bar(promedio_eficiencia.index, promedio_eficiencia.values, color=colores)
plt.title('Eficiencia promedio por reactor')
plt.xlabel('Reactor')
plt.ylabel('Eficiencia')
plt.tight_layout()
plt.show()
