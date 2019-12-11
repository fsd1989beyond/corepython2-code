#!/usr/bin/env python

db = {}

def newuser():
    prompt = 'login desired: '
    while 1:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = input('passwd: ')
    db[name] = pwd

def olduser():
    name = input('login: ')
    pwd = input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        pass
    else:
        print('login incorrect')
        return

    print('welcome back', name)

def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """

    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)

            if choice not in 'neq':
                print('invalid menu option, try again')
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'n': newuser()
        if choice == 'e': olduser()

if __name__ == '__main__':
    showmenu()