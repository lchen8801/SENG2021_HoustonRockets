from flask import Flask, jsonify, render_template
from flask_cors import CORS

# config
DEBUG = True

# Create the application.
APP = Flask(__name__)
APP.config.from_object(__name__)

NAVBAR = [
    {
        'title': 'Music',
        'items': ['All Music', 'Country', 'Dance/EDM', 'Jazz', 'Pop', 'Rap', 'Rock', 'World']
    },
    {
        'title': 'Sport',
        'items': ['All Sport', 'AFL', 'Basketball', 'Boxing', 'Cricket', 'Golf', 'Horse Racing', 'Netball', 'Rugby', 'Soccer', 'Tennis']
    },
    {
        'title': 'Arts',
        'items': ['All Arts', 'Ballet and Dance', 'Classical', 'Comedy', 'Fashion', 'Museums and Exhibits', 'Musical', 'Plays']
    },
    {
        'title': 'Food',
        'items': ['All Food', 'Fairs', 'Markets']
    }
]

# enable CORS
CORS(APP, resources={r'/*':{'origins': '*'}})

@APP.route('/test', methods=['GET'])
def test():
    return jsonify('why wont bootstrap work')

@APP.route('/')
def index():
    return jsonify(NAVBAR)


if __name__ == '__main__':
    APP.run()
