from flask import Flask, request, jsonify

app = Flask(__name__)

SITES = [
     {'id': 1, 'title': 'Google', 'url': 'http://google.com'},
     {'id': 2, 'title': 'Yahoo', 'url': 'http://yahoo.com'}
]


@app.route('/bookmarks/', methods = ['GET'])
def getall():
        return jsonify(SITES)   

@app.route('/bookmarks/', methods = ['POST'])
def add():
    title = request.args.get('title')
    url = request.args.get('url')
    ultimo_id = SITES[-1]['id']

    SITES.append({
        'id': (int(ultimo_id) + 1),
        'title': title,
        'url': url
    })

    return SITES[(int(ultimo_id))], 201

@app.route('/bookmarks/<int:site_id>', methods = ['PUT'])
def update(site_id):
    sitez = [s for s in SITES if s['id'] == ((site_id))]
    sitez[0]['title'] = request.json['title'] 
    sitez[0]['url'] = request.json['url']

    return jsonify({'atualizado': sitez[0]})

@app.route('/bookmarks/<int:id>', methods = ['DELETE'])
def remove(id):
    sitez = [s for s in SITES if s['id'] == id]
    SITES.remove(sitez[0])
    return jsonify(SITES)


@app.route('/bookmarks/<string:title>', methods = ['GET'])
def getsite(title):
    lista = []
    for elem in SITES:
	    lista.append(elem['title'].lower())
    sitez = [s for s in lista if s == title]

    return jsonify({'site desejado' : sitez[0]})


if __name__ == '__main__':
    app.run(debug=True)