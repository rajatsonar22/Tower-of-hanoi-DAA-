# TOWER OF HANOI
print(">>>TOWER OF HANOI")
print("")#...space
print("--- MOVING DISKS...")

def tower_of_hanoi(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1 , source , aux, target)
    print(f"Move disk {n} form {source} to {target}")
    tower_of_hanoi(n - 1, aux , target, source)

if __name__ == "__main__":
    num_disks = 3
    tower_of_hanoi(num_disks, 'A', 'C', 'B')
