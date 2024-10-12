import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int answer = 0;
        int len = people.length;
        int start =0;
        int end = len-1;
        //System.out.println(Arrays.toString(people));
        
        while(len > 0) {
            if(people[start] + people[end] <= limit) {
                answer++;
                start +=1;
                end -=1;
                len = len-2;
            }
            else {
                end-=1; //큰사람 먼저 태움
                answer+=1;
                len = len-1;
            }
        }
        //System.out.println(Arrays.toString(people));
        return answer;
    }
}