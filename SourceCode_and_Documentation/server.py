from flask import Flask, jsonify, request
from flask_cors import CORS
from json import loads

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

EVENTS = [
    {
        'name': 'Stormzy',
        'category': 'Music',
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/5e6/b9d2aa5d-7a06-46ae-9acc-ab78877e55e6_1245781_CUSTOM.jpg'
    },
    {
        'name': 'Rod Stewart',
        'category': 'Music',
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/e17/e18b2a71-25b5-47c5-a2cc-34ceb9e04e17_1294751_CUSTOM.jpg'
    },
    {
        'name': 'Together Fest',
        'category': 'Music',
        'img': 'https://discover.ticketmaster.com.au/wp-content/uploads/2020/03/TogetherFest_Graphics_1476x830.jpg'
    },
    {
        'name': 'James Blunt',
        'category': 'Music',
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/ed0/42019ef4-0c2f-4eec-8755-8621ebda7ed0_1216481_CUSTOM.jpg'
    },
    {
        'name': 'NSW Dart Masters',
        'category': 'Sport',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_NSWDartsMasters_2020_720405.jpg?auto=webp'
    },
    {
        'name': 'Nitro Circus Live',
        'category': 'Sport',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_NitroCircus_2018_720405.jpg?auto=webp'
    },
    {
        'name': 'Frozen The Musical',
        'category': 'Music/Arts',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_FrozenTheMusical_2020_V2_720405.jpg?auto=webp'
    },
    {
        'name': 'Hamilton',
        'category': 'Music/Arts',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_Hamilton_2019_720405.jpg?auto=webp'
    },
    {
        'name': 'Hella Mega Tour',
        'category': 'Music',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/HMT_720x405.jpg?auto=webp'
    },
]


# enable CORS
CORS(APP, resources={r'/*':{'origins': '*'}})

signedIn = True
user = "Luke"
@APP.route('/nav')
def nav():
    response = {
        'navBarHeaders': NAVBAR,
        'signedIn': signedIn,
        'user': user
    }
    return jsonify(response)

@APP.route('/events')
def events():
    return jsonify(EVENTS)

@APP.route('/login')
def login():
	global signedIn
	signedIn = True
	return jsonify({})

@APP.route('/logout')
def logout():
	global signedIn
	signedIn = False
	return jsonify({})

@APP.route('/search', methods=['GET'])
def search():
    response = []
    searchTerm = (loads(request.args.get('getParams'))["searchTerm"])
    for event in EVENTS:
        if event['name'] == searchTerm:
            response.append(event)
    return jsonify(response)

@APP.route('/categories', methods=['GET'])
def getCategories():
    response = []
    for event in EVENTS:
        print(event)
        if event['category'] not in response:
            response.append(event['category'])
    return jsonify(response)

if __name__ == '__main__':
    APP.run()
