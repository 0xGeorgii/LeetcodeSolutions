/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    
    if (s.length !== t.length) {
        return false;
    }
    
    if (s.length === 1) {
        return t.includes(s);
    }
    
    let freq = Array(26).fill(0);
    
    for (var i = 0; i < s.length; i++) {
        freq[s.charCodeAt(i) % 26]++;
        freq[t.charCodeAt(i) % 26]--;
    }
    
    for ( i = 0; i < 26; i++) {
        if (freq[i] !== 0) {
            return false;
        }
    }
    
    return true;
    
};
