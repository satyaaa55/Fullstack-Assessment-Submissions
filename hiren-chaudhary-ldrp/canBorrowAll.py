def canBorrowAll(copies, borrows):
    events = []

    for start, end in borrows:
        events.append((start, 1))   # borrow book
        events.append((end, -1))    # return book

    # Sort events by time, return events processed first if same time
    events.sort(key=lambda x: (x[0], x[1]))

    current = 0

    for time, change in events:
        current += change
        if current > copies:
            return False

    return True

copies = 2
borrows = [[1,4], [2,5], [6,8]]

print(canBorrowAll(copies, borrows))