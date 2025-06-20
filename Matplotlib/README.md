# Bakery Sales Visualization

This project visualizes weekly bakery sales using Python's Matplotlib library.

## What is Matplotlib?

**Matplotlib** is a popular Python library for creating static, interactive, and animated visualizations. It is widely used for plotting graphs, charts, and figures in data analysis and scientific research.

## Overview

The script [`first.py`](first.py) generates a line plot showing the number of sales for each day of the week. It demonstrates basic Matplotlib features such as:

- Customizing line color, style, and markers
- Adding titles and axis labels
- Displaying legends and grid lines
- Customizing tick labels

## Requirements

- Python 3.x
- matplotlib
- numpy

Install dependencies with:

```sh
pip install matplotlib numpy
```

## Usage

Run the script to display the sales chart:

```sh
python first.py
```

## Features

- Plots sales data for each day of the week
- Customizes appearance for better visualization
- Shows legend and grid for clarity

## Notes

- The script includes commented code for setting axis limits.
- The legend location is set to `'upper left'` (valid Matplotlib value).
- Custom x-tick labels are used for day abbreviations.

## Example Output

The script displays a line chart similar to:

```
Mo  Tu  We  Th  Fi  St  Sn
 |---|---|---|---|---|---|---|
 0   2   3   5  11   8  10
```

## License

This project is for educational purposes.