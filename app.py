from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Home Page'
first_name = 'albert'
sur_name = 'cova32'
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8070, debug=False)
