import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        int n = citations.length;
        int start=0;
        int end=0;
        for(int i=0; i<n; i++) {
            start = Math.min(start, citations[i]);
            end = Math.max(end, citations[i]);
        }
        int cnt;
        for(int h=start; h<=end; h++) {
            //h번 이상 인용된 논문이 h편 이상
            cnt =0;
            for(int i=0; i<n; i++) {
                if(citations[i] >= h) {
                    cnt++;
                }
            }
            if(cnt >=h) answer=h;
        }
        return answer;
    }
}