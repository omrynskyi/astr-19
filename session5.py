import math

def sin():
    num_entries = 1000
    
    for i in range(num_entries):
        x = 2 * math.pi * i / num_entries 
        sine_value = math.sin(x)
        print(f"{x/math.pi:.4f} pi\t sin:{sine_value:.4f}")

def main():
    sin()

if __name__ == "__main__":
    main()