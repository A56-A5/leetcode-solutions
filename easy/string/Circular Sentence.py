class Solution(object):
    def isCircularSentence(self, sentence):
        words = sentence.split(" ")  
        for i in range(len(words)):
            This = words[i]
            Next = words[(i + 1) % len(words)]  
            if This[-1] != Next[0]: 
                return False
        return True
