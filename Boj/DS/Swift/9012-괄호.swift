// 12ms

import Foundation

struct Stack<T>{
  private var stack: [T] = []
  
  public var count: Int{
    return stack.count
  }
  
  public var isEmpty: Bool{
    return stack.isEmpty
  }
  
  public mutating func push(_ element: T){
    stack.append(element)
  }
  
  public mutating func pop(){
    stack.popLast()
  }
}

var T = Int(readLine()!)!
var continue_flag = false
for _ in 1...T{
  var stack = Stack<Character>()
  
  let data = readLine()!
  
  for c in data{
    if c == "("{
      stack.push(c)
    }
    else{
      if stack.isEmpty{
        print("NO")
        continue_flag = true
        break
      }
      stack.pop()
    }
  }
  
  if continue_flag{
    continue_flag = false
    continue
  }
  
  if !stack.isEmpty{
    print("NO")
  }else{
    print("YES")
  }
}
