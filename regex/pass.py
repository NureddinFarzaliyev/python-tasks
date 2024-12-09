

str1 = 'AbbD2134@1'
str2 = 'aF1#'
str3 = '2W3e*'
str4 = '2We3345'

point = 0

def check_password(password):

    if(len(password) > 12): return

    if(len(password) >= 6):
        point += 1

