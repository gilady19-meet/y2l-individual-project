from flask import Flask, request
from flask import render_template
from database import add_action_to_database , get_all_activities
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/addaction', methods=['GET', 'POST'])
def form1():
    if request.method == 'GET':
        return render_template('actionsform.html')
    else:
        actioname = request.form['actioname']
        description = request.form['description']
        actype=request.form['actype']

        add_action_to_database(actioname , description , actype)        
        return render_template('response.html',
            a = actioname,
            d = description,
            t = actype
            )

@app.route('/allactions')
def all_activities():
    all_acts=get_all_activities()
    return render_template('allactivities.html', allacts=all_acts)


if __name__ == '__main__':
    app.run(debug=True)

