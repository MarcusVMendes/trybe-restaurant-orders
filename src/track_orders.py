class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})

    def customer_data(self, customer):
        return [item for item in self.orders if item["customer"] == customer]

    def get_most_ordered_dish_per_customer(self, customer):
        data = self.customer_data(customer)
        most_ordered = self.orders[0]["order"]
        counter = dict()
        for item in data:
            if item["order"] not in counter:
                counter[item["order"]] = 1
            else:
                counter[item["order"]] += 1
            if counter[item["order"]] > counter[most_ordered]:
                most_ordered = item["order"]
        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        data = self.customer_data(customer)
        orders = set([item["order"] for item in self.orders])
        costumer_orders = set([item["order"] for item in data])
        return orders.difference(costumer_orders)

    def get_days_never_visited_per_customer(self, customer):
        data = self.customer_data(customer)
        days = set([item["day"] for item in self.orders])
        costumer_days = set([item["day"] for item in data])
        return days.difference(costumer_days)

    def get_busiest_day(self):
        busiest_day = dict()
        for item in self.orders:
            if item["day"] not in busiest_day:
                busiest_day[item["day"]] = 1
            else:
                busiest_day[item["day"]] += 1
        return max(busiest_day, key=busiest_day.get)

    def get_least_busy_day(self):
        least_busy_day = dict()
        for item in self.orders:
            if item["day"] not in least_busy_day:
                least_busy_day[item["day"]] = 1
            else:
                least_busy_day[item["day"]] += 1
        return min(least_busy_day, key=least_busy_day.get)
