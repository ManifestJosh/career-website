from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'Location':'Lagos, Nigeria',
    'Salary':'N 150,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'Location':'Lagos, Nigeria',
    'Salary':'N 400,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'Location':'Abuja, Nigeria',
    'Salary':'N 600,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'Location':'Abuja, Nigeria',
    'Salary':'N 800,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)
