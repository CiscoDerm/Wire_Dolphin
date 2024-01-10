import os
from cryptography.fernet import Fernet
import requests
import getpass

allfiles = []
for file in os.listdir():
    if file == "key.key" or file == "decrypt1.py" or file == "decrypt1.exe" or file == "rick.mp3" or file == "salaire_2024.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)

print(allfiles)

# Récupérer la clé depuis le serveur HTTPS (exemple)
download_url = "https://example.com/download_key"
download_response = requests.get(download_url)

if download_response.status_code == 200:
    with open("key.key", "wb") as key_file:
        key_file.write(download_response.content)
    print("Clé récupérée avec succès depuis le serveur.")
else:
    print("Échec de la récupération de la clé depuis le serveur. Code d'état :", download_response.status_code)

with open("key.key", "rb") as key_file:
    key = key_file.read()

# Utiliser getpass pour saisir le mot de passe de manière sécurisée
passphrase = getpass.getpass("Entrer le mot de passe : ")

# Déchiffrer les fichiers avec la passphrase
fernet = Fernet(key)
for file in allfiles:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    try:
        content_decrypt = fernet.decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)
        print(f"Fichier {file} déchiffré avec succès.")
    except Exception as e:
        print(f"Échec du déchiffrement du fichier {file}: {e}")

print("Terminé.")
