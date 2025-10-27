import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int [2];
        
        int sum = brown + yellow; //전체 넓이
        for(int i=3; i<=sum; i++) {
            if(sum % i == 0) { //나눠지면
                int row = sum/i; //가로
                int col = i; //세로 
                //노란색 넓이
                if(row >= col) {
                    if( (row-2) * (col-2) == yellow) {
                        answer[0] = row;
                        answer[1] = col;
                    }

                }
            }
        }
        
        return answer;
    }
}