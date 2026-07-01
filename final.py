class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        s = 0

        for x in nums:
            s += x
            prefix.append(s)

        temp = [0] * len(prefix)

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            lo = hi = mid

            for i in range(left, mid):
                while lo < right and prefix[lo] - prefix[i] < lower:
                    lo += 1
                while hi < right and prefix[hi] - prefix[i] <= upper:
                    hi += 1
                count += hi - lo

            i, j, k = left, mid, left

            while i < mid and j < right:
                if prefix[i] <= prefix[j]:
                    temp[k] = prefix[i]
                    i += 1
                else:
                    temp[k] = prefix[j]
                    j += 1
                k += 1

            while i < mid:
                temp[k] = prefix[i]
                i += 1
                k += 1

            while j < right:
                temp[k] = prefix[j]
                j += 1
                k += 1

            prefix[left:right] = temp[left:right]
            return count

        return merge_sort(0, len(prefix))
