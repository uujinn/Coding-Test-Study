import Foundation

var N = Int(readLine()!)!

struct Stack<T> {
  private var stack: [T] = []
  
  public var count: Int{
    return stack.count
  }
  
  public var top: T?{
    return self.stack.last
  }
  
  public var isEmpty: Bool{
    return stack.isEmpty
  }
  
  public mutating func push(_ element: T){
    stack.append(element)
  }
  
  public mutating func pop() -> T?{
    return isEmpty ? nil : stack.popLast()
  }
}


var myStack = Stack<Int>()
var command_arr: Array<String>
for _ in 1...N{
  command_arr = readLine()!.components(separatedBy: " ")
  if command_arr[0] == "push"{
    myStack.push(Int(command_arr[1])!)
  }
  else if command_arr[0] == "pop"{
    if myStack.isEmpty{
      print(-1)
    }
    else{
      print(myStack.pop()!)
    }
  }
  else if command_arr[0] == "size"{
    print(myStack.count)
  }
  else if command_arr[0] == "empty"{
    if myStack.isEmpty{
      print(1)
    }
    else{
      print(0)
    }
  }
  else if command_arr[0] == "top"{
    if myStack.isEmpty{
      print(-1)
    }
    else{
      print(myStack.top!)
    }
  }
}

