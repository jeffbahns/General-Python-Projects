# Collatz Conjecture


def collatz_conjecture(num):
    seq = [num]
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            seq.append(num)
        else:
            num = num*3 + 1
            seq.append(num)
    steps = len(seq)
    return seq, str(steps) + " steps"

print (collatz_conjecture(13))
