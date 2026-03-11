def canBorrowAllBooks(copies, borrows):
    intervals = []
    
    # convert flat list to intervals
    for i in range(0, len(borrows), 2):
        intervals.append((borrows[i], borrows[i+1]))
    
    events = []
    
    for start, end in intervals:
        events.append((start, 1))   # borrow
        events.append((end, -1))    # return
    
    # sort events
    events.sort(key=lambda x: (x[0], x[1]))
    
    current = 0
    
    for time, change in events:
        current += change
        if current > copies:
            return 0
    
    return 1


copies = 1
borrows = [0,2,3,5,1,4]

print(canBorrowAllBooks(copies, borrows))