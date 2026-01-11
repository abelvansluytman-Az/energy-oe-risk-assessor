import random

def evaluate_environmental_risk():
    print("\n=== Environmental Risk Assessment (Oil & Gas) ===")
    factors = {
        "Proximity to water bodies (1=low, 5=high)": int(input("Enter value (1-5): ")),
        "Potential spill volume (1=low, 5=high)": int(input("Enter value (1-5): ")),
        "VOC/gas emissions (1=low, 5=high)": int(input("Enter value (1-5): ")),
        "Hazardous waste management (1=excellent, 5=poor)": int(input("Enter value (1-5): "))
    }
    env_score = sum(factors.values()) / len(factors) * 20  # Scale 0-100
    return env_score

def evaluate_cyber_risk():
    print("\n=== Basic OT Cybersecurity Risk Assessment ===")
    cyber_factors = {
        "Use of legacy unpatched systems (1=no, 5=yes)": int(input("Enter value (1-5): ")),
        "Employee phishing training (1=complete, 5=none)": int(input("Enter value (1-5): ")),
        "OT/IT network segmentation (1=yes, 5=no)": int(input("Enter value (1-5): "))
    }
    cyber_score = sum(cyber_factors.values()) / len(cyber_factors) * 20
    return cyber_score

def calculate_total_risk(env_score, cyber_score):
    total = (env_score * 0.6) + (cyber_score * 0.4)  # Higher weight on environmental
    if total < 40:
        level = "Low"
        recommendations = "Maintain current safeguards. Focus on continuous monitoring."
    elif total < 70:
        level = "Medium"
        recommendations = "Implement improvements in waste management and cyber training. Review environmental permits."
    else:
        level = "High"
        recommendations = "Immediate action: Full audit, strengthen OT barriers, and develop spill contingency plans."
    return level, recommendations

# Main program
print("OE Risk Assessment Tool - Energy Sector (Environmental + Cybersecurity)")
env_risk = evaluate_environmental_risk()
cyber_risk = evaluate_cyber_risk()
level, recs = calculate_total_risk(env_risk, cyber_risk)

print(f"\n=== Results ===")
print(f"Environmental Risk Score: {env_risk:.1f}/100")
print(f"Cybersecurity Risk Score: {cyber_risk:.1f}/100")
print(f"Total OE Risk Level: {level}")
print(f"Recommendations: {recs}")
print("\nThis tool simulates Chevron's Operational Excellence Management System (OEMS) principles for environmental protection and operational safety.")