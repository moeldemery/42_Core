#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    catalog: dict[str, dict[str, str | int]] = {
        'pixel_sword': {'type': 'weapon', 'value': 150},
        'quantum_ring': {'type': 'accessory', 'value': 500},
        'health_byte': {'type': 'consumable', 'value': 25},
        'data_crystal': {'type': 'material', 'value': 1000},
        'code_bow': {'type': 'weapon', 'value': 200}
    }
    inventory: dict[str, dict[str, str | int]] = dict()
    total_items_count: int = 0
    unique_items_count: int = 0
    total_gold_value: int = 0

    if len(sys.argv) <= 1:
        print("No Items provided!")
    else:
        i: int = 1
        while i < len(sys.argv):
            arg = sys.argv[i]
            parts = arg.split(":")
            try:
                if len(parts) < 2:
                    raise IndexError("Missing quantity (use item:qty)")
                item_name: str = parts[0]
                item_qty: int = int(parts[1])
                item_info = catalog.get(item_name,
                                        {'type': 'unknown', 'value': 0})
                item_value = int(item_info.get('value', 0))
                inventory.update({
                    item_name: {
                        "type": item_info.get('type', "Unknown"),
                        "quantity": item_qty,
                        "value": item_qty * item_value
                    }
                })
                total_items_count += item_qty
                total_gold_value += (item_qty * item_value)
            except IndexError as e:
                print(f"Input Error for '{arg}': {e}")
            except ValueError:
                print(f"Input Error for '{arg}': Quantity must be an integer.")
            except Exception as e:
                print(f"Unexpected error with '{arg}': {type(e).__name__}")

            i += 1

        print("\n=== Inventory System Analysis ===")
        print(f"Total items in inventory: {total_items_count}")
        unique_items_count = len(inventory.keys())
        print(f"Unique item types: {unique_items_count}")
        print(f"Total gold value: {total_gold_value}")

        print("\n=== Current Inventory ===")
        most_abundant_qty: int = -1
        most_abundant_name: str = ""
        least_abundant_qty: int = -1
        least_abundant_name: str = ""
        is_first: bool = True

        for item, details in inventory.items():
            qty: int = int(details.get("quantity", 0))
            val: int = int(details.get("value", 0))

            percentage: float = (qty / total_items_count) * 100
            print(f"{item}: {qty} units ({percentage:.1f}%)")
            if is_first:
                most_abundant_name = item
                most_abundant_qty = qty
                least_abundant_name = item
                least_abundant_qty = qty
                is_first = False
            else:
                if qty > most_abundant_qty:
                    most_abundant_qty = qty
                    most_abundant_name = item
                if qty < least_abundant_qty:
                    least_abundant_qty = qty
                    least_abundant_name = item

        print("=== Inventory Statistics ===")
        print(f"Most abundant: {most_abundant_name}"
              f" ({most_abundant_qty} units)")
        print(f"Least abundant: {least_abundant_name}"
              f" ({least_abundant_qty} units)")

        categories: dict[str, dict[str, int]] = dict()
        categories.update({"Moderate": dict(), "Scarce": dict()})

        for name, data in inventory.items():
            q: int = int(data.get("quantity", 0))
            if q >= 5:
                categories["Moderate"].update({name: q})
            else:
                categories["Scarce"].update({name: q})

        print("=== Item Categories ===")
        print(f"Moderate: {categories.get('Moderate')}")
        print(f"Scarce: {categories.get('Scarce')}")

        restock_list = []
        for name, data in inventory.items():
            qt: int = int(data.get("quantity", 0))
            if qt == least_abundant_qty:
                restock_list.append(name)

        print("\n=== Management Suggestions ===")
        print(f"Restock needed: {restock_list}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(inventory.keys())}")
        quantities_only: list[int] = []
        for details in inventory.values():
            qtt: int = int(details["quantity"])
            quantities_only.append(qtt)
        print(f"Dictionary values: {quantities_only}")
        print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
