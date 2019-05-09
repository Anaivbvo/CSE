import csv


with open("Sales Records.csv") as old_csv:
    class Sales(object):
        def __init__(self, region, country, item_type, sales_channel, order_priority, order_date, order_id, ship_date,
                     units_sold, unit_price, unit_cost, total_revenue, total_cost, total_profit):
            self.region = region
            self.country = country
            self.item_type = item_type
            self.sales_channel = sales_channel
            self.order_priority = order_priority
            self.order_date = order_date
            self.order_id = order_id
            self.ship_date = ship_date
            self.units_sold = units_sold
            self.unit_price = unit_price
            self.unit_cost = unit_cost
            self.total_revenue = total_revenue
            self.total_cost = total_cost
            self.total_profit = total_profit
    reader = csv.reader(old_csv)

    for row in reader:
        # old_number = int(row[0]) + 1
        old_num = row[13]
