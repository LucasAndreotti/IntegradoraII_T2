import collections
import pandas as pd
import numpy as np
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path_from = dir_path + "\\CSVs_formatado"

dir_path_to = dir_path + "\\CSVs_filtros"

dataset = pd.read_csv(dir_path_from +'\\formatado_semFiltro_Parte1.csv', sep=',')

dataset['Q1'] = np.where((dataset['Q1'] != 'Tristeza'),0,1)
dataset['Q2'] = np.where((dataset['Q2'] != 'Felicidade'),0,1)
dataset['Q3'] = np.where((dataset['Q3'] != 'Surpresa'),0,1)
dataset['Q4'] = np.where((dataset['Q4'] != 'Medo'),0,1)
dataset['Q5'] = np.where((dataset['Q5'] != 'Raiva'),0,1)
dataset['Q6'] = np.where((dataset['Q6'] != 'Desgosto'),0,1)

#print(dataset)
#dataset.to_csv(dir_path+'\\semFiltro.csv', index=False)

#filtroFem
#filtroMasc

filtroFem = dataset[dataset['Genero']=='Feminino']
filtroMasc  = dataset[dataset['Genero']=='Masculino']

filtroFem.to_csv(dir_path_to+'\\filtroFem.csv', index=False)
filtroMasc.to_csv(dir_path_to+'\\filtroMasc.csv', index=False)

#filtroIdade_Menor_30
#filtroIdade_Maior_30

filtroIdade_Menor_30 = dataset[(dataset['Faixa_Etaria']=='18-20') | (dataset['Faixa_Etaria']=='21-29')]
filtroIdade_Maior_30 = dataset[(dataset['Faixa_Etaria']=='30-39') | (dataset['Faixa_Etaria']=='40-49') | (dataset['Faixa_Etaria']=='50-59') | (dataset['Faixa_Etaria']=='60')]

filtroIdade_Menor_30.to_csv(dir_path_to+'\\filtroIdade_Menor_30.csv', index=False)
filtroIdade_Maior_30.to_csv(dir_path_to+'\\filtroIdade_Maior_30.csv', index=False)

#filtroFamiliaridade_Sim
#filtroFamiliaridade_Nao

filtroFamiliaridade_Sim = dataset[dataset['Familiaridade'] == 'Sim']
filtroFamiliaridade_Nao = dataset[dataset['Familiaridade'] == 'Nao']

filtroFamiliaridade_Sim.to_csv(dir_path_to+'\\filtroFamiliaridade_Sim.csv', index=False)
filtroFamiliaridade_Nao.to_csv(dir_path_to+'\\filtroFamiliaridade_Nao.csv', index=False)

#filtroEscolaridade_EMI_EMC_SI
#filtroEscolaridade_SC_PGC

filtroEscolaridade_EMI_EMC_SI = dataset[(dataset['Escolaridade']=='EMI') | (dataset['Escolaridade']=='EMC') | (dataset['Escolaridade']=='SI')]
filtroEscolaridade_SC_PGC = dataset[(dataset['Escolaridade']=='SC') | (dataset['Escolaridade']=='PGC')]

filtroEscolaridade_EMI_EMC_SI.to_csv(dir_path_to+'\\filtroEscolaridade_EMI_EMC_SI_.csv', index=False)
filtroEscolaridade_SC_PGC.to_csv(dir_path_to+'\\filtroEscolaridade_SC_PGC.csv', index=False)

#print(filtroEscolaridade_SC_PGC)

#==============================================================

""" condicao = dataset['Q1'] != 'Tristeza'
coluna = 'Q1'
dataset.loc[condicao,coluna] = 0

condicao = dataset['Q1'] == 'Tristeza'
coluna = 'Q1'
dataset.loc[condicao,coluna] = 1

print(dataset) """

""" dataset['Q1'] = dataset['Q1'].replace('Tristeza','1')
dataset['Q2'] = dataset['Q2'].replace('Felicidade','1')
dataset['Q3'] = dataset['Q3'].replace('Surpresa','1')
dataset['Q4'] = dataset['Q4'].replace('Medo','1')
dataset['Q5'] = dataset['Q5'].replace('Raiva','1')
dataset['Q6'] = dataset['Q6'].replace('Desgosto','1')
 """

""" datasetQ1 = dataset[dataset['Q1']=='Tristeza']
datasetQ2 = dataset[dataset['Q2']=='Felicidade']
datasetQ3 = dataset[dataset['Q3']=='Surpresa']
datasetQ4 = dataset[dataset['Q4']=='Medo']
datasetQ5 = dataset[dataset['Q5']=='Raiva']
datasetQ6 = dataset[dataset['Q6']=='Desgosto']

print(datasetQ1)
print(datasetQ2)
print(datasetQ3)
print(datasetQ4)
print(datasetQ5)
print(datasetQ6) """