visited = {}
def fibonacci(n):
    if n < 1:
        return "Wrong input!"

    if n in visited:
        return visited[n]

    if n == 1:
        return 0

    if n == 2:
        return 1
    
    visited[n] = fibonacci(n-1) + fibonacci(n-2)
    return visited[n]

for i in range(100):
    print(fibonacci(i), end=" ")