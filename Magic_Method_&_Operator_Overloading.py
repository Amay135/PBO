{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPXfBNmjkkgBhdLvAqRlUTs",
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
        "<a href=\"https://colab.research.google.com/github/Amay135/PBO/blob/main/Magic_Method_%26_Operator_Overloading.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "**1. Magic Method Dasar**"
      ],
      "metadata": {
        "id": "YfxaUUl2P4hp"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "id": "KkyNQS70OtkH",
        "outputId": "cdec84e1-025d-451f-e1d9-a1b91f3c028f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Point(2, 3)\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Point(2, 3)'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 16
        }
      ],
      "source": [
        "class Point:\n",
        "  def __init__(self, x, y):\n",
        "    self.x = x\n",
        "    self.y = y\n",
        "  def __str__(self):\n",
        "    return f\"Point({self.x}, {self.y})\"\n",
        "  def __repr__(self):\n",
        "    return f\"Point({self.x}, {self.y})\"\n",
        "# Tes output\n",
        "p = Point(2, 3)\n",
        "print(p)\n",
        "repr(p)\n",
        "# Output menggunakan __str__\n",
        "# Output menggunakan repг__"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**2. Operator Overloading**"
      ],
      "metadata": {
        "id": "nM3dQnVdQD_y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Vector:\n",
        "    def __init__(self, x, y):\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "    def __add__(self, other):\n",
        "        return Vector(self.x + other.x, self.y + other.y)\n",
        "    def __str__(self):\n",
        "        return f\"Vector({self.x}, {self.y})\"\n",
        "# Tes operator overloading\n",
        "v1 = Vector(1, 2)\n",
        "v2 = Vector(3, 4)\n",
        "print(v1 + v2) # Output: Vector(4, 6)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jGMRaxgmQG8j",
        "outputId": "e6c85e5d-1684-461b-9116-49809eba3c90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Vector(4, 6)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**3. Magic Method Membandingkan Objek**"
      ],
      "metadata": {
        "id": "ei6Bk074QKEZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Person:\n",
        "  def __init__(self, name, age):\n",
        "    self.name = name\n",
        "    self.age = age\n",
        "  def __eq__(self, other):\n",
        "    return self.age == other.age\n",
        "  def __lt__(self, other):\n",
        "    return self.age < other.age\n",
        "# Tes perbandingan\n",
        "p1 = Person(\"Alice\", 25)\n",
        "p2 = Person(\"Bob\", 30)\n",
        "print(p1 == p2) # Output: False\n",
        "print(p1 < p2) # Output: True"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TRjGlGNTQOcB",
        "outputId": "1561e114-d518-4a7a-acfb-bd220515a16e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**4. Magic Method pada Non OOP**"
      ],
      "metadata": {
        "id": "qQjC5dWIQQU3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import operator\n",
        "# Dictionary yang memetakan nama operator dunder ke fungsi operator yang sesuai\n",
        "dunder_comparison_operators = {\n",
        "\"__lt__\": operator.__lt__,\n",
        "\"__le__\": operator.__le__,\n",
        "\"__eq__\": operator.__eq__,\n",
        "\"__ne__\": operator.__ne__,\n",
        "\"__ge__\": operator.__ge__,\n",
        "\"__gt__\": operator.__gt__\n",
        "}\n",
        "# Contoh penggunaan\n",
        "a = 5\n",
        "b = 10\n",
        "# Melakukan perbandingan menggunakan dictionary dengan metode dunder\n",
        "for op_name, op_func in dunder_comparison_operators.items():\n",
        "  result = op_func(a, b)\n",
        "  print(f\"{op_name}({a}, {b}) -> {result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fiexeIm9QT7l",
        "outputId": "bbe7a820-eac3-4825-81da-b02e34657d7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "__lt__(5, 10) -> True\n",
            "__le__(5, 10) -> True\n",
            "__eq__(5, 10) -> False\n",
            "__ne__(5, 10) -> True\n",
            "__ge__(5, 10) -> False\n",
            "__gt__(5, 10) -> False\n"
          ]
        }
      ]
    }
  ]
}