
def main():
    year = get_input()
    animal_year = get_zodiac_animal(year)
    print(year, 'is the year of the', animal_year)

def get_input():
    year = int(input('Enter a year: '))
    return year
    
def get_zodiac_animal(year):
    animal_year = year % 12

    signs = ['monkey', 'rooster', 'dog',
            'pig', 'rat', 'ox', 'tiger',
            'rabbit', 'dragon', 'snake',
            'horse', 'sheep']

    return signs[animal_year]

main()

