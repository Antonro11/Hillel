import requests
import functools
import tracemalloc


def to_cache(limit_cache=5,cache = []):
    def inner(f):
        @functools.wraps(f)
        def deco(*args,**kwargs):
                for_check = []
                if len(cache)<limit_cache:
                    cache.append(f(*args,**kwargs))
                    cache.sort() 
                else:
                    for_check = [cache.count(i) for i in cache]
                    cache.pop(for_check.index(min(for_check)))
                    cache.sort() 
                    cache.append(f(*args,**kwargs))
                return cache                
        return deco
    return inner    

def memory_used():
    def inner(f):
        def deco(*args,**kwargs):
            tracemalloc.start()
            f(*args,**kwargs)
            res = tracemalloc.get_traced_memory()
            tracemalloc.stop 
            return 'current size: '+str(round(res[0] * (9.537*(10**-7)),2))+' megabytes'+'\n'+'peak size: ' + str(round(res[1] * (9.537*(10**-7)),2)) + ' megabytes'
        return deco
    return inner

@memory_used()
@to_cache(limit_cache=4)
def fetch_url(url, first_n=10):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content
