{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM1j1I06JP/yn27Zhaycbgi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/RheedWhan/AltSchool_DataScience_2023/blob/main/Ridwan's_Automation_Project_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# First Semester Project: Automating Accounting Procedures for a Business(Individual Project)"
      ],
      "metadata": {
        "id": "qahZBrNqmHEZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Project Overview"
      ],
      "metadata": {
        "id": "qLMsnEnMnrDY"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "A local retail business, dealing with a variety of products, aims to streamline and automate its accounting procedures. The business operates two shifts per day with one worker on each shift. The primary goal is to create a Python project that assists in automating essential accounting tasks, including calculating total sales, worker salaries, profit, tips, and total tips for the day.\n",
        "\n",
        "\n",
        "**Key Features:**\n",
        "\n",
        "- Calculate Total Sales for the Day: from sales data for morning and evening shifts, produce total sales for the day.\n",
        "- Calculate Worker's Salary: given hourly rate and hours worked by a worker. retrieve the worker's salary.\n",
        "- Calculate Profit: given a list of numbers representing total sales and total cost of items sold, find the profit.(or loss if negative)\n",
        "- Calculate Tips for a Shift: from sales data for a specific shift, workers get tipped for the shift (2% of shift sales).\n",
        "- Calculate Total Tips for the Day: with sales data for morning and evening shifts, return total tips for the day (sum of tips from both shifts).\n",
        "\n",
        "\t*Think of your shift sales as a list.*\n",
        "\n",
        "**User Interface:**\n",
        "\n",
        "- Create a user-friendly interface that displays a menu of available operations.\n",
        "- Accept user input to choose the desired operation (1-5) or exit (6).\n",
        "\n",
        "**Input Handling:**\n",
        "\n",
        "- Prompt the user to enter numbers for each operation.\n",
        "- Ensure that the program handles invalid inputs gracefully (e.g., non-numeric inputs).\n",
        "\n",
        "**Result Display:**\n",
        "\n",
        "- Display the result of the selected operation clearly to the user.\n",
        "\n",
        "**Program Loop:**\n",
        "\n",
        "- Implement a loop that allows the user to perform multiple calculations until choosing to exit.\n",
        "\n",
        "**Project Structure:**\n",
        "\n",
        "- Organize your code into functions to encapsulate specific operations.\n",
        "- Maintain a clear separation between function definitions and the main program.\n",
        "\n",
        "**Error Handling:**\n",
        "\n",
        "- Include error handling for scenarios such as division by zero.\n",
        "\n",
        "**Exiting the Program:**\n",
        "\n",
        "- Provide an option for users to exit the  program."
      ],
      "metadata": {
        "id": "JjA-DH65lvmB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Functions"
      ],
      "metadata": {
        "id": "Yk_N_iDQxCTf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculate Total Sales for the Day: from sales data for morning and evening shifts, produce total sales for the day."
      ],
      "metadata": {
        "id": "O1TYyNImARRj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def total_sales():\n",
        "\n",
        "    \"\"\"\n",
        "    Calculate the total sales by adding the sum of morning sales\n",
        "    and sum evening sales from the given sales data.\n",
        "\n",
        "    Returns:\n",
        "    - float: The total sum of morning sales.\n",
        "    - float: The total sum of evening sales.\n",
        "    - float: The total sum of sales.\n",
        "    \"\"\"\n",
        "\n",
        "    # Keep prompting the user until valid input is provided\n",
        "    while True:\n",
        "        try:\n",
        "            # Get input for morning sales as a comma-separated list\n",
        "            morning_sales = input(\"Enter a list of the morning sales separated by comma: \")\n",
        "            morning_sales_list = [float(sale) for sale in morning_sales.split(',')]\n",
        "            print(\"Calculating sum of morning sales\")\n",
        "            # Initialize the variable to store the sum of morning sales\n",
        "            morning_sales_sum = sum(morning_sales_list)\n",
        "            print(f'Sum of Morning Sales = {morning_sales_sum}')\n",
        "\n",
        "            # Get input for evening sales as a comma-separated list\n",
        "            evening_sales = input(\"\\nEnter a list of the evening sales separated by comma: \")\n",
        "            evening_sales_list = [float(sale) for sale in evening_sales.split(',')]\n",
        "            print(\"Calculating sum of evening sales\")\n",
        "            # Initialize the variable to store the sum of evening sales\n",
        "            evening_sales_sum = sum(evening_sales_list)\n",
        "            print(f'Sum of Evening Sales = {evening_sales_sum}\\n')\n",
        "\n",
        "            # Calculate the total sales by adding morning and evening sales\n",
        "            total_sales = morning_sales_sum + evening_sales_sum\n",
        "\n",
        "            print(f'Total Sales: {total_sales}')\n",
        "            return total_sales\n",
        "            break\n",
        "\n",
        "        except ValueError:\n",
        "            # Handle the case where the user provides invalid input\n",
        "            print('Invalid input. Kindly input numerical values only')"
      ],
      "metadata": {
        "id": "bc0MqxL4jNlc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculate Worker's Salary: given hourly rate and hours worked by a worker. retrieve the worker's salary."
      ],
      "metadata": {
        "id": "sfEm8ckLAOIN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def workers_salary():\n",
        "\n",
        "    \"\"\"\n",
        "    Calculate the worker's salary based on the hourly rate and hours worked provided by the user.\n",
        "\n",
        "    Returns:\n",
        "    - float: The calculated worker's salary.\n",
        "    \"\"\"\n",
        "\n",
        "  # Keep prompting the user until valid input is provided\n",
        "    while True:\n",
        "      try:\n",
        "        # Get input for hourly rate and hours worked\n",
        "        hourly_rate = float(input('Enter the rate per hour: '))\n",
        "        hours_worked = float(input('Enter the number of hours worked: '))\n",
        "\n",
        "        # Check if the user input a negative value\n",
        "        if hourly_rate < 0:\n",
        "          print('Hourly Rate can not be negative. Kindly input a positive value')\n",
        "        elif hours_worked < 0:\n",
        "          print('Hours Worked can not be negative. Kindly input a positive value')\n",
        "        else:\n",
        "          workers_salary = hourly_rate * hours_worked\n",
        "          print(f\"Worker's Salary is {workers_salary}\")\n",
        "          break # Break the loop\n",
        "\n",
        "      except ValueError:\n",
        "        # Handle the case where the user provides invalid input\n",
        "        print('Invalid input. Kindly input numerical values only')"
      ],
      "metadata": {
        "id": "yuFT99B0mOw1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculate Profit: given a list of numbers representing total sales and total cost of items sold, find the profit.(or loss if negative)"
      ],
      "metadata": {
        "id": "g4UhuHrAVZXG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def profit_or_loss():\n",
        "\n",
        "    \"\"\"\n",
        "    Calculate the profit or loss base on the\n",
        "    user-input sales and total cost of items.\n",
        "\n",
        "    Returns:\n",
        "    - float: The total sum of sales.\n",
        "    - float: The total cost of items\n",
        "    - float: The profit or loss of items.\n",
        "    - float: The profit or loss percentage.\n",
        "    \"\"\"\n",
        "\n",
        "    # Keep prompting the user until valid input is provided\n",
        "    while True:\n",
        "        try:\n",
        "            # Get input for sales as a comma-separated list\n",
        "            tot_sales = input(\"Enter a list of the sales separated by comma: \")\n",
        "            tot_sales_list = [float(sale) for sale in tot_sales.split(',')]\n",
        "            print(\"Calculating sum of total sales\")\n",
        "            # Initialize the variable to store the sum of sales\n",
        "            tot_sales_sum = sum(tot_sales_list)\n",
        "            print(f'Sum of total Sales = {tot_sales_sum}')\n",
        "\n",
        "            while True:\n",
        "              try:\n",
        "                # Get input for total cost of items\n",
        "                costs = input(\"\\nEnter the total cost of items / list of the cost seperated by comma: \")\n",
        "                total_cost = [float(cost) for cost in costs.split(',')]\n",
        "                # Initialize the variable to store the sum of sales\n",
        "                total_cost_sum = sum(total_cost)\n",
        "\n",
        "                # Calculate the profit or loss by subtracting total sales from total cost\n",
        "                profit_or_loss = tot_sales_sum - total_cost_sum\n",
        "                percent_of_profit_or_loss = round(((tot_sales_sum / total_cost_sum) * 100), 2)\n",
        "                break\n",
        "              except ZeroDivisionError:\n",
        "                print('Kindly input a non-zero value')\n",
        "\n",
        "            if profit_or_loss < 0 and percent_of_profit_or_loss < 100:\n",
        "              print(f'You made a loss of {profit_or_loss}.\\nThat is {percent_of_profit_or_loss - 100}% loss')\n",
        "            else:\n",
        "              print(f'You made a profit of {profit_or_loss}.\\nThat is {percent_of_profit_or_loss - 100}% profit')\n",
        "            break\n",
        "\n",
        "        except ValueError:\n",
        "            # Handle the case where the user provides invalid input\n",
        "            print('Invalid input. Kindly input numerical values only')"
      ],
      "metadata": {
        "id": "gYViBCLSTWIE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculate Tips for a Shift: from sales data for a specific shift, workers get tipped for the shift (2% of shift sales)."
      ],
      "metadata": {
        "id": "-DSX9lodA_av"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def tips_for_a_shift():\n",
        "\n",
        "    \"\"\"\n",
        "    Calculate the tip for a shift based on user-input sales.\n",
        "\n",
        "    Returns:\n",
        "    - float: The total sum of sales.\n",
        "    - float: The calculated tip for the shift.\n",
        "    \"\"\"\n",
        "\n",
        "    # Keep prompting the user until valid input is provided\n",
        "    while True:\n",
        "        try:\n",
        "            # Get input for sales as a comma-separated list\n",
        "            sales = input(\"Enter a list of the sales separated by comma: \")\n",
        "            sales_list = [float(sale) for sale in sales.split(',')]\n",
        "            print(\"Calculating sum of sales\")\n",
        "            # Initialize the variable to store the sum of sales\n",
        "            sales_sum = sum(sales_list)\n",
        "            print(f'Sum of Sales = {sales_sum}')\n",
        "\n",
        "            # Calculate the tip by multiplying sum of sales 0.02\n",
        "            tip = sales_sum * 0.02\n",
        "            print(f'Tip for the shift is {tip}')\n",
        "            break\n",
        "\n",
        "        except ValueError:\n",
        "            # Handle the case where the user provides invalid input\n",
        "            print('Invalid input. Kindly input numerical values only')"
      ],
      "metadata": {
        "id": "l6oDL3X_TWAj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculate Total Tips for the Day: with sales data for morning and evening shifts, return total tips for the day (sum of tips from both shifts)."
      ],
      "metadata": {
        "id": "c2VMIl4GGrFH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def total_tips():\n",
        "\n",
        "    \"\"\"\n",
        "    Calculate the total tips for both morning and evening shifts based on user-input sales.\n",
        "\n",
        "    Raises:\n",
        "    - ValueError: If the user provides invalid input.\n",
        "\n",
        "    Returns:\n",
        "    - None: Prints the total tips for both shifts.\n",
        "    \"\"\"\n",
        "\n",
        "    try:\n",
        "        # Get input for sales as a comma-separated list\n",
        "        total_sales_result = total_sales()\n",
        "\n",
        "        # Calculate the tip by multiplying sum of sales 0.02\n",
        "        tip = round((total_sales_result * 0.02), 2)\n",
        "        print(f'Total tips for both morning and evening shift: {tip}')\n",
        "\n",
        "    except ValueError:\n",
        "        # Handle the case where the user provides invalid input\n",
        "        print('Invalid input. Kindly input numerical values only')"
      ],
      "metadata": {
        "id": "HRxfd_F9Gu4e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# to call all other functions\n",
        "def menu():\n",
        "    while True:\n",
        "        print('\\nAutomation')\n",
        "        print('1. Total Sales')\n",
        "        print('2. Workers Salary')\n",
        "        print('3. Profit or Loss')\n",
        "        print('4. Tips for a Shift')\n",
        "        print('5. Total Tips')\n",
        "        print('6. Exit')\n",
        "\n",
        "        choice = input('Enter your choice (1-6): ')\n",
        "        if choice == '1':\n",
        "            total_sales()\n",
        "        elif choice == '2':\n",
        "            workers_salary()\n",
        "        elif choice == '3':\n",
        "            profit_or_loss()\n",
        "        elif choice == '4':\n",
        "            tips_for_a_shift()\n",
        "        elif choice == '5':\n",
        "            total_tips()\n",
        "        elif choice == '6':\n",
        "            break\n",
        "        else:\n",
        "            print('Invalid choice. please enter a number between 1 and 6.')"
      ],
      "metadata": {
        "id": "kKwKxfjpS9TY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Alternative Function for Total Sales"
      ],
      "metadata": {
        "id": "8hXAtU-8lq5I"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "'''\n",
        "\n",
        "def total_sales():\n",
        "  \"\"\"\n",
        "    Calculate the total sales by adding the sum of morning sales\n",
        "    and sum evening sales from the given sales data.\n",
        "\n",
        "    Returns:\n",
        "    - float: The total sum of morning sales.\n",
        "    - float: The total sum of evening sales.\n",
        "    - float: The total sum of sales.\n",
        "  \"\"\"\n",
        "  while True: # Keep prompting the user until valid input is provided\n",
        "    try:\n",
        "      # Get input for morning sales\n",
        "      morning_sales = input(\"Enter a list of the morning sales separated by comma: \")\n",
        "      morning_sales_list = morning_sales.split(',') # Convert the input string into a list of floats\n",
        "      print(\"Calculating sum of morning sales\")\n",
        "\n",
        "      morning_sales_sum = 0\n",
        "      for sale in morning_sales_list:\n",
        "        morning_sales_sum += float (sale)\n",
        "      print(f'Sum of Morning Sales = {morning_sales_sum}')\n",
        "\n",
        "      evening_sales = input(\"\\nEnter a list of the evening sales separated by comma: \")\n",
        "      evening_sales_list = evening_sales.split(',')\n",
        "      print(\"Calculating sum of evening sales\")\n",
        "      evening_sales_sum = 0\n",
        "      for sale in evening_sales_list:\n",
        "        evening_sales_sum += float (sale)\n",
        "      print(f'Sum of Evening Sales = {evening_sales_sum}')\n",
        "\n",
        "      total_sales = morning_sales_sum + evening_sales_sum\n",
        "      print(f'\\nTotal Sales: {total_sales}')\n",
        "      break\n",
        "\n",
        "    except ValueError:\n",
        "      print('Invalid input. Kindly input numerical values only')\n",
        "\n",
        "      '''"
      ],
      "metadata": {
        "id": "6pY01aGVoNrl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "963ff436-9016-4795-887a-733e93f2c3a0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'\\n\\ndef total_sales():\\n  \"\"\"\\n    Calculate the total sales by adding the sum of morning sales\\n    and sum evening sales from the given sales data.\\n\\n    Returns:\\n    - float: The total sum of morning sales.\\n    - float: The total sum of evening sales.\\n    - float: The total sum of sales.\\n  \"\"\"\\n  while True: # Keep prompting the user until valid input is provided\\n    try:\\n      # Get input for morning sales\\n      morning_sales = input(\"Enter a list of the morning sales separated by comma: \")\\n      morning_sales_list = morning_sales.split(\\',\\') # Convert the input string into a list of floats\\n      print(\"Calculating sum of morning sales\")\\n\\n      morning_sales_sum = 0\\n      for sale in morning_sales_list:\\n        morning_sales_sum += float (sale)\\n      print(f\\'Sum of Morning Sales = {morning_sales_sum}\\')\\n\\n      evening_sales = input(\"\\nEnter a list of the evening sales separated by comma: \")\\n      evening_sales_list = evening_sales.split(\\',\\')\\n      print(\"Calculating sum of evening sales\")\\n      evening_sales_sum = 0\\n      for sale in evening_sales_list:\\n        evening_sales_sum += float (sale)\\n      print(f\\'Sum of Evening Sales = {evening_sales_sum}\\')\\n\\n      total_sales = morning_sales_sum + evening_sales_sum\\n      print(f\\'\\nTotal Sales: {total_sales}\\')\\n      break\\n\\n    except ValueError:\\n      print(\\'Invalid input. Kindly input numerical values only\\')\\n\\n      '"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    }
  ]
}