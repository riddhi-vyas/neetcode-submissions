#Time comp: O(n + m), where n = len(nums2) and m = len(nums1). Each element of nums2 is pushed onto the stack at most once (when it appears in nums1) and popped at most once. Building nums1_map takes O(m). Overall linear in the combined input sizes.
#Space comp: O(m) for the map and stack; output also takes O(m).
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {num: i for i, num in enumerate(nums1)} # k:v -> num: idx
        ans = [-1] * len(nums1)
        stack = [] # stack stores numbers from nums2 only if they are also in nums1
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1_map[val]
                ans[idx] = cur
            # Push cur if it belongs to nums1, even if the stack is not empty.
            if cur in nums1_map:
                stack.append(cur)
        return ans