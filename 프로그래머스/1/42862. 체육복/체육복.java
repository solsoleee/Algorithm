import java.util.*;
import java.io.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        int answer = n-(lost.length); //도단당해서 남은 학생수
        
        //도둑 맞으면서 체육복 가져왔으면 제외
        for(int i=0; i<lost.length; i++) {
            for(int j=0; j<reserve.length; j++) {
                if(lost[i] == reserve[j]) {
                    answer++;
                    lost[i] = -1;
                    reserve[j] =-1;
                    break;
                }
            }
        }
        
        

        for(int i=0; i<lost.length; i++) {
            for(int j=0; j<reserve.length; j++) {
                if( lost[i] -1 == reserve[j] || lost[i] +1 == reserve[j]) {
                    answer++;
                    reserve[j] =-1;
                    break;
                }
            }
        }
        
        return answer;
    }
}