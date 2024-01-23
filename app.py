# Import packages
from dash import Dash, html, dash_table
import requests
import pandas as pd
import dash_mantine_components as dmc

# Incorporate data
df = pd.read_csv("insurance.csv")
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NjA5Mjc2LCJpYXQiOjE3MDYwMTcyNzYsImp0aSI6IjQwYmUyYTU4OWQxMzRlNjI4ZjU1NzA2MDgwZGRiNmY3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInFyX2NvZGUiOm51bGx9.XpljAZW_lkJNe6z3pGXGbKZQsotM7jnfdpzSZw7Bpyc"
headers = {"Authorization": token, "Content-Type": "application/json"}
domain = "https://preprod-nassamba-web.pacci.ci/"
users_url = f"{domain}/api/user/"

# Initialize the app
app = Dash(__name__)
response = requests.get(users_url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(len(data))
else:
    print(f"Erreur: {response.status_code}")
    print(response.text)

# App layout
app.layout = html.Div(
    [
        html.Div(children="My First App with Data"),
        # dash_table.DataTable(data=df.to_dict("records"), page_size=10),
        html.Div(len(data))
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
