from cmath import *
def golf(h,w):
  t,e=pi/2*w,sqrt(1-w/h*w/h)+1e-9
  return [round(t*w*h/3,2),round(t*abs(w+h*asin(e)/e),2)]
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert list(golf(4, 2)) == [8.38, 21.48]
#    assert list(golf(2, 2)) == [4.19, 12.57]
#    assert list(golf(2, 4)) == [16.76, 34.69]
#    print("All set? Click 'Check' to review your code and earn rewards!")