
from flask import Flask, make_response, request, jsonify
from flask_restful import Api
from apis.projects import Projects, Project
from apis.pages import Pages
from apis.langs import Langs, Lang
from apis.names import Names
from apis.texts import Texts
from apis.operation import PageTexts, LangTexts
from sqllite_helper import SqlLiteHelper

app = Flask(__name__)
api = Api(app)
api.add_resource(Projects,'/projects')
api.add_resource(Project,'/project/<id>')
api.add_resource(Pages, '/pages')
api.add_resource(Langs, '/langs')
api.add_resource(Names, '/names')
api.add_resource(Texts, '/texts')
api.add_resource(PageTexts, '/pageText')
api.add_resource(LangTexts, '/langTexts')





def main():
  sqlHelper = SqlLiteHelper()
  # cmd = '''CREATE TABLE test2 (
  #   ID INTEGER PRIMARY KEY AUTOINCREMENT,
  #   NAME TEXT NOT NULL
  # )'''

  # projectsTab = '''CREATE TABLE Projects (
  #     ID INTEGER PRIMARY KEY AUTOINCREMENT,
  #     NAME TEXT NOT NULL
  #   )'''

  pagesTab = '''CREATE TABLE PAGES (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProjectID INTEGER NOT NULL,
    NAME TEXT NOT NULL
  )'''

  langTab = '''CREATE TABLE LANG (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    LANG TEXT NOT NULL
  )'''

  namesTab = '''CREATE TABLE NAMES (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PageID INTEGER NOT NULL,
    NAME TEXT NOT NULL
  )'''


  textTab = '''CREATE TABLE TEXTS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NameID INTEGER NOT NULL,
    LangID INTEGER NOT NULL,
    TEXT TEXT NOT NULL
  )'''

  # cmd2 = '''INSERT INTO test2(NAME) VALUES ('xxx'
  #     )'''
  # sqlHelper.execute(projectsTab)
  # sqlHelper.execute(pagesTab)
  # sqlHelper.execute(langTab)
  # sqlHelper.execute(textTab)

  # sqlHelper.execute(cmd2)
  # sqlHelper.commit()
  # sqlHelper.test()

  app.run(host='0.0.0.0')

if __name__ == "__main__":
  main()