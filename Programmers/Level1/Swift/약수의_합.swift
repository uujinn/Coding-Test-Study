func solution(_ n:Int) -> Int {
    var answer = 0
    for i in 1..<n+1{
        if n % i == 0{
            answer += i
        }
    }
    return answer
}