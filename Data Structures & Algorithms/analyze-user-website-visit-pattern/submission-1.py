from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_history = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_history[user].append(web)
        
        score = defaultdict(int) # dictionary to store k:v -> pattern:score (score by default 0)
        for user in user_history:
            patterns = set() #set of unique 3-sequence patterns
            cur = user_history[user]
            for i in range(len(cur)):
                for j in range(i+1, len(cur)):
                    for k in range(j+1, len(cur)):
                        patterns.add((cur[i], cur[j], cur[k]))
            
            for p in patterns:
                score[p] += 1
        print(score)
            
        max_count = 0
        res = tuple()
        for pattern in score:
            if (score[pattern] > max_count or
               score[pattern] == max_count and 
               pattern < res): # cheks if pattern is alphabetically smaller
                max_count = score[pattern]
                res = pattern
        return list(res)