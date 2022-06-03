from flask import Flask,request,jsonify, render_template
import wikipedia
from word import list, GM_API_KEY
import googlemaps
import requests

map_client = googlemaps.Client(key=GM_API_KEY)
geoloc_url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key='AIzaSyBVHZn0r4ew-nmCvlI1v27fbfJcKtA31TM'"
map_url = "https://maps.googleapis.com/maps/api/staticmap?"

app = Flask(__name__)
app.config.from_object('config')
@app.route('/')
def index():
    return render_template('result.html')
@app.route('/url',methods=["POST"])

def post():
    valeur = request.form["value"]
    return parser(valeur)

def parser(valeur):
    resulta = ""
    if valeur == "" or valeur == " ":
        return jsonify({"wikipedia":"le formulaire est vide"})
    else :
        liste = valeur.split(" ")
        for word in liste:
            if word not in list:
                resulta += word +" "
        return api_result(resulta)

def api_result(resulta):
    try:
        localisation = map_client.geocode(resulta)
        adresse = localisation[0]['formatted_address']
        mape = requests.get(map_url, {"key"  : GM_API_KEY, "center": adresse, "zoom":15, "size": '400x400', "markers": adresse})
        wikipedia.set_lang('fr')
        wiki = wikipedia.search(resulta)
        page = wikipedia.page(wiki[0] )
        content = wikipedia.summary(wiki[0], sentences = 5)
        if page == 404 or wiki == []:
            return jsonify({"wikipedia":"pas de données"})
        return jsonify({"wikipedia":content, "wikipedia2":page.url, "map":mape.url})
    except Exception as error:
        return jsonify({"wikipedia":"ereur"})

def wiki_search(resulta):
    wikipedia.set_lang('fr')
    wiki = wikipedia.search(resulta)
    page = wikipedia.page(wiki[0])
    return (page.url)

def wiki_summarize(resulta):
    wikipedia.set_lang('fr')
    wiki = wikipedia.search(resulta)
    content = wikipedia.summary(wiki[0], sentences = 5)
    return (content)

def wiki_search_error(resulta):
    wikipedia.set_lang('fr')
    wiki = wikipedia.search(resulta)
    return (wiki)

def google_map_search(resulta):
    localisation = map_client.geocode(resulta)
    adresse = localisation[0]['formatted_address']
    mape = requests.get(map_url, {"key"  : GM_API_KEY, "center": adresse, "zoom":15, "size": '400x400', "markers": adresse})
    return (mape.url)

if __name__ == "__main__":
    app.run()