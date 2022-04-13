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

data = current.left
current.left = current.right 
current.right = data
    if node == None:
        return
        
    preorder(node.left)
    preorder(node.right)
    print(node.data, end=' ')