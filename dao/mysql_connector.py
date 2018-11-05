import pymysql

db = pymysql.connect(host='58.87.111.121', user='root', password='123456', database='wxbook', port=3301)


def get_cursor():
    return db.cursor()