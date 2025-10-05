class solution:
    def floodfill(self,sr, sc,image, color):
        starting_node = image[sr][sc]
        if starting_node == color:
            return image
        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            if r< 0 or r>= rows or c <0 or c>= cols:
                return -1
            
            if image[r][c] != starting_node:
                return -1
            
            image[r][c] = color

            dfs(r-1, c) #up
            dfs(r+1,c) # down
            dfs(r, c-1) # left
            dfs(r, c+1) # right
        dfs(sr, sc)
        return image

