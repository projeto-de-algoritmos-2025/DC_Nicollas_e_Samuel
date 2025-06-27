class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m  

        while low <= high:
           
            i = (low + high) // 2

            j = (m + n + 1) // 2 - i


            max_left_nums1 = nums1[i-1] if i > 0 else float('-inf')
       
            min_right_nums1 = nums1[i] if i < m else float('inf')

            max_left_nums2 = nums2[j-1] if j > 0 else float('-inf')
        
            min_right_nums2 = nums2[j] if j < n else float('inf')

    
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:

                if (m + n) % 2 == 1:
                    return float(max(max_left_nums1, max_left_nums2))
              
                else:
                    return float(
                        (max(max_left_nums1, max_left_nums2) +
                         min(min_right_nums1, min_right_nums2)) / 2.0
                    )

            elif max_left_nums1 > min_right_nums2:
                high = i - 1

            else: 
                low = i + 1

        return 0.0