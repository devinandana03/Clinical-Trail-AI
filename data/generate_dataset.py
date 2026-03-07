import pandas as pd
from faker import Faker
import random

fake = Faker()

conditions = [
    "Diabetes",
    "Hypertension",
    "Breast Cancer",
    "Asthma",
    "Alzheimer Disease"
]

phases = ["Phase 1", "Phase 2", "Phase 3"]

interventions = [
    "Drug A",
    "Drug B",
    "Immunotherapy",
    "Gene Therapy",
    "Lifestyle Intervention"
]

data = []

for i in range(200):

    row = {
        "trial_id": f"CT-{1000+i}",
        "condition": random.choice(conditions),
        "phase": random.choice(phases),
        "intervention": random.choice(interventions),
        "sample_size": random.randint(50,500),
        "duration_months": random.randint(6,36),
        "primary_outcome": fake.sentence()
    }

    data.append(row)

df = pd.DataFrame(data)

df.to_csv("clinical_trials.csv",index=False)

print("Dataset generated!")