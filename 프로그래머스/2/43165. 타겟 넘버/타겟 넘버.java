import java.util.*;

class Solution {
    static boolean visited[];
    static int n;
    static int arr[];
    static int answer;
    public int solution(int[] numbers, int target) {
        n = numbers.length;
        visited = new boolean[n];
        //선택한거 -, 선택 안한거 +
        arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = i+1;
        }
          
        subSet(0,numbers,target);
        
        return answer;
    }
    static void subSet(int cnt, int[] numbers, int target) {
        if(cnt == n) {
            int c = cal(numbers);
            if(c == target) answer++;
            return;
        }
        visited[cnt] = true;
        subSet(cnt+1, numbers, target);
        visited[cnt] = false;
        subSet(cnt+1, numbers, target);
    }
    static int cal(int[] numbers) { //선택된 것만 -을 해서 합을 계산
        int sum =0;
        for(int i=0; i<n; i++) {
            if(visited[i]) sum = sum -(numbers[i]);
            else sum = sum + numbers[i];
        }
        return sum;
    }
}