class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        start, end = 0, len(people) - 1
        NumberOfboats = 0
    
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            NumberOfboats += 1
    
        return NumberOfboats