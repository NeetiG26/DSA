'''
Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
'''

def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    set1 = set(list1) - set(list2)
    set2 = set(list2) - set(list1)
    common_interests = list((set(list1) - set1) - set2)
    
    int_val = 10000
    final_interest = []
    for ele in common_interests:
        val = list1.index(ele) + list2.index(ele)
        if val < int_val:
            int_val = val
            final_interest = [ele]
        elif val == int_val :
            final_interest.append(ele)
        
    return final_interest