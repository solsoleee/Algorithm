import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int memberNum = input.nextInt() + 1; // 회원 번호가 1번부터 시작하므로 memberNum 을 1개 늘려준다!
        boolean[][] memberRelations = new boolean[memberNum][memberNum];

        while (true) {
            int i = input.nextInt();
            int j = input.nextInt();

            if (i == -1 && j == -1) break;

            memberRelations[i][j] = true;
            memberRelations[j][i] = true;
        }

        solution(memberNum, memberRelations);
    }

    private static void solution(int memberNum, boolean[][] memberRelations) {
        int[] candidates = new int[memberNum]; // 후보를 저장할 배열
        int candidateCount = 0; // 후보 수
        int minScore = Integer.MAX_VALUE;

        // 각 멤버 점수 계산
        for (int i = 1; i < memberNum; i++) {
            int[] scores = new int[memberNum];
            Arrays.fill(scores, -1);
            int[] nextMembers = new int[memberNum];
            int queueSize = 0; // 큐의 크기를 관리
            nextMembers[queueSize++] = i;
            scores[i] = 0;

            for (int front = 0; front < queueSize; front++) {
                int member = nextMembers[front];

                for (int j = 1; j < memberNum; j++) {
                    if (memberRelations[member][j] && scores[j] < 0) {
                        nextMembers[queueSize++] = j;
                        scores[j] = scores[member] + 1;
                    }
                }
            }

            int score = Arrays.stream(scores).max().getAsInt();

            if (score > minScore) continue;

            if (score < minScore) {
                minScore = score;
                candidateCount = 0; // 후보 배열 초기화
            }

            candidates[candidateCount++] = i;
        }

        // 결과 출력
        System.out.println(minScore + " " + candidateCount);
        Arrays.sort(candidates, 0, candidateCount);
        for (int i = 0; i < candidateCount; i++) {
            System.out.print(candidates[i] + " ");
        }
    }
}