# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    match = True
    unMatchIndex = -1
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            #print('push {0}'.format(next) )

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0:
                match = False
                unMatchIndex = i
                break
            
            top = opening_brackets_stack.pop()
            #print('pop {0}'.format(top.bracket_type) )
            if top.Match(next) == False:
                match = False
                unMatchIndex = i
                break

    if match == True and len(opening_brackets_stack) > 0:
        top = opening_brackets_stack.pop()
        match = False
        unMatchIndex = top.position
        
    # Printing answer, write your code here
    if match==True:
        print("Success")
    else:
        print(unMatchIndex+1)
