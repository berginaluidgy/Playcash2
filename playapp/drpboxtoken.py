import pprint
import requests

url = "https://api.dropboxapi.com/oauth2/token"
data = {
    "code": "nGl6lL118AsAAAAAAAAAPKy3HMS1enPQctDsCrc7ilM",  # Remplacez par le code obtenu
    "grant_type": "authorization_code",
    "client_id": "m6yit15q69uy2vf",   # Remplacez par la clé de votre application
    "client_secret": "ted12iwqcprmdud",  # Remplacez par le secret de votre application
    "redirect_uri": "http://localhost:5173/videoMaker"  # L'URL de redirection utilisée
}

response = requests.post(url, data=data)
tokens = response.json()
pprint.pprint(tokens)
