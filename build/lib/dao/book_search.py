from dao.mysql_connector import get_cursor


class BookSearcher:

    @staticmethod
    def search_by_book_name(book_name=''):
        cursor = get_cursor()
        sql = 'SELECT book_name,book_author,download_link FROM book NATURAL JOIN download WHERE book_name = ' \
              + '\'' + book_name + '\''
        cursor.execute(query=sql)
        return cursor.fetchall()

    @staticmethod
    def search_by_author(author=''):
        cursor = get_cursor()
        sql = 'SELECT book_name,book_author,download_link FROM book NATURAL JOIN download WHERE book_author=' \
              + '\'' + author + '\''
        cursor.execute(query=sql)
        return cursor.fetchall()

    @staticmethod
    def search_by_type(book_type=''):
        cursor = get_cursor()
        sql = 'SELECT book_name,book_author,download_link FROM book NATURAL JOIN download WHERE book_type=' \
              + '\'' + book_type + '\''
        cursor.execute(query=sql)
        return cursor.fetchall()


# print(BookSearcher.search_by_type('武侠'))
