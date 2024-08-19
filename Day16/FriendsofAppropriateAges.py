class Solution(object):
    def numFriendRequests(self, ages):
        age_count = [0] * 121 
        for age in ages:
            age_count[age] += 1
        
        count = 0

        for age_a in range(1, 121):
            if age_count[age_a] == 0:
                continue
                
            for age_b in range(1, 121):
                if age_count[age_b] == 0:
                    continue
                
                if age_b <= 0.5 * age_a + 7:
                    continue
                if age_b > age_a:
                    continue
                if age_b > 100 and age_a < 100:
                    continue
                
                if age_a == age_b:
                    count += age_count[age_a] * (age_count[age_a] - 1)  
                else:
                    count += age_count[age_a] * age_count[age_b]
        
        return count
        