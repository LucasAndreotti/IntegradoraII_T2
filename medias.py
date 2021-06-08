import collections
import pandas as pd
import numpy as np
import os

from pandas.core.frame import DataFrame

dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path_from = dir_path + '\\CSVs_filtros'

dir_path_to = dir_path + '\\CSVs_medias'

lst_filtros = [

'_SEM_FILTRO',
'_Familiar_Sim',
'_Familiar_Nao',
'_Fem',
'_Masc',
'_Idade_Menor_30',
'_Idade_Maior_30',
'_Escolaridade_EMI_EMC_SI',
'_Escolaridade_SC_PGC',
]



def mediasParte1():

    dataset_medias = {'Questao': ['Q1','Q2','Q3','Q4','Q5','Q6']}
    dataset_medias = pd.DataFrame(dataset_medias)
    #print(dataset_medias)

    for filtro in lst_filtros:
        dataset_filtro = pd.read_csv(dir_path_from+'\\filtros_Parte1\\Parte1'+filtro+'.csv',sep=',')

        dataset_media = dataset_filtro.mean()
        
        lista_medias=[]

        for media in dataset_media:
            lista_medias.append(media)
        
        dataset_medias[filtro] = lista_medias
    
    print(dataset_medias)

    dataset_medias.to_csv(dir_path_to+'\\medias_Parte1.csv',index=False)

mediasParte1()

















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