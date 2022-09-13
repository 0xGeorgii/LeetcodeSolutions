bool validUtf8(int* data, int dataSize)
{
    if (dataSize == 1)
    {
        return (*data & 1 << 7) >> 7 == 0;
    }    
    
    for (int i = 0; i < dataSize; i++)
    {
        int n = *(data + i);
        if ((n & 1 << 7) >> 7 == 0)
        {
            continue;
        }
        else if (i + 1 >= dataSize)
        {
            return false;    
        }
        else
        {            
            int chunckLength = 0;
            
            for (int p = 7; p > 0; p--)
            {
                if ((n & 1 << p) >> p == 1)
                {
                    chunckLength++;
                }
                else
                {
                    break;
                }
            }
            
            if (i + chunckLength > dataSize)
            {
                return false;
            }
            
            if (chunckLength > 4 || chunckLength == 1)
            {
                return false;
            }
            
            for (int j = 1; j < chunckLength; j++)
            {
                n = *(data + i + j);
                if ((n & 1 << 7) >> 7 == 1 && (n & 1 << 6) >> 6 == 0)
                {
                    continue;
                }
                else
                {
                    return false;
                }
            }
            
            i += chunckLength - 1;
        }
    }
    
    return true;
}
