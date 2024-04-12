def check_valid(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥인 경우
            # 바닥 위이거나 보의 한쪽 끝 부분 위이거나 다른 기둥 위인 경우
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        elif a == 1:  # 보인 경우
            # 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는 경우
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치하는 경우
            answer.append([x, y, a])
            if not check_valid(answer):
                answer.remove([x, y, a])
        else:  # 삭제하는 경우
            answer.remove([x, y, a])
            if not check_valid(answer):
                answer.append([x, y, a])
    answer.sort()
    return answer
