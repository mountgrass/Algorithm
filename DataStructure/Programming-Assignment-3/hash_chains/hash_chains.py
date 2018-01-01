# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)+self._prime) % self._prime
        return (ans+self.bucket_count) % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems)
            #            if self._hash_func(cur) == query.ind)
            if query.ind in self.elems:
                self.write_chain( cur for cur in reversed(self.elems[query.ind]) )
            else:
                print('  ')
        else:
            hash_val = self._hash_func(query.s)
            if query.type == 'find':
                if hash_val in self.elems:
                    count = self.elems[hash_val].count(query.s)
                    self.write_search_result(count>0)
                else:
                    self.write_search_result(False)

            elif query.type == 'add':
                if hash_val in self.elems:
                    count = self.elems[hash_val].count(query.s)
                    if count == 0:
                        self.elems[hash_val].append(query.s)
                else:
                    self.elems[hash_val] = []
                    self.elems[hash_val].append(query.s)
                
            else: #del
                if hash_val in self.elems:
                    count = self.elems[hash_val].count(query.s)
                    if count == 0:
                        return
                    ind = self.elems[hash_val].index(query.s)
                    if ind != -1:
                        self.elems[hash_val].pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
