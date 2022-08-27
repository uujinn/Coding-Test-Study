import Foundation

func solution(_ s:String) -> Bool
{
    var p_cnt = 0
    var y_cnt = 0
    
    for i in s{
        if i == "y" || i == "Y"{
            y_cnt += 1
        }else if i == "p" || i == "P"{
            p_cnt += 1
        }
    }
    
    if y_cnt == p_cnt {
        return true
    }else{
        return false
    }

}