import java.util.*;
import java.io.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        // A 정렬, B 정렬
        Arrays.sort(A);
        Arrays.sort(B);
        // 큰 수 비교
        int lenA = A.length;
        int lenB = B.length;
        int minA =0;
        int minB =0;
        for(int i=0; i<A.length; i++) {
            if(A[lenA-1] > B[lenB-1]) {
                answer += A[lenA-1] * B[minB];
                lenA--;
                minB++;
            }
            else {
                // a가 작은거, B가 큰거
                answer += A[minA] * B[lenB-1];
                lenB--;
                minA++;
            }
        }

        return answer;
    }
}