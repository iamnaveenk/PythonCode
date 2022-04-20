{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "fibonacci_number_nt.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNloglni9G9E5aaqd6nA5Ee",
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
        "<a href=\"https://colab.research.google.com/github/naveenkumar1805/PythonCode/blob/main/fibonacci_number_nt.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "M6wiKbFQrSsy"
      },
      "outputs": [],
      "source": [
        "#Python Program for n-th Fibonacci number\n",
        "\n",
        "\n",
        "def fibonaci(n):\n",
        "\n",
        "  a=0\n",
        "  b=1\n",
        "\n",
        "  if n<0:\n",
        "    print(\" Incorrect number\")\n",
        "  elif n==0:\n",
        "    return a\n",
        "\n",
        "  elif n==1:\n",
        "    return b\n",
        "\n",
        "  else:\n",
        "    for i in range(2,n):\n",
        "      c= a+b\n",
        "      a=b\n",
        "      b=c\n",
        "    return b\n",
        "\n",
        "\n",
        "x=fibonaci(9)\n",
        "print(x)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#fabonacinusing recursion\n",
        "def fibonaci(n):\n",
        "\n",
        "  if n<=0:\n",
        "    print(\"Number is incorrect\")\n",
        "  elif n==1:\n",
        "    return  0\n",
        "\n",
        "  elif  n==2:\n",
        "    return 1\n",
        "\n",
        "  else:\n",
        "    return fabonaci(n-1)+ fabonaci(n-2)\n",
        "\n",
        "fibonaci(n=int(input(\"enter number\")))"
      ],
      "metadata": {
        "id": "_ZvYO1ODrUOt"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}