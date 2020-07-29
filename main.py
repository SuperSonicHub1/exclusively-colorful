from flask import Flask, render_template, flash, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from model import validate_image
import os
import base64

app = Flask(__name__)
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 2
app.config['MONGO_DBNAME'] = 'Team-1'
app.config['MONGO_URI'] = 'mongodb+srv://kwilliams:' + os.getenv("MONGOBD_PASS") + '@cluster0.g9lms.mongodb.net/Team-1?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def index():
  return render_template('index.html', path=request.path)

@app.route('/create')
def create():
  return render_template('create.html', path=request.path)

@app.route('/post/<objectID>')
def post(objectID):
  return render_template('post.html', post=mongo.db.posts.find_one_or_404({'_id': ObjectId(objectID)}))

@app.route('/render', methods=["POST"])
def render():
  uploaded_file = request.files['image']
  if uploaded_file.filename != '' and \
    os.path.splitext(uploaded_file.filename)[1] not in ALLOWED_EXTENSIONS and \
    os.path.splitext(uploaded_file.filename)[1] == validate_image(uploaded_file.stream):
    image = base64.b64encode(uploaded_file.read())
  else:
    image = ''

  posts = mongo.db.posts
  post = posts.insert_one({
      'title':request.form['title'],
      'description': request.form['description'],
      'image': image,
      'school': request.form['school'],
  })
  return redirect(url_for('post', objectID=post.inserted_id))

app.run(host='0.0.0.0', port=8080)