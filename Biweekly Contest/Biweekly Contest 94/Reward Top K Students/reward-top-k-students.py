class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        
        res = []
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        
        for i, r in zip(student_id, report):
            score = 0
            
            for s in r.split():
                if s in positive_feedback: score += 3
                if s in negative_feedback: score -= 1
                
            res.append( (score, i) )
        
        res = sorted(res, key=lambda x: (-x[0], x[1]))
        return [ x[1] for x in res[:k]]
