from flask_restful import Resource, reqparse
from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request


# sqlHelper = SqlLiteHelper()
# parser = reqparse.RequestParser()
# parser.add_argument('name')


class Pages(Resource):
  def __init__(self):
    self.sqlHelper = SqlLiteHelper()
    self.tabName = 'PAGES'

  def get(self):

    # args = parser.parse_args()
    # print('ppp', args)

    try:
      cmd = 'SELECT * FROM {}'.format(self.tabName)
      res =  self.sqlHelper.execute(cmd)
      resList = []
      for row in res.fetchall():
        data = {
          'id': row[0],
          'projectId': row[1],
          'name': row[2]
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
      cmd = '''INSERT INTO {}(NAME, PROJECTID) VALUES ('{}', '{}')'''.format(self.tabName, data['name'], data['projectId'])
      res =  self.sqlHelper.execute(cmd)
      self.sqlHelper.commit()
      resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
    except Exception as e:
      resp = make_response(jsonify({'code': 500, 'data': {}}))
    return resp