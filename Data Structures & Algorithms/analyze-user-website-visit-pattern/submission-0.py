from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Group visits by username and sort by timestamp
        user_history = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_history[user].append(web)
        
        pattern_counts = defaultdict(int)
        # Step 2: Generate unique 3-sequences for each user
        for user in user_history:
            patterns = set()
            cur = user_history[user]
            for i in range(len(cur)):
                for j in range(i+1, len(cur)):
                    for k in range(j+1, len(cur)):
                        patterns.add((cur[i], cur[j], cur[k]))
            for p in patterns:
                pattern_counts[p] += 1
        
        # Step 3: Find the pattern with the highest count, using lexicographical order as a tie-breaker
        # Sorting key first checks negative count (highest first), then the pattern itself (alphabetical)
        max_count = 0
        res = tuple()
        for pattern in pattern_counts:
            if (pattern_counts[pattern] > max_count or
               pattern_counts[pattern] == max_count and
               pattern < res):
                max_count = pattern_counts[pattern]
                res = pattern
        return list(res)