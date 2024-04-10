def information_nom_et_prenom(nom:str,prenom:str):
    nom=nom
    prenom=prenom
    if(nom=="" or prenom==""):
        print("erreur 103-5A")
        nom=input("entre votre  nom")
        prenom =input("entrez votre prenom")
    else:
        print("bien venu M/Mne",nom,prenom)

        
        
def info_age(age:int):
    age_annee_prochaine=0
    age=age
    age_annee_prochaine=int(age)+1
    if(age_annee_prochaine==0):
        print("erreur203-6B")
        age=input("entrez un chiffre pour votre age") 
    else:
        print("vous avez ",str(age)+"ans","l anne prochaine vous aurez",str(age_annee_prochaine)+"ans")
def date_naiss(annee_actuell:int,age:int):
    bissextile=False
    annee_actuell=annee_actuell
    age=age
    naiss=int(annee_actuell)-int(age)
    if naiss %400==0:
       bissextile ==True
    elif naiss %100==0:
        bissextile==False
    elif naiss %4==0:
        bissextile==True
    if bissextile==True:
        print("l annee de naissance est bissextile")
    else:
        print("cette date de naissance n est pas bissextile")


def info_supplementaire(lieux_orige:str,lieux_resid:str,religion:str,maladie_chroni:str,preference_alimentaire:str):
    lieux_orige=lieux_orige
    lieux_resid=lieux_resid
    religion=religion
    maladie_chroni=maladie_chroni
    preference_alimentaire
    if  maladie_chroni==True :
        print("vous devez consultez un medecin avant tout deplacement a l etranger")
    else:
        print("vous  etes operationnel")
    print(" votre lieux d origine est  ",lieux_orige)
    print(" vous reside actuellement ",lieux_resid)
    print("votus etes de religion  ",religion)
    print("votre alimentation prefere est ",preference_alimentaire)
    
    
    
    
    
    
        
    
def affichage():   
  information_nom_et_prenom()
  info_age()






