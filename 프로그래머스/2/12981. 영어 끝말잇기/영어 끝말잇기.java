import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        List<String> list = new ArrayList<>();
        list.add(words[0]);
        
        int len = words.length;
        char pre = words[0].charAt(words[0].length() - 1);
        
        for (int i = 1; i < len; i++) {
            String currentWord = words[i];
            
            // 중복 단어거나 규칙 위반일 경우
            if (list.contains(currentWord) || currentWord.charAt(0) != pre) {
                answer[0] = (i % n) + 1; // 사람 번호
                answer[1] = (i / n) + 1; // 차례
                break;
            }
            
            // 리스트에 단어 추가 및 다음 단어의 끝 글자 업데이트
            list.add(currentWord);
            pre = currentWord.charAt(currentWord.length() - 1);
        }
        
        return answer;
    }
}
