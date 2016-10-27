S = ["00000000", "00000000", "46F8E8C5", "460C6085",
     "70F83B8A", "284B8303", "513E1454", "F621ED22",
     "3125065D", "11A83A5D", "D427686B", "713AD82D",
     "4B792F99", "2799A4DD", "A7901C49", "DEDE871A",
     "36C03196", "A7EFC249", "61A78BB8", "3B0A1D2B",
     "4DBFCA76", "AE162167", "30D76B0A", "43192304",
     "F6CC1431", "65046380"]

din = '0000000100000001' # Input No. in hex
print('The value of din is:', din)

# Slicing
a_reg=int(din[0:8], 16)

b_reg=int(din[8:16], 16)

print('a_reg:', hex(a_reg))
print('b_reg:', hex(b_reg))

# a and b
a = a_reg
b = b_reg

# XOR
for i in range(1, 4):
      ab_xor = a_reg ^ b_reg
      print('calculating A[', i, ']')
      print('ab_xor=a_reg XOR b_reg')
      print('ab_xor:', hex(ab_xor))

      # rotation
      res = str((bin(ab_xor)))
      res1 = (res[2:])
      l = 32 - len(res1)

      for j in range(0, l):
            res1 = '0' + res1

      def lrot(num, amount):
            front = num[0:amount]
            num = num[amount:]
            num = num + front
            return num


      a_rot = lrot(res1, (b_reg % 32))

      a_rot = int(a_rot, 2)
      print('a_rot:', hex(a_rot))
      a = a_rot + int(S[2*i], 16)
      a=a%4294967296
      print('A[', i, '] = a_rot+S[2*', i, ']:', hex(a))

      # For B
      # XOR
      ba_xor = b_reg ^ a
      print('calculating B[', i, ']')
      print('ba_xor = b_reg XOR A[', i, ']')
      print('ba_xor:', hex(ba_xor))

      # rotation
      res = str((bin(ba_xor)))
      res1 = (res[2:])
      l = 32 - len(res1)

      for k in range(0, l):
            res1 = '0' + res1

      b_rot = lrot(res1, (a % 32))

      b_rot = int(b_rot, 2)
      print('b_rot:', hex(b_rot))

      b = b_rot + int(S[(2*i) + 1], 16)
      b=b%4294967296

      print('B[', i, '] = b_rot+S[2*', i, '+1]:', hex(b))
      b_reg = b
      a_reg = a

      print('b_reg:', hex(b_reg))
      print('a_reg:', hex(a_reg))