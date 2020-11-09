from argparse import ArgumentParser
from library_api import LibraryAPI

parser = ArgumentParser()
parser.add_argument(
    'command',
    choices=['list', 'add', 'set-title', 'del'])
parser.add_argument('params', nargs='*')  # 可选参数
args = parser.parse_args()

srv, port, db = 'localhost', 8069, 'dev13'
user, pwd = 'admin', 'admin'
api = LibraryAPI(srv, port, db, user, pwd)

if args.command == 'list':
    text = args.params[0] if args.params else None
    books = api.search_read(text)
    for book in books:
        print('%(id)d %(name)s' % book)

if args.command == 'add':
    for title in args.params:
        new_id = api.create(title)
        print('Book added with ID %d.' % new_id)
