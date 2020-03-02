def createstack():
	stack = []
	return stack
def isempty(stack):
	return len(stack) == 0
def push(stack,x):
	stack.append(x)
def pop(stack):
	if isempty(stack):
		print("stack is empty")
	else:
		return stack.pop()
def printNGE(arr): 
    s = createstack() 
    element = 0
    next = 0
  
    # push the first element to stack 
    push(s, arr[0]) 
  
    # iterate for rest of the elements 
    for i in range(1, len(arr), 1): 
        next = arr[i] 
  
        if isempty(s) == False: 
  
            # if stack is not empty, then pop an element from stack 
            element = pop(s) 
            print(element)
  
            '''If the popped element is smaller than next, then 
                a) print the pair 
                b) keep popping while elements are smaller and 
                   stack is not empty '''
            while element < next : 
                print(str(element)+ " -- " + str(next))
                if isempty(s) == True : 
                    break
                element = pop(s) 
               
  
            '''If element is greater than next, then push 
               the element back '''
            if  element > next: 
                push(s, element) 
  
        '''push next to stack so that we can find 
           next greater for it '''
        push(s, next) 
  
    '''After iterating over the loop, the remaining 
       elements in stack do not have the next greater 
       element, so print -1 for them '''
  
    while isempty(s) == False: 
            element = pop(s) 
            next = -1
            print(str(element) + " -- " + str(next)) 
  
# Driver program to test above functions 
arr = [11, 3, 21, 6,7] 
printNGE(arr) 
  