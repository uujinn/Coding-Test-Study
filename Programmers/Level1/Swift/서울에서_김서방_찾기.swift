func solution(_ seoul:[String]) -> String {
    var idx = 0
    
    for i in seoul{
        if i == "Kim"{
            return "김서방은 \(idx)에 있다"
        }    
        
        idx += 1
    }
    
    return "김서방은 \(idx)에 있다"
}