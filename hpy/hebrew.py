#-*= coding: utf-8 -*-
""" Hebrew data 

@copyright: (c) 2006 by Nir Soffer <nirs@freeshell.org>
@license: GNU GPL, see COPYING for details.
"""

names = {
    # Keywords
    u'וגם': 'and',
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
    u'הדפס': 'print',
    
    # Builtins
    u'אמת': 'True',
    u'שקר': 'False',
    u'אורך': 'len',
    u'הוסף': 'append',
    u'ספור': 'count',
    u'הרחב': 'extend',
    u'מפתח': 'index',
    u'הכנס': 'insert',
    u'שלוף': 'pop',
    u'הסר': 'remove',
    u'הפוך': 'reverse',
    u'מיין': 'sort',

    # turtle module
    u'צב': 'turtle',
    u'מעלות': 'degrees',
    u'רדיאן': 'radians',
    u'אתחל': 'reset',
    u'נקה': 'clear',
    u'עוקב': 'tracer',
    u'קדימה': 'forward',
    u'אחורה': 'backward',
    u'שמאלה': 'left',
    u'ימינה': 'right',
    u'מעלה': 'up',
    u'מטה': 'down',
    u'רוחב': 'width',
    u'צבע': 'color',
    u'כתוב': 'write',
    u'מלא': 'fill',
    u'מעגל': 'circle',
    u'לך_אל': 'goto',
    u'עט': 'Pen',
    u'עט_בסיסי': 'RawPen'
    }
 
# Generate hebrew character lists
# see http://www.unicode.org/charts/PDF/U0590.pdf

alpha = []

for i in range(int('0590', 16), int('05ff', 16) + 1):
    character = unichr(i)
    if character.isalpha():
        alpha.append(character)

