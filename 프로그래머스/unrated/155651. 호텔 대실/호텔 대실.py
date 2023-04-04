from heapq import heappush, heappop, heapify

def solution(book_time):
    answer = 0
    heap = []
    for book in book_time:
        book[0] = int(book[0][:2]) * 60 + int(book[0][3:])
        book[1] = int(book[1][:2]) * 60 + int(book[1][3:])
        heappush(heap, (book[0], 1))
        heappush(heap, (book[1] + 10, 0))
    now = 0
    for _ in range(len(heap)):
        t, n = heappop(heap)
        if n == 1:
            now += 1
        elif n == 0:
            now -= 1
        answer = max(answer, now)
    return answer