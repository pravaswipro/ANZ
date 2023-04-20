# PyTest

from currency_conversion import conversion
def test_conversion():
    input_currency='AUD 100.00'
    output_currency='USD'
    result=conversion.convert(input_currency,output_currency)
    print (result)
    assert result=='USD 83.71'

def test_conversion1():
    input_currency='AUD 100.00'
    output_currency='AUD'
    result=conversion.convert(input_currency,output_currency)
    print (result)
    assert result=='AUD 100.00'

def test_conversion2():
    input_currency='AUD 100.00'
    output_currency='DKK'
    result=conversion.convert(input_currency,output_currency)
    print (result)
    assert result=='DKK 505.80'

def test_conversion3():
    input_currency='JPY 100'
    output_currency='USD'
    result=conversion.convert(input_currency,output_currency)
    print (result)
    assert result=='USD 0.83'