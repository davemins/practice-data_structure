class Stack:
    def __init__(self):
        self.size = 10
        self.stack = [ None for _ in range(self.size) ]
        self.top = -1

    def is_stack_full(self):
        # 코드 작성 구간
        if (self.top >= self.size - 1):
            return True
        else:
            return False

    def is_stack_empty(self):
        # 코드 작성 구간
        if (self.top == -1):
            return True
        else:
            return False


    def push(self, data):
        # 코드 작성 구간
        if self.is_stack_full():
            return
        self.top += 1
        self.stack[self.top] = data


    def pop(self):
        # 코드 작성 구간
        if self.is_stack_empty():
            return None
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data
        
    def peek(self):
        # 코드 작성 구간
        if self.is_stack_empty():
            return None
        return self.stack[self.top]

    def validate_stack_sequences(self, pushed, popped):
        # 코드 작성 구간
        data4 = popped.index(pushed[4])
        data3 = popped.index(pushed[3])
        data2 = popped.index(pushed[2])
        data1 = popped.index(pushed[1])
        data0 = popped.index(pushed[0])

        list


        return True



# 실행 구문 (아래 코드를 수정하지 마시오.)
test_stack = Stack()
pushed = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
popped = [[3, 4, 5, 2, 1], [4, 5, 2, 3, 1]]
for i in range(len(pushed)):
    print(test_stack.validate_stack_sequences(pushed[i], popped[i]))
