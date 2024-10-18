class VendingMachine:
    def __init__(self):
        self._inventory = dict()

    @property
    def products(self) -> dict:
        return self._inventory

    def add_product(self, *, name: str, price: float = None, quantity: int) -> None:
        current = self._inventory.get(name)
        if not current and not price:
            raise Exception('New items must have a price')
        current_quantity = current.get("quantity") if current else 0
        self._inventory.update({
            name: {
                "price": price if price else current.get("price"),
                "quantity": current_quantity + quantity
            }
        })

    def remove_product(self, *, name: str) -> None:
        self._inventory.pop(name)

    def modify_product(self, *, name: str, new_name: str = None, price: float = None) -> None:
        current = self._inventory.pop(name)
        self._inventory.update({
           new_name if new_name else name: {
               "price": price if price else current.get("price"),
               "quantity": current.get("quantity")
           }
       })
