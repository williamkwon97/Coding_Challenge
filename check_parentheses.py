def createStack():
    stack = []
    return stack


def isEmpty(stack):

    return len(stack) == 0


def push(stack, x):
    return stack.append(x)


def pop(stack):
    if isEmpty(stack):
        return print("empty stack")
    else:
        return stack.pop()


def printPar(arr):
    next = []
    element = []
    s = createStack()
    arr.sort()
    print(arr)

    push(s, arr[0])

    for i in range(1, len(arr), 1):
        next = arr[i]

        if isEmpty(s) == False:

            element = pop(s)

            while element == "(" and next == ")":
                print(str(element) + str(next))
                if isEmpty(s) == True:
                    break
                element = pop(s)

        if element == "(" and next == "(" or element == ")" and next == ")":
            push(s, element)
        push(s, next)


arr = ["(", "(", ")", ")", "(", ")", ")", ")", "("]
printPar(arr)
