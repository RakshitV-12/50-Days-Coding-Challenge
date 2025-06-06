class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
        
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]
        
        return image

