# 과제 1. 스택함수를 이용하여 pushed 리스트에 대해서 popped 리스트 출력결과가 발생할 수 있는지 확인하라.
# (1) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [3, 4, 5, 2, 1]
# (1) 출력 예시: True
# (1) 설명: 다음의 순서대로 push, pop 수행할 수 있으므로 True 출력
# push(1), push(2), push(3), pop() -> 3, push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 2, pop() -> 1
# (2) 입력 예시
# pushed = [1, 2, 3, 4, 5], popped = [4, 5, 2, 3, 1]
# (2) 출력 예시: False
# (2) 설명: 2 은 3 이전에 pop 할 수 없음

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
        list = []

        list.append(pushed.index(popped[0]))
        list.append(pushed.index(popped[1]))
        list.append(pushed.index(popped[2]))
        list.append(pushed.index(popped[3]))
        list.append(pushed.index(popped[4]))

        test = list

        k = popped.index(pushed[4])
        test[k] = 'none'

        for i in range(k, 4):
                test[i] = test[i + 1]
                
        del(test[4]) 
        
        if (test == [0, 3, 1, 2] or test == [1, 3, 0, 2] or test == [2, 0, 1, 3] or test == [2, 0, 3, 1] or test == [2, 3, 0, 1] or test == [3, 0, 1, 2] or test == [3, 0, 2, 1] or test == [3, 1, 0, 2]  or test == [3, 1, 2, 0] or test == [3, 2, 0, 1]): # 배열 길이가 4개일 때 불가능한 경우
                return False
        else:
            if (k == 0):		
                if test == [3, 2, 1, 0]:
                    return True
                else:
                    return False
            if (k == 1):
                if (test == [3, 2, 1, 0] or test == [0, 3, 2, 1] or test == [1, 3, 2, 0] or test == [2, 3, 1, 0]):
                    return True
                else:
                    return False
            if (k == 2):
                if (test == [0, 3, 2, 1] or test == [2, 3, 1, 0] or test == [1, 3, 2, 0]  or test == [0, 1, 3, 2] or test == [0, 2, 3, 1] or test == [1, 2, 3, 0]):
                    return True
                else:
                    return False
            if (k == 3):
                return True
            if (k == 4):
                return True
            else:
                pass

# 실행 구문 (아래 코드를 수정하지 마시오.)
test_stack = Stack()
pushed = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
popped = [[3, 4, 5, 2, 1], [4, 5, 2, 3, 1]]
for i in range(len(pushed)):
    print(test_stack.validate_stack_sequences(pushed[i], popped[i]))