import string
class endecrypt:
        global charlist
        otherchars = "0123456789áéíöüóőúű:"
        charlist = list(f"{string.ascii_lowercase}{string.ascii_uppercase}{otherchars}")
        print(charlist)
        def en(wte):
                wte = list(wte)
                out = ""
                for char in wte:
                    out = out + " " + f"{charlist.index(char)}"
                out = out[1:]
                print(out)
                return out
        def de(wtd):
                wtd = wtd.split(" ")
                print(wtd)
                out = ""
                for num in wtd:
                    num = int(num)
                    out = out + charlist[num]
                print(out)
                return out
def signin(ux, px):
        usr = ux
        password = px
        user = list()
        fhand = open('database.sys' , 'r')
        for line in fhand:
                print(line)
                line = endecrypt.de(line)
                user = line.split(':')
                if usr == user[1]:
                        exist = 1
                        break
        fhand.close()
        if usr == user[0]:
                if password == user[1]:
                        print(f'You are Logged In As {user[0]}, Welcome !')
                        quit()
                else: print('Wrong Username or Password!')
        else: print('Wrong Username or Password!')
def signup(ux, px):
        usr = ux#input('Username: ')
        password = px#input('Password: ')
        with open('database.sys', 'a') as database:
                data = endecrypt.en(f'{usr}:{password}')
                print(data)
                database.write(f"\n{data}")
                database.close()

