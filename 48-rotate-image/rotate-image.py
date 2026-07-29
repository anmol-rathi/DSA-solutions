class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        flat=[0]*(len(matrix)*len(matrix[0]))
        glat=[0]*(len(matrix)*len(matrix[0]))
        flat = [num for row in matrix for num in row]
        # print(flat)
        count=1
        for i in range(len(flat)):
            if (i%n)==0:
                count+=n-2
            else:
                count+=n-1
            glat[(i+count)%(n*n)]=flat[i]
        print(glat)
        k=0
        for i in range(n):
            for  j in range(n):
                matrix[i][j]=glat[k]
                k+=1
        # n=len(matrix)
        # flat=[0]*(len(matrix)*len(matrix[0]))
        # # flat = [num for row in matrix for num in row]
        # # print(flat)
        # count=1
        # for i in range(n):
        #     for j in range(n):
        #         if j==0:
        #             count+=n-2
        #         else:
        #             count+=n-1
        #         flat[(i+j+count)%(n*n)]=matrix[i][j]
        #     print(flat)
        #     print(count)
