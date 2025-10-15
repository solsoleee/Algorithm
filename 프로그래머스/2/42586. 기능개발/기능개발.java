import java.util.*;
class Solution {
    public List solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        int len = progresses.length;
        int days[] = new int[len];
        for(int i=0; i<len; i++) {
            int p = progresses[i];
            int day = 0;
            int s = speeds[i];
            while(true) {
                p= p+ s;
                day++;
                if(p >= 100) break;
            }

            days[i] = day;
        }
        //System.out.println(Arrays.toString(days));
        int dev = 1;
        int maxDay = days[0];
        for(int i=1; i<len; i++) {
            if(maxDay >= days[i]) dev++;
            else {
                list.add(dev);
                maxDay = days[i];
                dev = 1;
            }
        }
        list.add(dev);
        //System.out.println(list);
        return list;
    }
}