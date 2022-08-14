import Foundation

func solution(_ n:Int) -> Int
{
    var arr: [Int] = String(n).map{ Int(String($0))! }
    var answer:Int = arr.reduce(0, +)
    
    return answer
}