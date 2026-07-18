   :rtype: int
        """
        h1,m1,s1=map(int,startTime.split(":"))
        h2,m2,s2=map(int,endTime.split(":"))
        start=h1*3600+m1*60+s1
        end=h2*3600+m2*60+s2
        if end<start:
            end+=start
        return end-start  
        