class Solution {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;
        int start = 0, end = 0;
        int sum = 0;
        int[] answer = {-1, -1}; // 결과를 저장할 배열
        int minLength = Integer.MAX_VALUE; // 최소 길이를 추적할 변수

        while (end < n) {
            // end 포인터의 요소를 sum에 추가
            sum += sequence[end];
            
            // sum이 k보다 크다면 start 포인터를 옮기면서 sum을 감소시킴
            while (sum > k && start <= end) {
                sum -= sequence[start];
                start++;
            }
            
            // 합이 정확히 k가 되는 경우, 최소 구간을 갱신
            if (sum == k) {
                int length = end - start;
                if (length < minLength || (length == minLength && start < answer[0])) {
                    minLength = length;
                    answer[0] = start;
                    answer[1] = end;
                }
            }
            
            // end 포인터 증가
            end++;
        }

        return answer;
    }
}
