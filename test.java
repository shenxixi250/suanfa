import java.util.*;
public class test
{
   public static void main(String[] args)
	{
	    Fangfa fangfa = new Fangfa();
		System.out.println("输入 n 和 每个数字");
		Scanner sc = new Scanner(System.in);
		int n= sc.nextInt();
		int [] a=new int[n];
		for(int i=0;i<n;i++)
		    a[i]=sc.nextInt();
		int jieguo=fangfa.ff(a,a.length);
		System.out.println(jieguo);

	}


}
