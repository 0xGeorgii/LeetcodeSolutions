void swap(int* x, int* y)
{
    *x ^= *y;
    *y ^= *x;
    *x ^= *y;
}

void rotate(int** matrix, int matrixSize, int* matrixColSize)
{
    for (int i = 0; i < matrixSize; i++)
    {
        for (int j = i + 1; j < matrixSize; j++)
        {
            swap(&matrix[i][j], &matrix[j][i]);
        }
    }
    
    for (int i = 0; i < matrixSize; i++)
    {
        for (int j = 0; j < matrixSize  / 2; j++)
        {
            swap(&matrix[i][j], &matrix[i][matrixSize - j - 1]);
        }
    }
}
