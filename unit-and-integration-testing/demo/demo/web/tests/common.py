from django.test import TestCase

from django.test import TestCase
from django.core.exceptions import ValidationError

'''
# Tests where environment Language Matters( if Django Tests in Python)
1.Unit Tests ->  concrete isolated piece of code 
2.Integration Tests -> integration of coupled pieces of code
# Tests where environment Language Don't Matter
3.Api Tests -> Testing end result of API
 - Check result of HTTP call returns JSON
4.Functional -> End-to-End,UI Tests, Bot clicks on site
#Other Tests
5.Load Tests
6.Performance Tests
7.Security Tests
'''

'''
- Tests Change!
- Tests are part of the Code!
- Test give us "Fast Fail!"
- Tests give us Peace of Mind
'''

def validate_greater_than_zero(value):
    if value < 0:
        raise ValidationError('Value must be greater than 0')


'''
Check for Negative Value -> Error
Check for Zero Value -> Error
Check for Positive Value -> No Error
'''


def get_only_positive_values(values):
    positive_values = []
    for value in values:
        try:
            validate_greater_than_zero(value)
            positive_values.append(value)
        except:
            pass
    return positive_values


'''
With unit tests:
-Check for Empty list
-Check for List with positives
-Check for List with Negatives
With Integration Tests:
-No mocking
-[]->[]
-[1,2,3]->[1,2,3]
-[0,1,2]->[1,2]
-[0,0,0]->[]
-[....

'''
