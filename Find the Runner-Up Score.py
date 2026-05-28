if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

#remove duplicates    
arr = list(set(arr))   
arr.sort()              # sort list
print(arr[-2])