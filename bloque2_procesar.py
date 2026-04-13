import pandas as pd
datos={
'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
'turno': ['manana','tarde','noche','manana','tarde','noche','manana','tarde'],
'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}

df=pd.DataFrame(datos)
print(df['turno'])
print(df[['reactor', 'incidentes']])
manana=df[df['turno']=='manana']

print('Turno manana:')
print(manana)

sin_incidentes=df[df['incidentes']== 0]

print('Sin incidentes:')
print(sin_incidentes)
ef_turno = df.groupby('turno')['eficiencia'].mean()
print('Eficiencia promedio por turno:')
print(ef_turno)
inc_reactor = df.groupby('reactor')['incidentes'].sum()
print('Total incidentes por reactor:')
print(inc_reactor)
