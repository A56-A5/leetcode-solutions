class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i] = image[i][::-1]
            image[i] = [1 - j for j in image[i]]
        
        return image
