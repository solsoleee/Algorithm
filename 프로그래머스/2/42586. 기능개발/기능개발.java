import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = new int[100];
        for(int i=0; i<100; i++) {
            answer[i] = 0;
        }
        int time=1;
        int cnt=0;
        for(int i=0; i<progresses.length; i++) {
            if(progresses[i] + speeds[i] * time >= 100) {
                answer[cnt]++;
            }
            else {
                //System.out.println(cnt);
                if(i!=0) cnt++; 
               while(progresses[i]<100) {
                if(progresses[i] + speeds[i] * time >= 100) {
                    answer[cnt]++;
                    
                    break;
                }
                else time ++;
            } 
            }
            //System.out.println(Arrays.toString(answer));
        }
        int res[] = new int[cnt+1];
        for(int j=0; j<cnt+1; j++) {
            //System.out.println(answer[j]);
            res[j] = answer[j];
        }
        return res;
    }
}