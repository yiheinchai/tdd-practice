class Checkout:
    def __init__(self) -> None:
        self._items = []
        self._discount_rules = []

    @property
    def items(self):
        return self._items

    @property
    def discount_rules(self):
        return self._discount_rules

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

    @discount_rules.setter
    def discount_rules(self, new_rules):
        self._discount_rules = new_rules

    def _find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

    def add(self, item):
        itm = self._find_item(item.name)
        if itm:
            itm.qty += item.qty
        else:
            self.items = [*self.items, item]

    def apply_discount(self):
        for rule in self.discount_rules:
            itm = self._find_item(rule.item_name)
            if itm and itm.qty >= rule.qty_req:
                itm.price = itm.price * rule.discount

    def add_discount_rule(self, discount_rule):
        self.discount_rules = [*self.discount_rules, discount_rule]


class DiscountRule:
    def __init__(self, item_name, qty_req, discount):
        self._item_name = item_name
        self._qty_req = qty_req
        self._discount = discount

    @property
    def item_name(self):
        return self._item_name

    @property
    def qty_req(self):
        return self._qty_req

    @property
    def discount(self):
        return self._discount


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
