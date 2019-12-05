''' 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗'''

def is_odd(da):
    return da % 2 == 0

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass
    
if __name__ == "__main__":
    da = input("input data ")
    if(is_odd(int(da))):
        print("%d is even data" % int(da))
    else:
        print("%d is not even data" % int(da))
