output = [i for i in range(1,100)if '{:b}'.format(i).count('0') == 1]

for i in output:
    print(f'{i} : {'{:b}'.format(i)}')

print(sum(output))
