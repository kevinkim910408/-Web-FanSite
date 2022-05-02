from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# mongoDB - pymongo, dnspython 패키지
from pymongo import MongoClient

# sparta@cluster0 (내 db폴더이름@내클러스터이름)
client = MongoClient('mongodb+srv://test:sparta@cluster0.m7jzf.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 기본으로 보여줄 index.html 파일
@app.route('/')
def home():
   return render_template('index.html')

# post comment and name
@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.fanSite.insert_one(doc)
    return jsonify({'msg':'Saved!'})

# get all of data from db
@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.fanSite.find({},{'_id':False}))
    return jsonify({'msg':comment_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)