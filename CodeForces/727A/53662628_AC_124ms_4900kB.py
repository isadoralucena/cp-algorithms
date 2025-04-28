inicio, fim = map(int, input().split())

visited = []
flag = False

def dfs(atual, final):
    global flag
    if atual > final: return
    if atual == final:
        visited.append(atual)
        flag = True
        return
    
    if flag: return

    dfs(2 * atual, final)
    dfs(int(f"{atual}1"), final)
    
    if flag:
        visited.append(atual)
    
dfs(inicio, fim)
visited.reverse()
if len(visited) != 0:
    print("YES")
    print(len(visited))
    print(f"{' '.join(map(str, visited))}")
else:
    print("NO")