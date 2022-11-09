class StockSpanner:

    def __init__(self):
        self.data = []

    def next(self, price: int) -> int:
        
        if len(self.data) == 0:
            self.data.append(
                (price, 0)
            )
            return 1

        price1 = self.data.pop()

        if price < price1[0]:
            self.data.append(price1)
            self.data.append(
                (price, 0)
            )
            return 1
        else:
            self.data.append(price1)
        
        p = 1

        while self.data:
            n = self.data.pop()
            if price >= n[0]:
                p += n[1] if n[1] > 0 else 1
            else:
                self.data.append(n)
                self.data.append(
                    (price, p)
                )
                break
        else:
            self.data.append(
                    (price, p)
                )

        return p
