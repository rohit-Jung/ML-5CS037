"""
This module contains exercises of basic concepts of python

Lamda functions are used to define functions in a single line 
"""

import matplotlib.pyplot as plt
from dataset import temperatures


def classify_temperature(temp_list: list[int]) -> dict:
    """
    Classify a list of temperatures into three categories: cold, mild, and comfortable.

    Parameters:
    temperature (list[int]): A list of temperature values.

    Returns:
    dict:
        A dictionary with keys 'cold', 'mild', and 'comfortable', 
        each containing a list of temperatures.
    """
    cold = list(filter(lambda x: x < 10, temp_list))
    mild = list(filter(lambda x: 10 <= x <= 15, temp_list))
    comfortable = list(filter(lambda x: 15 <= x <= 20, temp_list))
    return {
        'cold': cold,
        'mild': mild,
        'comfortable': comfortable
    }

def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    temp =  (celsius * 9 / 5) + 32
    return round(temp, 2)
    
def analyze_temperature_opatterns_by_time_of_day(temp_list: list[int]) -> None:
    """
    Analyze temperature patterns by time of day.

    Parameters:
    temp_list (list[int]): A list of temperature values.
    """
    night = list(filter(lambda x: 0 < x <= 8, temp_list))
    evening = list(filter(lambda x: 8 < x <= 16, temp_list))
    day = list(filter(lambda x: 16 < x <= 24, temp_list))

    print("Night time temperatures", night)
    print("Evening time temperatures", evening)
    print("Day time temperatures", day)
    print("\n")
    average_day_temp = sum(day) / len(day)
    print("Average day time temperature", average_day_temp)
    
    # Update the plot with title and labels
    plt.bar(range(len(day)), day)
    plt.title("Day vs Temperature")  
    plt.xlabel("Time of Day")        
    plt.ylabel("Temperature")          
    plt.show() 

def main():
    """
    Main function to execute the temperature classification process.
    """
    classifed = classify_temperature(temperatures)

    #Task 1. Classify Temperatures:
    print("Cold temperatures", classifed['cold'])
    print("Mild temperatures", classifed['mild'])
    print("Comfortable temperatures", classifed['comfortable'])
    print("\n")
    #Task 2. Based on Data - Answer all the Questions:
    print("Times it was mild", len(classifed['mild']))
    print("Times it was cold", len(classifed['cold']))
    print("Times it was comfortable", len(classifed['comfortable']))
    print("\n")
    #Task 3. Convert Temperatures from Celsius to Fahrenheit
    print("Temperature to farhenheit", list(map(convert_celsius_to_fahrenheit, temperatures)))
    print("\n")
    #Task 4. Analyze Temperature Patterns by Time of Day:
    analyze_temperature_opatterns_by_time_of_day(temperatures)


if __name__ == '__main__':
    main()
