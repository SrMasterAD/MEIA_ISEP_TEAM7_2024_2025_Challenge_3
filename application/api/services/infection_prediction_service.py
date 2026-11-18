import numpy as np
import math
import application.api.constants.diseases as diseases
display_percentages = [0.2, 0.8]

def brown_rust_infected_area_prediction(total_area, p=display_percentages,rG=0.09):
    y0 = 1 / total_area  
    p = np.asarray(p, dtype=float)
    
    t = -(1 / rG) * np.log(np.log(p) / np.log(y0))
    t = np.round(t)
    
    area = np.exp(np.log(y0) * np.exp(-rG * t)) * total_area
    
    return t, area

def yellow_rust_infected_area_prediction(total_area, p=display_percentages, r=0.294):
    y0 = 1 / total_area  
    p = np.asarray(p, dtype=float)
    
    t = -1 / r * np.log((1 - p) / p * y0 / (1 - y0))
    t = np.round(t)
    
    area = 1 / (1 + ((1 - y0) / y0) * np.exp(-r * t)) * total_area
    return t, area

def mildew_infected_area_prediction(total_area, p=display_percentages):
    p = np.asarray(p, dtype=float)
    p = p * 100
    
    t = (np.log((1/p) - 0.01) - np.log(1.236)) / np.log(0.938)
    t = np.round(t)
    
    area = 1 / (0.01 + 1.236 * (0.938 ** t)) * total_area
    return t, area

def septoria_infected_area_prediction(total_area, p=display_percentages, r= 0.074):
    y0 = 1 / total_area
    p = np.asarray(p, dtype=float)
    C = -math.log(-math.log(y0))
    t = (-np.log(-np.log(p)) - C) / r
    t = np.round(t)
    area = np.exp(-np.exp(-(r * t + C))) * total_area
    return t, area

def predict_infection(disease_type, area, p=display_percentages):
    match disease_type:
        case diseases.BROWN_RUST:
            return brown_rust_infected_area_prediction(area, p)
        case diseases.YELLOW_RUST:
            return yellow_rust_infected_area_prediction(area, p)
        case diseases.MILDEW:
            return mildew_infected_area_prediction(area, p)
        case diseases.SEPTORIA:
            return septoria_infected_area_prediction(area, p)
        case _:
            raise ValueError("Invalid disease type")
