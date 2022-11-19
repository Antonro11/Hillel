import requests
import functools
import tracemalloc


def cache(limit=4):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            result = f(*args,**kwargs)
            
            if sum(cache.values()) < limit:
                if args not in cache.keys():
                    cache[args] = 1
                else:
                    cache[args] += 1
            else:
                for i in cache.keys():
                    if cache.get(i) == min(i for i in cache.values()):
                        delete = i                        
                cache.pop(delete)
                if args not in cache.keys():
                    cache[args] = 1
                else:
                    cache[args] += 1
            cache_copy =cache.copy()
            sorted_cache = dict()
            count =0
            while len(cache_copy)!=0:
                count+=1
                for i in cache_copy:
                    if cache_copy[i] == min(cache_copy.values()):
                        sorted_cache[i] = (cache_copy.get(i) * (str(result)+' ')),cache_copy.get(i)
                        delete = i
                cache_copy.pop(delete)
            print(sorted_cache)
            return result
        cache = dict()
        return deco
    return internal    

def memory_used(f):
    @functools.wraps(f)
    def deco(*args,**kwargs):
        tracemalloc.start()
        result  = f(*args,**kwargs)
        res = tracemalloc.get_traced_memory()
        tracemalloc.stop 
        print(result,': middle size: '+str(round(res[0]/1048576,2))+' MB, '+'max size: ' + str(round(res[1] /1048576,2)) + ' MB') 
        return result
    return deco
   

@memory_used
@cache(limit=5)
def fetch_url(url, first_n=10):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('http://ithillel.ua')
fetch_url('http://ithillel.ua')
fetch_url('http://youtube.com')
fetch_url('http://google.com')
fetch_url('http://youtube.com')
fetch_url('http://ithillel.ua')
