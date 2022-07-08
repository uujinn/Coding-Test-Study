func solution(_ x:Int) -> Bool {

    var sum_x = String(x).map{ Int(String($0))!}.reduce(0, +)

    return x % sum_x == 0

}