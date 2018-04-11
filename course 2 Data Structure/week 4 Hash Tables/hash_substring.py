# python3

_x = 263
_p = 1000000007

def read_input():
    return (input().rstrip(), input().rstrip())

def _hash_func(s):
    global _x,_p
    ans = 0
    for c in s[::-1]:
        ans = (ans * _x + ord(c)) % _p
    return ans

def hash_table(text,m):
    global _x,_p
    n = len(text)
    h_table = [None]*(n-m+1)
    h_table[n-m] = _hash_func(text[n-m:n])
    y = (_x**m)%_p
    for i in range(n-m):
        j = n-m-i
        h_table[j-1] = (h_table[j]*_x+ord(text[j-1])-ord(text[j-1+m])*y)%_p
    return h_table

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    results = []
    pHash = _hash_func(pattern)
    n = len(text)
    m = len(pattern)
    text_hash_table = hash_table(text,m)
    for i in range(n-m+1):
        if text_hash_table[i] == pHash:
            if text[i:i+m] == pattern:
                results.append(i)
    return results

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

