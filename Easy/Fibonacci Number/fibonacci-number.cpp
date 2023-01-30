class Solution {
public:
    int fib(int n) {
        
        double sq5 = sqrt(5);
        double phi = (1 + sq5) / 2;

        return round(pow(phi, n) / sq5);
    }
};
