func solution(_ x:Int, _ n:Int) -> [Int] {
    var answer: [Int] = [] 
    for i in 0..<n{
        answer.append(x + i * x)
    }
    return answer
}