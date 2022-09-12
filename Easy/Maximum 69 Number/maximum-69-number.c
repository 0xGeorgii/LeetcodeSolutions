int maximum69Number (int num)
{
    int res = 0;
    int changed = 0;
    
    for(int i = log10(num); i >= 0; i--)
    {
        int p = (int)pow(10, i);
        int n = (num / p) % 10;        
        if (changed == 0 && n == 6)
        {
            res += 9 * p;
            changed = 1;
        }
        else
        {
            res += n * p;
        }
    }
    
    return res;
}
