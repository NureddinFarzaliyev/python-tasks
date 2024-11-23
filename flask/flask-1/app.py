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