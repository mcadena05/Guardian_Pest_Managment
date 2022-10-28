from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    # View homepage and About Me

    return render_template("homepage.html")

# @app.route("/quote", methods=["POST"])
# def request_quote():
#     # "Create a new user."

#     name = request.form.get("name")
#     email = request.form.get("email")
#     phone = request.form.get('phone')
#     message = request.form.get("message")
    


#     return redirect("/")



if __name__ == "__main__":
   
    app.run(host="0.0.0.0", debug=True)