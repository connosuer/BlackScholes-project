# Black-Scholes Calculator

## Overview

This project is a Black-Scholes Calculator application with a graphical user interface (GUI) built using Python and Tkinter. It provides a user-friendly way to calculate various option pricing metrics using the Black-Scholes model.

## Features

- Calculate call and put option prices
- Compute option Greeks: Delta, Gamma, Vega, Theta, and Rho
- User-friendly GUI with input fields for all necessary parameters
- Dark-themed interface for better visibility
- Displays results in a formatted text area

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- NumPy
- SciPy

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required packages:

   ```
   pip install numpy scipy
   ```

3. Clone this repository or download the source code.

## Usage

1. Run the `BSCalculatorApp.py` script:

   ```
   python BSCalculatorApp.py
   ```

2. Enter the following parameters in the GUI:
   - Spot Price
   - Strike Price
   - Risk-free Rate
   - Days to Expiration
   - Volatility
   - Contract Multiplier

3. Click the "Calculate" button to compute the option prices and Greeks.

4. The results will be displayed in the text area below the input fields.

## Structure

The project consists of two main classes:

1. `BSCalculatorApp`: Implements the GUI using Tkinter.
2. `BS`: Contains the Black-Scholes model calculations.

## Customization

You can modify the default values in the `BSCalculatorApp` class to suit your needs. Look for the `default_values` dictionary in the `create_widgets` method.
