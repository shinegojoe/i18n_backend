import sqlite3

class SqlLiteHelper:
  def __init__(self):
    print('init')
    self.dbName = 'i18n.db'
    self.connect()
    # self.conn = sqlite3.connect(dbName)
    # self.cursor = self.conn.cursor()
    print('conn', self.conn)

  def connect(self):
    try:
      self.conn = sqlite3.connect(self.dbName)
      self.cursor = self.conn.cursor()
    except:
      raise Exception
  
  def execute(self, cmd):
    return self.cursor.execute(cmd)
    
  def commit(self):
    self.conn.commit()
    self.conn.close()

  def test(self):
    self.connect()
    res = self.cursor.execute('SELECT * FROM test2')
    for row in res.fetchall():
      print('row', row)
    # for row in self.cursor.execute('SELECT * FROM test2')
    #   print('row', row)
    self.conn.close()
