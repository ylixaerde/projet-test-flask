# Projet Flask d'Encodage d'Adresse E-mail

Ce projet consiste en une application web Flask simple qui permet aux utilisateurs d'encoder une adresse e-mail via un formulaire HTML. L'adresse e-mail soumise est enregistrée dans un fichier JSON, et l'utilisateur voit une page de résultat affichant l'adresse e-mail qu'il a soumise.

## Structure du Projet

Le projet est organisé autour de deux fichiers principaux et un dossier statique pour les fichiers CSS.

### Fichiers Python

1. **app.py**: Ce fichier contient le code Flask qui définit les routes de l'application. Les routes principales sont `/` pour la page d'accueil et `/submit` pour le traitement du formulaire lorsqu'il est soumis. L'adresse e-mail est extraite du formulaire et enregistrée dans un fichier JSON appelé `data.json`.

```python
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    data = {'email': email}

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    return render_template('result.html', email=email)

if __name__ == '__main__':
    app.run(debug=True)
```

### Fichiers HTML

2. **templates/base.html**: Fichier de base pour les pages HTML. Il contient la structure générale du document HTML, y compris les balises `<head>` et `<body>`. Il est étendu par d'autres templates.

```html
<!doctype html>
<html lang="fr">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- CSS -->
        <link rel="stylesheet" href="{{ url_for('static', filename= 'css/style.css') }}">

        <title>{% block title %} {% endblock %}</title>
    </head>
    <body>
        {% block content %} {% endblock %}
    </body>
</html>
```

3. **templates/index.html**: Template spécifique pour la page d'accueil. Il étend le fichier `base.html` et définit le contenu spécifique de la page d'accueil.

```html
{% extends 'base.html' %}

{% block content %}
    <h1>{% block title %} Encoder une adresse e-mail {% endblock %}</h1>
    <form method="POST" action="{{ url_for('submit') }}">
		<label for="email">Adresse e-mail :</label>
		<input type="email" id="email" name="email" required>
		<button type="submit">Encoder</button>
	</form>
{% endblock %}
```

4. **templates/result.html**: Template spécifique pour la page de résultat. Il étend également `base.html` et affiche l'adresse e-mail soumise.

```html
{% extends 'base.html' %}

{% block content %}
    <h1>{% block title %} Résultat de l'Encodage {% endblock %}</h1>
    <p>L'adresse e-mail <strong>{{ email }}</strong> a été encodée avec succès.</p>
{% endblock %}
```

### Dossier Statique

5. **static/css/style.css**: Fichier CSS pour définir le style de l'application web.

## Utilisation

1. Assurez-vous d'avoir Flask installé (`pip install Flask`).
2. Exécutez le fichier `app.py`.
3. Accédez à l'application via votre navigateur à l'adresse [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
4. Remplissez le formulaire avec une adresse e-mail et appuyez sur le bouton "Encoder".
5. Vous serez redirigé vers une page de résultat affichant l'adresse e-mail encodée.

Ce projet peut être utilisé comme base pour des applications plus complexes impliquant la collecte de données via des formulaires web.