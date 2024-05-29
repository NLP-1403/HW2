import string

DEBUG = False
INDEX_TABLE = lambda x: chr(x)

ESCAPE = '{([])^$.|*+?}\\' + '\u061f'  # Inside () or Outside
INESCAPE = '^-'  # Inside []
DIGIT = string.digits
# DIGIT = string.digits + '٠١٢٣٤٥٦٧٨٩'
# DIGIT = string.digits + '\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669'
UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
LETTERS = string.ascii_letters
# LETTERS = string.ascii_letters + 'ابتثجحخدذرزژسشصضطظعغفقكلمنهويءآأؤإئ'
# LETTERS = string.ascii_letters + ('\u0627\u0628\u062a\u062b\u062c\u062d\u062e\u062f\u0630\u0631\u0632\u0698\u0633'
#                                   '\u0634\u0635\u0636\u0637\u0638\u0639\u063a\u0641\u0642\u0643\u0644\u0645\u0646'
#                                   '\u0647\u0648\u064a\u0621\u0622\u0623\u0624\u0625\u0626')
WORD = LETTERS + DIGIT + '_'
LOWER_HEXDIGIT = DIGIT + LOWER[:6]
UPPER_HEXDIGIT = DIGIT + UPPER[:6]
CHAR_RANGE = WORD[:-1]  # A-Za-z0-9
SYMBOL = '''!@#$%^&*()[]';./,<>?:"{}-=`~|+-\\ '''
CHAR_RANGE_WITH_SYMBOLS = WORD[:-1] + SYMBOL
SPACE = '\x0c\n\r\t\x0b\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u200a\u2028\u2029\u202f\u205f\u3000\ufeff'
