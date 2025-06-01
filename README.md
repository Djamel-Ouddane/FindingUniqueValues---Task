
# 🧺 Exclusive Products – CodeSignal Task

Hey! 👋

This little script is a solution to a CodeSignal task where I needed to compare two product inventories and figure out which items are **exclusive** to each one. In other words, I had to find which products are only in one inventory and **not** the other.

### 🧠 How It Works

Here’s the game plan:

1. I convert every item in both inventories to **uppercase** so that the comparison isn’t thrown off by case differences (like `"shirt"` vs `"Shirt"`).
2. Then I turn both lists into sets to:

   * Remove any duplicate items.
   * Use set difference to find what’s in `inventory1` but not `inventory2`, and vice versa.
3. Finally, I sort the results (because it looks nicer) and return them as a tuple of two lists.

### 📦 Example

```python
inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
exclusive_products(inventory1, inventory2)
# ➜ (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])
```

You can throw anything at it, even empty inventories, and it’ll still handle it gracefully. 💪

### ✅ Edge Cases? Covered.

* Inventories with different casing: ✅
* Duplicate items: ✅
* Empty lists: ✅
* Completely identical inventories: ✅

### 🔧 Code

```python
def exclusive_products(inventory1, inventory2):
    inv1 = [item.upper() for item in inventory1]
    inv2 = [item.upper() for item in inventory2]
    unique_items1 = set(inv1) - set(inv2)
    unique_items2 = set(inv2) - set(inv1)
    return (sorted(list(unique_items1)), sorted(list(unique_items2)))
```

That’s it! Simple, clean, and does exactly what it needs to do. 🚀

---

I realise I could have done it using a counter as well.
