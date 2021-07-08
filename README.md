# app

This script allows found the first and last names of some players belongs NBA which and json file whose summed heights in inches are equal to the parameter entered by the console.

Works like a lineal search, but this is optimized because avoid the index previously analized getting better performance, however, the performance could increase if first use the quicksort and after and binary search with neighborhood index checking in every match.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages, if thoses are installed in your system ignore this instructions.

```bash
pip install sys
pip install json
pip install request
```

## Usage

```bash
python app.py your_number
```
The parameter must be positive integer and between 50 and 180

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.