func solution(_ arr:[Int]) -> [Int] {
    var answer = arr
    
    let min = arr.min()
    
    for (index, num) in answer.enumerated() {
        if num == min{
            answer.remove(at: index)
        }
    }
    
    return answer.count == 0 ? [-1] : answer
}