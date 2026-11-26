class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        count={}
        for i in range (len(hand)):
            if hand[i] in count:
                count[hand[i]]+=1
            else : 
                count[hand[i]]=1
        
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count.get(i, 0):
                        return False
                    count[i] -= 1
        return True
