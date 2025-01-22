import os
import itertools
import string
from flask import Flask, request, render_template, send_file, jsonify
import PyPDF2

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf_file = request.files.get("pdf_file")
        password_length = int(request.form.get("password_length"))
        password_type = request.form.get("password_type")

        if not pdf_file:
            return "No PDF uploaded.", 400

        pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
        pdf_file.save(pdf_path)

        output_path = os.path.join(OUTPUT_FOLDER, f"unlocked_{pdf_file.filename}")

        characters = ""
        if "letters" in password_type:
            characters += string.ascii_uppercase
        if "digits" in password_type:
            characters += string.digits

        if not characters:
            return "Invalid password type selected.", 400

        success, password = unlock_pdf(pdf_path, output_path, characters, password_length)
        if success:
            return render_template("success.html", password=password, file_path=output_path)
        else:
            return "Password not found.", 400

    return render_template("index.html")


def unlock_pdf(pdf_path, output_path, characters, password_length):
    possible_passwords = ("".join(pw) for pw in itertools.product(characters, repeat=password_length))

    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        for password in possible_passwords:
            try:
                print(f"Trying password: {password}")
                if reader.decrypt(password):
                    print(f"Password found: {password}")
                    return True, password
                    # break
                    # with open(output_path, "wb") as output_file:
                    #     writer = PyPDF2.PdfWriter()
                    #     for page in reader.pages:
                    #         writer.add_page(page)
                    #     writer.write(output_file)
                    
            except Exception as e:
                print(f"Error with password {password}: {e}")
                continue

    return False, None


if __name__ == "__main__":
    app.run(debug=True)
