from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to execute Python script
@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        os.system('python ml_gui.py')
        #os.system('ml_gui.py')
        return jsonify({"status": "success", "message": "Process executed successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
