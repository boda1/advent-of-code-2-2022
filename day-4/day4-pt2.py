no_groups_overlapping = 0

with open('input.txt') as f:
    for line in f.read().split('\n'):
        char00 = int(line.split(',')[0].split('-')[0])
        char01 = int(line.split(',')[0].split('-')[1])
        char10 = int(line.split(',')[1].split('-')[0])
        char11 = int(line.split(',')[1].split('-')[1])

        if char10 <= char00 <= char11 or char10 <= char01 <= char11 or char00 <= char10 <= char01 or char00 <= char11 <= char01:
            no_groups_overlapping += 1

        print(line, char00, char01, char10, char11, no_groups_overlapping)


print(no_groups_overlapping)