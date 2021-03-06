#-*= coding: utf-8 -*-
""" Hebrew data 

@copyright: (c) 2006 by Nir Soffer <nirs@freeshell.org>
@license: GNU GPL, see COPYING for details.
"""

class DuplicateTranslationError(Exception):
    """" Raised when 2 hebrew names translated to same Python name """    

# Used to translate from Hebrew to Python
# XXX check translation at the http://hebrew-terms.huji.ac.il/

pythonNames = {
    
    # Keywords
    # http://docs.python.org/ref/keywords.html
      
    u'וגם': 'and',
    u'מחק': 'del',
    u'לכל': 'for',
    u'הוא': 'is',
    u'זרוק': 'raise',    
    u'ודא': 'assert',
    u'אחרתאם': 'elif', # XXX אחרת_אם?
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
    u'כלעוד': 'while', # XXX כל_עוד?
    u'המשך': 'continue',  
    u'בצע': 'exec',      
    u'יבא': 'import',    
    u'עבור': 'pass',      
    u'צור': 'yield',    
    u'הגדר': 'def',       
    u'לבסוף': 'finally',   
    u'בתוך': 'in',        
    u'הדפס': 'print',

    # In some future version of Python, will both become keywords:
    u'בתור': 'as', # מתוך פו יבא בר בתור בז
    u'כלום': 'None', # אם א הוא כלום
    
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
    
    # Won't translate the dangerous 'input'
    u'קלט': 'raw_input',
    }

# Create reversed map for reversed translation
hebrewNames = {}
for key, value in pythonNames.items():
    if value in hebrewNames:
        raise DuplicateTranslationError('duplicate translation for %s' % key)
    hebrewNames[value] = key
 
# Generate hebrew character lists
# see http://www.unicode.org/charts/PDF/U0590.pdf

alpha = []

for i in range(int('0590', 16), int('05ff', 16) + 1):
    character = unichr(i)
    if character.isalpha():
        alpha.append(character)

