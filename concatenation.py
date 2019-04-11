import pandas as pd
base = 'registros/Registro_Nacional_De_Accidentalidad_'
df = pd.DataFrame()
for year in range (2013, 2018):
    actual_year = pd.read_csv(base + str(year) + '.csv')
    df = pd.concat([df, actual_year])
df.to_csv('accidents_concat.csv', index=False)