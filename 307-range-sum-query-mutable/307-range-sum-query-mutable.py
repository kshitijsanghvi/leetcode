class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        p = floor(log(n,2))
        lt = 0
        if 2**p == n:
            lt = n + n -1
        else:
            p = p + 1
            lt = 2**p + 2**p -1
    
        st = [0 for i in range(lt)]
        
        def create_tree(l,r,pos):
            nonlocal st
        
            if l == r:
                st[pos] = nums[l]
                return nums[l]
            else:
                mid = l + (r-l)//2
                l = create_tree(l,mid,2*pos + 1)
                r = create_tree(mid + 1,r,2*pos + 2)
                st[pos] = l + r
                return st[pos]
        create_tree(0,n-1,0)
        self.t = st    
        self.n = n        


    def update(self, index: int, val: int) -> None:
        d = val - self.nums[index]
        self.nums[index] = val
        st = self.t
        n = self.n
        
        def tree_update(l,r,pos,idx,d):
            nonlocal st
            nonlocal n

            if l <= idx <= r:
                st[pos]+=d
                if l == r:
                    return 
                else:
                    mid = l + (r-l)//2
                    tree_update(l,mid,2*pos+1,idx,d)
                    tree_update(mid+1,r,2*pos+2,idx,d)
            return 
            
        tree_update(0,n-1,0,index,d)

            
    def sumRange(self, left: int, right: int) -> int:
        
        ql = left
        qr = right
        st = self.t
        n = self.n
        
        def query(l,r,ql,qr,pos):
            nonlocal st
            nonlocal n
            if l == ql and r == qr:
                return st[pos]
            if r < ql or l > qr:
                return 0
            if ql <= l <= r <= qr:
                return st[pos]
            mid = l + (r-l)//2
            l = query(l,mid,ql,qr,2*pos+1)
            r = query(mid+1,r,ql,qr,2*pos+2)
            return l + r
        
        return query(0,n-1,ql,qr,0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)