{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/funeea/CSC-101/blob/main/Edwin_Funez_CSC101Lesson2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# $\\textbf{Strings}$"
      ],
      "metadata": {
        "id": "oAjJtH6CMX_l"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# String Literals\n",
        "\n",
        "In python to represent strings we surround them by either single quotation marks or double quotation marks.\n",
        "\n",
        "'string' is same as \"string\"\n",
        "\n",
        "\n",
        "If you want to display the string literal you can use print() command"
      ],
      "metadata": {
        "id": "wIZroXPoMtq7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Hello\")\n",
        "print('Hello World')"
      ],
      "metadata": {
        "id": "M4Xf-SO2M1If",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bcb290bf-f570-453e-e8cb-707fce9b6a15"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello\n",
            "Hello World\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Multiline Strings\n",
        "You can assign a multiline string to a variable by using three quotes:"
      ],
      "metadata": {
        "id": "Gd3X9064M7qb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Poem: Roses Are Red by Mother Goose\n",
        "\n",
        "\n",
        "poem = \"\"\"The rose is red,\n",
        "The violet's blue,\n",
        "Sugar is sweet,\n",
        "And so are you.\"\"\"\n",
        "print(poem)"
      ],
      "metadata": {
        "id": "7n40q-nNNGXQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f21ee07e-3e01-47b1-a827-cd9859355201"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The rose is red,\n",
            "The violet's blue,\n",
            "Sugar is sweet,\n",
            "And so are you.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "BSI13hmf3WdN"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "SifX2BQH3W27"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "```\n",
        "# This is formatted as code\n",
        "```\n",
        "\n",
        "Or three single quotes:"
      ],
      "metadata": {
        "id": "vnVv2SZANZIf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "poem='''The rose is red,\n",
        "The violet's blue,\n",
        "Sugar is sweet,\n",
        "And so are you.'''\n",
        "print(poem)"
      ],
      "metadata": {
        "id": "R-ijDO50Nanw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "00f662eb-56eb-4841-d443-46a85e324ba3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The rose is red,\n",
            "The violet's blue,\n",
            "Sugar is sweet,\n",
            "And so are you.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# More about strings\n",
        "\n",
        "Using + operator we can link two or more distinct strings. It is called string concatenation\n",
        "\n"
      ],
      "metadata": {
        "id": "flP3ylogNpFG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('a'+'b')\n",
        "print('a'+' '+'b') # a blank space\n",
        "print ('a', ' ', 'b')\n",
        "print ('a', 'b')\n"
      ],
      "metadata": {
        "id": "HyeShTiwOeNu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bdbde166-ed95-4e2d-e995-f4fe92adcdf3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ab\n",
            "a b\n",
            "a   b\n",
            "a b\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Working'+'on'+'this'+'exercise.') #There is no space in between\n",
        "print('Working'+' '+'on'+' '+'this'+' '+'exercise.')"
      ],
      "metadata": {
        "id": "lhhGTJSJOfF5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "948778d2-c37b-4bee-fc1d-5f60f44ce847"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Workingonthisexercise.\n",
            "Working on this exercise.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Exercise\n",
        "\n",
        "Write a code following the directions:\n",
        "\n",
        "- Assign a string \"My favorite food is\" into a variable named X\n",
        "- Assign your favorite meal into a variable named Y\n",
        "- Using string concatenation link X and Y and display it on the screen using print\n",
        "\n",
        "\n",
        "If your favorite meal is fries after you concatenate it will appear as\n",
        "\n",
        "My favorite food is fries.\n"
      ],
      "metadata": {
        "id": "T3Y65najQeLN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Note\n",
        "\n",
        "We can't combine strings and int or float data type with concetanation"
      ],
      "metadata": {
        "id": "EbQS3clnQmfS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#We can't perform arithmetical operations between\n",
        "#strings and integers, or strings and floats (decimal numbers).\n",
        "\n",
        "\n",
        "print('4'+' '+'1')"
      ],
      "metadata": {
        "id": "9PiikAb6Qj66",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "041d85ac-8af6-4c9e-f209-bedded21a421"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Exercise\n",
        "\n",
        "In the given Python script what is the data type of var3?\n",
        "\n",
        "var1=\"4\"\n",
        "\n",
        "var2=\"1\"\n",
        "\n",
        "var3=var1+var2\n",
        "\n",
        "print(var3)"
      ],
      "metadata": {
        "id": "SL4SZRhCQztJ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# $\\textbf{Escape Character in String}$\n",
        "\n",
        "In Python, strings are sequences of characters that represent textual data. They allow us to store and manipulate text, but sometimes, we encounter special characters that have a specific meaning in Python. To represent these special characters within a string, we use escape characters.\n",
        "\n",
        "# Escape Character:\n",
        "\n",
        "An escape character is a backslash (\\) followed by another character that changes the meaning of the following character in a string. It is used to represent characters that are difficult to type or have special significance, such as newlines, tabs, or quotation marks.\n",
        "\n",
        "Common Escape Sequences:\n",
        "\n",
        "    \\n: Represents a newline character. It is used to start a new line in the output.\n",
        "    \\t: Represents a tab character. It is used to create horizontal spacing.\n",
        "    \\\\: Represents a literal backslash. It is used when you need to include an actual backslash in your string.\n",
        "    \\\" or \\': Represents a double quote or a single quote, respectively. It is used to include quotes within a string defined with the same type of quotes."
      ],
      "metadata": {
        "id": "8RSzkynNRBCC"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Newline"
      ],
      "metadata": {
        "id": "lrLjwY6uR3OY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Hello\\nWorld\")"
      ],
      "metadata": {
        "id": "v3_1cP9kRAW6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ee6ccad7-adf1-42c1-bbf9-285d26b49817"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello\n",
            "World\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Tab"
      ],
      "metadata": {
        "id": "w0Km3nP_R7zM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Name:\\tJohn\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XPxq7sr7R9cw",
        "outputId": "6903741a-7051-420e-976b-fef2241bbbbd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name:\tJohn\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Literal Backslash"
      ],
      "metadata": {
        "id": "VWTXwhEnSBK8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"C:\\\\Users\\\\John\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tDoBs7_fSJGY",
        "outputId": "ef062def-6344-418e-9c29-73564e4190f2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "C:\\Users\\John\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Quotation Marks"
      ],
      "metadata": {
        "id": "TLSxYlyfSD38"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"He said, \\\"Hello!\\\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "94epO0XSSNnp",
        "outputId": "a964b137-d3fc-4fdc-8b8e-c2c3408df827"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "He said, \"Hello!\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# $\\textbf{Reading Input From the Keyboard}$\n",
        "\n",
        "- When you are programming usually you will require user to enter an input and program will read the input to perform operations\n",
        "-  The data is read from the keyboard and it is stored in a variable to use later by the program\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "Gt83j7P40Qku"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Get the user's first name\n",
        "first_name= input('Enter your first name:')\n",
        "\n",
        "# Get the user's last name\n",
        "last_name = input ('Enter your last name:')\n",
        "\n",
        "#Print a greeting to the user\n",
        "print('Welcome', first_name, last_name)\n",
        "\n"
      ],
      "metadata": {
        "id": "XOqftgy60UdG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "464f298e-a19e-4489-88dd-574e8769f1f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your first name:Edwin\n",
            "Enter your last name:Funez\n",
            "Welcome Edwin Funez\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Reading Number with the input Function\n",
        "\n",
        "-  The input function always returns the user's input as a string, even if the user enters numeric data\n",
        "-  For example, suppose you call the input function and enter the number 100, and press ENTER key. The value returned from the input is '100'\n",
        "-  If you want to do mathematical operations you can't because your output is a string\n",
        "-  You can use built-in functions to convert a string to a numeric data type\n",
        "-  After you convert a string to numeric data type you can perform arithmetic operations\n"
      ],
      "metadata": {
        "id": "uzlZIbrE0YhG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "number= input(\"What is the number?\")\n",
        "print(type(number))"
      ],
      "metadata": {
        "id": "I1B5eEX20bUu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3d2788e7-ef55-4ea6-ed92-2185b941dc99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What is the number?12\n",
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "int(number)  # value converted to an int\n",
        "float(number) #  value converted to a float"
      ],
      "metadata": {
        "id": "tTHczIxn0cAH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "328f6b07-ed30-486c-9d18-d160573fd36b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12.0"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#First statement gets the number of hours and assign to a value as a string\n",
        "#Second statement calls the int()function, passing string_value as an argument\n",
        "#This is inefficient because it creates two varaiables\n",
        "\n",
        "string_value= input('How many hours did you work?')\n",
        "\n",
        "hours=int(string_value)\n",
        "print(type(hours))"
      ],
      "metadata": {
        "id": "imA6gCZM0fLW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e8879a94-8173-45a7-9300-4b32ca1bccf0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "How many hours did you work?40\n",
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Displaying Formatted Output with F-strings\n",
        "-  F-strings are special type of string literal that allow you to format a variety of ways\n",
        "-  With an f-string, you can create messages that contain the contents of variables, and you can format numbers in a variety of ways\n",
        "-  An f-string is a string literal that is enclosed in quotation marks and prefixed with the letter f"
      ],
      "metadata": {
        "id": "gJTPgpQwTgRq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#f'Hello world'\n",
        "print(f\"Hello world\")\n",
        "print(f'Hello world')"
      ],
      "metadata": {
        "id": "_GgXUJhfTjVN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "96d8bd2c-bc7c-4a12-ab4c-be29a66321d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello world\n",
            "Hello world\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name='Johny'\n",
        "last_name= 'Dean'\n",
        "print(f'Hello {name}') #{name} is a placeholder inside f-string\n",
        "print(f\"Hello {last_name}\")\n",
        "print(f\"Hello {name} {last_name}\")\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "# print(\"Hello \"+name)\n",
        "# print(\"Hello\", name)\n",
        "# print(\"Hello Johny\")"
      ],
      "metadata": {
        "id": "_FAa8IxZTotk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b7460245-d63e-4f3f-bb71-09cbe2c09522"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello Johny\n",
            "Hello Dean\n",
            "Hello Johny Dean\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#With f-string and without f-string\n",
        "\n",
        "age = 20\n",
        "name= \"Mark\"\n",
        "\n",
        "print(f'{name} is currently {age} years old.')\n",
        "\n",
        "print(name, \"is currently\", age, \"years old\")\n"
      ],
      "metadata": {
        "id": "ShkBHASXTrJw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3127961b-685a-4033-ae8d-947697c68d2c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mark is currently 20 years old.\n",
            "Mark is currently 20 years old\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Exercise\n",
        "\n",
        "Ask the user to enter his/her first name, last name and age and using f string display for example My name is Mark Jones and I am 20 years old"
      ],
      "metadata": {
        "id": "xYldfEDOTu5F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Work on it here"
      ],
      "metadata": {
        "id": "Gr54UF4oTzzB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Placeholders can contain any valid expression\n",
        "\n",
        "\n",
        "print(f'The number is {10+2}.')\n",
        "\n",
        "print(f'The number is 10+2.')\n",
        "\n",
        "number=10\n",
        "print(f'The number is {number+2}.')\n",
        "\n"
      ],
      "metadata": {
        "id": "s4wUAQbTT40P",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7308b53f-6562-4985-a960-4180d2c6c14a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The number is 12.\n",
            "The number is 10+2.\n",
            "The number is 12.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Formatting Values\n",
        "## Rounding Floating-Point Numbers\n",
        "-  Sometimes we want to format the decimal display\n",
        "-  17 significant digits appear when float data type is used"
      ],
      "metadata": {
        "id": "J2lw7fTFT8cc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#how a floating-point number is displayed with no formatting\n",
        "\n",
        "water_bill= 7000.0\n",
        "monthly_water_bill = water_bill/12.0\n",
        "print(monthly_water_bill)\n",
        "print(f'The monthly payment is {monthly_water_bill}')"
      ],
      "metadata": {
        "id": "D5kNDPyVT_5f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "18474b3a-b4b8-40fd-b78f-de4934089172"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "583.3333333333334\n",
            "The monthly payment is 583.3333333333334\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "-  In the above examplemonthly payment is representing dollor value. When we are talking about money as you know we can have at most 2 decimal places\n",
        "-  We can format monthly_water_bill value using .2f"
      ],
      "metadata": {
        "id": "YKOxllbXUIRA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Rounding floating-point number\n",
        "\n",
        "water_bill= 7000.0\n",
        "monthly_water_bill = water_bill/12.0\n",
        "\n",
        "print(f'The monthly payment is {monthly_water_bill:.2f}')"
      ],
      "metadata": {
        "id": "HIhcIN8_UDMH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "061d598e-78df-4d86-87c2-3a3476c53575"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The monthly payment is 583.33\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "number=123123.456\n",
        "print(f'Here is my number {number:.1f}')\n",
        "\n"
      ],
      "metadata": {
        "id": "eYndTnuyUPzb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "45674ee5-d6a0-4866-c57d-52697459a48a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Here is my number 123123.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# You can also round it to 1 decimal place\n",
        "\n",
        "a=2\n",
        "b=3\n",
        "\n",
        "print(f'{a/b:.3f}')"
      ],
      "metadata": {
        "id": "kYm1rEp8USsN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ca1d5f33-33d6-4f6f-cd51-16417ced023e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "-  Sometimes it is better to read a number which consists of few digits with comma\n",
        "\n",
        "-  We can format a number to have comma seperator"
      ],
      "metadata": {
        "id": "BCxJ0ivHUV41"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# You can even combine comma seperators and rounding the number\n",
        "\n",
        "value = 123456789.12345\n",
        "print(f'{value:,.3f}')"
      ],
      "metadata": {
        "id": "9Jh11e2uUYuL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "044a0d8a-de1e-44e1-c614-462f937b6ccf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "123,456,789.123\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=10020030045.12345\n",
        "print(f'{x:,.3f}')"
      ],
      "metadata": {
        "id": "Iktzd8RKUawL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "53e26869-b80c-4771-d1f6-55d7e160ff93"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10,020,030,045.123\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Formatting a Floating-Point Number as a Percentage\n",
        "\n",
        "-  % can  be used to format floating numbers as a percentage\n",
        "\n",
        "-  When you use % the number is multiplied by 100"
      ],
      "metadata": {
        "id": "IstqdG7cUgQs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "percent= 0.6\n",
        "\n",
        "print(f'{percent:%}')\n"
      ],
      "metadata": {
        "id": "95ZPk12IUhvm",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fd9a139b-9011-408e-eb82-de363e08dd93"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "60.000000%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Round output value to 0 decimal places\n",
        "percent= 0.6\n",
        "print(f'{percent:.0%}')"
      ],
      "metadata": {
        "id": "6mI9Whu7UmP0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "edbc2e13-7c3a-42d6-97ed-fedb076b6616"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "60%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Work on it Now Together\n",
        "\n",
        "- Assign 971825.12334 to a variable called value_1 and using the print function and f-string display your output as rounded to 3 decimal places\n",
        "\n",
        "- Assign 6734911444 to a variable called value_2 and using the print function and appropriate f-string display your output with comma.\n"
      ],
      "metadata": {
        "id": "RpLD9uX4UpWP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# $\\textbf{Lists}$\n",
        "\n",
        "In Python we represent list with square bracket. List consists of items which can be changed and the list\n",
        "items are ordered."
      ],
      "metadata": {
        "id": "BEVHdy50i2Ym"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Length of a List"
      ],
      "metadata": {
        "id": "pUjHkkI3MchJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Create a list\n",
        "lst1 = ['kiwi', \"banana\", \"orange\"]\n",
        "lst2=[1,2,3,4]\n",
        "\n",
        "#len returns the number of items in the list\n",
        "\n",
        "print(len(lst1))\n",
        "print(len(lst2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PrWAwRRHLE3k",
        "outputId": "848bb4f3-dd8a-4b6e-aca2-0272ae6245f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Concatanate Two Lists"
      ],
      "metadata": {
        "id": "md_cd-IiMW-Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Concatanate two lists\n",
        "\n",
        "lst3=lst1+lst2\n",
        "print(lst3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RXkto2r5L8Wu",
        "outputId": "0c13095d-b59e-4840-a471-c6cce3389dff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['kiwi', 'banana', 'orange', 1, 2, 3, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#The Repitation Operator\n",
        "\n",
        "As you might remember we used to multiply two numbers. We can also use as a repitation operator. When we use * and a list to repeat the items in the list."
      ],
      "metadata": {
        "id": "lzLvwNtmMpw-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numbers=[0]*5\n",
        "print(numbers)\n",
        "\n",
        "lst4 = ['x', 'y'] * 5\n",
        "print(lst4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SExegfP3MyE7",
        "outputId": "14680706-6e00-437c-cdb5-e4e166959b94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 0, 0, 0, 0]\n",
            "['x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Positive indexing, Negative indexing\n",
        "\n",
        "First item: [0] (Note: List first index starts from 0 in python, this is called positive indexing)\n",
        "\n",
        "Last item: [-1] (Note: List index from last starts from -1 in python, this is called negative indexing)"
      ],
      "metadata": {
        "id": "BQuwrpr_NK70"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "list1 = [\"a\", 15, 2.9] #List can contain int, float, string at the same time\n",
        "\n",
        "print(list1)\n",
        "print(list1[0]) # Accessing First item in list1\n",
        "print(list1[1]) # Accessing Second item in list1\n",
        "print(list1[2]) # Accessing Third item in list1\n",
        "print(list1[-1]) # Accessing Last item in list1\n",
        "print(list1[-2]) # Accessing Second Last item in list1\n",
        "print(list1[-3]) # Accessing Third Last item in list1"
      ],
      "metadata": {
        "id": "0ZZG_QAFNiRh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "33f0c1e6-e325-4946-8717-9ae690114fc7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['a', 15, 2.9]\n",
            "a\n",
            "15\n",
            "2.9\n",
            "2.9\n",
            "15\n",
            "a\n"
          ]
        }
      ]
    }
  ]
}