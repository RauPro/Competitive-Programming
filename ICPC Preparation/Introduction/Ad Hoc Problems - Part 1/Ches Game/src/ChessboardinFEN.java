import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class ChessboardinFEN {
    static char [][]map;
    static int r;
    static int dy[]={2,2,-2,-2,-1,1,-1,1};
    static int dx[]={-1,1,-1,1,2,2,-2,-2};
    static int dy2[]={1,1,-1,-1,1,-1,0,0};
    static int dx2[]={1,-1,-1,1,0,0,1,-1};
    public static boolean check(int i,int j)
    {
        if(i<r&&j<8&&i>=0&&j>=0)
            return true;
        else
            return false;
    }
    private static void fillr(int i, int j)
    {
        for(int x=i+1;x<r;x++)
        {

            if(map[x][j]=='.'||map[x][j]=='x')
            {
                map[x][j]='x';
            }
            else
                break;
        }

        for(int x=i-1;x>=0;x--)
        {
            if(map[x][j]=='.'||map[x][j]=='x')
            {
                map[x][j]='x';
            }
            else
                break;
        }

        for(int y=j+1;y<8;y++)
        {
            if(map[i][y]=='.'||map[i][y]=='x')
            {
                map[i][y]='x';
            }
            else
                break;
        }

        for(int y=j-1;y>=0;y--)
        {
            if(map[i][y]=='.'||map[i][y]=='x')
            {
                map[i][y]='x';
            }
            else
                break;
        }
    }
    public static void fillb(int i,int j)
    {
        int y,x;
        for(y=i-1,x=j+1;check(y,x);y--,x++)
        {
            if(map[y][x]=='.'||map[y][x]=='x')
            {
                map[y][x]='x';
            }
            else
                break;
        }

        for(y=i-1,x=j-1;check(y,x);y--,x--)
        {
            if(map[y][x]=='.'||map[y][x]=='x')
            {
                map[y][x]='x';
            }
            else
                break;
        }

        for(y=i+1,x=j+1;check(y,x);y++,x++)
        {
            if(map[y][x]=='.'||map[y][x]=='x')
            {
                map[y][x]='x';
            }
            else
                break;
        }

        for(y=i+1,x=j-1;check(y,x);y++,x--)
        {
            if(map[y][x]=='.'||map[y][x]=='x')
            {
                map[y][x]='x';
            }
            else
                break;
        }
    }

    public static void filln(int i,int j)
    {
        for(int k=0;k<8;k++)
        {
            int nr=i+dy[k];
            int nc=j+dx[k];
            if(check(nr,nc))
            {
                if(map[nr][nc]=='.')
                    map[nr][nc]='x';

            }
        }
    }

    public static void fillk(int i,int j)
    {
        for(int k=0;k<8;k++)
        {
            int nr=i+dy2[k];
            int nc=j+dx2[k];
            if(check(nr,nc))
            {
                if(map[nr][nc]=='.')
                    map[nr][nc]='x';

            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            int count=0;
            String st = sc.next();
            String s[]=st.split("/");
            map=new char[s.length][8];
            r=s.length;
            for (int i = 0; i < s.length; i++)
            {
                int col=0;
                for(int j=0;j<s[i].length();j++)
                {
                    char c=s[i].charAt(j);
                    int f=(int )(c-'0');

                    if(f>0&&f<9)
                    {
                        for(int k=0;k<f&&col<8;k++)
                        {
                            map[i][col++]='.';
                        }
                    }
                    else if(col<8)
                        map[i][col++]=c;

                }
            }

            for(int i=0;i<r;i++)
            {
                for(int j=0;j<8;j++)
                {
                    char c=map[i][j];
                    if(c=='r'||c=='R')
                    {
                        fillr(i,j);
                    }
                    else if(c=='b'||c=='B')
                    {
                        fillb(i,j);
                    }
                    else if(c=='q'||c=='Q')
                    {
                        fillr(i,j);
                        fillb(i,j);
                    }
                    else if(c=='n'||c=='N')
                    {
                        filln(i,j);
                    }
                    else if(c=='k'||c=='K')
                    {
                        fillk(i,j);
                    }
                    else if(c=='p')
                    {
                        int y1=i+1;
                        int x1=j-1;
                        if(check(y1,x1)&&map[y1][x1]=='.')
                        {
                            map[y1][x1]='x';
                        }
                        y1=i+1;
                        x1=j+1;
                        if(check(y1,x1)&&map[y1][x1]=='.')
                        {
                            map[y1][x1]='x';
                        }
                    }
                    else if(c=='P')
                    {
                        int y1=i-1;
                        int x1=j+1;
                        if(check(y1,x1)&&map[y1][x1]=='.')
                        {
                            map[y1][x1]='x';
                        }
                        y1=i-1;
                        x1=j-1;
                        if(check(y1,x1)&&map[y1][x1]=='.')
                        {
                            map[y1][x1]='x';
                        }
                    }

                }
            }
            for(int i=0;i<8;i++)
                for(int j=0;j<8;j++)
                    if(map[i][j]=='.')
                        count++;
            System.out.println(count);
        }
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
