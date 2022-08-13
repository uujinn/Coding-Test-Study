import Foundation

func solution(_ n:Int64) -> [Int] {
  let arr = Array(String(n).map{ String($0) }.reversed()).map { Int($0)! }
  return arr
}