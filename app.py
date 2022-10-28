from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'ID' : 1,
    'TITLE' : 'Data analysist',
    'LOCATION' : 'Bangluru',
    'SALARY' : 'Rs.10,00000'
  },

  {
    'ID' : 2,
    'TITLE' : 'Data scientist',
    'LOCATION' : 'pune',
    'SALARY' : 'Rs.12,00000'
  },

  {
    'ID' : 3,
    'TITLE' : 'front end engineer',
    'LOCATION' : 'Hydrabad',
    'SALARY' : 'Rs.10,00000'
  },

  {
    'ID' : 1,
    'TITLE' : 'Back end engineer',
    'LOCATION' : 'Bilaspur',
    'SALARY' : '$120,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name= 'praveen softtech')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
