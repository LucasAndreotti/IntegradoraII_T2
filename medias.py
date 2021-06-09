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

def mediaDosFiltros(dataset_medias,path,tipo):

    for filtro in lst_filtros:
        dataset_filtro = pd.read_csv(path+filtro+'.csv',sep=',')
        dataset_filtro_media = dataset_filtro.mean()

        lst_medias=[]
        for media in dataset_filtro_media:
            if tipo==1:
                lst_medias.append("{:.2%}".format(media))
            else:
                lst_medias.append("{:.2f}".format(media))
        dataset_medias[filtro]=lst_medias

    return dataset_medias

def mediasParte1():

    dataset_medias = {'Questao': ['Q1','Q2','Q3','Q4','Q5','Q6']}
    dataset_medias = pd.DataFrame(dataset_medias)
        
    path = dir_path_from+'\\filtros_Parte1\\Parte1'

    dataset_medias = mediaDosFiltros(dataset_medias,path,1)
    #print(dataset_medias)

    dataset_medias.to_csv(dir_path_to+'\\medias_Parte1.csv',index=False)

def mediasParte2A():

    dataset_medias = {'Questao' : ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']}
    dataset_medias = pd.DataFrame(dataset_medias)

    path = dir_path_from+'\\filtros_Parte2A\\Parte2A'

    dataset_medias = mediaDosFiltros(dataset_medias,path,1)

    dataset_medias.to_csv(dir_path_to+'\\medias_Parte2A.csv',index=False)

def mediasParte2B():

    dataset_medias = {'Questao' : ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']}
    dataset_medias = pd.DataFrame(dataset_medias)

    path = dir_path_from+'\\filtros_Parte2B\\Parte2B'

    dataset_medias = mediaDosFiltros(dataset_medias,path,1)

    dataset_medias.to_csv(dir_path_to+'\\medias_Parte2B.csv',index=False)

def mediasCarisma():

    dataset_medias = {'Questao' : ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']}
    dataset_medias = pd.DataFrame(dataset_medias)

    path = dir_path_from+'\\filtros_Carisma\\Carisma'

    dataset_medias = mediaDosFiltros(dataset_medias,path,2)

    dataset_medias.to_csv(dir_path_to+'\\medias_Carisma.csv',index=False)

def mediasConforto():

    dataset_medias = {'Questao' : ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']}
    dataset_medias = pd.DataFrame(dataset_medias)

    path = dir_path_from+'\\filtros_Conforto\\Conforto'

    dataset_medias = mediaDosFiltros(dataset_medias,path,2)

    dataset_medias.to_csv(dir_path_to+'\\medias_Conforto.csv',index=False)



mediasParte1()
mediasParte2A()
mediasParte2B()
mediasConforto()
mediasCarisma()
















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