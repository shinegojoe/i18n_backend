from flask_restful import Resource
from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request

class Langs(Resource):
    def __init__(self):
        self.tabName = 'lang'
        self.sqlHelper = SqlLiteHelper()
    
    def get(self): 
        try:
            cmd = 'SELECT * FROM {}'.format(self.tabName)
            res =  self.sqlHelper.execute(cmd)
            resList = []
            for row in res.fetchall():
                data = {
                'id': row[0],
                'lang': row[1]
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
            cmd = '''INSERT INTO {}(LANG) VALUES ('{}')'''.format(self.tabName, data['lang'])
            res =  self.sqlHelper.execute(cmd)
            self.sqlHelper.commit()
            resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
        except Exception as e:
            resp = make_response(jsonify({'code': 500, 'data': {}}))
        return resp

class Lang(Resource):
    def __init__(self):
        pass

    def delete(self, id):
        pass

    def put(self, id):
        pass