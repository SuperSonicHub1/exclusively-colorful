from flask import Flask, render_template, flash, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from model import validate_image, schools
from datetime import datetime
import os
import base64

app = Flask(__name__)
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 2
app.config['MONGO_DBNAME'] = 'Team-1'
app.config['MONGO_URI'] = 'mongodb+srv://kwilliams:' + os.getenv("MONGOBD_PASS") + '@cluster0.g9lms.mongodb.net/Team-1?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Index
@app.route('/')
def index():
  return render_template('index.html', path=request.path)


# Activism
@app.route('/activism')
def activism():
  return render_template('activism/index.html', path=request.path, posts=mongo.db.activism.find({}))

@app.route('/activism/create')
def createActivism():
  return render_template('activism/create.html',schools=schools())

@app.route('/activism/post/<objectID>')
def postActivism(objectID):
  return render_template('activism/post.html', post=mongo.db.activism.find_one_or_404({'_id': ObjectId(objectID)}))

@app.route('/activism/render', methods=["POST"])
def renderActivism():
  uploaded_file = request.files['image']
  if uploaded_file.filename != '' and \
    os.path.splitext(uploaded_file.filename)[1] not in ALLOWED_EXTENSIONS and \
    os.path.splitext(uploaded_file.filename)[1] == validate_image(uploaded_file.stream):
    image = base64.b64encode(uploaded_file.read()).decode('ascii', 'strict')
  else:
    image = ''

  posts = mongo.db.activism
  post = posts.insert_one({
      'title':request.form['title'],
      'description': request.form['description'],
      'image': image,
      'school': request.form['school'],
      'time': datetime.now()
  })
  return redirect(url_for('postActivism', objectID=post.inserted_id))

# Casual
@app.route('/casual')
def casual():
  return render_template('casual/index.html', path=request.path, posts=mongo.db.casual.find({}))


@app.route('/casual/create')
def createCasual():
  return render_template('casual/create.html',schools=schools())

@app.route('/casual/post/<objectID>')
def postCasual(objectID):
  return render_template('casual/post.html', post=mongo.db.casual.find_one_or_404({'_id': ObjectId(objectID)}))

@app.route('/casual/render', methods=["POST"])
def renderCasual():
  uploaded_file = request.files['image']
  if uploaded_file.filename != '' and \
    os.path.splitext(uploaded_file.filename)[1] not in ALLOWED_EXTENSIONS and \
    os.path.splitext(uploaded_file.filename)[1] == validate_image(uploaded_file.stream):
    image = base64.b64encode(uploaded_file.read()).decode('ascii', 'strict')
  else:
    image = ''

  posts = mongo.db.casual
  post = posts.insert_one({
      'title':request.form['title'],
      'description': request.form['description'],
      'image': image,
      'school': request.form['school'],
      'time': datetime.now()
  })
  return redirect(url_for('postCasual', objectID=post.inserted_id))

app.run(host='0.0.0.0', port=8080)
