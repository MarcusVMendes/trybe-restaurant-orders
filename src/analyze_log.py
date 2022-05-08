import csv


def read_file(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        with open(path_to_file) as file:
            fieldnames = ["customer", "order", "weekday"]
            data = csv.DictReader(file, fieldnames=fieldnames)
            return list(data)
    except IOError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def filter_by_customer(data, customer):
    return [item for item in data if item["customer"] == customer]


def most_made_order(data):
    counter = {}
    most_made = data[0]["order"]
    for item in data:
        if item["order"] not in counter:
            counter[item["order"]] = 1
        else:
            counter[item["order"]] += 1
        if counter[item["order"]] > counter[most_made]:
            most_made = item["order"]
    return most_made


def count_order(data, dish):
    counter = 0
    for item in data:
        if item["order"] == dish:
            counter += 1
    return counter


def orders_never_made_by_customer(data, customer):
    orders_data = set([item["order"] for item in data])
    orders_customer = set([item["order"] for item in customer])
    return orders_data.difference(orders_customer)


def days_without_orders(data, customer):
    days = set([item["weekday"] for item in data])
    days_customer = set(item["weekday"] for item in customer)
    return days.difference(days_customer)


def analyze_log(path_to_file):
    data = read_file(path_to_file)
    maria = filter_by_customer(data, "maria")
    arnaldo = filter_by_customer(data, "arnaldo")
    joao = filter_by_customer(data, "joao")
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f'{most_made_order(maria)}\n'
            f'{count_order(arnaldo, "hamburguer")}\n'
            f'{orders_never_made_by_customer(data, joao)}\n'
            f'{days_without_orders(data, joao)}\n'
        )
