from checkout import Checkout, Item, DiscountRule
import pytest


@pytest.fixture
def coffeepack():
    return Item('Coffee', 3, 4)


@pytest.fixture
def discountrule():
    return DiscountRule('Coffee', 3, 0.5)


@pytest.fixture
def cart(coffeepack):
    ckout = Checkout()
    ckout.add(coffeepack)
    ckout.add(Item('Tea', 2))
    return ckout


@pytest.fixture
def cart_with_discount(cart, discountrule):
    cart.add_discount_rule(discountrule)
    return cart


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


class TestDiscountRule:
    def test_discount_attrs(self):
        dr = DiscountRule('Coffee', 3, 0.50)
        assert dr.item_name == 'Coffee'
        assert dr.qty_req == 3
        assert dr.discount == 0.50


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
        assert cart.total_cost == 14

    def test_add_discount_rule(self, cart):
        cart.add_discount_rule(DiscountRule('Coffee', 3, 0.5))
        assert cart.discount_rules[0].item_name == 'Coffee'

    def test_apply_discount(self, cart_with_discount):
        cart_with_discount.apply_discount()
        assert cart_with_discount.total_cost == 8
