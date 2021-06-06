def test_bmr(w,h,y,s):
    if s == 'm':
        BMR = 66.5 + (13.75 * w) + (5.003 * h) - (6.755 * y)
        print(BMR)
    if s == 'f':
        BMR = 655 + (9.563 * w) + (1.850 * h) - (4.676 * y)
        print(BMR)