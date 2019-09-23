import gmpy2
import binascii
N_hex=0x180be86dc898a3c3a710e52b31de460f8f350610bf63e6b2203c08fddad44601d96eb454a34dab7684589bc32b19eb27cffff8c07179e349ddb62898ae896f8c681796052ae1598bd41f35491175c9b60ae2260d0d4ebac05b4b6f2677a7609c2fe6194fe7b63841cec632e3a2f55d0cb09df08eacea34394ad473577dea5131552b0b30efac31c59087bfe603d2b13bed7d14967bfd489157aa01b14b4e1bd08d9b92ec0c319aeb8fedd535c56770aac95247d116d59cae2f99c3b51f43093fd39c10f93830c1ece75ee37e5fcdc5b174052eccadcadeda2f1b3a4a87184041d5c1a6a0b2eeaa3c3a1227bc27e130e67ac397b375ffe7c873e9b1c649812edcd
e_hex=0x01
c_hex=0x4963654354467b66616c6c735f61706172745f736f5f656173696c795f616e645f7265617373656d626c65645f736f5f63727564656c797d

c_hex=gmpy2.mpz(c_hex)
N_hex=gmpy2.mpz(N_hex)

i=0
while i<10:
    m_hex=hex(c_hex+gmpy2.mpz(hex(i))*N_hex)
    print(m_hex[2:])
    try:
        print(binascii.a2b_hex(m_hex[2:]).decode("utf8"))
    except binascii.Error as e:
        print("位数非偶数，跳过...")
    i+=1