import java.util.*;
class Solution {
    public String[] solution(String[] record) {

        String[] answer={};
        List<String> list = new ArrayList<>();
        Map<String, String> map = new HashMap<>();
        String s[][] = new String[record.length][3];
        for(int i=0; i<record.length; i++) {
            s[i] = record[i].split(" ");

            if(s[i][0].equals("Enter")) {
                map.put(s[i][1], s[i][2]);
            }
            else if (s[i][0].equals("Change")) {
                map.put(s[i][1], s[i][2]);
            }
        }

        for(String r[]: s) {
            
            if(r[0].equals("Enter")) {
                list.add(map.get(r[1]) +"님이 들어왔습니다.");
                
            }
            else if(r[0].equals("Leave")) {
                list.add(map.get(r[1]) +"님이 나갔습니다.");
            }
            else continue;
            
        }
        //System.out.println(list);
        answer = list.toArray(new String[0]);
        return answer;
    }
}