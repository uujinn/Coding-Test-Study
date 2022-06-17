// 시간초과

import Foundation

struct Queue<T>{
  private var queue: [T] = []
  
  public var count: Int{
    queue.count
  }
  
  public var isEmpty: Bool{
    return queue.isEmpty
  }
  
  public mutating func enqueue(_ element: T){
    queue.append(element)
  }
  
  public mutating func dequeue() -> T?{
    return isEmpty ? -1 as! T : queue.removeFirst()
  }
  
  public var front: T? {
    return isEmpty ? -1 as! T : queue[0]
  }
  
  public var back: T? {
    return isEmpty ? -1 as! T : queue[queue.count-1]
  }
}

let N = Int(readLine()!)!

var command: Array<String>
var q = Queue<Int>();

for _ in 1...N{
  command = readLine()!.components(separatedBy: " ")
  
  if command[0] == "push"{
    q.enqueue(Int(command[1])!)
  }
  else if command[0] == "pop"{
    print(q.dequeue()!)
  }
  else if command[0] == "size"{
    print(q.count)
  }
  else if command[0] == "empty"{
    print(q.isEmpty ? 1: 0)
  }
  else if command[0] == "front"{
    print(q.front!)
  }
  else if command[0] == "back"{
    print(q.back!)
  }
}
