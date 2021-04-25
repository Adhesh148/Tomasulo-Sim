def convertToInt(mantissa_str):
  
    power_count = -1
    mantissa_int = 0

    for i in mantissa_str:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1

    return (mantissa_int + 1)
  
def ieee2float(ieee_32):

    #ieee_32 = '1 10000000 00100000000000000000000'
  
    # First bit will be sign bit.
    sign_bit = int(ieee_32[0])
  
    # Next 8 bits will be 
    # Exponent Bits in Biased
    # form.
    exponent_bias = int(ieee_32[1 : 9], 2)
  
    # In 32 Bit format bias
    # value is 127 so to have
    # unbiased exponent
    # subtract 127.
    exponent_unbias = exponent_bias - 127
  
    # Next 23 Bits will be
    # Mantissa (1.M format)
    mantissa_str = ieee_32[9 : ]
  
    # Function call to convert
    # 23 binary bits into 
    # 1.M real no. form
    mantissa_int = convertToInt(mantissa_str)
  
    # The final real no. obtained
    # by sign bit, mantissa and
    # Exponent.
    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)
  
    # Printing the obtained
    # Real value of floating
    # Point Representaion.
    return real_no