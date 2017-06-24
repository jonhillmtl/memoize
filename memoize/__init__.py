from functools import wraps

def memoize(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        if hasattr(self, '_memoize_cache') is False:
            self._memoize_cache = {}
            
        if(hasattr(self, 'hash')):
            args = (str(method_args),
                    str(method_kwargs),
                    method.__name__,
                    str(self.hash()))
        else:
            args = (str(method_args),
                    str(method_kwargs),
                    method.__name__)

        h = hash(args)
        if h in self._memoize_cache:
            return self._memoize_cache[h]

        return_value = method(self, *method_args, **method_kwargs)
        self._memoize_cache[h] = return_value
        return return_value
        
    return _impl