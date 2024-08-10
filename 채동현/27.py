import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = [sys.stdin.readline().strip() for _ in range(n)]
def get_num_set(cards, k, selected, result):
    if len(selected) == k:
        number = int(''.join(map(str, selected)))
        result.add(number)
        return

    for i in range(len(cards)):
        get_num_set(cards[:i] + cards[i+1:], k, selected + [cards[i]], result)
    return result

def get_len(cards, k):
    return len(get_num_set(cards, k, [], set()))

print(get_len(cards, k))