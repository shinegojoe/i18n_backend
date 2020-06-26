from flask_restful import Resource
from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request
from tableList import tableList

class AddLangCol(Resource):
    pass

class AddNewRow(Resource):
    pass

class PageTexts(Resource):
    def __init__(self):
        self.sqlHelper = SqlLiteHelper()

    
    def getLangList(self):
        cmd = 'SELECT * FROM {}'.format(tableList['langs'])
        res =  self.sqlHelper.execute(cmd)
        langList = []
        for row in res.fetchall():
            data = {
                'id': row[0],
                'lang': row[1]
            }
            langList.append(data)
        return langList

    def getNameList(self, pageId):
        cmd = 'SELECT * FROM {} WHERE pageId = {}'.format(tableList['names'], pageId)
        res =  self.sqlHelper.execute(cmd)
        nameList = []
        for row in res.fetchall():
            # print(row)
            data = {
                'id': row[0],
                'pageId': row[1],
                'name': row[2]
            }
            nameList.append(data)
        return nameList


    def get(self):
        try:
            resList = []
            args = request.args
            pageId = args['pageId']
            langId = args['langId']
            print('ppp', args)
            langList = self.getLangList()
            nameList = self.getNameList(pageId=pageId)
            for item in nameList:
                # print('item', item)
                data = {}
                data['name'] = item['name']
                for lang in langList:
                    langName = lang['lang']
                    cmd = 'SELECT * FROM {} WHERE nameID = {} AND langId = {}'.format(tableList['texts'], item['id'], lang['id'])
                    res =  self.sqlHelper.execute(cmd)
                    for row in res.fetchall():
                        # print('xxx', row)
                        data[langName] = row[3]
                print('data', data)
                resList.append(data)
                    
            resp = make_response(jsonify({'code': 200,'data': resList}))

        except Exception as e:
            print('err', e)
            resp = make_response(jsonify({'code': 500, 'data': {}}))

        return resp



class LangTexts(Resource):
    def __init__(self):
        self.sqlHelper = SqlLiteHelper()

    def getPageList(self, projectId):
        cmd = 'SELECT * FROM {} WHERE PROJECTID = {}'.format(tableList['pages'], projectId)
        res =  self.sqlHelper.execute(cmd)
        pageList = []
        for row in res.fetchall():
            data = {
                'id': row[0],
                # 'projectId': row[1],
                'name': row[2]
            }
            pageList.append(data)
        return pageList

    def getNameList(self, pageId):
        cmd = 'SELECT * FROM {} WHERE pageId = {}'.format(tableList['names'], pageId)
        res =  self.sqlHelper.execute(cmd)
        nameList = []
        for row in res.fetchall():
            # print(row)
            data = {
                'id': row[0],
                'pageId': row[1],
                'name': row[2]
            }
            nameList.append(data)
        return nameList

    def getTextName(self, nameId, langId):
        print('nameId', nameId, 'langId', langId)
        cmd = 'SELECT * FROM {} WHERE nameId = {} AND langId = {}'.format(tableList['texts'], nameId, langId)
        res = self.sqlHelper.execute(cmd)
        for row in res.fetchall():
            print('text', row)
            return row[3]


    def get(self):
        try:
            args = request.args
            projectId = args['projectId']
            langId = args['langId']

            pageList = self.getPageList(projectId)
            # print(pageList)
            resList = {}
            for page in pageList:
                pageName = page['name']
                nameList = self.getNameList(page['id'])
                print('pageName', pageName)
                textNames = {}
                for name in nameList:
                    print('name', name)
                    textNames[name['name']] = self.getTextName(nameId=name['id'], langId=langId)
                resList[pageName] = textNames

            resp = make_response(jsonify({'code': 200,'data': resList}))


        except Exception as e:
            print('err', e)
            resp = make_response(jsonify({'code': 500, 'data': {}}))

        return resp
