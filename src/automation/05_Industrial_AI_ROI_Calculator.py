import argparse

def calculate_industrial_savings(eng_count, avg_salary, downtime_hours, hourly_downtime_cost, productivity_boost=0.25, downtime_reduction=0.40):
    total_eng_cost = eng_count * avg_salary
    eng_savings = total_eng_cost * productivity_boost
    
    total_downtime_cost = downtime_hours * hourly_downtime_cost
    downtime_savings = total_downtime_cost * downtime_reduction
    
    total_annual_savings = eng_savings + downtime_savings
    
    return {
        "total_eng_cost": total_eng_cost,
        "eng_savings": eng_savings,
        "total_downtime_cost": total_downtime_cost,
        "downtime_savings": downtime_savings,
        "total_annual_savings": total_annual_savings
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Maya HTT Industrial AI & CAE ROI.")
    parser.add_argument("--engineers", type=int, default=50, help="Number of R&D / CAE Engineers (Default: 50)")
    parser.add_argument("--avg-salary", type=float, default=120000.0, help="Average Engineer Salary in CAD (Default: $120,000)")
    parser.add_argument("--downtime-hours", type=float, default=120.0, help="Annual Unplanned Downtime Hours (Default: 120 hrs)")
    parser.add_argument("--downtime-cost", type=float, default=15000.0, help="Cost per Unplanned Downtime Hour (Default: $15,000)")

    args = parser.parse_args()
    res = calculate_industrial_savings(args.engineers, args.avg_salary, args.downtime_hours, args.downtime_cost)

    print("\n" + "="*60)
    print("      MAYA HTT INDUSTRIAL AI & CAE ROI COMMERCIAL MODEL")
    print("="*60)
    print(f"Engineering R&D Base Cost:           ${res['total_eng_cost']:,.2f}")
    print(f"Engineering Productivity Savings:   ${res['eng_savings']:,.2f}")
    print(f"Annual Unplanned Downtime Exposure: ${res['total_downtime_cost']:,.2f}")
    print(f"AI Downtime Reduction Value:        ${res['downtime_savings']:,.2f}")
    print("-" * 60)
    print(f"NET TOTAL ANNUAL ROI:              ${res['total_annual_savings']:,.2f}")
    print("="*60 + "\n")
