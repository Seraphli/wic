# wechat image convert
import binascii

# first need two file to find rule
trans = 'color_trans.dat'
sheet = 'color_sheet.jpg'

binfile = open(trans,'rb')
a = binfile.read()
hex_trans = binascii.b2a_hex(a)

binfile = open(sheet,'rb')
a = binfile.read()
hex_sheet = binascii.b2a_hex(a)

rule = [0] * 256
flag = [False] * 256
for i in range(len(hex_trans)/2):
  hex_t = hex_trans[2*i:2*(i+1)]
  hex_s = hex_sheet[2*i:2*(i+1)]
  int_t = int(hex_t,16)
  int_s = int(hex_s,16)
  if flag[int_t] == False:
    rule[int_t] = int_s
    flag[int_t] = True
  if flag.count(True) == 256:
    break

# second convert dat file
in_file = 'in.dat'
out_file = 'out.jpg'

binfile = open(in_file, 'rb')
a = binfile.read()
binfile.close()
hex_in = binascii.b2a_hex(a)

out_ret = ''
for i in range(len(hex_in)/2):
  hex_t = hex_in[2*i:2*(i+1)]
  int_t = int(hex_t,16)
  int_ret = rule[int_t] 
  if int_ret>15:
    hex_ret = hex(int_ret)[2:]
  else:
    hex_ret = '0' + hex(int_ret)[2:]
  out_ret += hex_ret
hex_file = out_ret.decode('hex')

binfile = open(out_file, 'wb')
binfile.write(hex_file)
binfile.close()