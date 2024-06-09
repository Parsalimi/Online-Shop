def filter_and_sort_by_price(items_list, min_price: float = None, max_price: float = None, ascending: bool = True):
    # Apply filtering
    if min_price is not None:
        items_list = [item for item in items_list if item['price'] >= min_price]
    if max_price is not None:
        items_list = [item for item in items_list if item['price'] <= max_price]
    
    # Sort the items based on price
    items_list.sort(key=lambda x: x['price'], reverse=not ascending)
    
    return items_list

# Example usage
items_list = [
    {'item_id': 1, 'name': 'iPhone 13', 'price': 999.9, 'count': '2', 'category_id': 'Phones', 'detail': '-', 'is_item_deleted': 0},
    {'item_id': 2, 'name': 'iPhone 12', 'price': 700, 'count': '2', 'category_id': 'Phone', 'detail': '', 'is_item_deleted': 0},
    {'item_id': 3, 'name': 'iPhone 11', 'price': 1000, 'count': '2', 'category_id': 'Phone', 'detail': '', 'is_item_deleted': 0}
]

filtered_sorted_items = filter_and_sort_by_price(items_list, min_price=700, ascending=False)
print(filtered_sorted_items)