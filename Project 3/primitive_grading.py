starter = 1

gate_a = 0
gate_b = 0
gate_c1 = 0
gate_c2 = 0
reject = 0


while starter > 0:
    if gate_a >= 30 and gate_b >= 40 and gate_c1 >= 50 and gate_c2 >= 50:

        print("All orders completed!")
        break
    else:
        fish_wheight = (input("Enter piece weight: "))

        if fish_wheight == "q":
            break

        f_w = int(fish_wheight)

        if f_w <= 3 and gate_a < 30:
            gate_a += f_w
            print(f'Piece weight: {fish_wheight}kg. -> Gate A')

        elif f_w > 3 and f_w <= 8 and gate_b < 40:
            gate_b += f_w
            print(f'Piece weight: {fish_wheight}kg. -> Gate B')

        elif f_w > 8 and f_w <= 15:
            if gate_c1 < 50:
                gate_c1 += f_w
                print(f'Piece weight: {fish_wheight}kg. -> Gate C1')
            else:
                if gate_c2 < 50:
                    gate_c2 += f_w
                    print(f'Piece weight: {fish_wheight}kg. -> Gate C2')
                else:
                    print(f'Piece weight: {f_w}kg. -> Reject!')
                    reject += f_w


        elif fish_wheight == "q":
            break


        else:
            print(f'Piece weight: {f_w}kg. -> Reject!')
            reject += f_w





print("-- Run results --")
print(f'Gate A: {gate_a} kg.')
print(f'Gate B: {gate_b} kg.')
print(f'Gate C1: {gate_c1} kg.')
print(f'Gate C2: {gate_c2} kg.')
print(f'Reject: {reject} kg. ')