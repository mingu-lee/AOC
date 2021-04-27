def password_check(input):
    password_count = 0
    with open("c:/Users/lmg37/Desktop/algorism/day2/puzzle.txt") as f:
        for line in f:
            password = line.split(" ", 2)[2]
            letter = line.split(":", 1)[0][-1]
            policy = line.split(" ", 1)[0]
            min_num = int(policy.split("-")[0])
            max_num = int(policy.split("-")[1])

            count = 0
            for character in password:
                if character == letter:
                    count += 1
            
            if count >= min_num and count <= max_num:
                password_count += 1
    
    return password_count

print(password_check("c:/Users/lmg37/Desktop/algorism/day2/puzzle.txt"))

def password_check_part2(input):
    password_count = 0
    with open('c:/Users/lmg37/Desktop/algorism/day2/puzzle.txt') as f:
        for line in f:
            password = line.split(" ", 2)[2]
            letter = line.split(":", 1)[0][-1]
            policy = line.split(" ", 1)[0]
            first_num = int(policy.split("-")[0])
            second_num = int(policy.split("-")[1])

            count = 1
            valid_password = 0
            for character in password:
                if (count == first_num and character == letter) or (count == second_num and character == letter):
                    valid_password += 1
                count += 1
            
            if valid_password == 1:
                password_count += 1
    
    return password_count

print(password_check_part2("c:/Users/lmg37/Desktop/algorism/day2/puzzle.txt"))