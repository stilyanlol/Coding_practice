books = input().split('&')

while True:

    commands = input()

    if 'Add Book' in commands:
        
        command, book_name = commands.split(' | ')
        
        if book_name not in books:

            books.insert(0, book_name)

        else:
            continue

    if 'Take Book' in commands:

        command, book_name = commands.split(' | ')

        if book_name in books:

            books.remove(book_name)

        else:
            continue

    if 'Swap Books' in commands:

        command, book_name, book_2 = commands.split(' | ')

        item_1 = book_name
        item_2 = book_2

        index_item_1 = books.index(item_1)
        index_item_2 = books.index(item_2)

        if book_name in books and book_2 in books:

            books[index_item_1], books[index_item_2] = books[index_item_2], books[index_item_1]
        
        else:
            continue

    if 'Insert Book' in commands:

        command, book_name = commands.split(' | ')

        if book_name not in books:

            books.append(book_name)

        else:
            continue

    if 'Check Book' in commands:
        
        command, book_name = commands.split(' | ')

        index = int(book_name)

        if 0 <= index < len(books):
        
            check_book = books.index[index]

            print(check_book)

    organised_books = ', '.join(books)

    if 'Done' in commands:
        print(f'{organised_books}')
        break