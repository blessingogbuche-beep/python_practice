def balanced_brackets(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False

    return len(stack) == 0
    
    

print(balanced_brackets("(hello)"))      
print(balanced_brackets("{[()]}"))       
print(balanced_brackets("([)]"))         
print(balanced_brackets("((hello)")) 

