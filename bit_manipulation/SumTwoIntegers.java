
// Given two integers a and b, return the sum of the two integers without using the operators + and -.
// Example 1:
// Input: a = 1, b = 2
// Output: 3

class Solution{
    public int getSum(int a, int b){
        while (b != 0){
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}

class Main {
    public static void main(String[] args) {
        Solution f = new Solution();
        int a = 1;
        int b = 2;
        System.out.println(f.getSum(a,b));
    }
}

