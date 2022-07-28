func solution(_ arr:[Int]) -> Double {
    var sum = arr.map{ $0 }.reduce(0, +)

    return Double(sum) / Double(arr.count)
}