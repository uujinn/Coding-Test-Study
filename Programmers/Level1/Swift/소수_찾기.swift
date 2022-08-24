import Foundation

func isSosu(_ n: Int) -> Bool{
  
  for i in 2...Int(sqrt(Double(n))+1){
    if n == 0 || n == 1{
      return false
    }else if n == 2{
      return true
    }
    
    if n % i == 0{ // 소수 X
      return false
    }
  }
  
  return true //  소수 O
}

func solution(_ n:Int) -> Int {
  
  var answer: Int = 0
  
  for i in 1...n{
    if isSosu(i){
      answer += 1
    }
  }
  
  return answer
}