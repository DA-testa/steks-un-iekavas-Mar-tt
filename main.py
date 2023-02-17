# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
  

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]



def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.push(Bracket(next, i+1))
            

        if next in ")]}":
          number = ")]}".index(next)
          match number: 
            case 1:
            skobka = "("
            case 2:
            skobka = "["
            case 3:
            skobka = "{"
            if len(opening_brackets_stack)>0 and opening_brackets_stack.peek() == skobka:
                opening_brackets_stack.pop()
            else: return i+1
        if len(opening_brackets_stack)==0:
            return 0;
        else: return len(text)
        
          
          

def main():
    wait = input()
    if ("I" in wait)
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == 0:
            print("Success")
        else:
            print(mismatch)


if __name__ == "__main__":
    main()