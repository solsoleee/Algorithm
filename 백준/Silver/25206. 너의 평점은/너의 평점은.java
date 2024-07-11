import java.util.*;





public class Main {
	
	public static double change(String grade) {
	    if (grade.equals("A+")) {
	        return 4.5;
	    } else if (grade.equals("A0")) {
	        return 4.0;
	    } else if (grade.equals("B+")) {
	        return 3.5;
	    } else if (grade.equals("B0")) {
	        return 3.0;
	    } else if (grade.equals("C+")) {
	        return 2.5;
	    } else if (grade.equals("C0")) {
	        return 2.0;
	    } else if (grade.equals("D+")) {
	        return 1.5;
	    } else if (grade.equals("D0")) {
	        return 1.0;
	    } else if (grade.equals("F")) {
	        return 0.0;
	    } else {
	        throw new IllegalArgumentException("Invalid grade: " + grade);
	    }
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner sc =new Scanner(System.in);
        double total=0;
        double num=0;
        for(int i=0; i<20; i++) {
        	String input[] = sc.nextLine().split(" ");
        	String sub = input[0];
        	double score = Double.parseDouble(input[1]);
        	if (input[2].equals("P")) num+=0;
        	else {
        		double grade = change(input[2]);
        		total+=(score * grade);
        		num+=score;
        	}
        }
        System.out.printf("%.6f",total/num);
        sc.close();
		
		
	}

}