from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/success", methods=["POST"])
def success():
    name = request.form["name"]
    roll = request.form["roll"]
    email = request.form["email"]
    year = request.form["year"]
    department = request.form["department"]

    return render_template(
        "success.html",
        name=name,
        roll=roll,
        email=email,
        year=year,
        department=department
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)