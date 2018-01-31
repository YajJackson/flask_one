from flask import Flask, jsonify, request

app = Flask(__name__)

stores =[
  {
    'name': 'mine', 
    'items': [
      {
        'name': 'My Item',
        'price': 15.99
      }
    ]
  }
]

@app.route('/store', methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)

@app.route('/store/<name>')
def get_store(name):
  return jsonify(next(({'store': s} for s in stores if s['name'] == name), {'message': 'store not found'}))

@app.route('/store')
def get_stores():
   return jsonify({'stores': stores})

@app.route('/store/<name>/item', methods=['POST'])
def create_item_in_store(name):
   pass

@app.route('/store/<name>/item')
def get_items_in_store(name):
  return jsonify(next(({'items': s['items']} for s in stores if s['name'] == name), {'message': 'store not found'}))

app.run(port=5000)
