import datetime
from dash import Dash, html, dcc, callback, Output, Input
import requests
import json

token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NjA5Mjc2LCJpYXQiOjE3MDYwMTcyNzYsImp0aSI6IjQwYmUyYTU4OWQxMzRlNjI4ZjU1NzA2MDgwZGRiNmY3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInFyX2NvZGUiOm51bGx9.XpljAZW_lkJNe6z3pGXGbKZQsotM7jnfdpzSZw7Bpyc"
headers = {"Authorization": token, "Content-Type": "application/json"}
domain = "https://preprod-nassamba-web.pacci.ci/"
users_url = f"{domain}/api/user/"

def serve_layout():
    response = requests.get(users_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(len(data))
    # Faire quelque chose avec les données
    else:
        print(f"Erreur: {response.status_code}")
        print(response.text)
    # print("Statut de la requête preinclusion:", response.status_code)
    # print("Réponse du serveur preinclusion:", response.json())
    # return html.H1('The time is: ' + str(datetime.datetime.now()))
    return html.H1("Nombre d'utilisateurs: " + str(len(data)))


app = Dash(__name__, suppress_callback_exceptions=True)
app.layout = serve_layout
if __name__ == "__main__":
    app.run(debug=True)
