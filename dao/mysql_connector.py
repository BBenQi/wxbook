import pymysql

db = pymysql.connect(host='39.105.162.147', user='root', password='123456', database='wxbook', port=3301)


def get_cursor():
    return db.cursor()