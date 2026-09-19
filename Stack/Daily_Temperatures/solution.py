class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures) 
        rs = [0]*n 
        st = [] 
        for i in range( n-1 , -1 , -1 ) : 
            while st and temperatures[ st[-1] ] <= temperatures[i] : 
                st.pop() 
            if st : 
                rs[i] = st[-1] - i 
            st.append(i) 
        return rs        