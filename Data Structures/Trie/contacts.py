#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

class TrieNode:
    
    def __init__(self, char):
        self.char = char
        self.counter = 1
        self.children = {}
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
                node.counter += 1
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
                
    def search(self, word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        
        return node.counter
    

def contacts(queries):
    trie = Trie()
    results = []
    
    for query in queries:
        if query[0] == "add":
            trie.insert(query[1])
        else:
            results.append(trie.search(query[1]))
    
    return results
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
