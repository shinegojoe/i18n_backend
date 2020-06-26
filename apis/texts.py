from flask_restful import Resource
from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request

class Texts(Resource):
    def __init__(self):
        self.sqlHelper = SqlLiteHelper()
        self.tabName = 'texts'


    def get(self):
        try:
            cmd = 'SELECT * FROM {}'.format(self.tabName)
            res =  self.sqlHelper.execute(cmd)
            resList = []
            for row in res.fetchall():
                data = {
                'id': row[0],
                'nameId': row[1],
                'langId': row[2],
                'text': row[3]
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
            cmd = '''INSERT INTO {}(NAMEID, LANGID, TEXT) 
            VALUES ('{}', '{}', '{}')'''.format(self.tabName, data['nameId'], data['langId'], data['text'])
            res =  self.sqlHelper.execute(cmd)
            self.sqlHelper.commit()
            resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
        except Exception as e:
            print('err', e)
            resp = make_response(jsonify({'code': 500, 'data': {}}))
        return resp