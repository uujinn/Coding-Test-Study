func changeWord(_ word: String) -> String {
    
    var str = ""
    
    for (index, chr) in word.enumerated() {
        if index % 2 == 0{
            str += chr.uppercased()
        }else{
            str += chr.lowercased()
        }
    }
    
    return str
}

func solution(_ s:String) -> String {
    var arr = s.components(separatedBy: " ")
    var answer: [String] = []
    for word in arr{
        answer.append(changeWord(word))
    }

    return answer.joined(separator:" ")
}


