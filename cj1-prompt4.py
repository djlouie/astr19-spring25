class Hamster:
    def __init__(self):
        self.length_of_arms = 0.0
        self.length_of_legs = 11.0  # mm
        self.num_eyes = 2
        self.has_tail = True
        self.is_furry = True

    def print_characteristics(self):
        print(f"The length of this hamster's arms is {self.length_of_arms} mm.")
        print(f"The length of this hamster's legs is {self.length_of_legs} mm.")
        print(f"This hamster has {self.length_of_legs} eyes.")

        if self.has_tail:
            print('This hamster has a tail.')
        else:
            print('This hamster doesn\'t have a tail.')

        if self.is_furry:
            print('This hamster is furry.')
        else:
            print('This hamster isn\'t furry.')

def main():
    ham1 = Hamster()
    ham1.print_characteristics()

if __name__ == '__main__':
    main()