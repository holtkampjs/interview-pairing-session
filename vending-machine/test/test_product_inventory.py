from src.vending_machine import VendingMachine


def test_vending_machine_init():
    vm = VendingMachine()
    assert vm


def test_add_product_pop():
    vm = VendingMachine()
    vm.add_product(name="pop", price=1, quantity=5)
    assert vm.products == {
        "pop": {
            "price": 1,
            "quantity": 5
        }
    }
    

def test_add_morep_roduct_pop():
    vm = VendingMachine()
    vm.add_product(name="pop", price=1, quantity=5)
    vm.add_product(name="pop", quantity=2)
    assert vm.products == {
        "pop": {
            "price": 1,
            "quantity": 7
        }
    }


def test_add_second_product():
    vm = VendingMachine()
    vm.add_product(name="pop", price=1, quantity=5)
    vm.add_product(name="chips", price=2, quantity=10)
    assert vm.products == {
        "pop": {
            "price": 1,
            "quantity": 5
        },
        "chips": {
            "price": 2,
            "quantity": 10
        }
    }

    
def test_remove_product():
    vm = VendingMachine()

    # Add pop as product
    vm.add_product(name="pop", price=1, quantity=5)

    # Assert pop is present
    assert vm.products == {
        "pop": {
            "price": 1,
            "quantity": 5
        }
    }

    # Remove pop as product
    vm.remove_product(name="pop")

    # Assert pop is not present
    assert vm.products == {}


def test_remove_product_with_multiple_products():
    vm = VendingMachine()

    # Add 2 products
    vm.add_product(name="pop", price=1, quantity=5)
    vm.add_product(name="chips", price=2, quantity=10)

    # Assert products are present
    assert vm.products == {
        "pop": {
            "price": 1,
            "quantity": 5
        },
        "chips": {
            "price": 2,
            "quantity": 10
        }
    }

    # Remove pop product
    vm.remove_product(name="pop")

    # Assert chips are present
    assert vm.products == {
        "chips": {
            "price": 2,
            "quantity": 10
        }
    }


def test_remove_chips_product_with_multiple_products():
    vm = VendingMachine()

    # Add 2 products
    vm.add_product(name="pop", price=1, quantity=5)
    vm.add_product(name="chips", price=2, quantity=10)

    # Assert products are present
    assert vm.products == {
        "pop": {
            "price": 1,
            "quantity": 5
        },
        "chips": {
            "price": 2,
            "quantity": 10
        }
    }

    # Remove chips product
    vm.remove_product(name="chips")

    # Assert pop is present
    assert vm.products == {
        "pop": {
            "price": 1,
            "quantity": 5
        }
    }


def test_modify_product_pop_price():
    vm = VendingMachine()

    # Add pop as product
    vm.add_product(name="pop", price=1, quantity=5)

    # Update pop product
    vm.modify_product(name="pop", price=2)

    # Assert price is updated
    assert vm.products == {
        "pop": {
            "price": 2,
            "quantity": 5
        }
    }


def test_modify_product_chips_price():
    vm = VendingMachine()

    # Add chips as product
    vm.add_product(name="chips", price=1, quantity=5)

    # Update chips product
    vm.modify_product(name="chips", price=2)

    # Assert price is updated
    assert vm.products == {
        "chips": {
            "price": 2,
            "quantity": 5
        }
    }

def test_modify_product_pop_and_chips():
    vm = VendingMachine()

    # Add products
    vm.add_product(name="pop", price=1, quantity=5)
    vm.add_product(name="chips", price=2, quantity=10)

    # Rename pop to pepsi
    vm.modify_product(name="pop", new_name="pepsi")

    # Adjust chips price
    vm.modify_product(name="chips", price=3.5)

    # Assert price is updated
    assert vm.products == {
        "pepsi": {
            "price": 1,
            "quantity": 5
        },
        "chips": {
            "price": 3.5,
            "quantity": 10
        }
    }
