# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:

    def __init__(self):
        self.rem_count = 0
        self.rem_str = []
        # self.bp=0
    def read(self, buf: List[str], n: int) -> int:
        
        ans = []
        if self.rem_count >= n:
            self.rem_count -= n
            ans = self.rem_str[:n]
            self.rem_str = self.rem_str[n:]
            for i,v in enumerate(ans):
                buf[i] = v
            # self.bp+= len(ans)
            return len(ans)
        
        else:
            n = n - self.rem_count
            self.rem_count = 0
            ans = self.rem_str
            self.rem_str = []
            
            count_read = 0
            temp_buf = ['','','','']
            ans2 = []
            while count_read < n:
                curr_count = read4(temp_buf)
                if curr_count == 0:
                    break
                else:
                    count_read += curr_count
                    ans2+=temp_buf[:curr_count]
                    
            if count_read >= n:
                self.rem_count = -n + count_read
                self.rem_str = ans2[n:]
                for i,v in enumerate(ans + ans2[:n]):
                    buf[i] = v
                # self.bp += len(ans + ans2[:n])
                return len(ans + ans2[:n])
            
            for i,v in enumerate(ans + ans2):
                buf[i] = v
            # self.bp += len(ans + ans2)
            return len(ans + ans2)
        