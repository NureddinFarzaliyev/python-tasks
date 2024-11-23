# Flask Notes

****
### Initialization
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_
```

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

```
flask run
```

To reload flask automatically on each change:
```
flask --app app.py --debug run
```

### Placeholders in HTML Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    hello, {{ placeholder }}
</body>
</html>
```

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args["name"]
    return render_template("index.html", placeholder=name)
```

Checking if argument exists
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = 'world'
    return render_template("index.html", placeholder=name)
```

**Better** code:
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", placeholder=name)
```

**Note:** If the method is changed to `POST`, instead of `request.args.get`, `request.form.get` must be used
### Using Layout Templates
layout.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% block body %}{% endblock %}
</body>
</html>
```

greet.html
```html
{% extends "layout.html" %}

{% block body %}

    <h1>Hello, {{name}}</h1>

{% endblock %}
```

index.html
```html
{% extends "layout.html" %}

{% block body %}

    <form action="/greet" method="get">
        <input type="text" placeholder="name" name="name">
        <button type="submit">Greet</button>
    </form>

{% endblock %}
```
### Other Methods
```python
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "world")
    return render_template("greet.html", name=name)
```

**Note:** If the method is changed to `POST`, instead of `request.args.get`, `request.form.get` must be used
### Conditional Rendering
```python
@app.route("/", methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        name = request.form.get("name")
        return render_template("greet.html", name=name)

    return render_template("index.html")
```

```html
{% extends "layout.html" %}

{% block body %}
    <h1>Hello, {% if name %} {{name}} {% else %} world {% endif %}</h1>
{% endblock %}
```
### Rendering an array
```python
from flask import Flask, render_template, request
app = Flask(__name__)

# This is an array that will be rendered
SPORTS = ['a', 'b', 'c', 'd']

@app.route("/", methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        name = request.form.get("name")
        sport = request.form.get("sport")
        return render_template("greet.html", name=name, sport=sport)

    # This line here will render an index.html file with array of sports as an argument 
    return render_template("index.html", sports = SPORTS)
```

```html
<select name="sport">
	<option value="" disabled selected>Choose a sport</option>
	<!-- An array of sports will be rendered as a selection list -->
	{% for sport in sports %}
		<option value={{sport}}>{{sport}}</option>
	{% endfor %}
</select>
```
### Validation on Server Side and `getlist`
```python
from flask import Flask, render_template, request
app = Flask(__name__)

SPORTS = ['a', 'b', 'c', 'd']

@app.route("/", methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        if not request.form.get('name'):
            return render_template('failure.html', message="You have to fill the name blank.")
        
        if not request.form.get('sport'):
            return render_template('failure.html', message="You have to choose a sport.")
        
        for sport in request.form.getlist("sport"):
            if sport not in SPORTS:
                return render_template('failure.html', message="Bad User Input")
        
        name = request.form.get("name")
        return render_template("greet.html", name=name)

    # This line here will render an index.html file with array of sports as an argument 
    return render_template("index.html", sports = SPORTS)
```