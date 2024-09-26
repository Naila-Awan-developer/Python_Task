flag_register=0x1234
the_mask=1<<3
flag_register &=(~ the_mask)
flag_register |= the_mask
flag_register ^= the_mask
if flag_register & the_mask:
    print("the third bit is set")
else:
    print("the third bit is reset")