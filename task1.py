from queue import Queue

q = Queue()

print(q)
def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args

def generate_request():
    id = input('Enter your id: ')
    q.put(id)
    print('You have been added to the queue')

def process_request():
    if q.empty():
        print('Queue is empty')
        return

    next = q.get()
    print('Next is ', next)

while True:
#     put / get / close / show
    user_input = input('What I need to do? ')
    command, *args = parse_input(user_input)

    if command == 'close':
        break

    if command == 'put':
        generate_request()

    if command == 'get':
        process_request()

    if command == 'show':
        temp = []
        while not q.empty():
            item = q.get()
            print(item, ' ')
            temp.append(item)

        for item in temp:
            q.put(item)