# Repository Reorganization Plan

## Current Status
This repository needs to be reorganized from a mixed structure to a clean two-directory setup.

## Target Structure
```
Competitive_Programmings/
├── Leetcode_problem_solution/
│   ├── 26-remove-duplicates-from-sorted-array/
│   ├── 33-search-in-rotated-sorted-array/
│   ├── 35-search-insert-position/
│   ├── 36-valid-sudoku/
│   ├── 49-group-anagrams/
│   ├── 349-intersection-of-two-arrays/
│   ├── 463-island-perimeter/
│   ├── 557-reverse-words-in-a-string-iii/
│   ├── 594-longest-harmonious-subsequence/
│   ├── 643-maximum-average-subarray-i/
│   ├── 861-flipping-an-image/
│   ├── 898-transpose-matrix/
│   ├── 1586-longest-subarray-of-1s-after-deleting-one-element/
│   ├── 1633-minimum-number-of-increments-on-subarrays-to-form-a-target-array/
│   ├── 1988-minimize-maximum-pair-sum-in-array/
│   ├── 2137-final-value-of-variable-after-performing-operations/
│   ├── 2233-number-of-smooth-descent-periods-of-a-stock/
│   ├── 2265-partition-array-according-to-given-pivot/
│   ├── 2631-sort-the-students-by-their-kth-score/
│   ├── 2812-find-the-maximum-achievable-number/
│   ├── 2866-longest-even-odd-subarray-with-threshold/
│   ├── 2917-count-pairs-whose-sum-is-less-than-target/
│   ├── 3379-score-of-a-string/
│   ├── 3846-minimum-operations-to-make-array-sum-divisible-by-k/
│   └── 4087-maximum-substrings-with-distinct-start/
│
├── Codeforce_problem_solution/
│   └── basic/
│       ├── A - Vanya and Fence/
│       ├── B - Calculating Function/
│       ├── C - In Search of an Easy Problem/
│       ├── D - Game of Mathletes/
│       ├── E - Long Long/
│       └── F - Contest Proposal/
│
└── README.md
```

## Migration Steps

### Files to Move to `Leetcode_problem_solution/`
- All problem directories currently in `leetcode/` directory
- Standalone problem folders (2137-final-value..., 26-remove-duplicates..., etc.)
- LeetCode-specific `.py` files

### Files to Move to `Codeforce_problem_solution/`
- All problem directories from `Codeforces/basic/`
- Individual Codeforces solution files (e.g., `A. Anton and Danik.py`, `A.magnets.py`, etc.)

### Cleanup
- Remove old `leetcode/` directory (empty after migration)
- Remove old `Codeforces/` directory (after migration)
- Remove old `Codeforce/` directory (appears to be duplicate)
- Remove old `cpp/` directory if empty
- Remove old `python/` directory if empty
- Remove root-level standalone solution files

## Notes
- Each problem should maintain its own README with problem statement and solution explanation
- Keep consistent naming: `[number]-[problem-name]/` format
- All solutions preserved with their original code

---

**Next Steps:** Use GitHub's file management interface or git commands to move files according to this plan.
