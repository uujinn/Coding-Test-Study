def getDistance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def solution(numbers, hand):
  answer = ''
  keypads = {'1': (0,0), '2': (1,0), '3': (2,0), '4': (0,1), '5': (1,1), '6': (2, 1),'7': (0,2), '8': (1,2), '9': (2, 2), '*': (0,3), '0': (1,3), '#': (2, 3)}
  
  l_pos = keypads['*']
  r_pos = keypads['#']
  
  for n in numbers:
      if n == 1 or n == 4 or n == 7:
          l_pos = keypads[str(n)]
          answer += 'L'
      elif n == 3 or n == 6 or n == 9:
          r_pos = keypads[str(n)]
          answer += 'R'
      else:
          if getDistance(keypads[str(n)][0],keypads[str(n)][1], l_pos[0], l_pos[1]) < getDistance(keypads[str(n)][0],keypads[str(n)][1], r_pos[0], r_pos[1]):
              l_pos = keypads[str(n)]
              answer += 'L'
          elif getDistance(keypads[str(n)][0],keypads[str(n)][1], l_pos[0], l_pos[1]) >getDistance(keypads[str(n)][0],keypads[str(n)][1], r_pos[0], r_pos[1]):
              r_pos = keypads[str(n)]
              answer += 'R'
          else:
              if hand == "right":
                  r_pos = keypads[str(n)]
                  answer += 'R'
              else:
                  l_pos = keypads[str(n)]
                  answer += 'L'
          
  
  return answer