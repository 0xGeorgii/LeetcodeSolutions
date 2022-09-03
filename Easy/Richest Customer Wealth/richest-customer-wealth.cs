public class Solution {
    public int MaximumWealth(int[][] accounts)
    {
        var max = 0;
        
        for (var i = 0; i < accounts.Length; i++)
        {
            var n = accounts[i].Sum();
            if (n > max)
            {
                max = n;
            }
        }
        
        return max;
    }
}
