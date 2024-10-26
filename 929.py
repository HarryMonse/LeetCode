from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        arr=[]
        for i in emails:
            if '@' in i:
                at = i.index('@')
                temp=i[:at]
                temp=temp.replace(".","")
                
                if '+' in temp:
                    plus = temp.index('+')
                    temp = temp[0:plus]
                temp+=i[at:]
                if temp not in arr:
                    arr.append(temp)
            else:
                continue
        #print(arr)
        return len(arr)
    

solution_instance = Solution()

result = solution_instance.numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(result)

result = solution_instance.numUniqueEmails(emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
print(result)