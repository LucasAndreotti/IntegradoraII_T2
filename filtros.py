import collections
import pandas as pd
import numpy as np
import os 


""" 
** CSVs para Carisma e Conforto estão formatados em /CSVs_formatado

** CSVs para Parte1 Parte2A Parte2B estão corrigidos em /CSVs_corrigido
"""

""" 
Parte1  -> /CSVs_filtros/filtros_Parte1
Parte2A -> /CSVs_filtros/filtros_Parte2A
Parte2B -> /CSVs_filtros/filtros_Parte2B

Carisma  -> /CSVs_filtros/filtros_Carisma
Conforto -> /CSVs_filtros/filtros_Conforto
"""

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path_to = dir_path + "\\CSVs_filtros\\filtros_"

#dir_path_from

def aplica_filtros(nome):
    
    if(nome == 'Carisma' or nome == 'Conforto'): 
        dir_path_from = dir_path+'\\CSVs_formatado\\formatado_semFiltro_' 
    else:
        dir_path_from = dir_path+'\\CSVs_corrigido\\corrigido_semFiltro_'

    dataset = pd.read_csv(dir_path_from+nome+'.csv',sep=',')

    dir_path_to_nome = dir_path_to + nome 

    ###

    #SEM_FILTRO

    dataset.to_csv(dir_path_to_nome+'\\'+nome+'_SEM_FILTRO.csv', index=False)

    #filtroFem
    #filtroMasc

    filtroFem = dataset[dataset['Genero']=='Feminino']
    filtroMasc = dataset[dataset['Genero']=='Masculino']
    filtroFem.to_csv(dir_path_to_nome+'\\'+nome+'_Fem.csv', index=False)
    filtroMasc.to_csv(dir_path_to_nome+'\\'+nome+'_Masc.csv', index=False)

    #filtroIdade_Menor_30
    #filtroIdade_Maior_30

    filtroIdade_Menor_30 = dataset[(dataset['Faixa_Etaria']=='18-20') | (dataset['Faixa_Etaria']=='21-29')]
    filtroIdade_Maior_30 = dataset[(dataset['Faixa_Etaria']=='30-39') | (dataset['Faixa_Etaria']=='40-49') | (dataset['Faixa_Etaria']=='50-59') | (dataset['Faixa_Etaria']=='60')]
    filtroIdade_Menor_30.to_csv(dir_path_to_nome+'\\'+nome+'_Idade_Menor_30.csv', index=False)
    filtroIdade_Maior_30.to_csv(dir_path_to_nome+'\\'+nome+'_Idade_Maior_30.csv', index=False)

    #filtroFamiliaridade_Sim
    #filtroFamiliaridade_Nao

    filtroFamiliaridade_Sim = dataset[dataset['Familiaridade'] == 'Sim']
    filtroFamiliaridade_Nao = dataset[dataset['Familiaridade'] == 'Nao']
    filtroFamiliaridade_Sim.to_csv(dir_path_to_nome+'\\'+nome+'_Familiar_Sim.csv', index=False)
    filtroFamiliaridade_Nao.to_csv(dir_path_to_nome+'\\'+nome+'_Familiar_Nao.csv', index=False)

    #filtroEscolaridade_EMI_EMC_SI
    #filtroEscolaridade_SC_PGC

    filtroEscolaridade_EMI_EMC_SI = dataset[(dataset['Escolaridade']=='EMI') | (dataset['Escolaridade']=='EMC') | (dataset['Escolaridade']=='SI')]
    filtroEscolaridade_SC_PGC = dataset[(dataset['Escolaridade']=='SC') | (dataset['Escolaridade']=='PGC')]
    filtroEscolaridade_EMI_EMC_SI.to_csv(dir_path_to_nome+'\\'+nome+'_Escolaridade_EMI_EMC_SI.csv', index=False)
    filtroEscolaridade_SC_PGC.to_csv(dir_path_to_nome+'\\'+nome+'_Escolaridade_SC_PGC.csv', index=False)

    ###

lst_partes = ['Parte1','Parte2A','Parte2B','Carisma','Conforto']
for parte in lst_partes:
    aplica_filtros(parte)



