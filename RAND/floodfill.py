class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        starting_node = image[sr][sc]
        if starting_node == color:
            return image
        
        cols = len(image[0])
        rows = len(image)

        def dfs(r, c):
            if r<0 or r> rows or c <0 or c > cols:
                return None
            if image[r, c] != starting_node:
                return None
            
            image[r, c] = color
            
            dfs(r-1, c) #up
            dfs(r+1, c) #down
            dfs(r, c+1) #right
            dfs(r, c-1) # left
        dfs(sr, sc)
        return image



        
    

        