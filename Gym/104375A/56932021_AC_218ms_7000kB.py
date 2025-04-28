n = int(input())
alias_dict  = {}

while n >= 1:
    n -= 1
    line = input().split()
    line.pop(0)
    alias = ''.join(word[0] for word in line)  
    alias_dict[alias] = alias_dict.get(alias, 0) + 1  

count = sum(1 for value in alias_dict.values() if value == 1)

print(count)