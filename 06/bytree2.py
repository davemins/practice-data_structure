# 과제 2. 주어진 이진 탐색 트리에서 트리 순회를 변형하여 내림차순 배열을 출력하라.
# 출력 예시
# 임의의 숫자 배열: [3, 3, 0, 2, 4, 3, 3, 2, 3, 2]
# 내림차순 배열: [4, 3, 2, 0]

class TreeNode:
    def __init__ (self):
        self.left = None
        self.data = None
        self.right = None


def generate_tree(sellAry):
    # 코드 작성 구간: 판매 물품 트리 생성
    node = TreeNode()
    node.data = sellAry[0]
    root = node

    for name in sellAry[1:]:
        node = TreeNode()
        node.data = name

        current = root
        while True:
            if name == current.data:
                break
            elif name < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right
    return root


def traverse_node(root, result):
    # 코드 작성 구간: 이진 탐색 트리에서 작은 값부터 큰 값 순으로 순회 (트리 순회 이용하기)
    # 힌트: 중위 순회 활용
    if root == None:
        return

    traverse_node(root.right, result)
    result.append(root.data)
    traverse_node(root.left, result)

    return result


# 실행 구문 (아래 코드를 수정하지 마시오.)
import random
random.seed(0)  # 결과 재현을 위한 seed 통일
node_array = list(random.randint(0, 5) for _ in range(10) )  # 임의의 숫자 배열
result = []
print(f'임의의 숫자 배열: {node_array}')
rootNode = generate_tree(node_array)  # Tree 최상위 노드 (중복 X)
print(f'내림차순 배열: {traverse_node(rootNode, result)}')