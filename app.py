from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    assigned_number = None
    if request.method == "POST":
        # Get the user's name from the form
        name = request.form["name"]
        
        # Generate a random lucky number
        assigned_number = random.randint(1, 100)
        
        # Save the name and lucky number to a text file
        with open("registrations.txt", "a") as file:
            file.write(f"Name: {name}, Lucky Number: {assigned_number}\n")
        
        # Return the rendered page with the name and lucky number
        return render_template("index.html", name=name, assigned_number=assigned_number)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
