class Hamster:
    def __init__(self,
                length_of_arms = 0.0,
                length_of_legs = 11.0,
                num_eyes = 2,
                has_tail = True,
                is_furry = True,
                ):
        
        self.length_of_arms = length_of_arms
        self.length_of_legs = length_of_legs  # mm
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def print_characteristics(self):
        print(f"The length of this hamster's arms is {self.length_of_arms} mm.")
        print(f"The length of this hamster's legs is {self.length_of_legs} mm.")
        print(f"This hamster has {self.num_eyes} eyes.")

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