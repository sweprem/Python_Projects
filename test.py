def blackjack_hand_greater_than(hand_1, hand_2):
    ans = 0
    anss = 0
    list1 = {}
    list2 = {}
    # Calculation of hand_1
    for value in hand_1:
        if value in ('J', 'Q', 'K'):
            list1[value]=10
        elif value=='A':
            list1[value]=1
        else:
            list1[value]=int(value)
    print(list1)
    for m,n in list1.items():
        ans = ans + n
    if (ans <= 21) and (m=='A' in list1.keys()):
        list1['A']=10
        print(list1)
        ans=0
        for n in list1.values():
          ans = ans + n
    hand_1 = ans
    print(hand_1)
    # Calculation of hand_2
    for values in hand_2:
        if values in ('J', 'Q', 'K'):
            list2[values]=10
        elif values=='A':
            list2[values]=1
        else:
            list2[values]=int(values)
    print(list2)
    for o,p in list2.items():
        anss = anss + p
    if (ans <= 21) :
        list2['A']=10
        print(list2)
        ans=0
        for p in list2.values():
          ans = ans + p
    hand_2 = anss
    print(hand_2)

    if hand_2 < hand_1 and hand_1 < 21:
        return True
    return False


answer=blackjack_hand_greater_than(['5','Q','Q','2'], ['K','1','J'])
print(answer)

