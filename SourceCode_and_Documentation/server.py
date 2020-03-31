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
        ,'id': 0
        ,'location': 'Hordern+Pavillion'
        ,'desc': 'Handsome Tours, Astral People, and triple j are thrilled to announce that UK rap phenomenon Stormzy will be returning to Australian shores for an epic national tour in 2020. Having announced his upcoming album Heavy Is The Head, out December 13, Stormzy will perform his biggest shows to date in Perth, Sydney, Adelaide, Melbourne & Brisbane this coming May.The visit represents Stormzy’s first national run of Australian headline performances since his 2017 tour, which saw him sell out two Enmore Theatres in Sydney, two Forums in Melbourne, Thebarton Theatre in Adelaide and Metro City in Perth — not to mention his unforgettable appearance at Splendour In The Grass. Stormzy’s rare blend of swagger and authentic storytelling through his songs has been the winning formula which has allowed him to connect with audiences all over the world. Since his breakthrough, Stormzy has been recognised for his amazing talents having won a multitude of awards including an Ivor Novello, two Brit Awards, six MOBO Awards, two GQ Awards as well as being nominated for a Mercury Prize and NME Award. Once an underdog in the game but now a true frontrunner, Stormzy has played at some of the biggest festivals in Australia and abroad including Listen Out, Field Day, Outlook (CRO) and Wireless (UK) to name a few. However, this year marked a historic moment for the British rapper at Glastonbury Festival. The first black solo British artist to headline the acclaimed festival on the Pyramid Stage wearing a custom-made Banksy bullet-proof vest, Stormzy’s monumental set brought to the stage the likes of notable figures Dave and Fredo, signifying how far British rap music has come in the industry.' 
    },
    {
        'name': 'Rod Stewart',
        'category': 'Music',
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/e17/e18b2a71-25b5-47c5-a2cc-34ceb9e04e17_1294751_CUSTOM.jpg'
        ,'id': 1
        ,'location': 'Roche+Estate'
    },
    {
        'name': 'Together Fest',
        'category': 'Music',
        'img': 'https://discover.ticketmaster.com.au/wp-content/uploads/2020/03/TogetherFest_Graphics_1476x830.jpg'
        ,'id': 2
    },
    {
        'name': 'James Blunt',
        'category': 'Music',
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/ed0/42019ef4-0c2f-4eec-8755-8621ebda7ed0_1216481_CUSTOM.jpg'
        ,'id': 3
    },
    {
        'name': 'NSW Dart Masters',
        'category': 'Sport',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_NSWDartsMasters_2020_720405.jpg?auto=webp'
        ,'id': 4
    },
    {
        'name': 'Nitro Circus Live',
        'category': 'Sport',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_NitroCircus_2018_720405.jpg?auto=webp'
        ,'id': 5
    },
    {
        'name': 'Frozen The Musical',
        'category': 'Music/Arts',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_FrozenTheMusical_2020_V2_720405.jpg?auto=webp'
        ,'id': 6
    },
    {
        'name': 'Hamilton',
        'category': 'Music/Arts',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_Hamilton_2019_720405.jpg?auto=webp'
        ,'id': 7
    },
    {
        'name': 'Hella Mega Tour',
        'category': 'Music',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/HMT_720x405.jpg?auto=webp'
        ,'id': 8
    },
]


# enable CORS
CORS(APP, resources={r'/*':{'origins': '*'}})

signedIn = False
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

@APP.route('/login', methods = ['POST'])
def login():
	global signedIn
	global user
	signedIn = True
	user = request.get_json().get("username")
	return jsonify({})

@APP.route('/signup', methods = ['POST'])
def signup():
	global signedIn
	global user
	signedIn = True
	user = request.get_json().get("username")
	return jsonify({})

@APP.route('/logout', methods = ['POST'])
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

@APP.route('/event', methods=['GET'])
def getEvent():
    eid = int(loads(request.args.get('getParams'))["id"])
    print(eid)
    for event in EVENTS:
        if event['id'] == eid:
            print(event);
            return jsonify(event)

if __name__ == '__main__':
    APP.run()
