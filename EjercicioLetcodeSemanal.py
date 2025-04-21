class Solution(object):
    def search(self, nums, target):
        izquierda, derecha = 0, len(nums) - 1
        while izquierda <= derecha :
            mitad = (izquierda + derecha) //2
            if nums[mitad] == target:
                return mitad
            if nums[izquierda] <= nums[mitad]:
                if nums[izquierda] <= target < nums[mitad]:
                    derecha = mitad - 1 
                else:
                    izquierda = mitad + 1 
            else: 
                if nums[mitad] <= target < nums[derecha]:
                    derecha = mitad + 1
                else:
                    izquierda = mitad - 1 
        return -1
