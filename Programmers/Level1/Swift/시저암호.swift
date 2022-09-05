func solution(_ s:String, _ n:Int) -> String {
    let upper_alpha = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    let lower_alpha = Array("abcdefghijklmnopqrstuvwxyz")
    
    var arr = Array(s)
    
    for i in 0..<s.count{
        if lower_alpha.contains(arr[i]){
            let index = (lower_alpha.firstIndex(of: arr[i])! + n) % 26
            arr[i] = lower_alpha[index]
        }else if upper_alpha.contains(arr[i]){
            let index = (upper_alpha.firstIndex(of: arr[i])! + n) % 26
            arr[i] = upper_alpha[index]
        }
    }
    
    return String(arr)

}