# Desafío - Juegos Olimpicos
# Patricio Cortés
# G18
# 12-09-2021

# importa libreria pandas
import pandas as pd

# un data frame es un contenedor de datos
df = pd.read_csv("doc/athlete_events.csv") # el archivo está en la carpeta doc/

# ****** Ejercicio 1 ******
# la cantidad de registros y campos se guardará en la varable ejercicio_1
ejercicio_1 = df.shape # usamos el atributo "shape"
# solo para comprobar
print(ejercicio_1)

# ****** Ejercicio 2 ******
# la cantidad de competencias que se ha realizado se guardarán en la varable ejercicio_2
ejercicio_2 = df["Year"].value_counts().shape[0]
# solo para comprobar
print(ejercicio_2)

# ****** Ejercicio 3 ******
# porcentaje de atletas en los juegos de verano e invierno
ejercicio_3 = df["Season"].value_counts("%") # obtenemos el porcentaje entre 0 y 1
# solo para comprobar
print(ejercicio_3)

# ****** Ejercicio 4 ******
# informar donde fue primer juego de verano
juegos_verano = df[df["Season"] == "Summer"]
primer_juego_verano = juegos_verano["Year"].min()
lugar_primer_juego_verano = df[df["Year"] == primer_juego_verano]["City"].unique()[0]
ejercicio_4 = lugar_primer_juego_verano
# solo para comprobar
print(ejercicio_4)

# ****** Ejercicio 5 ******
# informar donde fue primer juego de invierno
juegos_invierno = df[df["Season"] == "Winter"]
primer_juego_invierno = juegos_invierno["Year"].min()
lugar_primer_juego_invierno = df[df["Year"] == primer_juego_invierno]["City"].unique()[0]
ejercicio_5 = lugar_primer_juego_invierno
# solo para comprobar
print(ejercicio_5)

# nota
# una disculpa profe, no me dio el tiempo para hacer los demas ejercicios

# Fin del desafío
