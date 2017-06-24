from memoize import memoize

class MemoizedClass:
    def __init__(self, x):
        self.x = x
        
    @memoize
    def func(self, y):
        return self.x ** y
        
    def hash(self):
        return [self.x]

        
class MemoizedListClass:
    def __init__(self, xs):
        self.xs = xs
        
    @memoize
    def func(self, index):
        return self.xs[index]
    
    def func2(self, index):
        return self.xs[int((index / 2))]
        
    def hash(self):
        return [self.xs]


class NoHashClass:
    def func(self):
        return "no_hash_class"

    
def test_basic():
    tc = MemoizedClass(3)
    assert tc.func(4) == 81
    assert len(tc._memoize_cache) == 1
    
    assert tc.func(4) == 81
    assert tc.func(5) == 243
    assert len(tc._memoize_cache) == 2
    
    assert tc.func(4) == 81
    
    tc2 = MemoizedClass(2)
    assert tc2.func(4) == 16
    assert tc2.func(4) == 16
    assert tc2.func(5) == 32
    assert tc2.func(4) == 16
    

def test_complicated_hash():
    tc = MemoizedListClass([1, 2, 3, 4, 5, 6])
    assert tc.func(2) == 3
    assert tc.func(2) == 3

    assert tc.func2(2) == 2
    assert tc.func2(2) == 2
    

def test_no_hash():
    tc = NoHashClass()
    assert tc.func() == "no_hash_class"
    assert tc.func() == "no_hash_class"
    
    