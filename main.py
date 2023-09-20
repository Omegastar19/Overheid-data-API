import cbsodata
import pandas as pd


def filter_data(selected_gender, selected_age):
    # Obtain data from API
    gedetineerden = pd.DataFrame(cbsodata.get_data('82321NED'))

    # Specify which data will be used
    gedetineerden = gedetineerden[['Geslacht', 'Leeftijd', 'Perioden', 'Migratieachtergrond', 'TotaalGedetineerden_1']]

    # Map user's choices to gender and age options
    gender_options = {
        '1': 'Totaal mannen en vrouwen',
        '2': 'Mannen',
        '3': 'Vrouwen',
        '4': 'Geslacht onbekend',
    }
    age_options = {
        '1': 'Totaal',
        '2': '18 tot 25 jaar',
        '3': '25 tot 45 jaar',
        '4': '45 tot 65 jaar',
        '5': '65 jaar of ouder',
        '6': 'Overige leeftijden',
    }

    selected_gender = gender_options.get(selected_gender)
    selected_age = age_options.get(selected_age)

    # Filter the data based on the user's choices
    filtered_gedetineerden = gedetineerden[
        (gedetineerden['Geslacht'] == selected_gender) &
        (gedetineerden['Leeftijd'] == selected_age) &
        (gedetineerden['Migratieachtergrond'] == 'Totaal') &
        (gedetineerden['Perioden'].astype(int).between(2005, 2022))
        ]

    # Select only the columns you want to display
    filtered_gedetineerden = filtered_gedetineerden[['Perioden', 'TotaalGedetineerden_1']]

    # Rename columns
    filtered_gedetineerden = filtered_gedetineerden.rename(
        columns={'Perioden': 'Jaren', 'TotaalGedetineerden_1': 'Aantal gedetineerden'})

    # Display the options that the user selected
    print(f"Het aantal gedetineerde {selected_gender} tussen de leeftijden van {selected_age}")

    # Display the filtered Data without row numbers
    print(filtered_gedetineerden.to_string(index=False))

    # Save the filtered data to a CSV file including 'Geslacht' and 'Leeftijd' columns
    filtered_gedetineerden.to_csv('filtered_data.csv', index=False)

# Main loop
while True:
    # Let user select the gender
    print("Select a gender:")
    print("1. Totaal mannen en vrouwen")
    print("2. Mannen")
    print("3. Vrouwen")
    print("4. Geslacht onbekend")

    user_gender_choice = input("Enter the number of your gender choice: ")

    if user_gender_choice not in ['1', '2', '3', '4']:
        print("Invalid gender choice. Please select a valid option.")
        continue

    # Let the user select the age group
    print("Select an age group:")
    print("1. Totaal")
    print("2. 18 tot 25 jaar")
    print("3. 25 tot 45 jaar")
    print("4. 45 tot 65 jaar")
    print("5. 65 jaar of ouder")
    print("6. Overige leeftijden")

    user_age_choice = input("Enter the number of your age choice: ")

    if user_age_choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid age choice. Please select a valid option.")
        continue

    # Input the user's choices and display the result
    filter_data(user_gender_choice, user_age_choice)

    # Ask user if they want to run the program again
    repeat = input("Do you want to repeat the program? (yes/no): ").lower()
    if repeat != 'yes':
        break