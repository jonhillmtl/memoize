from functools import wraps

def memoize(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        if hasattr(self, '_memoize_cache') is False:
            self._memoize_cache = {}
            
        if(hasattr(self, 'hash')):
            args = (str(self.hash()),
                    method.__name__,
                    str(method_args),
                    str(method_kwargs))
        else:
            args = (method.__name__,
                    str(method_args),
                    str(method_kwargs))

        h = hash(args)
        if h not in self._memoize_cache:
            self._memoize_cache[h] = method(self, *method_args, **method_kwargs)
            
        return self._memoize_cache[h]
        
    return _impl