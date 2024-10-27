import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if(cacheSize == 0 ) return cities.length * 5;
                
        List<String> list = new ArrayList<>();
        int answer = 0;
        
        for(String c: cities) {
            c = c.toUpperCase();//대문자로 바꾸기
            if(!list.contains(c)) { //없는 경우
                
                if(list.size() >= cacheSize) { //꽉차있을 때
                   //최근에 사용하지 않은거 제일 앞에 있는거 제거
                    list.remove(0); //사용하지 않는 앞에거 제거
                }
                
                answer +=5;
                list.add(c);
            }
            
            else{ 
                //있는 경우, 제일 최근에 사용했다는 표시?..
                answer++;
                
                list.remove(c);
                
                list.add(c); //c를 제거하고 다시 넣기
                
            }
            //System.out.println(answer);
            //System.out.println(c);
            //System.out.println(list);
        }
        
        
        
        return answer;
    }
}