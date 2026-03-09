class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                ans.append("".join(cur_string))
                return
            if left_count < n:
                cur_string.append("(")
                backtrack(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(")")
                backtrack(cur_string, left_count, right_count + 1)
                cur_string.pop()
        backtrack([], 0, 0)
        return ans