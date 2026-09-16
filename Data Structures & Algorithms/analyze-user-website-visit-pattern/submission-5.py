from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_history = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_history[user].append(web)
        
        patterns = defaultdict(int)
        for user in user_history:
            user_patterns = set()
            cur = user_history[user] 
            for i in range(len(cur)):
                for j in range(i+1, len(cur)):
                    for k in range(j+1, len(cur)):
                        user_patterns.add((cur[i], cur[j], cur[k]))
            for pat in user_patterns:
                patterns[pat] += 1
        
        max_count = 0
        res = tuple()
        for pat in patterns:
            if (patterns[pat] > max_count or
                patterns[pat] == max_count and pat < res):
                max_count = patterns[pat]
                res = pat
        return list(res)