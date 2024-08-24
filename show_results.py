# app.py
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    script_path = 'question_final/format_data.py'
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    return jsonify({'output': result.stdout, 'error': result.stderr})

if __name__ == '__main__':
    app.run(debug=True)
