  
3.[数组中重复的数字](#1)  
4.[二维数组中的查找](#2)  
5.[替换空格](#3)  
6.[从尾到头打印链表](#4)  
7.[重建二叉树](#5)  
8.[二叉树的下一个结点](#6)  
9.[用两个栈实现队列](#7)  
10.1[斐波那契数列](#8)  
10.2[矩形覆盖](#9)  
10.3[跳台阶](#10)  
10.4[变态跳台阶](#11)  
  
  
  
<A name="1"> 数组中重复的数字 </A>   

在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的，也不知道每个数字重复几次。请找出数组中任意一个重复的数字。

```
Input:
{2, 3, 1, 0, 2, 5}

Output:
2
```
解法

<A name="2"> 二维数组中的查找 </A>   
题目描述
给定一个二维数组，其每一行从左到右递增排序，从上到下也是递增排序。给定一个数，判断这个数是否在该二维数组中。

Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.


结题思路
```

该二维数组中的一个数，小于它的数一定在其左边，大于它的数一定在其下边。
因此，从右上角开始查找，就可以根据 target 和当前元素的大小关系来缩小查找区间
，当前元素的查找区间为左下角的所有元素。

标准解答
public boolean Find(int target, int[][] matrix) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
        return false;
    int rows = matrix.length, cols = matrix[0].length;
    int r = 0, c = cols - 1; // 从右上角开始
    while (r <= rows - 1 && c >= 0) {
        if (target == matrix[r][c])
            return true;
        else if (target > matrix[r][c])
            r++;
        else
            c--;
    }
    return false;
}
```
需要学习的地方就是  matrix.length表示行  matrix[0].length表示数组的列

```
public class Find {
    public static void main(String[] args) {


    int[][] a= new int[][]{
            {1, 4, 7, 11, 15},
            {2, 5, 8, 12, 19},
            {3, 6, 9, 16, 22},
            {10, 13, 14, 17, 24},
            {19, 21, 23, 26, 30}
    };
    Boolean i=find(a,5,5);
    System.out.println(i);
}
    public static boolean find(int a[][],int m,int n)
    {
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        int p=1;
        int q=0;
        for (int j = 0; j <m+n-1 ; j++) {
            if(i>a[q][m-p])
            {
                if (q>=m-1) return false; else q++; } if(i<a[q][m-p]) {
                if(p>=n-1)
                    return false;
                else
                    p++;

            }
            if(i==a[q][m-p])
            {return true;}
        }
        return false;
    }
}
```


<A name="3"> 替换空格 </A>   

替换空格

将一个字符串中的空格替换成 "%20"。

Input:
"A B"

Output:
"A%20B"

1.  在字符串尾部填充任意字符，使得字符串的长度等于替换之后的长度。因为一个空格要替换成三个字符（%20），所以当遍历到一个空格时，需要在尾部填充两个任意字符。

2. 令 P1 指向字符串原来的末尾位置，P2 指向字符串现在的末尾位置。P1 和 P2 从后向前遍历，当 P1 遍历到一个空格时，就需要令 P2 指向的位置依次填充 02%（注意是逆序的），否则就填充上 P1 指向字符的值。从后向前遍是为了在改变 P2 所指向的内容时，不会影响到 P1 遍历原来字符串的内容。

3. 当 P2 遇到 P1 时（P2 <= P1），或者遍历结束（P1 < 0），退出。

![](<++>) <++>

```
public class paix {
	public static void main(String[] args) {
		StringBuffer sb= new StringBuffer("a 1 i o u");
		String st=fangfa(sb);
		System.out.println(st+"");
		System.out.println(fangfa(sb));
	}
	public static String fangfa(StringBuffer Sb)
	{
		int j;
		int i=0;
		char [] c =Sb.toString().toCharArray();
		for(char a: c)
			if (a == ' ')
				i++;
		//Sb.append(2*i);
		char [] b= new char[Sb.length()+2*i];
		for (int d=c.length-1;d>=0;d--)
		{
			if(c[d]==' ') {
				j=2*i-1;
				b[d + j] = '2';
				b[d + j-1] = '1';
				b[d + j+1] = '3';
				i=i-1;
			}
			else
			{
				b[d+i+i]=c[d];
			}
		}
		System.out.println(b);
		return b.toString();

	}


}
```
要学习的地方就是 这个i的处理 老是出问题 然后就是
System.out.print(str)显示的居然是 str的地址值  我炸  
System.out.print(str+"")就可以显示具体值了
```
public String replaceSpace(StringBuffer str) {
    int P1 = str.length() - 1;
    for (int i = 0; i <= P1; i++)
        if (str.charAt(i) == ' ')
            str.append("  ");

    int P2 = str.length() - 1;
    while (P1 >= 0 && P2 > P1) {
        char c = str.charAt(P1--);
        if (c == ' ') {
            str.setCharAt(P2--, '0');
            str.setCharAt(P2--, '2');
            str.setCharAt(P2--, '%');
        } else {
            str.setCharAt(P2--, c);
        }
    }
    return str.toString();
}
```
这里仅仅使用了一个StringBuffer就解决了问题 值得学习学习
是通过P1 P2 来进行位置的调换   实在是好方法啊

<A name="4"> 从尾到头打印链表 </A>   

典型的对栈使用的考察

使用头插法也可以解决这个问题 

使用递归
```

import java.util.ArrayList;
import java.util.Stack;

/**
 * 剑指offer面试题5：从尾到头打印链表
 * 输入一个链表的头结点，从尾到头打印出每个结点的值
 * 解决方案一：首先遍历链表的节点后打印，典型的“后进先出”，可以使用栈来实现这种顺序。
 * 解决方案二：栈的本质就是递归，直接使用递归的方式，打印一个节点的时候先打印它后面的节点，再打印该节点自身，实现反向打印
 * 解决方案三：遍历链表，把链表中的元素复制到ArrayList中，然后逆序打印ArrayList中的元素
 * 解决方案四：前三种解决方案本身属于在打印链表的时候不修改链表本身结构，
 * 在允许修改链表结构的情况下可以把链表中的节点指针反转过来，改变链表方向，然后重新遍历打印改变方向后的链表
 * @author GL
 *
 */
public class link {

    public static void main(String[] args) {
        ListNode node1=new ListNode(1);
        ListNode node2=new ListNode(2);
        ListNode node3=new ListNode(3);
        ListNode node4=new ListNode(4);
        ListNode node5=null;
        ListNode node6=new ListNode(6);
        ListNode node7=new ListNode();
        node1.next=node2;
        node2.next=node3;
        node3.next=node4;


        printListFromTailToHead(node1);
        printList(node1);//这个是我修改的只是会显示的代码
        ArrayList<Integer>  fin= new ArrayList<Integer>();
        fin = printListFromTailTo(node1);//这个是一个会返回一个数组的代码
        System.out.println(fin);


       // printListFromTailToHead(node5);
       // printListFromTailToHead(node6);
       // printListFromTailToHead(node7);
       // //使用栈实现逆序打印链表
     printListFromTailToHeadByStack(node1);
       // //使用递归实现逆序打印链表
       // printListFromTailToHead(node1);
      //使用递归反转实现逆序打印
     printListFromTailToHeadByReverseList(node1);
      //使用ArrayList逆序打印链表
     printListFromTailToHeadByArrayList(node1);
    }

    /*
     * 方案一：通过使用栈结构，遍历链表，把先遍历的节点的值推入栈中，遍历结束后通过弹出栈内元素实现逆序打印
     */
    public static void printListFromTailToHeadByStack(ListNode node){
        Stack<Integer> stack=new Stack<Integer>();
        while(node!=null){
            stack.push(node.val);
            node=node.next;
        }
        while(!stack.isEmpty()){
            System.out.print(stack.pop()+",");
        }
    }


    /*
     * 方案二：递归法逆序打印链表
     */
    public static ArrayList<Integer> printListFromTailTo(ListNode listNode) {
        ArrayList<Integer> ret = new ArrayList<>();
        if (listNode != null) {
            ret.addAll(printListFromTailTo(listNode.next));
            ret.add(listNode.val);
        }
        return ret;
    }
    public static void printListFromTailToHead(ListNode node){
        if(node!=null){
            if(node.next!=null){
                printListFromTailToHead(node.next);
            }
            System.out.print(node.val+",");
        }
        else
            System.out.println("输入的链表为空");
    } 
    public static void printList(ListNode listNode) {
        ArrayList<Integer> ret = new ArrayList<>();
        if (listNode != null) {
            printList(listNode.next);
            //ret.add(listNode.val);
            System.out.println(listNode.val);
        }
    }
    /*
     * 方案三：使用ArrayList逆序打印链表
     */
    public static void    printListFromTailToHeadByArrayList(ListNode node){
        if(node==null)
            System.out.print("输入链表为null");
        ArrayList<Integer> arrayList=new ArrayList<Integer>();
        while(node!=null){
            arrayList.add(node.val);
            node=node.next;
        }
        for(int i=arrayList.size()-1;i>=0;i--){
            System.out.print(arrayList.get(i)+",");
        }
    }


    /*
     * 方案四：递归反转链表，后遍历打印
     */
    public static void printListFromTailToHeadByReverseList(ListNode node){
        ListNode reversedNode=reverse(node);
        while(reversedNode!=null){
            System.out.print(reversedNode.val+",");
            reversedNode=reversedNode.next;
        }

    }
    //递归反转
    private static ListNode reverse(ListNode head){
        if(head.next==null)
            return head;
        ListNode reversedListNode=reverse(head.next);
        head.next.next=head;
        head.next=null;
        return reversedListNode;
    }

}
class ListNode{
    int val;
    ListNode next=null;
    public ListNode(){

    }
    public ListNode(int value){
        this.val=value;
    }
}
```


<A name="5"> 重建二叉树 </A>   

<A name="6"> 二叉树的下一个结点 </A> 

<A name="7"> 用两个栈实现队列 </A>


	class test {
	Stack in = new Stack();
	Stack out = new Stack();
	public void push(int code)
	{
		in.push(node);
	}
	public int pop() throws Exception
	{
		if(out.isEmpty())
			while(!in.isEmpty())
				out.push(in.pop());
		if(out.isEmpty())
			throw new Exception("queue is empty")
		return out.pop();
	}
}*
 * 重点在于思路在于我们有两个栈我们分别编号栈1和栈2 
 * 当外面的队列使用push时候我们就直接用栈1push就可以了 并不是你每次 外面的队列push后我们里面的栈1都要立刻吧数据放到栈2去这个是不对的  
 * 当我们要pop的时候  我们要首先把自己的栈2中的数据先倒完之后 我们再去 把栈1的数据给重新放到占中

<A name="8"> 斐波那契数列 </A>   

一个典型的迭代问题哈

public static int test3(int n) {
	if (n == 1 || n == 0) {
		return 1;
	}else {
		return test3(n-1) + test3(n-2);
	}
}

简单的循环解决
```
public int Fibonacci(int n) {
	int l = 1, j = 1, k = 1;
	for (int i = 3; i <= n; i++) {
		k = l + j;
		l = j;
		j = k;
	}
	return n == 0 ? 0 : k;
}
```




<A name="9"> 矩形覆盖 </A>   

当 n 为 1 时，只有一种覆盖方法：
当 n 为 2 时，有两种覆盖方法：
要覆盖 2*n 的大矩形，可以先覆盖 2*1 的矩形，再覆盖 2*(n-1) 的矩形；或者先覆盖 2*2 的矩形，再覆盖 2*(n-2) 的矩形。而覆盖 2*(n-1) 和 2*(n-2) 的矩形可以看成子问题。该问题的递推公式如下：
当n<=0时，f(n)=0;
当n<=2时，f(n)=n;
当n>2时，f(n)=f(n-1)+f(n-2);
其实就变成了具体版斐波那契数列了
```
public int RectCover(int n) {
    if (n <= 2)
        return n;
    int pre2 = 1, pre1 = 2;
    int result = 0;
    for (int i = 3; i <= n; i++) {
        result = pre2 + pre1;
        pre2 = pre1;
        pre1 = result;
    }
    return result;
}
```

<++>
<A name="10"> 跳台阶 </A>   

  一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
 其实和上面的一题是同样的效果   
跳 n 阶台阶，可以先跳 1 阶台阶，再跳 n-1 阶台阶；或者先跳 2 阶台阶，再跳 n-2 阶台阶。而 n-1 和 n-2 阶台阶的跳法可以看成子问题，该问题的递推公式为：
当n<=2时，f(n)=n;
当n>2时，f(n)=f(n-1)+f(n-2);
一样的 

<A name="11"> 变态跳台阶 </A>   

一样的思路这个也是一个递归解决的问题
因为现在青蛙有n-1中跳法  所以 f(n)=f(n-1)+f(n-2)+ *** +f(1)+1 
 //方法二、递归方法
    public static int JumpFloorIIj(int target) {   
        if(target==0||target==1)
            return 1;
        if(target==2)
            return 2;
        int sum = 0;
        for(int i=0;i<target;i++){
            sum += JumpFloorIIj(i);
        }
        return sum;
    }
     
    //方法三、动态规划方法    自底向上
    public static int JumpFloorr(int target){
    	if(target==0){   //如果为0层台阶时，返回0
    		return 0;
    	}
    	 int a[] = new int[target+2];   //加2的原因是下面的a数组要初始化到第三个元素
    	 int b=3;
    	 a[0]=1;
    	 a[1]=1;
    	 a[2]=2;
    	if(target<b&&target>0){
    		return a[target];
    	}
    	for(int i=3;i<=target;i++){
    		a[i]=2*a[i-1];
    	}
    	return a[target];
    }
    
}

动态规划的办法有必要好好说一下 首先我们对比  递归的缺点在哪里呢   
 
1 重复计算  在f(4)和f*(3)的时候我们都要计算f(2) 所以f(2)就会被重复计算 那么我们为什么不找一个a[n] 把之前的数据存储起来呢  

2 没有运用规律 只做了一层的总结  
如这里面我们就 发现了 a[i] = 2a[i-1]
这个规律:
