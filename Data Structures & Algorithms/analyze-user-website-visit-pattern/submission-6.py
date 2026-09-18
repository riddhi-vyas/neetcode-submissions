# Let N be the total number of visits and vᵤ be the number of visits made by user u
#Time: O(N log N + Σ vᵤ³), worst-case = O(N³) when one user has all the visits.
#Space:O(N+P+U), Worst-case: O(N³) because the number of distinct triples can grow cubically.
# user_history and sorting: O(N).
# patterns: O(P), where P is the number of distinct patterns across all users.
# user_pat: O(U), where U is the largest number of distinct patterns generated for one user.
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_history = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x:x[1]):
            user_history[user].append(web)
        
        patterns = defaultdict(int)
        for user in user_history:
            websites = user_history[user]
            user_pat = set()
            # Extract pattern combinations of 3-websites
            for i in range(len(websites)):
                for j in range(i+1, len(websites)):
                    for k in range(j+1, len(websites)):
                        user_pat.add((websites[i], websites[j], websites[k]))
            # Add user_pat with freq to patterns
            for pat in user_pat:
                patterns[pat] += 1
        # check and return most freq pattern
        res = tuple()
        most_visited = 0
        for pat in patterns:
            if (patterns[pat] > most_visited or
                patterns[pat] == most_visited and pat < res): #condition to return lex smallest
                most_visited = patterns[pat]
                res = pat
        return list(res)        