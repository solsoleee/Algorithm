import java.util.Stack;

class Solution {
    public String solution(String p) {
        return dfs(p);
    }

    private String dfs(String p){
        //균형잡힌 문자열로 분리
        if(p.isEmpty()){
            return "";
        }
        String u_str="", v_str="";
        int index = divide(p);

        u_str = p.substring(0, index+1);
        v_str = p.substring(index+1);

        if(check(u_str)) { //u_str가 올바른 문자열이라면
            return u_str + dfs(v_str); //u_str은 이미 올바르니까 v_str만 제대로 정렬
        }

        else{
            String new_u_str = "(" + dfs(v_str) + ")";

            u_str = u_str.substring(1, u_str.length()-1); //u의 첫번째와 마지막 문자 제거

            //문자 뒤집기
            for(int i=0; i<u_str.length(); i++){
                new_u_str += (u_str.charAt(i) == '(') ? ')' : '(';
            }
            return new_u_str;
        }
    }

    //균형잡힌 문자열로 분리
    private int divide(String p){
        int left=0, right=0;
        for(int i=0; i<p.length(); i++){
            if (p.charAt(i)=='('){
                left++;
            }
            else{
                right++;
            }
            if(left!=0 && right!=0 && left==right) {
                return i;
            }
        }
        return 0;
    }

    private boolean check(String p){ //올바른 문자열인지 확인하는 함수
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<p.length(); i++){
            if (p.charAt(i)=='('){
                stack.push('(');
            }
            else {
                if(stack.isEmpty()){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
