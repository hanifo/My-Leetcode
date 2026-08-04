class Solution(object):
    def flipAndInvertImage(self, image):
        ans=[]
        for i in image:
            i.reverse()
            for j in range(len(i)):
                if i[j]==0:
                    i[j]=1
                else:
                    i[j]=0
            ans.append(i)
        return ans