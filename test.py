#!/usr/bin/python3
#_*_ coding: UTF-8 _*_

jours = 337 #total des 11 mois sans fevrier

mois_fevrier = int(input("donnez le nombre de jour :") # mois de fevrier

if mois_fevrier == 28:
    print("vous avez entrez : %d" %mois_fevrier, "jrs")
elif mois_fevrier == 29:
    print("vous avez entrez : %d" %mois_fevrier, "jrs")
else:
    print("erreur")
    mois_fevrier = int(input("donnez le nombre de jour :"))
    while mois_fevrier != 28 or mois_fevrier != 29:
        mois_fevrier = int(input("donnez 28 ou 29 :"))
        if mois_fevrier == 28:
            print("vous avez entrez :",mois_fevrier)
            break
        elif mois_fevrier == 29:
            print("vous avez entrez :",mois_fevrier)
            break

total_jours = jours + mois_fevrier

if total_jours == 366: #test sur le type d'annee
    print("nous sommes dans une annee bixestile car le nombre de jours est :%d" %total_jours)
else:
    print("nous sommes dans une annee normale car le nombre de jours est :%d" %total_jours)
