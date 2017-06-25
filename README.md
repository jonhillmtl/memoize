# Description

A Python decorator allowing a method or function's return value to be memoized.

# Installation

`pip install git+https://github.com/jonhillmtl/memoize`

# Usage

```
from memoize import memoized

class Tester(object):

    @memoize
    def func(self, x):
        return x
```

`func` is now memoized.

If you want to fine-tune the caching, you should provide a `hash` function on the class.

```

class Tester(object):
    l = []
    
    def __init__(self, l):
        self.l = l
        
    def hash(self):
        return [self.l]
```

The return value will be folded into the hash used in the memoization cache.