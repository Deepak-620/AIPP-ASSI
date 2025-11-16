from typing import Dict, List, Tuple
from collections import defaultdict

class ShoppingCart:
    def __init__(self):
        self.items: Dict[str, Dict[str, float]] = {}
    
    def add_item(self, name: str, price: float) -> bool:
        if not isinstance(name, str) or not name.strip():
            return False
        if not isinstance(price, (int, float)) or price < 0:
            return False
        
        name = name.strip()
        if name in self.items:
            self.items[name]['quantity'] += 1
        else:
            self.items[name] = {'price': price, 'quantity': 1}
        return True
    
    def remove_item(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        
        name = name.strip()
        if name not in self.items:
            return False
        
        if self.items[name]['quantity'] > 1:
            self.items[name]['quantity'] -= 1
        else:
            del self.items[name]
        return True
    
    def total_cost(self) -> float:
        total = 0.0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return round(total, 2)
    
    def get_items(self) -> Dict[str, Dict[str, float]]:
        return self.items.copy()
    
    def clear_cart(self) -> None:
        self.items.clear()
    
    def get_item_count(self) -> int:
        return sum(item['quantity'] for item in self.items.values())

def run_tests():
    test_results = []
    
    print("=" * 90)
    print("SHOPPING CART CLASS TEST SUITE")
    print("=" * 90)
    
    cart = ShoppingCart()
    
    test_cases = [
        ("Add single item", lambda: cart.add_item("Apple", 1.50), True),
        ("Verify item added", lambda: "Apple" in cart.get_items(), True),
        ("Add duplicate item", lambda: cart.add_item("Apple", 1.50), True),
        ("Verify quantity increased", lambda: cart.get_items()["Apple"]["quantity"] == 2, True),
        ("Add different item", lambda: cart.add_item("Banana", 0.75), True),
        ("Add third item", lambda: cart.add_item("Orange", 2.00), True),
        ("Check total with 3 items", lambda: cart.total_cost() == 6.00, True),
        ("Remove existing item", lambda: cart.remove_item("Apple"), True),
        ("Verify quantity after removal", lambda: cart.get_items()["Apple"]["quantity"] == 1, True),
        ("Remove item completely", lambda: cart.remove_item("Apple"), True),
        ("Verify item removed from cart", lambda: "Apple" not in cart.get_items(), True),
        ("Check total after removal", lambda: cart.total_cost() == 2.75, True),
        ("Remove non-existing item", lambda: cart.remove_item("Grape"), False),
        ("Add item with zero price", lambda: cart.add_item("Free Sample", 0.0), True),
        ("Add item with decimal price", lambda: cart.add_item("Mango", 1.99), True),
        ("Verify decimal price total", lambda: cart.total_cost() == 4.74, True),
        ("Add multiple identical items", lambda: all(cart.add_item("Milk", 3.50) for _ in range(3)), True),
        ("Check item count", lambda: cart.get_items()["Milk"]["quantity"] == 3, True),
        ("Clear cart", lambda: (cart.clear_cart(), True)[1], True),
        ("Verify cart is empty", lambda: len(cart.get_items()) == 0, True),
        ("Total cost of empty cart", lambda: cart.total_cost() == 0.0, True),
        ("Add item after clearing", lambda: cart.add_item("Bread", 2.50), True),
        ("Invalid item name - empty string", lambda: cart.add_item("", 5.00), False),
        ("Invalid item name - None", lambda: cart.add_item(None, 5.00), False),
        ("Invalid price - negative", lambda: cart.add_item("Cheese", -1.50), False),
        ("Invalid price - string", lambda: cart.add_item("Butter", "5.00"), False),
        ("Invalid price - None", lambda: cart.add_item("Yogurt", None), False),
        ("Remove from non-existing item", lambda: cart.remove_item("NonExistent"), False),
        ("Remove with invalid type", lambda: cart.remove_item(123), False),
        ("Add item with whitespace", lambda: cart.add_item("  Pasta  ", 1.25), True),
        ("Add expensive item", lambda: cart.add_item("Steak", 25.99), True),
        ("Large quantity of items", lambda: all(cart.add_item("Rice", 2.00) for _ in range(10)), True),
        ("Total with large quantity", lambda: cart.total_cost() > 0, True),
        ("Remove multiple times", lambda: all(cart.remove_item("Rice") for _ in range(5)), True),
        ("Verify partial removal", lambda: cart.get_items()["Rice"]["quantity"] == 5, True),
        ("Add item with float price", lambda: cart.add_item("Coffee", 3.99), True),
        ("Precision in total calculation", lambda: len(str(cart.total_cost()).split('.')[-1]) <= 2, True),
        ("Multiple different items calculation", lambda: (
            cart.clear_cart(),
            cart.add_item("Item1", 10.50),
            cart.add_item("Item2", 20.75),
            cart.add_item("Item3", 5.25),
            cart.total_cost() == 36.50
        )[-1], True),
    ]
    
    for test_name, test_func, expected in test_cases:
        try:
            result = test_func()
            status = "PASS" if result == expected else "FAIL"
            if result == expected:
                test_results.append((test_name, "PASS"))
            else:
                test_results.append((test_name, "FAIL"))
                print(f"[FAIL] {test_name}")
                print(f"    Expected: {expected}, Got: {result}\n")
        except Exception as e:
            status = "ERROR"
            test_results.append((test_name, "ERROR"))
            print(f"[ERROR] {test_name}")
            print(f"    Exception: {str(e)}\n")
    
    passed = sum(1 for _, status in test_results if status == "PASS")
    failed = sum(1 for _, status in test_results if status == "FAIL")
    errors = sum(1 for _, status in test_results if status == "ERROR")
    total = len(test_results)
    
    print("\n" + "=" * 90)
    print(f"Test Results: {passed} passed, {failed} failed, {errors} errors out of {total} total")
    pass_percentage = (passed / total) * 100
    print(f"Pass Rate: {pass_percentage:.1f}%")
    print("=" * 90)
    
    print("\nDetailed Test Summary:")
    for test_name, status in test_results:
        symbol = "✓" if status == "PASS" else "✗" if status == "FAIL" else "!"
        print(f"{symbol} {test_name}: {status}")

if __name__ == "__main__":
    run_tests()
