from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Folk, Rock, Rhythm, folk_schema, folks_schema, rock_schema, rocks_schema, rhythm_schema, rhythms_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

# ---------------------------------------------------------------
#  FOLK ROUTES

@api.route('/folk', methods = ['POST'])
@token_required
def create_folk(current_user_token):
    working_title = request.json['working_title']
    genre = request.json['genre']
    writer_name = request.json['writer_name']
    length = request.json['length']
    rating = request.json['rating']
    latest_user_update = request.json['latest_user_update']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    folk = Folk(working_title, genre, writer_name, length, rating, latest_user_update, user_token = user_token )

    db.session.add(folk)
    db.session.commit()

    response = folk_schema.dump(folk)
    return jsonify(response)



@api.route('/folk', methods = ['GET'])
@token_required
def get_folk(current_user_token):
    a_user = current_user_token.token
    folks = Folk.query.filter_by(user_token = a_user).all()
    response = folks_schema.dump(folks)
    return jsonify(response)



@api.route('/folk/<id>', methods = ['GET'])
@token_required
def get_single_folk(current_user_token, id):
    folk = Folk.query.get(id)
    response = folk_schema.dump(folk)
    return jsonify(response)



@api.route('/folk/<id>', methods = ['POST','PUT'])
@token_required
def update_folk(current_user_token,id):
    folk = Folk.query.get(id) 
    folk.working_title = request.json['working_title']
    folk.genre = request.json['genre']
    folk.writer_name = request.json['writer_name']
    folk.length = request.json['length']
    folk.rating = request.json['rating']
    folk.latest_user_update = request.json['latest_user_update']
    folk.user_token = current_user_token.token

    db.session.commit()
    response = folk_schema.dump(folk)
    return jsonify(response)



@api.route('/folk/<id>', methods = ['DELETE'])
@token_required
def delete_folk(current_user_token, id):
    folk = Folk.query.get(id)
    db.session.delete(folk)
    db.session.commit()
    response = folk_schema.dump(folk)
    return jsonify(response)

#-----------------------------------------------------------
# ROCK ROUTES


@api.route('/rock', methods = ['POST'])
@token_required
def create_rock(current_user_token):
    working_title = request.json['working_title']
    genre = request.json['genre']
    writer_name = request.json['writer_name']
    length = request.json['length']
    rating = request.json['rating']
    latest_user_update = request.json['latest_user_update']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    rock = Rock(working_title, genre, writer_name, length, rating, latest_user_update, user_token = user_token )

    db.session.add(rock)
    db.session.commit()

    response = rock_schema.dump(rock)
    return jsonify(response)



@api.route('/rock', methods = ['GET'])
@token_required
def get_rock(current_user_token):
    a_user = current_user_token.token
    rocks = Rock.query.filter_by(user_token = a_user).all()
    response = rocks_schema.dump(rocks)
    return jsonify(response)



@api.route('/rock/<id>', methods = ['GET'])
@token_required
def get_single_rock(current_user_token, id):
    rock = Rock.query.get(id)
    response = rock_schema.dump(rock)
    return jsonify(response)



@api.route('/rock/<id>', methods = ['POST','PUT'])
@token_required
def update_rock(current_user_token,id):
    rock = Rock.query.get(id) 
    rock.working_title = request.json['working_title']
    rock.genre = request.json['genre']
    rock.writer_name = request.json['writer_name']
    rock.length = request.json['length']
    rock.rating = request.json['rating']
    rock.latest_user_update = request.json['latest_user_update']
    rock.user_token = current_user_token.token

    db.session.commit()
    response = rock_schema.dump(rock)
    return jsonify(response)



@api.route('/rock/<id>', methods = ['DELETE'])
@token_required
def delete_rock(current_user_token, id):
    rock = Rock.query.get(id)
    db.session.delete(rock)
    db.session.commit()
    response = rock_schema.dump(rock)
    return jsonify(response)

#-----------------------------------------------------------
# RHYTHM & BLUES ROUTES

@api.route('/rhythm_blues', methods = ['POST'])
@token_required
def create_rhythm(current_user_token):
    working_title = request.json['working_title']
    genre = request.json['genre']
    writer_name = request.json['writer_name']
    length = request.json['length']
    rating = request.json['rating']
    latest_user_update = request.json['latest_user_update']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    rhythm = Rhythm(working_title, genre, writer_name, length, rating, latest_user_update, user_token = user_token )

    db.session.add(rhythm)
    db.session.commit()

    response = rhythm_schema.dump(rhythm)
    return jsonify(response)



@api.route('/rhythm_blues', methods = ['GET'])
@token_required
def get_rhythm(current_user_token):
    a_user = current_user_token.token
    rhythms = Rhythm.query.filter_by(user_token = a_user).all()
    response = rhythms_schema.dump(rhythms)
    return jsonify(response)



@api.route('/rhythm_blues/<id>', methods = ['GET'])
@token_required
def get_single_rhythm(current_user_token, id):
    rhythm = Rhythm.query.get(id)
    response = rhythm_schema.dump(rhythm)
    return jsonify(response)



@api.route('/rhythm_blues/<id>', methods = ['POST','PUT'])
@token_required
def update_rhythm(current_user_token,id):
    rhythm = Rhythm.query.get(id) 
    rhythm.working_title = request.json['working_title']
    rhythm.genre = request.json['genre']
    rhythm.writer_name = request.json['writer_name']
    rhythm.length = request.json['length']
    rhythm.rating = request.json['rating']
    rhythm.latest_user_update = request.json['latest_user_update']
    rhythm.user_token = current_user_token.token

    db.session.commit()
    response = rhythm_schema.dump(rhythm)
    return jsonify(response)



@api.route('/rhythm_blues/<id>', methods = ['DELETE'])
@token_required
def delete_rhythm(current_user_token, id):
    rhythm = Rhythm.query.get(id)
    db.session.delete(rhythm)
    db.session.commit()
    response = rhythm_schema.dump(rhythm)
    return jsonify(response)



