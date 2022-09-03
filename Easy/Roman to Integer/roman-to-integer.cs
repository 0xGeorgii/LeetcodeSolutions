public class Solution {
    public int RomanToInt(string s) {
        var res = 0;        
        for(var i  = 0; i < s.Length; i++) {
            var symbol = s[i];
            var symbolValue = SymbolToInt(symbol);
                        
            if(i + 1 == s.Length) {
                res += symbolValue;
                break;
            }
            
            symbol = s[i + 1];
            var nextSymbolValue = SymbolToInt(symbol);
            if (symbolValue < nextSymbolValue) {
                res += nextSymbolValue - symbolValue;
                i++;
            }
            else {
                res += symbolValue;
            }
        }
        return res;
    }
    
    private static int SymbolToInt(char symbol) => symbol switch
    {
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000,
        _ => 0,
    };
}
