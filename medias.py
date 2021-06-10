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

media_medias = 0.0

def mediaDosFiltros(nome):
    if nome == 'Parte1':
        dataset_medias = {'Questao': ['Q1','Q2','Q3','Q4','Q5','Q6','Media_Medias']}
        n_questoes = 6
    else:
        dataset_medias = {'Questao' : ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','Media_Medias']}
        n_questoes = 20

    dataset_medias = pd.DataFrame(dataset_medias)
    
    path = dir_path_from+'\\filtros_'+nome+'\\'+nome

    global media_medias

    for filtro in lst_filtros:
        dataset_filtro = pd.read_csv(path+filtro+'.csv',sep=',')
        dataset_filtro_media = dataset_filtro.mean()

        media_medias = 0.0
        lst_medias=[]

        for media in dataset_filtro_media:
            media_medias =  media_medias + media
            print(media_medias)
            media = "{:.4f}".format(media)
            media = (media.replace('.',','))
            lst_medias.append(media)

        media_medias = media_medias/n_questoes
        media_medias = "{:.4f}".format(media_medias)
        media_medias = media_medias.replace('.',',')

        lst_medias.append(media_medias)
        dataset_medias[filtro]=lst_medias

    dataset_medias.to_csv(dir_path_to+'\\medias_'+nome+'.csv',index=False,sep=';')


##

lst_partes = ['Parte1','Parte2A','Parte2B','Carisma','Conforto']
for parte in lst_partes:
    mediaDosFiltros(parte) 



""" 
        semFiltro    Fem    Masc    Fam_Sim     Fam_Nao     menor_30    maior_30    emi_emc_si      sc_pg

        
Q1
Q2
Q3
Q4
Q5
Q6
 """