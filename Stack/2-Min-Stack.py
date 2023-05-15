# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack():
# initialize the arrays used by all functions
    def __init__(self):
        self.stack = []
        # give a min value to each element in stack since we are only pushing and popping elements
        self.minStack = []

    def push(self, val: int) -> None:
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # if minStack is empty then it's just val, otherwise compare the min value with new value
        minValue = val if not self.minStack else min(val, self.minStack[-1])
        self.minStack.append(minValue)

    def pop(self) -> None:
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

# return most recently appended element at the top of stack
    def top(self) -> int:
        """
        :rtype: int
        """
        print (self.stack[-1])
        return self.stack[-1]

# return the minimum value correctlating to the top most element of stack
    def getMin(self) -> int:
        """
        :rtype: int
        """
        print(self.minStack[-1])
        return self.minStack[-1]

# Input:
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   # return -3
minStack.pop()
minStack.top()      # return 0
minStack.getMin()   # return -2

# Output:
# [null,null,null,null,-3,null,0,-2]