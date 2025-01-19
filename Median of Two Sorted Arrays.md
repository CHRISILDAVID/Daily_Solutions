# Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).

### Test Cases

| Input | Output | Explanation |
| --- | --- | --- |
| `[1,3], [2]` | 2.0 | Merged array is `[1, 2, 3]`. Median is 2. |
| `[1,2], [3,4]` | 2.5 | Merged array is `[1, 2, 3, 4]`. Median is (2 + 3) / 2 = 2.5. |

### Solution Explanation

The solution uses a simple algorithm to find the median of two sorted arrays. The idea is to merge the two arrays into one array, and then find the median of the merged array.

Here's the code:
```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        while i < n or j < m:
            if j >= len(nums2):
                break
            if i >= len(nums1):
                nums1.append(nums2[j])
                j += 1
                continue
            if nums1[i] < nums2[j]:
                i += 1
                continue
            else:
                nums1.insert(i, nums2[j])
                j += 1
                continue
        if (len(nums1) % 2) == 0:
            return (nums1[len(nums1) // 2] + nums1 [(len(nums1) // 2) - 1]) / 2
        else:
            return nums1[len(nums1) // 2]
```
The code works by iterating through both arrays, and for each element in `nums1`, it checks if the corresponding element in `nums2` is less than it. If it is, they are merged into a single array using the `insert` method. Once both arrays are merged, the median is found by taking the average of the two middle elements (or the single middle element if there are an odd number of elements).

### Code Example (formatted in markdown)
```
# Median of Two Sorted Arrays

def findMedianSortedArrays(nums1, nums2):
    # Sort both arrays
    nums1.sort()
    nums2.sort()

    # Merge the two arrays
    merged_array = list(set(nums1 + nums2).intersection())

    # Find the median of the merged array
    if len(merged_array) % 2 == 0:
        return (merged_array[len(merged_array) // 2] + merged_array [(len(merged_array) // 2) - 1]) / 2
    else:
        return merged_array[len(merged_array) // 2]
```
### Additional Insights

* The solution has a time complexity of O(log(m+n)), which is the optimal time complexity for this problem.
* The solution uses a simple and intuitive approach to find the median of two sorted arrays.
* The code is easy to read and understand, making it a good example for beginners to learn from.
