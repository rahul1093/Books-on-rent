def book():
    try:
        book_dictionary = {'regular': 1.5, 'fiction': 3, 'novel': 1.5}
        book_dictionary2 = {'regular': 2, 'fiction': 3, 'novel': 4.5}
        version = input("enter version:")
        book_type = input("enter book type:")
        rented_days = int(input("enter number of days:"))
        if version == "old":
            print("total charge Rs:", rented_days * book_dictionary.get(book_type, 1.0))
        else:
            if (rented_days > 2 and book_dictionary['regular']) or (rented_days > 3 and book_dictionary['novel']):
                print("total new charge Rs:", rented_days * book_dictionary.get(book_type))
            elif (rented_days <= 2 and book_dictionary2['regular']) or (rented_days < 3 and book_dictionary2['novel']):
                print("total new charge Rs:", book_dictionary2.get(book_type))

    except (ValueError, TypeError):
        print("please provide prepare value..! ")


book()
