def solution(sizes):
    
    sizes = [sorted(size) for size in sizes]

    return max(x[0] for x in sizes) * max(x[1] for x in sizes)