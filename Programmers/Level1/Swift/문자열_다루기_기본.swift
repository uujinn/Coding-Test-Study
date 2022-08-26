func solution(_ s:String) -> Bool {
    
    if (s.count == 4 || s.count == 6) && (Double(s) != nil){
        return true
    }
    
    return false
}