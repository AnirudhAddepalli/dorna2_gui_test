from flask import Flask, render_template, request

app = Flask(__name__)

# Index route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if 'saveButton' in request.form:
        # Retrieve data from the submitted form
        dropdown_value = request.form['dropdownValue']
        input_field_value = request.form['inputFieldValue']

    print(dropdown_value)
    print(input_field_value)

    # Process the data or perform desired actions
    # Add your logic here

    return 'Data submitted successfully'  # Example response

# Route to handle loading tweezers button
@app.route('/load_tweezers', methods=['POST'])
def load_tweezers():
    # Process the loading tweezers action
    # Add your logic here

    return 'Load tweezers action performed'  # Example response

# Route to handle spray position button
@app.route('/spray_position', methods=['POST'])
def spray_position():
    # Process the spray position action
    # Add your logic here

    return 'Spray position action performed'  # Example response

# Route to handle plunge button
@app.route('/plunge', methods=['POST'])
def plunge():
    # Process the plunge action
    # Add your logic here

    return 'Plunge action performed'  # Example response

# Route to handle store grid button
@app.route('/store_grid', methods=['POST'])
def store_grid():
    # Process the store grid action
    # Add your logic here

    return 'Store grid action performed'  # Example response

# Run the Flask application
if __name__ == '__main__':
    app.run()
