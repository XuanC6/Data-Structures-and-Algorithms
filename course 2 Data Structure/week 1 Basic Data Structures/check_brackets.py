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
    result = False
    exist_non_match_close = False
    for i, next_ in enumerate(text):
        if next_ == '(' or next_ == '[' or next_ == '{':
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next_,i+1))

        if next_ == ')' or next_ == ']' or next_ == '}':
            # Process closing bracket
            if len(opening_brackets_stack)==0:
                result = False
                exist_non_match_close = True
                break
            else:
                last = opening_brackets_stack.pop()
                result = last.Match(next_)
                if not result:
                    exist_non_match_close = True
                    break
    # Printing answer
    if result and len(opening_brackets_stack)==0:
        print('Success')
    else:
        if exist_non_match_close:
            print(i+1)
        else:
            last = opening_brackets_stack.pop()
            print(last.position)