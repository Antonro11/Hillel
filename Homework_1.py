import requests
import functools
import tracemalloc


def cache(limit=5):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            result = f(*args, **kwargs)
            key = (args, tuple(kwargs.items()))               
            if len(cache_result) < limit:
                if key not in cache:
                    cache[key] = 1  
                    cache_result[key] = result                                   
                else:
                    cache[key] +=1
            else:
                if key not in cache:
                    sorted_cache = sorted(cache.items(),key= lambda x:x[1])
                    cache.pop(sorted_cache[0][0])
                    cache_result.pop(sorted_cache[0][0])
                    cache[key] = 1
                    cache_result[key] = result 
                else:
                    cache[key] +=1
                
            print(cache_result)
            return result
        cache = dict()
        cache_result = dict() 
        return deco
    return internal    

def memory_used(f):
    @functools.wraps(f)
    def deco(*args,**kwargs):
        tracemalloc.start()
        result  = f(*args,**kwargs)
        res = tracemalloc.get_traced_memory()
        tracemalloc.stop 
        print('Request',args,'takes lower size: '+str(round(res[0]/1048576,2))+' MB, '+'max size: ' + str(round(res[1] /1048576,2)) + ' MB') 
        return result
    return deco
   

@memory_used
@cache(limit=3)
def fetch_url(url, first_n=20):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content



fetch_url('http://ithillel.ua')
fetch_url('http://ithillel.ua')
fetch_url('http://youtube.com')
fetch_url('http://youtube.com')
fetch_url('http://ithillel.ua')
fetch_url('http://google.com')
fetch_url('http://google.com')
fetch_url('http://comfy.ua')
fetch_url('http://youtube.com')
