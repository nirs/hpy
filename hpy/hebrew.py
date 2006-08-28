#-*= coding: utf-8 -*-
""" Hebrew data """

keywords = {u'וגם': 'and',
            u'מחק': 'del',
            u'לכל': 'for',
            u'הוא': 'is',
            u'זרוק': 'raise',    
            u'ודא': 'assert',
            u'אחרתאם': 'elif',      
            u'מתוך': 'from',      
            u'למדה': 'lambda',    
            u'החזר': 'return',   
            u'צא': 'break',     
            u'אחרת': 'else',      
            u'גלובלי': 'global',    
            u'לא': 'not',       
            u'נסה': 'try',      
            u'מחלקה': 'class',     
            u'תפוס': 'except',    
            u'אם': 'if',        
            u'או': 'or',        
            u'כלעוד': 'while',    
            u'המשך': 'continue',  
            u'הפעל': 'exec',      
            u'יבא': 'import',    
            u'עבור': 'pass',      
            u'צור': 'yield',    
            u'הגדר': 'def',       
            u'לבסוף': 'finally',   
            u'בתוך': 'in',        
            u'הדפס': 'print'}
 
# Generate hebrew character lists
# see http://www.unicode.org/charts/PDF/U0590.pdf

alpha = []

for i in range(int('0590', 16), int('05ff', 16) + 1):
    character = unichr(i)
    if character.isalpha():
        alpha.append(character)

