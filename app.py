from flask import Flask, render_template
from db_config import init_db
from api_handler import fetch_data
from data_parser import parse_data
from data_encryptor import encrypt_data

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch and parse data
    raw_data = fetch_data()
    parsed_data = parse_data(raw_data)
    
    # Encrypt sensitive data
    encrypted_data = encrypt_data(parsed_data)
    
    # Initialize database and store data
    init_db(encrypted_data)
    
    return render_template('index.html', data=encrypted_data)

if __name__ == '__main__':
    app.run()
