from application.api.services.disease_classification_service import classify_disease
from application.api.services.infection_prediction_service import predict_infection
from application.api.services.loss_prediction_service import predict_loss
from application.api.services.treatment_generation_service import generate_treatment
from application.api.services import user_configurations_service
import application.api.constants.diseases as diseases
from fastapi import HTTPException
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
        "disease_treatment": disease_treatment.get("treatment"),
        "disease_cause": disease_treatment.get("cause"),
        "disease_management": disease_treatment.get("management"),
    }
    return report

async def generate_report(image, user_id):

    configurations = await user_configurations_service.get_configuration_by_user_id(user_id)
    
    if not configurations.expected_yield or not configurations.expected_profit or not configurations.plantation_cost or not configurations.area:
        raise HTTPException(status_code=401, detail="Incomplete user configurations")
    
    classified_disease = await classify_disease(image)
    if classified_disease == diseases.HEALTHY:
        return {
            "wheat_disease": diseases.HEALTHY
        }

    days, infected_areas = predict_infection(classified_disease, configurations.area)
    profit_loss, plantation_loss, yield_loss = predict_loss(
        configurations.area, infected_areas, configurations.plantation_cost, configurations.expected_profit, configurations.expected_yield
    )
    try:
        disease_treatment = await generate_treatment(classified_disease)
    except Exception as e:
        # Instead of raising an HTTPException, simply return the exception message as a response.
        return {"error": str(e)}

    return generate_json_report(days, infected_areas, profit_loss,
                                 plantation_loss, yield_loss,
                                   classified_disease, disease_treatment)