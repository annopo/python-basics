class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        
        # countが3以上のとき、total_priceを1割引
        if count >= 3:
            total_price *= 0.9
        
        # total_priceを四捨五入
        return round(total_price)