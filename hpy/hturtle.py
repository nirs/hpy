#-*- coding: utf-8 -*-
""" צב - גרפיקה בסגנון לוגו """

import turtle

# Map Hebrew color names to TK color names
hpy_d7a6d791d7a2d799d79d = {
u'אדום': 'red',
u'ירוק': 'green',
u'כחול': 'blue',
}

def hpy_d79ed7a2d79cd795d7aa():
    """שנה את יחידות הזוית למעלות"""
    turtle.degrees()
    
def hpy_d7a8d793d799d790d7a0d799d79d():
    """שנה את יחידות הזוית לרדיאנים"""
    turtle.radians()
    
def hpy_d790d7aad797d79c():
    """אתחל את לוח הציור"""
    turtle.reset()
    
def hpy_d7a0d7a7d794():
    """נקה את לוח הציור"""
    turtle.clear()
    
def hpy_d7a2d795d7a7d791(hpy_d793d792d79c):
    """קבע מעקב להיות אמת או שקר (לפי הדגל), מעקב אומר כי הקוים יצויירו לאט יותר ועם סמן משולש"""
    turtle.tracer(hpy_d793d792d79c)
    
def hpy_d7a7d793d799d79ed794(hpy_d79ed7a8d797d7a7):
    """הזז את הצב קדימה"""
    turtle.forward(hpy_d79ed7a8d797d7a7)
    
def hpy_d790d797d795d7a8d794(hpy_d79ed7a8d797d7a7):
    """הזז צב אחורה"""
    turtle.backward(hpy_d79ed7a8d797d7a7)
    
def hpy_d7a9d79ed790d79cd794(hpy_d796d795d799d7aa):
    """סובב צב נגד כיוון השעון"""
    turtle.left(hpy_d796d795d799d7aa)
    
def hpy_d799d79ed799d7a0d794(hpy_d796d795d799d7aa):
    """סובב צב עם כיוון השעון"""
    turtle.right(hpy_d796d795d799d7aa)
    
def hpy_d79ed7a2d79cd794():
    """הרם את העט למעלה (הפסק לצייר)"""
    turtle.up()
    
def hpy_d79ed798d794():
    """הורד את העט למטה (התחל לצייר)"""
    turtle.down()
    
def hpy_d7a2d795d791d799(hpy_d7a8d795d797d791):
    """קבע את עובי העט"""
    turtle.width(hpy_d7a8d795d797d791)
    
def hpy_d7a6d791d7a2(hpy_d7a6d791d7a2):
    """שנה את צבע העט"""
    turtle.color(hpy_d7a6d791d7a2d799d79d[hpy_d7a6d791d7a2])
    
def hpy_d7a6d791d7a2(hpy_d790d793d795d79d, hpy_d799d7a8d795d7a7, hpy_d79bd797d795d79c):
    """שנה את צבע העט לפי חלקים מהאחד של אדום, ירוק וכחול"""
    turtle.color(hpy_d790d793d795d79d, hpy_d799d7a8d795d7a7, hpy_d79bd797d795d79c)
    
def hpy_d79bd7aad795d791(hpy_d79ed79cd79c):
    """כתוב טקסט על לוח הציור"""
    turtle.write(hpy_d79ed79cd79c)
    
def hpy_d79ed79cd790(hpy_d793d792d79c):
    """קבע את אופי הציור להיות משטחים מלאים לפי אמת/שקר"""
    turtle.fill(hpy_d793d792d79c)
    
def hpy_d79ed7a2d792d79c(hpy_d79ed797d795d792):
    """צייר מעגל על לוח הציור בגודל מחוג"""
    turtle.circle(hpy_d79ed797d795d792)
    
def hpy_d79cd79a5fd790d79c(hpy_d790, hpy_d791):
    """לך אל נקודה בלוח הציור"""
    turtle.goto(hpy_d790, hpy_d791)
    
def hpy_d792d795d791d7945fd797d79cd795d79f():
    """החזר את גובה החלון"""
    return  turtle.window_height()
    
