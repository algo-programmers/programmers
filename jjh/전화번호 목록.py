def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        now, nxt = phone_book[i], phone_book[i+1]
        if len(now) < len(nxt) and now == nxt[:len(now)]:
            return False
    return True