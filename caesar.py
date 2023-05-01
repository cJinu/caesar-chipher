def _invert(s, mode):
    if mode == '1' : AscII = ord(s) - 3
    else: AscII = ord(s) + 3
    if AscII < 97: AscII += 26
    if AscII > 122: AscII -= 26
    return chr(AscII)

def caeser(st, mode):
    ans = ''
    st = list(st)
    for s in st:
        ans += _invert(s, mode)
    return ans

if __name__ == '__main__':
    while not (mode := input('0: Decode, 1: Encode, input mode: ')) in ['0','1']:
        mode = input('0: Decode, 1: Encode, please input 0 or 1 :')
    print(chr(caeser(input('input word: '), mode)))
