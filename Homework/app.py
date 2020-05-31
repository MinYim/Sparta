from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/myshop', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    option_receive = request.form['option_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    
    doc = {
        'name':name_receive,
        'option':option_receive,
        'address':address_receive,
        'phone':phone_receive
    }
    db.myshop.insert_one(doc)

    return jsonify({'result':'success', 'msg': '주문이 접수되었습니다.'})


@app.route('/myshop', methods=['GET'])
def read_reviews():
    orders = list(db.myshop.find({},{'_id':False}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)