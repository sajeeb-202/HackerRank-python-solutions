if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Get unique scores and find second lowest
    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1]

    # Get names with second lowest score
    names = [name for name, score in students if score == second_lowest]

    # Print names alphabetically
    for name in sorted(names):
        print(name)