
def twoday():
    f = open("c:/Users/lmg37/Desktop/algorism/day2/puzzle.txt", 'r')
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    answer = 0

    for i in lines:
        puzzle_section = i.split(' ')

        puzzle_section_1 = puzzle_section[0].split('-')

        valid_num = int(puzzle_section_1[0])
        invalid_num = int(puzzle_section_1[1])

        puzzle_section_2 = puzzle_section[1].split(':')[0]

        puzzle_section_3 = puzzle_section[2]

        if puzzle_section_2 == puzzle_section_3[valid_num-1] and puzzle_section_2 != puzzle_section_3[invalid_num-1] :
                answer += 1
    return answer

print(twoday())