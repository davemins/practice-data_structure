# 과제 1. 편의점 판매 물품 종류 트리를 좌우 반전시키고 후위 순회하라.
# 출력 예시
# 오늘 판매된 종류(중복X) 트리 전위 순회 -->  바나나맛우유 레쓰비캔커피 도시락 츄파춥스 삼다수  
# 오늘 판매된 종류(중복X) 반전 트리 후위 순회 -->  삼다수 츄파춥스 도시락 레쓰비캔커피 바나나맛우유 

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

def preorder(node):
    # 코드 작성 구간: 전위 순회 구현
    if node == None:
        return

    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    # 코드 작성 구간: 후위 순회 구현
    if node == None:
        return
        
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')
    

def invertTree(root):
    # 코드 작성 구간: 트리 노드들의 위치를 좌우 반전
    # 힌트: 트리의 마지막 leaf 노드부터 반전시키면서 root방향으로 올라가기 (후위 순회)
    if root == None:
        return
    
    invertTree(root.left)    
    invertTree(root.right)

    root.left, root.right = root.right, root.left

    return root

# 실행 구문 (아래 코드를 수정하지 마시오.)
dataAry = ['바나나맛우유', '츄파춥스', '삼다수', '레쓰비캔커피', '도시락']  # 판매 물품 종류
rootNode = generate_tree(dataAry)  # Tree 최상위 노드
print('오늘 판매된 종류(중복X) 트리 전위 순회 --> ', end = ' ')
preorder(rootNode)
print('\n오늘 판매된 종류(중복X) 반전 트리 후위 순회 --> ', end = ' ')
postorder(invertTree(rootNode))