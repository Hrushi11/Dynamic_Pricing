from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('index2.html')

@app.route('/products', methods=['GET', 'POST'])
def products():
    return render_template('products.html', price=1000)

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data.get('input')
    
    # Process the user input as needed (you can do something with it here)
    print(user_input)

    # For example, you can send a response back to the client
    response_data = {"message": "Input received successfully"}
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, port=2000)
