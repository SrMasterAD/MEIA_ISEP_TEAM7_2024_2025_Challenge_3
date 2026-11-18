from application.api.services.disease_classification_service import classify_disease
from report_system.infection_prediction_service import predict_infection
from report_system.loss_prediction_service import predict_loss
from application.api.services.treatment_generation_service import generate_treatment
import application.api.utils.disease as disease
import json

def generate_json_report(days, infected_areas, profit_loss, plantation_loss, yield_loss, classified_disease, disease_treatment):
    infection_by_day = []
    for i in range(len(days)):
        infection_by_day.append({
            "day": "{:.0f}".format(days[i]),
            "infected_area": "{:.0f}".format(infected_areas[i]) + " m²",
            "yield_loss": "{:.0f}".format(yield_loss[i]) + " tons",
            "economic_impact": {
                "profit_loss": "{:.2f}".format(profit_loss[i]) + " €",
                "plantation_loss": "{:.2f}".format(plantation_loss[i]) + " €"
            }
        })

    report = {
        "wheat_disease": classified_disease,
        "infection_by_day": infection_by_day,
        "disease_treatment": disease_treatment
    }
    return report

def generate_report(image, area, plantation_cost, expected_profit, expected_yield):
    classified_disease = classify_disease(image)
    if classified_disease == disease.HEALTHY:
        return {
            "wheat_disease": disease.HEALTHY
        }

    days, infected_areas = predict_infection(classified_disease, area)
    profit_loss, plantation_loss, yield_loss = predict_loss(
        area, infected_areas, plantation_cost, expected_profit, expected_yield
    )
    disease_treatment = generate_treatment(classified_disease)

    return generate_json_report(days, infected_areas, profit_loss,
                                 plantation_loss, yield_loss,
                                   classified_disease, disease_treatment)