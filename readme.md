
# **Dash Plotly - Prise en main**

*Cloner le dépôt et le lancer localement ou sur Docker.*
 
1. Cloner le repo 🔗

> ```git clone <lien.git>```


2. Créé un environnement virtuel 🌐

> ```python -m virtualenv env```


3. Lancer l'environnement virtuel 💡

> ```source env/bin/activate```


4. Installation des dépendances ⬇️

> ```pip install -r requirements.txt```


5. Lancer le projet localement ⛏️

> ``` python app.py ``` 


1. Lancer le projet sur docker ⛏️

> ``` docker build --tag dash . ```

> ```docker run -h localhost -p 9002:9000 -d --name container_dash dash```