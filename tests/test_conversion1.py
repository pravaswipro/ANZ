# PyTest

from currency_conversion import conversion
def test_conversion4():
    input_currency='KRW 1000.00'
    output_currency='FJD'
    result=conversion.convert(input_currency,output_currency)
    print (result)
    assert result=='Unable to find rate for KRW/FJD'