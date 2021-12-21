# 逆暗号
# 文字列を逆順に並べ替える
message = 'Three can keep a secret, if two of them are dead.'
translated = '' 

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)

