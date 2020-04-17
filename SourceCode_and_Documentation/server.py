from flask import Flask, jsonify, request
from flask_cors import CORS
from json import loads
import requests
import os.path
import pickle
import dateutil.parser as dp
from datetime import datetime, timedelta

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
    'password': '',
    'favourites': []
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
        'password': password,
        'favourites': []
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
    print(loads(request.args.get('getParams')))
    searchTerm = (loads(request.args.get('getParams'))["searchTerm"])
    date = (loads(request.args.get('getParams'))["date"])
    location = (loads(request.args.get('getParams'))["location"])
    category = (loads(request.args.get('getParams'))["category"])
    genre = (loads(request.args.get('getParams'))["genre"])
    
    classification = []
    if category != '' and category != 'Any category':
        classification.append(category)
    if genre != '' and genre != 'Any genre':
        classification.append(genre)
    if len(classification) == 0:
        classification = ''
    
    if date == 'Any Date' or date == '':
        startDate = ''
        endDate = ''
    elif date == 'Today':
        startDate = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')
        endDate = datetime.today().strftime('%Y-%m-%dT23:59:59Z')
    elif date == 'Tomorrow':
        startDate = (datetime.today() + timedelta(days = 1)).strftime('%Y-%m-%dT00:00:00Z')
        endDate = (datetime.today() + timedelta(days = 1)).strftime('%Y-%m-%dT23:59:59Z')
    elif date == 'This week':
        startDate = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')
        endDate = (datetime.today() + timedelta(days = 7)).strftime('%Y-%m-%dT23:59:59Z')
    else:
        print(f"date: {date}")
        startDate = dp.parse(date).strftime('%Y-%m-%dT00:00:00Z')
        endDate = dp.parse(date).strftime('%Y-%m-%dT23:59:59Z')

    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=zt4Jdbkyp5qGsV6M5GKGHCR3GKlDVgxE&keyword={searchTerm}&classificationName={classification}&startDateTime={startDate}&endDateTime={endDate}&countryCode=AU"
    print(url)
    res = requests.get(url)
    if '_embedded' in res.json():
        events = res.json()['_embedded']['events']
        return jsonify(events)
    else:
        return ''

@APP.route('/categories', methods=['GET'])
def getCategories():
    response = {
        'categories': [],
        'genres': []
    }
    searchTerm = (loads(request.args.get('getParams'))["searchTerm"])
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=zt4Jdbkyp5qGsV6M5GKGHCR3GKlDVgxE&keyword={searchTerm}&countryCode=AU"
    res = requests.get(url)
    events = res.json()['_embedded']['events']
    for event in events:
        if event['classifications'][0]['segment']['name'] not in response['categories']:
            response['categories'].append(event['classifications'][0]['segment']['name'])
        if event['classifications'][0]['genre']['name'] not in response['genres']:
            response['genres'].append(event['classifications'][0]['genre']['name'])
    return jsonify(response)

@APP.route('/event', methods=['GET'])
def getEvent():
    eid = loads(request.args.get('getParams'))["id"]
    url = f"https://app.ticketmaster.com/discovery/v2/events/{eid}.json?apikey=zt4Jdbkyp5qGsV6M5GKGHCR3GKlDVgxE"
    res = requests.get(url)
    event = res.json()
    # Get weather information
    r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={event['_embedded']['venues'][0]['location']['latitude']}&lon={event['_embedded']['venues'][0]['location']['longitude']}&appid=b228ffe1aaa8f657c39a46b39d6d9499&units=metric").json()['list']
    try:
        date = dp.parse(event['dates']['start']['dateTime'])
    except:
        date = dp.parse(event['dates']['start']['localDate'])
        date += timedelta(hours = 16)
    event['date'] = date.strftime('%s')
    weatherInfo = next((i for i in r if i['dt'] >= int(event['date'])), None)
    event['weather'] = weatherInfo
    event['favourite'] = False
    try:
        x = list(event['_embedded']['attractions'][0]['externalLinks'].keys())
        print(x)
        for i in x:
            print(i)
            if 'url' in event['_embedded']['attractions'][0]['externalLinks'][i][0].keys():
                event['_embedded']['attractions'][0]['externalLinks'][i][0]['imageLink'] = '/assets/' + i + '.png'
            else:
                event['_embedded']['attractions'][0]['externalLinks'].pop(i)
            if i == 'wiki':
                title = event['_embedded']['attractions'][0]['externalLinks'][i][0]['url'].split('/')[-1]
                r = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext=1&titles={title}").json()['query']['pages']
                event['description'] = r[list(r.keys())[0]]['extract'].split('\n\n\n')[0]
                event['_embedded']['attractions'][0]['externalLinks'].pop('wiki')
    except:
        pass

    if not event['_embedded']['attractions'][0]['externalLinks']:
        event['_embedded']['attractions'][0].pop('externalLinks')

    if 'description' not in event.keys():
        query = event['name']
        if len(query.split()) > 3:
            query = ' '.join(query.split()[0:3])
        r = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&utf8=&format=json").json()
        title = r['query']['search'][0]['title']
        r = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext=1&titles={title}").json()['query']['pages']
        event['description'] = r[list(r.keys())[0]]['extract'].split('\n\n\n')[0]
    return jsonify(event)

@APP.route('/favourite', methods=['POST'])
def favourite():
    global signedIn
    global user
    if signedIn:
        print(user)
        eid = request.get_json().get('eid')
        if eid not in user['favourites']:
            user['favourites'].append(eid)
        else:
            user['favourites'].remove(eid)        
    return jsonify({})

def filterCategory(events, category):
    response = []
    for event in events:
        if event['category'] == category:
            response.append(event)
    return response

@APP.route('/get_favourites', methods=['GET'])
def get_favourites():
    favourites = []
    global user
    for favourite in user['favourites']:
        url = f"https://app.ticketmaster.com/discovery/v2/events/{favourite}.json?apikey=zt4Jdbkyp5qGsV6M5GKGHCR3GKlDVgxE"
        res = requests.get(url)
        event = res.json()
        print(event)
        favourites.append(event)
    return jsonify(favourites)

@APP.route('/check_signed', methods=['GET'])
def signed():
    global signedIn
    return jsonify(signedIn)

if __name__ == '__main__':
    APP.run()
