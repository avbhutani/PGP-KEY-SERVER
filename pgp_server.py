from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)



# Define the directory where your PGP key files are stored
keys_directory = 'keys'

def search_pgp_key(email):
    # Search for the PGP key on the keyserver


    # Search for the PGP key in local files
    local_result = search_pgp_key_in_files(email)

    if local_result:
        return local_result

    return None

def search_pgp_key_in_files(email):
    key_file = [os.path.join(keys_directory, file) for file in os.listdir(keys_directory) if file.endswith(email+'.asc')]

    if key_file:
        with open(key_file[0], 'r') as file:
            key_data = file.read()
            return key_data
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        pgp_key = search_pgp_key(email)
        return render_template("result.html", email=email, pgp_key=pgp_key)
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        email = request.form["email"]
        key_file = request.files["key_file"]
        if email and key_file:
            # Save the uploaded key to the keys_directory with the email as the filename
            key_file.save(os.path.join(keys_directory, email + ".asc"))
            return redirect(url_for("index"))
    return render_template("upload.html")

if __name__ == "__main__":
    app.run()

