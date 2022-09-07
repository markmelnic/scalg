py -m pip install --upgrade build
py -m pip install --upgrade twine

py -m build
py -m twine upload dist/*
