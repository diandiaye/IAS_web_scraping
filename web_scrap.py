# Importer la librarie bs4 et requests
from bs4 import BeautifulSoup

import requests
# Variable permetant de demander à l'utilisateur de saisir un lien
url = input("Entrez l'URL du Site Web dans laquelle vous voulez extraire du contenu: ")
# Obtenir le contenu du Site Web
r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data)
# Afficher le contenu du Site Web
for link in soup.find_all('a'):
    print(link.get('href'))
