
from sql.databases import PymysqlClass


def create_db(host, user, port, password, database):
    db = PymysqlClass(host=host, user=user, password=password, database=database,
                      port=port)
    db.connect()
    cursor = db.get_cursor()
    print('连接到数据库')
    return db, cursor
