Python Multi-Purpose Unit Converter
Project Overview
This project is a command-line utility designed to streamline the process of converting various units of measurement. It was developed to provide a quick, offline solution for common conversion needs without the distraction of web-based tools.
The application uses a straightforward menu system, making it accessible even to users who are not familiar with command-line interfaces. It focuses on precision and ease of use, handling categories ranging from physical dimensions like length and weight to digital measurements like data storage.
Features
The tool currently supports six major conversion categories with specific logic for each:
•	Length: Converts Meters to Feet.
•	Temperature: Converts Fahrenheit to Celsius.
•	Volume: Converts Litres to Millilitres.
•	Weight: Handles conversions between Kilograms, Grams, and Milligrams.
•	Data Storage: Converts Megabytes (MB) to Kilobytes (KB) and KB to Bytes, using the binary standard (1024).
•	Power: Converts Horsepower to Watts.
Key Functional Highlights:
•	Menu-Driven Interface: Users are guided through numbered options, preventing the need to memorize input arguments.
•	Input Validation: The program checks for non-numeric inputs and invalid menu selections to prevent crashes.
•	Clean Output: Results are formatted to remove unnecessary trailing zeros while maintaining calculation precision.
•	Continuous Workflow: You can perform multiple conversions in a row without restarting the script.
Technologies and Tools Used
•	Programming Language: Python 3.x
•	Development Environment: Standard Python IDLE / Text Editor
•	Libraries: Uses Python's standard library (no external dependencies required).
Steps to Run
Follow these steps to get the tool running on your local machine.

Prerequisites
You need to have Python installed on your computer. You can check if it is installed by typing the following command in your terminal or command prompt:
python --version

Running the Application
Just copy and paste the code to your python application or your python ide


Instructions for Testing
Since this is a manual CLI tool, testing involves running the program and inputting known values to verify the mathematical accuracy. Here is a recommended testing procedure:
Test 1: Standard Weight Conversion
1.	Launch the application.
2.	Select "Weight" from the main menu.
3.	Choose "Kilogram" as the primary unit and "Gram" as the secondary unit.
4.	Enter the value "2.5".
5.	Verify that the result displays "2500 grams".
Test 2: Temperature Accuracy
1.	Select "Temperature" from the main menu.
2.	Choose "Fahrenheit" to "Celsius".
3.	Enter "32".
4.	Verify that the result is "0 Celsius" (Freezing point of water).
Test 3: Input Handling
1.	Start any conversion.
2.	When asked for a numeric value, type a word like "test" and press Enter.
3.	The system should display an error message asking for a valid number, rather than crashing.

