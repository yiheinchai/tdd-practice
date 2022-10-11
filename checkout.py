class Checkout:
    def __init__(self) -> None:
        self._items = []

    @property
    def items(self):
        return self._items

    @property
    def total_cost(self):
        cost = 0
        for item in self.items:
            item_cost = item.price * item.qty
            cost += item_cost
        return cost

    @items.setter
    def items(self, new_items):
        self._items = new_items

    def _find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

    def add(self, item):
        itm = self._find_item(item.name)
        if itm:
            itm.qty += 1
        else:
            self.items = [*self.items, item]

    def apply_discount(self):
        for item in self.items:
            if item.qty > 2:
                item.price = 1


class Item:
    def __init__(self, name='Untitled', price=0, qty=1) -> None:
        self._name = name
        self._price = price
        self._qty = qty

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    @property
    def qty(self):
        return self._qty

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @qty.setter
    def qty(self, new_qty):
        self._qty = new_qty
