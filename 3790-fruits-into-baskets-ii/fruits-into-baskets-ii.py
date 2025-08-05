class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self.build(data, 2*node+1, l, mid)
            self.build(data, 2*node+2, mid+1, r)
            self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, index, value, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.tree[node] = value
        else:
            mid = (l + r) // 2
            if index <= mid:
                self.update(index, value, 2*node+1, l, mid)
            else:
                self.update(index, value, 2*node+2, mid+1, r)
            self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def query(self, value, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if self.tree[node] < value:
            return -1
        # Leaf: this basket fits
        if l == r:
            return l
        mid = (l + r) // 2
        left = self.query(value, 2*node+1, l, mid)
        if left != -1:
            return left
        return self.query(value, 2*node+2, mid+1, r)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)
        unplaced = 0
        for fruit in fruits:
            idx = st.query(fruit)
            if idx == -1:
                unplaced += 1
            else:
                st.update(idx, -1)
        return unplaced
        