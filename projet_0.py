a=input("entrez votre nom :")
b=input("entrez votre prenom :")
c=input("entrez votre age :")
d=input("entrez la date actuelle")

from projet_1 import information_nom_et_prenom
from projet_1 import info_age
from projet_1 import date_naiss
information_nom_et_prenom(a,b)
info_age(c)
date_naiss(d,c)
print("entrez vous information supplementaire")
e=input("entrez votre lieux d origine")
f=input("entrez votre lieux de residence actuelle")
g=input("entrez votre religion")
h=input("entrez vos preference alimentaire")
k=input("entrz vos maladis chronique")
maladie_chroni=True
if k=="":
     maladie_chroni==False
else:
     maladie_chroni==True
from projet_1 import info_supplementaire
info_supplementaire(e,f,g,k,h)