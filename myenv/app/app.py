# Entry file to run this backend 
from flask import Flask
from controller.controller import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)