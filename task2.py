from collections import deque

d = deque()

while True:
    d.clear()
    word = input('Enter your word: ')
    word = word.replace(' ', '').lower()
    print(word)
    for letter in word:
        d.append(letter)

    while len(d) > 1:
        left = d.popleft()
        right = d.pop()
        if left != right:
            print(left)
            print(right)
            print('Не поліндром')
            break

    if len(d) <= 1:
        print('Поліндром')