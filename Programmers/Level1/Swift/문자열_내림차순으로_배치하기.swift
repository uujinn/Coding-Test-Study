func solution(_ s:String) -> String {
    
    var arr = s.map({ String($0) })
    arr.sort(by: >)
    
    return arr.joined(separator: "")
}