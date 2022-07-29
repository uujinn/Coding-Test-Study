func solution(_ num:Int) -> Int {
    var n = num
    var cnt = 0
    
    if num == 1 {
        return 0
    }
    
    while true{
        
        if n == 1{ break }
        else if cnt > 500{
            cnt = -1
            break
        }
        
        if n % 2 == 0{
            n /= 2
        }else{
            n *= 3
            n += 1
        }
        
        cnt += 1
    }
    
    return cnt
}