# Using recursion thereby storing elements in the function stack alone

def insertatBottom(stack,item):
    if isEmpty(stack):
        push(stack,item)
    else:
        temp = pop(stack)
 	insertatBottom(stack,item)
	push(stack,temp)

def reverse(stack):
    if not isEmpty(stack):
	temp = pop(stack)
	reverse(stack)
	insertatBottom(stack,temp)
    else:
	return

def prints(stack):
    for i in range(len(stack)-1, -1, -1):
	print stack[i]
 
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
	print 'Stack empty'
        exit(1)
    return stack.pop()

if __name__ == '__main__':
    stack = createStack()
    push(stack, str(84))
    push(stack, str(37))
    push(stack, str(42))
    push(stack, str(15))
    print 'Original Stack:'
    prints(stack)
    reverse(stack)
    print 'Reversed Stack'
    prints(stack)
