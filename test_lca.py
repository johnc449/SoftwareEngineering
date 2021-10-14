import LCA
def test_One():
    root = LCA.Node(1)
    root.left = LCA.Node(2)
    root.right = LCA.Node(3)
    root.left.left = LCA.Node(4)
    root.left.right = LCA.Node(5)
    root.left.right.left = LCA.Node(6)
    root.left.right.right = LCA.Node(7)
    assert LCA.findLCA(root, 4, 5) == 2
    assert LCA.findLCA(root, 4, 6) == 2
    assert LCA.findLCA(root, 3, 4) == 1
    assert LCA.findLCA(root, 2, 4) == 2
    assert LCA.findLCA(root, 7, 6) == 5

def test_Two():
    root = LCA.Node(1)
    root.right = LCA.Node(2)
    root.right.right = LCA.Node(3)
    root.right.right.right = LCA.Node(4)
    root.right.right.right.right = LCA.Node(5)
    assert LCA.findLCA(root, 4, 5) == 4
    assert LCA.findLCA(root, 2, 4) == 2
    assert LCA.findLCA(root, 5, 5) == 5
    assert LCA.findLCA(root, 5, 4) == 4
