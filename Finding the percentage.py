if __name__ == '__main__':
    Sum = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    
    for key, values in student_marks.items() :
        if key == query_name:
            average = sum(values)/ len(values)
            
            
            
            
            
       
    print(f"{average:.2f}")    