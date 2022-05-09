keywords = ["auto","break","case","char","const","continue","default","do",
"double","else","enum","extern","float","for","goto",
"if","int","long","register","return","short","signed",
"sizeof","static","struct","switch","typedef","union",
"unsigned","void","volatile","while","printf","scanf","%d","include","stdio.h","main()"]

operators   = ["=", "==", "+", "-", "*", "/", "++", "--", "+=", "-=", "!=", "||", "&&"]
punctuations= [";", "(", ")", "{", "}", "[", "]"]

def is_int(st):
    try:
        int(st)
        return True
    except:
        return False


my_code='''
#include <stdio.h>
void main()
{
    printf ( "hello" ) ;
}
'''

line=my_code.split()
for i in line:
    if i in keywords:
        print(f'{i} is a keyword')
    elif i in operators:
        print(f'{i} is a operator')
    elif i in punctuations:
        print(f'{i} is a punctutation')
    elif i is is_int(i):
        print(f'{i} is an integer')
    else:
        print(f'{i} is an indentifier')
