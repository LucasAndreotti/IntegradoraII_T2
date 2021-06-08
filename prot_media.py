import collections
import pandas as pd
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


dataset = pd.read_csv(dir_path+'\\CSVs_corrigido\\corrigido_semFiltro_Parte1.csv',sep=",")

#print(dataset)

dataset_mean = dataset.mean()

print(dataset_mean)
exit()

data = {'Questao': ['Q1','Q2','Q3','Q4','Q5','Q6']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Declare a list that is to be converted into a column
#address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
#df['Address'] = address
  
# Observe the result


lista=[]

for i in dataset_mean:
    lista.append(i)

#print(lista)

df['teste'] = lista
print(df)


""" 
                Q1  Q2  Q3  Q4  Q5  Q6

semFiltro       medias
Fem         
Masc 
Fam_Sim
Fam_Nao
menor_30
maior_30
emi_emc_si
sc_pgc

        semFiltro    Fem    Masc    Fam_Sim     Fam_Nao     menor_30    maior_30    emi_emc_si      sc_pg

        
Q1
Q2
Q3
Q4
Q5
Q6
 """

#conforto_dataset_mean.to_csv('C:/Users/lucas.andreotti/Desktop/03 - Integradora/DadosFormulario/Analise_Conforto_Carisma/python_Carisma/media_formatado_semFiltro_Conforto.csv', index=False)