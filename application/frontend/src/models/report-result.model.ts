export type ReportResult = {
  wheat_disease: WheatDisease;
  infection_by_day: InfectionDay[];
  disease_treatment: string;
  disease_cause: string;
  disease_management: string;
};

export type WheatDisease =
  | "Brown Rust"
  | "Yellow Rust"
  | "Septoria"
  | "Mildew"
  | "Healthy";


type InfectionDay = {
  day: string;
  infected_area: string;
  yield_loss: string;
  economic_impact: EconomicImpact;
};

type EconomicImpact = {
  profit_loss: string;
  plantation_loss: string;
};
