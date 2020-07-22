# import pandas as pd
# df = pd.read_csv('NEW-DATA-1.T15.txt', sep=' ', header=0)
# df.to_csv('NEW-DATA-1.T15.csv', sep=' ', index=0)
# 1:Date
# 2:Time
# 3:Temperature_Comedor_Sensor
# 4:Temperature_Habitacion_Sensor
# 5:Weather_Temperature
# 6:CO2_Comedor_Sensor
# 7:CO2_Habitacion_Sensor
# 8:Humedad_Comedor_Sensor
# 9:Humedad_Habitacion_Sensor
# 10:Lighting_Comedor_Sensor
# 11:Lighting_Habitacion_Sensor
# 12:Precipitacion
# 13:Meteo_Exterior_Crepusculo
# 14:Meteo_Exterior_Viento
# 15:Meteo_Exterior_Sol_Oest
# 16:Meteo_Exterior_Sol_Est
# 17:Meteo_Exterior_Sol_Sud
# 18:Meteo_Exterior_Piranometro
# 19:Exterior_Entalpic_1
# 20:Exterior_Entalpic_2
# 21:Exterior_Entalpic_turbo
# 22:Temperature_Exterior_Sensor
# 23:Humedad_Exterior_Sensor
# 24:Day_Of_Week

import pandas as pd

data = pd.read_csv("NEW-DATA-1.T15.csv", sep=" ", header=0)

print(data)




