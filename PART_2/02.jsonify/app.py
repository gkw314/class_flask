from flask import request
from flask import Flask, jsonify

app = Flask(__name__)


# GET
# 게시글을 조회하는 api
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'results':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}

    return data

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_fone_feed(feed_id):
    print(feed_id)
    data = {'results':'success', 'data':{'feed1':'data1'}}
    
    return data


# POST
# 게시글을 작성하는 api
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result':'success'})


## 데이타 추가하기

datas = [{"items": [{"name": "item1", "price": 10}]}]

@app.route("/api/v1/datas", methods=['GET'])
def get_datas():
    return {'datas':datas}

@app.route("/api/v1/datas", methods=['POST'])
def create_data():
    request_data = request.get_json()

    new_data = {"items": request_data.get('items', [])}
    datas.append(new_data)

    return new_data, 201