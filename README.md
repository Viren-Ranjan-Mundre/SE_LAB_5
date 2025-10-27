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


1. **Which issues were the easiest to fix, and which were the hardest?**  
Mutable default arguments and `eval()` were easiest to fix, while blanket `except:` and type errors were harder because they required careful checks and safe handling.

2. **Did the static analysis tools report any false positives? If so, describe one example.**  
Bandit flagged the `except:` block; technically correct, but low risk in this small script.

3. **How would you integrate static analysis tools into your actual software development workflow?**  
Run static analysis locally in the IDE and in CI pipelines (e.g., GitHub Actions) to catch issues before merging.

4. **What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**  
Code is now safer, more robust, readable, and maintainable, with better error handling and no unsafe `eval()`.

