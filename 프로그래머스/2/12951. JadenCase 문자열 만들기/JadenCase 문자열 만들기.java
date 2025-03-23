import java.util.*;
import java.io.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        boolean flag = true;
        for(char c: s.toCharArray()) {
            if(flag) {
                answer.append(Character.toUpperCase(c));
            }
            else {
                answer.append(Character.toLowerCase(c));
            }
            flag = (c==' ');
        }
        return answer.toString();
    }
}