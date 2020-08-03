# from flask import Flask, render_template, request, redirect, url_for, make_response
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
# from model import validate_image, schools, topics
# from datetime import datetime
# import os
# import base64

# app = Flask(__name__)
# ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
# app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 2
# app.config['MONGO_DBNAME'] = 'Team-1'
# app.config['MONGO_URI'] = 'mongodb+srv://kwilliams:' + os.getenv(
#     "MONGOBD_PASS"
# ) + '@cluster0.g9lms.mongodb.net/Team-1?retryWrites=true&w=majority'
# mongo = PyMongo(app)


# # Index
# @app.route('/')
# def index():
#     return render_template('index.html', path=request.path, topics=topics())


# # About Us
# @app.route('/about')
# def about():
#     return render_template('about.html')


# # Activism
# @app.route('/activism')
# def activism():
#     return render_template(
#         'activism/index.html',
#         path=request.path,
#         posts=mongo.db.activism.find({}),
#         topics=topics())


# @app.route('/activism/create')
# def createActivism():
#     return render_template(
#         'activism/create.html',
#         path=request.path,
#         schools=schools(),
#         topics=topics(),
#         school=request.cookies.get('school'))


# @app.route('/activism/post/<objectID>')
# def postActivism(objectID):
#     return render_template(
#         'activism/post.html',
#         path=request.path,
#         post=mongo.db.activism.find_one_or_404({
#             '_id': ObjectId(objectID)
#         }),
#         topics=topics())


# @app.route('/activism/render', methods=["POST"])
# def renderActivism():
#     image = ''
#     uploaded_file = request.files.get('image')
#     if uploaded_file.filename != '' and \
#       os.path.splitext(uploaded_file.filename)[1] not in ALLOWED_EXTENSIONS and \
#       os.path.splitext(uploaded_file.filename)[1] == validate_image(uploaded_file.stream):
#         image = base64.b64encode(uploaded_file.read()).decode(
#             'ascii', 'strict')
#         image_format = validate_image(uploaded_file.stream)
#     else:
#         image = ''
#         image_format = ''

#     posts = mongo.db.activism
#     post = posts.insert_one({
#         'title': request.form.get('title'),
#         'description': request.form.get('description'),
#         'image': image,
#         'image_format': image_format,
#         'school': request.form.get('school'),
#         'time': datetime.now()
#     })
#     response = make_response(
#         redirect(url_for('postActivism', objectID=post.inserted_id)))
#     response.set_cookie("school", request.form.get('school'))
#     return response


# # Casual
# @app.route('/casual')
# def casual():
#     if request.args.get('t'):
#         return render_template(
#             'casual/index.html',
#             path=request.path,
#             posts=mongo.db.casual.find({
#                 'topic': request.args.get('t')
#             }),
#             topics=topics(),
#             topic=request.args.get('t'))
#     return render_template(
#         'casual/index.html',
#         path=request.path,
#         posts=mongo.db.casual.find({}),
#         topics=topics(),
#         topic='')


# @app.route('/casual/create')
# def createCasual():
#     return render_template(
#         'casual/create.html',
#         path=request.path,
#         schools=schools(),
#         topics=topics(),
#         school=request.cookies.get('school'))


# @app.route('/casual/post/<objectID>')
# def postCasual(objectID):
#     return render_template(
#         'casual/post.html',
#         post=mongo.db.casual.find_one_or_404({
#             '_id': ObjectId(objectID)
#         }),
#         path=request.path,
#         topics=topics())


# @app.route('/casual/render', methods=["POST"])
# def renderCasual():
#     uploaded_file = request.files['image']
#     if uploaded_file.filename != '' and \
#       os.path.splitext(uploaded_file.filename)[1] not in ALLOWED_EXTENSIONS and \
#       os.path.splitext(uploaded_file.filename)[1] == validate_image(uploaded_file.stream):
#         image = base64.b64encode(uploaded_file.read()).decode(
#             'ascii', 'strict')
#         image_format = validate_image(uploaded_file.stream)
#     else:
#         image = ''
#         image_format = ''

#     posts = mongo.db.casual
#     post = posts.insert_one({
#         'title': request.form['title'],
#         'description': request.form['description'],
#         'image': image,
#         'image_format': image_format,
#         'school': request.form['school'],
#         'topic': request.form['topic'],
#         'time': datetime.now()
#     })
#     response = make_response(
#         redirect(url_for('postCasual', objectID=post.inserted_id)))
#     response.set_cookie('school', request.form.get('school'))
#     return response


# app.run(host='0.0.0.0', port=8080)
