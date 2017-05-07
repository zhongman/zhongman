t=["subjects", ["sciences", ["biology", "chemistry"]], ["philosophy"], ["languages", ["Chineses", "English"]]]
print(t)
def tree(label,branches=[]):
    return[label]+list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
print(label(t))
print(branches(t))
t=tree("subjects", [tree("sciences", [tree("biology"), tree("chemistry")]), tree("philosophy"), tree("languages", [tree("Chineses"), tree("English")])])
print(t)
def is_leaf(t):
    if not branches(t):
        print("t is a leaf.")
    else:
        print("t is not a leaf.")
is_leaf(t)
print(tree(subtree))
