# SE_LAB_5
# Inventory System - Exception and Safety Fixes

This Python inventory management script has been updated to prevent exceptions and unsafe behavior.

## Changes Summary

| Issue Type | Line(s) | Description | Fix Approach |
|------------|---------|-------------|--------------|
| Mutable default arg | 7 | `logs=[]` shared across calls | Change default to `None` and initialize inside the function |
| Type Safety | 9-12 | `addItem(123, "ten")` could crash on invalid types | Added `isinstance` checks for `item` (str) and `qty` (int) |
| KeyError in removeItem | 17 | Blanket `except:` hides errors | Replaced with `try/except KeyError` and explicit warning for missing items |
| KeyError in getQty | 26 | Direct access `stock_data[item]` could raise KeyError | Used `stock_data.get(item, 0)` to return 0 if missing |
| File Handling in loadData | 30-36 | File missing or JSON invalid could crash | Added `try/except FileNotFoundError, JSONDecodeError` with fallback to empty stock |
| File Handling in saveData | 38-40 | File could remain open on error | Used `with open()` for automatic file closing |
| Unsafe eval() | 62 | `eval("print('eval used')")` executes arbitrary code | Removed `eval()` and replaced with safe `print()` |

## Notes

- These changes **fix exceptions and unsafe behavior** without changing the main program logic.  
<<<<<<< HEAD
- Optional logging or reporting can be added later for production-quality debugging.
=======
- Optional logging or reporting can be added later for production-quality debugging.
>>>>>>> 72bd68c679b50ac9e0a5ac86d3b0678488dc4ca5
