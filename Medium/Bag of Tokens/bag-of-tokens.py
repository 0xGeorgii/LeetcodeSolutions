class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        score, start, end = 0, 0, -1
        tokens.sort()
        tokens_utilized = 0
        
        while start + abs(end) <= len(tokens):
            
            token = tokens[start]
            
            if token <= power:
                score += 1
                power -= token
                start += 1
                tokens_utilized += 1
                continue
            
            if score > 0 and len(tokens) - tokens_utilized > 1:
                token = tokens[end]
                power += token
                score -= 1
                end -= 1
                tokens_utilized += 1
                continue
            
            break
                
        return score
