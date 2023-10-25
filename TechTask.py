# First Task

def sum(nums, target):
    nums.sort()
    n = len(nums)
    quads = []

    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue
            l, r = b + 1, n - 1
            while l < r:
                total = nums[a] + nums[b] + nums[l] + nums[r]
                if total == target:
                    quads.append([nums[a], nums[b], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1

    return quads
#After Function is defined.. U can use it in the main func like this :

int main() {
    int nums[] = {1, 0, -1, 0, -2, 2};
    int numsSize = 6;
    int target = 0;
    int returnSize;
    int* returnColumnSizes;

    int** result = fourSum(nums, numsSize, target, &returnSize, &returnColumnSizes);
    for (int i = 0; i < returnSize; i++) {
        printf("[");
        for (int j = 0; j < 4; j++) {
            printf("%d", result[i][j]);
            if (j < 3) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
    free(returnColumnSizes);

    return 0;
}



#------------------------------------------------------------------------------------------------------
#Second Task


def lengthOfLastWord(s):
    s = s.rstrip()
    length = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            break
        length += 1

    return length
##Heres how u can use the function : call it like this  :
##s1 = "Hello World"
##print(lengthOfLastWord(s1))
