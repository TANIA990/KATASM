planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
title = f'datos de gravedad sobre {nombre}'
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""
template = f"""{title.title()} 
{hechos} 
""" 
print(hechos)
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
print(hechos)
new_template = """
Datos de Gravedad sobre: {nombre}
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))