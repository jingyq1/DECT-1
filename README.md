# Foobar

Use DD-Net to reconstruct CT images with higher quality, and classify CT images for COVID-19 positive or negative.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
conda install numpy
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
conda install scikit-image
conda install -c anaconda pillow
pip install scikit-image
pip install pathlib
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
