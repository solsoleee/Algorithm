T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    results = []
    N, k = map(int, input().split())
    for i in range(N):
        mid, final, hw = map(int, input().split())
        # 성적 계산
        score = mid * 0.35 + final * 0.45 + hw * 0.20
        results.append(score)
    
    # 점수로 내림차순 정렬
    sorted_scores = sorted(results, reverse=True)
    
    # 각 등급별 학생 수
    students_per_grade = N // 10
    
    # 성적에 등급 할당
    final_grades = {}
    for index, score in enumerate(sorted_scores):
        grade = grades[index // students_per_grade]
        final_grades[score] = grade
    
    # k번째 학생의 성적 조회
    k_score = results[k-1]
    k_grade = final_grades[k_score]
    
    print(f'#{t} {k_grade}')
