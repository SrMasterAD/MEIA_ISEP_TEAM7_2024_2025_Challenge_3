def predict_plantation_loss(total_area, infected_area, plantation_cost):
    return infected_area * plantation_cost / total_area

def predict_profit_loss(total_area, infected_area, expected_profit):
    return infected_area * expected_profit / total_area

def predict_yield_loss(total_area, infected_area, expected_yield):
    return infected_area * expected_yield / total_area


def predict_loss(total_area, infected_area, plantation_cost, expected_profit, expected_yield):
    plantation_loss = predict_plantation_loss(total_area, infected_area, plantation_cost)
    profit_loss = predict_profit_loss(total_area, infected_area, expected_profit)
    yield_loss = predict_yield_loss(total_area, infected_area, expected_yield)
    return profit_loss, plantation_loss, yield_loss

