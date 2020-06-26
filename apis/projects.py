from flask_restful import Resource
from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request


# sqlHelper = SqlLiteHelper()

class Projects(Resource):
  def __init__(self):
    self.sqlHelper = SqlLiteHelper()
    self.tabName = 'projects'

  def get(self):
    try:
      cmd = 'SELECT * FROM {}'.format(self.tabName)
      res =  self.sqlHelper.execute(cmd)
      resList = []
      for row in res.fetchall():
        data = {
          'id': row[0],
          'name': row[1]
        }
        resList.append(data)
      resp = make_response(jsonify({'code': 200,'data': resList}))
  
    except Exception as e:
      print('error', e)
      resp = make_response(jsonify({'code': 500, 'data': {}}))
  
    return resp

  def post(self):
    try:
      data = request.get_json(force=True)
      print(data)
      cmd = '''INSERT INTO {}(NAME) VALUES ('{}')'''.format(self.tabName, data['name'])
      res =  self.sqlHelper.execute(cmd)
      self.sqlHelper.commit()
      resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
    except Exception as e:
      resp = make_response(jsonify({'code': 500, 'data': {}}))
    return resp

class Project(Resource):
  def __init__(self):
    self.sqlHelper = SqlLiteHelper()
    self.tabName = 'projects'



  def delete(self, id):
    try:
      print('id', id)
      cmd = '''DELETE FROM {} WHERE ID={}'''.format(self.tabName ,id)
      self.sqlHelper.execute(cmd)
      self.sqlHelper.commit()
      resp = make_response(jsonify({'code': 200,'data': 'sucess'}))

    except Exception as e:
      print('err', e)
      resp = make_response(jsonify({'code': 500, 'data': {}}))

    return resp


  def put(self, id):
    try:
      data = request.get_json(force=True)
      print('data', data)
      cmd = '''UPDATE {} SET NAME='{}' WHERE ID={}'''.format(self.tabName, data['name'], id)
      self.sqlHelper.execute(cmd)
      self.sqlHelper.commit()
      resp = make_response(jsonify({'code': 200,'data': 'sucess'}))

    except Exception as e:
      print('err', e)
      resp = make_response(jsonify({'code': 500, 'data': {}}))
    
    return resp
