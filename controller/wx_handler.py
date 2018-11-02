import werobot
from dao.book_search import BookSearcher

robot = werobot.WeRoBot(token='ynlbq')


@robot.text
def search_book(message):
    book_name = message.content
    book_set = BookSearcher.search_by_book_name(book_name)
    return book_set[0] + '\n' + book_set[1] + '\n' + book_set[2]


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
