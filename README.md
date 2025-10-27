# SE_LAB_5
# Inventory System - Exception and Safety Fixes

This Python inventory management script has been updated to prevent exceptions and unsafe behavior.

## Key Fixes

- **Mutable default arguments:** 
  Replaced `logs=[]` with `logs=None` and initialized inside functions.

- **Type safety:** 
  Added `isinstance` checks for item names and quantities in `addItem` and `removeItem`.

- **KeyError prevention:** 
  Used `dict.get()` in `getQty()` and added explicit checks for missing items in `removeItem`.

- **File handling:** 
  Replaced raw `open()` calls with `with open()` context manager and added exception handling for missing or corrupt JSON files.

- **Removed unsafe eval():** 
  Replaced `eval()` with safe `print()` statements.

- **Logging improvements:** 
  Optional logging in functions to track changes safely without crashing.

## Usage

```python
from inventory_system import addItem, removeItem, getQty, saveData, loadData, printData

logs = []
addItem("apple", 10, logs)
removeItem("banana", 2)
print(getQty("apple"))
saveData()
loadData()
printData()
