from flask import Flask, jsonify, request
from flask_cors import CORS
from json import loads
import requests
import os.path
import pickle
import dateutil.parser as dp

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
    events = []
    page = 0
    while len(events) < 9:
        url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=zt4Jdbkyp5qGsV6M5GKGHCR3GKlDVgxE&page={page}&countryCode=AU"
        res = requests.get(url)
        events.extend(res.json()['_embedded']['events'])
        events.sort(key = lambda x: x['name'])
        j = 0
        while j < len(events) - 1:
            event1 = events[j]
            # print("event1 " + str(events.index(event1)) + " " + event1['id'] + " " + event1['name'])
            i = j + 1
            while i < len(events):
                event2 = events[i]
                j = i
                # print("event2 " + str(events.index(event2)) + " " + event2['id'] + " " + event2['name'])
                if event1['name'] in event2['name']:
                    events.pop(i)
                    # print("hit")
                else:
                    break
        page += 1

    return jsonify(events[0:9])


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
    eid = loads(request.args.get('getParams'))["id"]
    url = f"https://app.ticketmaster.com/discovery/v2/events/{eid}.json?apikey=zt4Jdbkyp5qGsV6M5GKGHCR3GKlDVgxE"
    res = requests.get(url)
    event = res.json()
    # Get weather information
    r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={event['_embedded']['venues'][0]['location']['latitude']}&lon={event['_embedded']['venues'][0]['location']['longitude']}&appid=b228ffe1aaa8f657c39a46b39d6d9499&units=metric").json()['list']
    date = dp.parse(event['dates']['start']['dateTime'])
    event['date'] = date.strftime('%s')
    weatherInfo = next((i for i in r if i['dt'] > int(event['date'])), None)
    event['weather'] = weatherInfo
    event['favourite'] = False
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
