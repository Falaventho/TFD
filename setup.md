# Setup for testing

Brief guide on workspace setup for test execution

### Steps

- Obtain a copy of the files, either through a git clone or zip file download and extraction.
- Create and set up a virtual environment in the workspace by navigating to the workspace in a terminal and executing the following commands:

```bash
# For Linux, replace 'python' with 'python3'
python -m venv .venv

./.venv/Scripts/activate

pip install -r requirements.txt
```

- Run the tests with the following command:

```bash
pytest
```

### Notes

If pip requirements installation does not work properly, all required modules are currently installed as dependencies when installing pytest like so:

```bash
pip install pytest
```

The investmentcalc.py file is full of mock functions that are not implemented, but are required for pytest to fail properly instead of error.

For reference, all tests are found in test_api.py
