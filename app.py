from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Step 2: Generate and Store Numbers in a Text File (once at the start)
def generate_and_store_numbers():
    # Generate a list of numbers from 1 to 100
    numbers = list(range(1, 78))
    random.shuffle(numbers)  # Shuffle numbers to randomize their order

    # Store these numbers in a text file
    with open("assigned_numbers.txt", "w") as file:
        for number in numbers:
            file.write(f"{number}\n")
    
    print("Numbers have been generated and stored.")

# Step 3: Assign a Number to a User and Store Name and Number
def assign_number(name):
    with open("assigned_numbers.txt", "r") as file:
        numbers = file.readlines()

    # Check if there are any numbers left
    if numbers:
        # Assign the first number to the user
        assigned_number = numbers.pop(0).strip()  # Remove newline
        
        # Write the updated list back to the file (removes assigned number)
        with open("assigned_numbers.txt", "w") as file:
            file.writelines(numbers)
        
        # Store the name and assigned number in the result file
        with open("assigned_numbers_results.txt", "a") as result_file:
            result_file.write(f"{name} - {assigned_number}\n")
        
        return assigned_number
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the name from the form submission
        name = request.form.get('name')
        
        # Assign a unique number
        assigned_number = assign_number(name)
        
        if assigned_number:
            # Return a response with the assigned number
            return render_template('index.html', assigned_number=assigned_number, name=name)
        else:
            return "Sorry, no numbers are available."
    return render_template('index.html')

if __name__ == "__main__":
    # Generate and store numbers once when the app starts (only the first time)
    generate_and_store_numbers()
    app.run(host ='0.0.0.0', port = 80)
