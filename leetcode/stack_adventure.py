def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (check_empty(stack)):
        return "Stack Empty"
    return stack.pop()

if __name__=="__main__":

    stack = create_stack()  
    print("Enter values in the stack: ")
    i = 0
    n = int(input("Number of items: "))
    while(i<n):
        push(stack, str(input("Enter a Value to stack: ")))
        print("stack after pushed: " + str(stack))
        i += 1
    while True:
        userpreference = input("Enter 0 for pushing a new value \n 1 for Popping an item \n 2 for See the list or either 3 to break: ")
        if userpreference == '1':
            print("Your popped item is: " + pop(stack))
            print("stack after popped: " + str(stack))
        elif userpreference == '2':
            print("Current stack: " + str(stack))
        elif userpreference == '3':
            break
        else:
            print("Invalid")
    
