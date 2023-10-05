from flask import Flask,render_template
from UserDao import UserDao

app = Flask(__name__)

@app.route("/")
def index():

    dao = UserDao("users_db.db")

    users = list(dao.findAll()) 

    return render_template("user_list.html",users=users)

# flask run