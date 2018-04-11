# python3

class Node(object):
    def __init__(self,key,next_node=None):
        self.key = key
        self.next_node = next_node
    
    def set_next_node(self,next_node):
        self.next_node = next_node


class Singly_Linked_List(object):
    def __init__(self,head=None,lengh = 0):
        self.head = head
        self.length = lengh
    
    def pushfront(self,key):
        new_first_node = Node(key)
        
        if self.length == 0:
            self.head = new_first_node
        else:
            _next = self.head
            self.head = new_first_node
            self.head.set_next_node(_next)
        self.length += 1
    
    def del_node(self,key):
        if self.length > 0:
            if self.head.key == key:
                next_node = self.head.next_node
                self.head = next_node
                self.length -= 1
            else:
                prev_node = self.head
                for i in range(self.length-1):
                    now_node = prev_node.next_node
                    if now_node.key == key:
                        next_node = now_node.next_node
                        prev_node.next_node = next_node
                        self.length -= 1
                        break
                    prev_node = now_node
            
    def check_key(self,key):
        now_node = self.head
        for i in range(self.length):
            if now_node.key == key:
                return True
            now_node = now_node.next_node
        return False
                    


class Query(object):
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor(object):
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [Singly_Linked_List() for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in s[::-1]:
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        str_arr = [None]*chain.length
        now_node = chain.head
        for i in range(chain.length):
            str_arr[i] = now_node.key
            now_node = now_node.next_node
                
        print(' '.join(str_arr))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        
        if query.type == "check":
            self.write_chain(self.elems[query.ind])

        else:
            hash_val = self._hash_func(query.s)
            if query.type == "add":
                if not self.elems[hash_val].check_key(query.s):
                    self.elems[hash_val].pushfront(query.s)
            if query.type == 'find':
                self.write_search_result(self.elems[hash_val].check_key(query.s))
            if query.type == 'del':
                self.elems[hash_val].del_node(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
