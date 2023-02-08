import pandas as pd 

data=pd.read_csv("./empleados.csv")
filtro1=data.head(10)
filtro2= data["nombres"].head(10)
filtro3=data[["nombres","salario"]].tail(5)
filtro4=data.head(20).describe()

#Filtrando Por Pondiciones Logicas 
filtroEdad=data[data["edad"]<30].head(20)
print(filtroEdad)

#Limpiando Datos 
dataLimpia=filtroEdad.dropna()
print("\n")
print(dataLimpia)