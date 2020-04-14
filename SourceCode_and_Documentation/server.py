from flask import Flask, jsonify, request
from flask_cors import CORS
from json import loads
import requests
import os.path
import pickle

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
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/5e6/b9d2aa5d-7a06-46ae-9acc-ab78877e55e6_1245781_CUSTOM.jpg', 'id': 0, 'location': 'Hordern+Pavillion', 'latitude': -33.8940687, 'longitude': 151.2219894, 'desc': 'Handsome Tours, Astral People, and triple j are thrilled to announce that UK rap phenomenon Stormzy will be returning to Australian shores for an epic national tour in 2020. Having announced his upcoming album Heavy Is The Head, out December 13, Stormzy will perform his biggest shows to date in Perth, Sydney, Adelaide, Melbourne & Brisbane this coming May.The visit represents Stormzy’s first national run of Australian headline performances since his 2017 tour, which saw him sell out two Enmore Theatres in Sydney, two Forums in Melbourne, Thebarton Theatre in Adelaide and Metro City in Perth — not to mention his unforgettable appearance at Splendour In The Grass. Stormzy’s rare blend of swagger and authentic storytelling through his songs has been the winning formula which has allowed him to connect with audiences all over the world. Since his breakthrough, Stormzy has been recognised for his amazing talents having won a multitude of awards including an Ivor Novello, two Brit Awards, six MOBO Awards, two GQ Awards as well as being nominated for a Mercury Prize and NME Award. Once an underdog in the game but now a true frontrunner, Stormzy has played at some of the biggest festivals in Australia and abroad including Listen Out, Field Day, Outlook (CRO) and Wireless (UK) to name a few. However, this year marked a historic moment for the British rapper at Glastonbury Festival. The first black solo British artist to headline the acclaimed festival on the Pyramid Stage wearing a custom-made Banksy bullet-proof vest, Stormzy’s monumental set brought to the stage the likes of notable figures Dave and Fredo, signifying how far British rap music has come in the industry.', 'date': 1587180800, 'favourite': False
    },
    {
        'name': 'Rod Stewart',
        'category': 'Music',
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/e17/e18b2a71-25b5-47c5-a2cc-34ceb9e04e17_1294751_CUSTOM.jpg', 'id': 1, 'location': 'Roche+Estate', 'desc': 'SIR ROD STEWART returns to Australia for an eight-date tour across the country, playing both arenas and winery dates. Kicking off at the Sandalford Winery in Perth on Saturday, October 17 the tour wraps up at Sirromet Wines in Mount Cotton on Saturday, November 7, following stops in Sydney, Melbourne, Geelong, Bowral and the Hunter Valley. Still, at the very top of his game, Stewart has followed a triumphant stadium tour this UK summer with one of his biggest UK tours ever, with live performances running through November and December of 2019. In addition, he has also toured the USA, with highlights including headlining a series of shows at Caesars Palace in Las Vegas as part of a multi-year residency and adding a third sold-out Hollywood Bowl concert in LA for a landmark reunion set with his former bandmate Jeff Beck. Warner Music will honour the legendary singer-songwriter with a new album to be released November 22 which will allow fans to hear Stewart’s biggest hits with his classic vocal style set to full orchestral arrangements.  YOU’RE IN MY HEART: ROD STEWART WITH THE ROYAL PHILHARMONIC ORCHESTRA pairs classical vocal tracks from his most popular songs with new arrangements performed by The Royal Philharmonic Orchestra. In 2019, Sir Rod Stewart celebrates 50 years as a solo artist. The legendary singer-songwriter is one of the best-selling music artists of all time, with more than 250 million records sold worldwide during a stellar career that includes nine #1 albums and 26 Top 10 singles in the UK. Plus, 17 Top 10 albums and 16 Top 10 singles in the US.  As a singer and songwriter his many hits include “You Wear It Well”, “You’re in My Heart”, Tonight’s the Night (The Final Acclaim)”, “Gasoline Alley”, “Every Picture Tells a Story”, “Mandolin Wind”, “Sailing”, “The Killing of Georgie”, “Young Turks”, “Forever Young”, “Hot Legs”, “Infatuation” and the indelible, “Maggie May”. Stewart has earned countless of the industry’s highest awards, among them; two inductions into the Rock and Roll Hall of Fame, GrammyTM Living Legend. In 2016 he officially became “Sir Rod Stewart” after being knighted at Buckingham Palace for his services to music and charity. He has performed for millions of fans on all seven continents, even holding the record for the largest-ever free concert, for an estimated 4.2 million in Rio de Janeiro on New Year’s Eve in 1996.', 'date': '05 APR 2020', 'favourite': False
    },
    {
        'name': 'Together Fest',
        'category': 'Music',
        'img': 'https://discover.ticketmaster.com.au/wp-content/uploads/2020/03/TogetherFest_Graphics_1476x830.jpg', 'id': 2,
        'favourite': False
    },
    {
        'name': 'James Blunt',
        'category': 'Music',
        'img': 'https://s1.ticketm.net/tm/en-au/dam/a/ed0/42019ef4-0c2f-4eec-8755-8621ebda7ed0_1216481_CUSTOM.jpg', 'id': 3,
        'favourite': False
    },
    {
        'name': 'NSW Dart Masters',
        'category': 'Sport',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_NSWDartsMasters_2020_720405.jpg?auto=webp', 'id': 4,
        'favourite': False
    },
    {
        'name': 'Nitro Circus Live',
        'category': 'Sport',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_NitroCircus_2018_720405.jpg?auto=webp', 'id': 5,
        'favourite': False
    },
    {
        'name': 'Frozen The Musical',
        'category': 'Music/Arts',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_FrozenTheMusical_2020_V2_720405.jpg?auto=webp', 'id': 6,
        'favourite': False
    },
    {
        'name': 'Hamilton',
        'category': 'Music/Arts',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/AU_Hamilton_2019_720405.jpg?auto=webp', 'id': 7,
        'favourite': False
    },
    {
        'name': 'Hella Mega Tour',
        'category': 'Music',
        'img': 'https://uk.tmconst.com/ccp-salesforce-images/AU/HMT_720x405.jpg?auto=webp', 'id': 8,
        'favourite': False
    },
]

user_data = []

# loads existing data from file data.p
if os.path.isfile('data.p'):
    user_data = pickle.load(open('data.p', 'rb'))

# loads data into file data.p


def save():
    with open('data.p', 'wb') as FILE:
        pickle.dump(user_data, FILE)


# enable CORS
CORS(APP, resources={r'/*': {'origins': '*'}})

signedIn = False
user = {
    'first_name': '',
    'last_name': '',
    'email': '',
    'username': '',
    'password': ''
}
@APP.route('/nav')
def nav():
    response = {
        'navBarHeaders': NAVBAR,
        'signedIn': signedIn,
        'user': user['username']
    }
    return jsonify(response)


@APP.route('/events')
def events():
    return jsonify(EVENTS)


@APP.route('/login', methods=['POST'])
def login():
    global user_data
    global signedIn
    global user
    username = request.get_json().get("username")
    password = request.get_json().get("password")
    
    for i in user_data:
        if i['username'] == username and i['password'] == password:
            signedIn = True
            user = i
            return jsonify('success')
    return jsonify('fail')

@APP.route('/signup', methods = ['POST'])
def signup():
    global user_data
    first_name = request.get_json().get("firstName")
    last_name = request.get_json().get("lastName")
    email = request.get_json().get("email")
    username = request.get_json().get("username")
    password = request.get_json().get("password")
    user_data.append({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username,
        'password': password
    })
    print(user_data)
    save()
    return jsonify({})

@APP.route('/logout', methods = ['POST'])
def logout():
	global signedIn
	signedIn = False
	return jsonify({})

@APP.route('/search', methods=['GET'])
def search():
    response = []
    print(loads(request.args.get('getParams')))
    searchTerm = (loads(request.args.get('getParams'))["searchTerm"])
    category = (loads(request.args.get('getParams'))["category"])
    for event in EVENTS:
        if searchTerm in event['name'] or searchTerm in event['category']:
            response.append(event)
    if category is not None and category != 'Any category':
        filteredResponse = filterCategory(response, category)
        return jsonify(filteredResponse)
    return jsonify(response)

@APP.route('/categories', methods=['GET'])
def getCategories():
    response = []
    for event in EVENTS:
        if event['category'] not in response:
            response.append(event['category'])
    return jsonify(response)

@APP.route('/event', methods=['GET'])
def getEvent():
    eid = int(loads(request.args.get('getParams'))["id"])
    print(eid)
    for event in EVENTS:
        if event['id'] == eid:
            # Get weather information
            r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={event['latitude']}&lon={event['longitude']}&appid=b228ffe1aaa8f657c39a46b39d6d9499&units=metric").json()['list']
            weatherInfo = next((i for i in r if i['dt'] > event['date']), None)
            event['weather'] = weatherInfo
            print(event)
            return jsonify(event)

@APP.route('/favourite', methods=['POST'])
def favourite():
    eid = request.get_json().get('eid')
    favourite = request.get_json().get('isFavourite')
    for event in EVENTS:
        if event['id'] == eid:
            event['favourite'] = favourite
    return jsonify({})

def filterCategory(events, category):
    response = []
    for event in events:
        if event['category'] == category:
            response.append(event)
    return response

if __name__ == '__main__':
    APP.run()
