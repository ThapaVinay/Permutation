import java.util.Scanner;
public class permutation{
    static int time =0,co =0;
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i =0;i <n ;i++)
        {
            arr[i] = sc.nextInt();
        }
        int size = n;
        int c[] = new int[fact(n)];
        c[0] = join(arr,size);
        co++;
        System.out.println(permute(c,arr,n-1,size,co));
        print(c,co);
        
    }


    static int permute(int c[] , int a[] , int n, int size, int co)
    {

        if(n>=0){
            int f[] = new int[size];
            for(int i=0; i<n;i++)   // the loop will only run for (n-1) times
            {
                permute(c, a, n-1,size,co);  // it will generate 4 outcomes in [1,2,3]
                time ++; 
                swap(a,n);
                int d = join(a,size);
                check(c,d,co);
                for(int k =0;k < size ;k++)   // we need to copy the array value to another array 
                {
                    f[k] = a[k];
                }
            }
            permute(c,f,n-1,size,co);  // to generate the remaining combinations 
        }
        return time;
    }

    // to swap the numbers 
    static void swap(int b[], int s)
    {
        int temp = b[s];
        b[s] = b[s-1];
        b[s-1] = temp;
    }

    // to join the numbers 
    static int join(int b[], int s)
    {
        int temp =1;
        int x=0;
        for(int i=0; i<s;i++)
        {
             x = x + temp*b[i];
             temp = temp *10;
        }
        return x;
    }


    // to print the array
    static void print(int b[], int s)
    {
        for(int i=0; i<s; i++)
        {
            System.out.print(b[i] + " ");
        }
        System.out.println();
    }
    

    // to check if the number already exists
    static void check(int b[], int x , int size)
    {
        int i=0,count =0;
        for(i=0; i<co ;i++)
        {
            if(b[i] == x)
            {
                count = 1;
                break;
            }
        }
        if(count ==0)
        {
            
            b[co] = x;
            co++;
        }
    }

    static int fact(int n)
    {
        int sum =1;
        for(int i =1;i<=n;i++)
        {
            sum = sum *i;
        }
        return sum;

    }
}