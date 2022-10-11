from checkout import Checkout, Item
import pytest


@pytest.fixture
def cart():
    ckout = Checkout()
    ckout.add(Item('Coffee', 3))
    ckout.add(Item('Coffee', 3))
    ckout.add(Item('Coffee', 3))
    ckout.add(Item('Tea', 2))
    return ckout


class TestItem:
    def test_item_name(self):
        itm = Item('Coffee')
        assert itm.name == 'Coffee'

    def test_item_price(self):
        itm = Item(price=5)
        assert itm.price == 5

    def test_item_quantity(self):
        itm = Item(qty=3)
        assert itm.qty == 3

    def test_set_item_quantity(self):
        itm = Item(qty=3)
        assert itm.qty == 3
        itm.qty = 10
        assert itm.qty == 10

    def test_item_set_price(self):
        itm = Item(price=5)
        assert itm.price == 5
        itm.price = 3
        assert itm.price == 3


class TestCheckout:
    def test_initial_empty_checkout_list(self):
        ckout = Checkout()
        assert ckout.items == []

    def test_add_item_to_checkout(self):
        ckout = Checkout()
        ckout.add(Item('Coffee', 3))
        assert ckout.items[0].name == 'Coffee'

    def test_add_same_item_to_checkout(self):
        ckout = Checkout()
        ckout.add(Item('Coffee', 3))
        assert ckout.items[0].qty == 1
        ckout.add(Item('Coffee', 3))
        assert len(ckout.items) == 1
        assert ckout.items[0].qty == 2

    def test_add_different_item_to_checkout(self):
        ckout = Checkout()
        ckout.add(Item('Coffee', 3))
        ckout.add(Item('Tea', 2))
        assert len(ckout.items) == 2

    def test_get_total_cost(self, cart):
        assert cart.total_cost == 11

    def test_apply_discount(self, cart):
        cart.apply_discount()
        assert cart.total_cost == 5
