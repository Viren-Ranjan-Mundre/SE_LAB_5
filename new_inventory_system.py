import json
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    # simple type safety
    if not isinstance(item, str) or not isinstance(qty, int):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    if logs is not None:
        logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

def removeItem(item, qty):
    if not isinstance(item, str) or not isinstance(qty, int):
        return
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # handle missing item explicitly
        print(f"Warning: Tried to remove '{item}', but it's not in stock.")
    except Exception as e:
        # catch unexpected errors but don’t silently ignore them
        print(f"Error removing item '{item}': {e}")

def getQty(item):
    # prevent KeyError
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"File '{file}' not found, starting with empty stock.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error decoding '{file}', starting with empty stock.")
        stock_data = {}

def saveData(file="inventory.json"):
    with open(file, "w") as f:
        f.write(json.dumps(stock_data))

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    logs = []
    addItem("apple", 10, logs)
    addItem("banana", -2, logs)
    addItem(123, "ten", logs)  # invalid types → safely ignored
    removeItem("apple", 3)
    removeItem("orange", 1)     # handled gracefully
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    print("Program finished safely.")

if __name__ == "__main__":
    main()
