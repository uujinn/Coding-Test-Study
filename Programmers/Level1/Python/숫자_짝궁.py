from collections import Counter

def solution(X, Y):
    answer = ''
    inters = []
    
    counter = Counter(X)
    counter2 = Counter(Y)
    xinter_dict = dict(counter)
    yinter_dict = dict(counter2)

    
    for x in xinter_dict.keys():
        if x in yinter_dict.keys():
            if xinter_dict[x] >= yinter_dict[x]:
                for _ in range(yinter_dict[x]):
                    inters.append(x)
            elif xinter_dict[x] < yinter_dict[x]:
                for _ in range(xinter_dict[x]):
                    inters.append(x)

                
    if not inters:
        return "-1"
    
    filtering_inters = [i for i in inters if i != "0"]
    
    if not filtering_inters:
        return "0"
    
    return "".join(sorted(inters, reverse = True))