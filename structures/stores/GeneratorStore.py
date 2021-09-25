from structures.Stores import Store, CookieStore

"""
A custom store to store data about generators.
Extends base methods to automatically increment and decrement the CookieStore's CPS accordingly.
"""
class GeneratorStore(Store):
    def __init__(self, cookieStore: CookieStore, name: str, cost: int, cps: int):
        super().__init__(name, 0)
        self._cpsPerUnit = cps
        self._baseCostPerUnit = cost
        self._cookieStore = cookieStore

    """
    Get the latest cost for a generator.
    """
    def getCost(self):
        if self.quantity == 0:
            return self._baseCostPerUnit
        return round(self._baseCostPerUnit * (self.quantity + 2.5))

    """
    Buys a specific amount of generators. Returns True on success, False on failure.
    """
    def add(self, amount: int = 1):
        totalCost = self.getCost() * amount
        if self._cookieStore.quantity >= totalCost:
            super().add(amount)
            self._cookieStore.remove(totalCost)
            self._cookieStore.addCPS(self._cpsPerUnit)
            return True
        return False

    """
    Sells a specific amount of generators.
    """
    def remove(self, amount: int = 1):
        refund = amount * self._baseCostPerUnit
        super().remove(amount)
        self._cookieStore.add(refund)
        self._cookieStore.removeCPS(self._cpsPerUnit * amount)
