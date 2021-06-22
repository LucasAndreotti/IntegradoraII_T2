
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

dic_P1 = {'p':'pos','n':'neg'}

dic_alias_P1 = {
1 : 'n',
2 : 'p',
3 : 'p',
4 : 'n',
5 : 'n',
6 : 'n'
}

dic_P2 = { 'pp':'pos_pos','pn':'pos_neg','nn':'neg_neg','np':'neg_pos'}

dic_alias_P2 = {
7  :	'pn', 
8  :	'pn' ,
9  :	'np' ,
10 :	'nn' ,
11 :	'np' ,
12 :	'nn' ,
13 :	'nn' ,
14 :	'pn' ,
15 :	'pp' ,
16 :	'pn' ,
17 :    'nn' ,
18 : 	'np' ,
19 :	'np' ,
20 : 	'np' ,
21 :	'pp' ,
22 :	'nn' ,
23 :	'nn' ,
24 :	'nn' ,
25 :	'pn' ,
26 :	'np' }

lst_P1_micro_answers =[
'Q1_Micro_Tristeza',
'Q2_Micro_Felicidade',
'Q3_Micro_Surpresa',
'Q4_Micro_Medo',
'Q5_Micro_Raiva',
'Q6_Micro_Desgosto'
]

lst_P2_macro_answers=[
'Q7_Macro_Felicidade',
'Q8_Macro_Surpresa',
'Q9_Macro_Tristeza',
'Q10_Macro_Medo'    ,
'Q11_Macro_Raiva',
'Q12_Macro_Medo',
'Q13_Macro_Tristeza',
'Q14_Macro_Surpresa',
'Q15_Macro_Surpresa',
'Q16_Macro_Felicidade',
'Q17_Macro_Desgosto',
'Q18_Macro_Raiva',
'Q19_Macro_Medo',
'Q20_Macro_Desgosto',
'Q21_Macro_Felicidade',
'Q22_Macro_Tristeza',
'Q23_Macro_Medo',
'Q24_Macro_Desgosto',
'Q25_Macro_Surpresa',
'Q26_Macro_Medo']

lst_P2_micro_answers=[
'Q7_Micro_Tristeza',
'Q8_Micro_Tristeza',
'Q9_Micro_Felicidade',
'Q10_Micro_Raiva',
'Q11_Micro_Felicidade',
'Q12_Micro_Desgosto',
'Q13_Micro_Raiva',
'Q14_Micro_Medo',
'Q15_Micro_Felicidade',
'Q16_Micro_Raiva',
'Q17_Micro_Tristeza',
'Q18_Micro_Surpresa',
'Q19_Micro_Surpresa',
'Q20_Micro_Surpresa',
'Q21_Micro_Surpresa',
'Q22_Micro_Desgosto',
'Q23_Micro_Desgosto',
'Q24_Micro_Medo',
'Q25_Micro_Desgosto',
'Q26_Micro_Felicidade'
]

lst_P2_micro_macro_answers=[
'Q7_Felicidade_Tristeza',
'Q8_Surpresa_Tristeza',
'Q9_Tristeza_Felicidade',
'Q10_Medo_Raiva',    
'Q11_Raiva_Felicidade',
'Q12_Medo_Desgosto',
'Q13_Tristeza_Raiva',
'Q14_Surpresa_Medo',
'Q15_Surpresa_Felicidade',
'Q16_Felicidade_Raiva',
'Q17_Desgosto_Tristeza',
'Q18_Raiva_Surpresa',
'Q19_Medo_Surpresa',
'Q20_Desgosto_Surpresa',
'Q21_Felicidade_Surpresa',
'Q22_Tristeza_Desgosto',
'Q23_Medo_Desgosto',
'Q24_Desgosto_Medo',
'Q25_Surpresa_Desgosto',
'Q26_Medo_Felicidade'
]


def mediaDosFiltros(nome):
    dataset_medias= {}
    if nome == 'Parte1':
        lista = lst_P1_micro_answers
        lista += ['Med_Porcent','Med_Pos','Med_Neg']
    else:

        if nome == 'Carisma' or nome == 'Conforto':
            lista= lst_P2_micro_macro_answers
        elif nome == 'Parte2A':
            lista=lst_P2_macro_answers
        else:   
            lista=lst_P2_micro_answers

        lista=lista+['Med_Porcent','Med_PosPos','Med_PosNeg','Med_NegNeg','Med_NegPos']
    
    dataset_medias = {'Questao': lista}

    #print(dataset_medias['Questao'],'\n\n')
    dataset_medias = pd.DataFrame(dataset_medias)
    
    path = dir_path_from+'\\filtros_'+nome+'\\'+nome

    for filtro in lst_filtros:
        dataset_filtro = pd.read_csv(path+filtro+'.csv',sep=',')
        dataset_filtro_media = dataset_filtro.mean()

        lst_medias = dataset_filtro_media.tolist()
        media_percents = dataset_filtro_media.mean() 

        if nome == 'Parte1' or nome == 'Parte2A' or nome == 'Parte2B':
            print(nome)
            media_percents = media_percents * 100
            for i in range(len(lst_medias)):
                lst_medias[i] = lst_medias[i] * 100

        lst_medias.append(media_percents)

        if nome != 'Parte1':
            n_questao = 7
            media_PosPos = []
            media_PosNeg = []
            media_NegNeg = []
            media_NegPos = []

            for i in range(len(lst_medias)-1):
                if(dic_P2[dic_alias_P2[n_questao]]=='pos_pos'):
                    media_PosPos.append(lst_medias[i])
                elif(dic_P2[dic_alias_P2[n_questao]]=='pos_neg'):
                    media_PosNeg.append(lst_medias[i])
                elif(dic_P2[dic_alias_P2[n_questao]]=='neg_neg'):
                    media_NegNeg.append(lst_medias[i])
                else:    
                    media_NegPos.append(lst_medias[i])
                n_questao+=1

            media_PosPos = sum(media_PosPos)/len(media_PosPos)
            media_PosNeg = sum(media_PosNeg)/len(media_PosNeg)
            media_NegNeg = sum(media_NegNeg)/len(media_NegNeg)
            media_NegPos = sum(media_NegPos)/len(media_NegPos)

            lst_medias.append(media_PosPos)
            lst_medias.append(media_PosNeg)
            lst_medias.append(media_NegNeg)
            lst_medias.append(media_NegPos)

        else:
            n_questao = 1
            media_Pos = []
            media_Neg = []
            for i in range(len(lst_medias)-1):
                if(dic_P1[dic_alias_P1[n_questao]]=='pos'):
                    media_Pos.append(lst_medias[i])
                else:
                    media_Neg.append(lst_medias[i])
                n_questao+=1

            media_Pos = sum(media_Pos)/len(media_Pos)
            media_Neg = sum(media_Neg)/len(media_Neg)

            lst_medias.append(media_Pos)
            lst_medias.append(media_Neg)

        for i in range(len(lst_medias)):
            lst_medias[i] = ("{:.4f}".format(lst_medias[i]).replace('.',','))

        dataset_medias[filtro]=lst_medias

    dataset_medias.to_csv(dir_path_to+'\\medias_'+nome+'.csv',index=False,sep=';')

##

mediaDosFiltros('Parte1')
mediaDosFiltros('Parte2A')
mediaDosFiltros('Parte2B')
mediaDosFiltros('Conforto')
mediaDosFiltros('Carisma')

""" 
        semFiltro    Fem    Masc    Fam_Sim     Fam_Nao     menor_30    maior_30    emi_emc_si      sc_pg

        
Q1
Q2
Q3
Q4
Q5
Q6
 """
""" 
                semFiltro    Fem    Masc    Fam_Sim     Fam_Nao     menor_30    maior_30    emi_emc_si      sc_pg

Parte1
    media_%
    media_pp
    media_pn
    media_nn
    media_np

Parte2A
    media_%
    media_pp
    media_pn
    media_nn
    media_np

Parte2B
    media_%
    media_pp
    media_pn
    media_nn
    media_np

"""
