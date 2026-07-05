class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## numbers
        ## target

        # example [1,2,3,4]
        #          ^     
        for index, number in enumerate(numbers):
            for index2,number2 in enumerate(numbers):
                if number != number2:
                    if number + number2 == target:
                        return [index+1, index2+1]