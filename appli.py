import sqlite3
import datetime

# Établir une connexion à la base de données
conn = sqlite3.connect("imc.db")
cursor = conn.cursor()


#recuperation des variables

poids = int(input("Indiquez votre poid en kg : "))

taille = int(input("Indiquez votre taille en cm : "))

pseudo = str(input("Indiquez votre pseudo : "))

nom = str(input("Indiquez votre nom : "))

prenom = str(input("Indiquez votre prenom : "))

time = datetime.datetime.now()

def calculImc(poids,taille,pseudo):
    taille_m = taille / 100  # conversion de cm en mètres
    imc = poids / (taille_m * taille_m) 
    if imc < 18.5:
        print(f"Ton IMC est insuffisant {pseudo}, il faut manger plus que ça !")
    elif imc > 18.5 and imc < 24.9:
        print(f"Ton IMC est normal, {pseudo}")
    else:
        print(f"Il va falloir faire un régime {pseudo} !")
    return imc

imc = calculImc(poids, taille, pseudo)
print(imc)

# Insérer les données dans la table user
cursor.execute("INSERT INTO user (username, first_name, last_name) VALUES (?, ?, ?)",
               (pseudo, prenom, nom))

# Insérer les données dans la table bmi
cursor.execute("INSERT INTO bmi (weight, height, bmi_value, date_recorded) VALUES (?, ?, ?, ?)",
               (poids, taille, imc, time))

# Valider la transaction et fermer la connexion
conn.commit()
conn.close()


"""n IMC inférieur à 18,5 est considéré comme insuffisant et indique une possible insuffisance pondérale.
Un IMC entre 18,5 et 24,9 est considéré comme normal et suggère un poids corporel approprié.
Un IMC entre 25 et 29,9 est considéré comme en surpoids.
Un IMC de 30 ou plus est généralement considéré comme obésité."""