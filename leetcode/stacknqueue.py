class stacknqueue:
    def check(self, listitem):
        if len(listitem) == 0:
            print('There is no item, so you can input the values again \n')
            listinput()

    def stack(self, listitem):
        print("Starting with stack: " + str(listitem))
        while True:
            if len(listitem) != 0:
                val = input("Enter a Value or \n To Exit enter x \n or To pop an item enter pop \n") 
                if val in 'xX':
                    break
                elif val == 'pop' and len(listitem) > 0 :
                    popitem = listitem.pop()
                    print(f'poped item is {popitem} \n and the list is {listitem}')
                else:
                    listitem.append(val)
                    print(f'The itemlist after push is {listitem}')
            else:
                self.check(listitem)


    def queue(self, listitem):
        print("\n Starting with queue: " + str(listitem))
        while True:
            if len(listitem) != 0:
                val = input("Enter a Value or \n To Exit enter x \n or To pop an item enter pop \n")

                if val in 'xX':
                    break
                elif val == 'pop':
                    popitem = listitem.pop(0)
                    print(f'poped item is {popitem} \n and the list is {listitem}')
                else:
                    listitem.append(val)
                    print(f'The itemlist after push is {listitem}')
            else:
                self.check(listitem)

def listinput():
    listitem = []
    n = int(input('How many values: '))
    i = 0 
    while n > i:
        listitem.append(input(f"Enter Value {i+1}: "))
        i += 1
    print(listitem)

    val = input("Which you gonna use? \n A: Stack \n B: Queue \n")
    sq = stacknqueue()
    if val in 'aA':
        sq.stack(listitem)
        #how call stack funtion here?
    elif val in 'bB':
        sq.queue(listitem)
        #how call queue funtion here?
    else:
        print('type error :( ')

if __name__=="__main__":
    print('Welcome to mini project ')
    listinput()
    