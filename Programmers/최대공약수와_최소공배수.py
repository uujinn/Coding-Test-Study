func GCD(_ min: Int, _ max: Int) -> Int { // 최대공약수
    let remain = min % max
    if remain == 0 {
        return max
    }
    else {
        return GCD(max, remain)
    }
}

func LCM(_ a: Int, _ b: Int) -> Int { // 최소공배수
    return a * b / GCD(a, b)
}

func solution(_ n:Int, _ m:Int) -> [Int] {
    return [GCD(n,m), LCM(n, m)]
}