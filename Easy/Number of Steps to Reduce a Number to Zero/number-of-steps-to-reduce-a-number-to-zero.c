int numberOfSteps(int num){
    int steps = 0;
    
    while (num > 0)
    {
        if (num & 1 == 1)
        {
            num = (num >> 1) << 1;
            steps++;
        }
        else
        {
            num /= 2;
            steps++;
        }
    }
    
    return steps;
}
