from flask import Flask, render_template, request

# Create a Flask application instance
app = Flask(__name__)


# Route to display the HTML form
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Route to process the submitted form
@app.route("/read-form", methods=["POST"])
def read_form():

    # Retrieve form data
    email = request.form.get("userEmail")
    password = request.form.get("userPassword")
    contact = request.form.get("userContact")
    gender = request.form.get("gender")

    # Check whether the newsletter checkbox was selected
    newsletter = "Yes" if request.form.get("newsletter") else "No"

    # Return the submitted data
    return {
        "email": email,
        "contact": contact,
        "gender": gender,
        "newsletter": newsletter,
        "message": "Form submitted successfully!"
    }


# Run the application
if __name__ == "__main__":
    app.run(debug=True)