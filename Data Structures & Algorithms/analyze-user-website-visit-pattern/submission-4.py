from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        if not username or not timestamp or not website:
            return []
        user_history = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_history[user].append(web)
        
        patterns = defaultdict(int)
        for user in user_history:
            visited = user_history[user]
            user_patterns = set()
            for i in range(len(visited)):
                for j in range(i+1, len(visited)):
                    for k in range(j+1, len(visited)):
                        user_patterns.add((visited[i], visited[j], visited[k]))
            for pattern in user_patterns:
                patterns[pattern] += 1
        
        max_count = 0
        res = tuple()
        for pat in patterns:
            if (patterns[pat] > max_count or
               patterns[pat] == max_count and pat < res):
               max_count = patterns[pat]
               res = pat
        return list(res)