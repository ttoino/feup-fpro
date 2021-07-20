def invoice_totals(orders, min):
    return list(map(lambda x: (x[0], x[2]*x[3] if x[2]*x[3] >= min else x[2]*x[3] + 10), orders))