pwd_dict = {
    "gmail": "fkdqjhryhu",  # 此字典值为加密后的密文
    "campus": "fdpsxv456",  # mnopqrst
    "163email": "klssrsrwdpxv",
    "taobao": "uklqrfhurv",
    "mobilephone": "prelohccb6",  # 密码明文为：mobile9983
    "soft": "mAxihvriw"
}
# 定义字符源顺序和位移秘钥
char_source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
shift_key = 3

# 定义解密单个密码的函数
def decrypt_password(ciphertext):
    plaintext = ""
    for char in ciphertext:
        index = (char_source.index(char) - shift_key) % len(char_source)
        plaintext += char_source[index]
    return plaintext


# 循环遍历字典并解密每个密码
for key, value in pwd_dict.items():
    plaintext_password = decrypt_password(value)
    print(f"{key}: {plaintext_password}")

