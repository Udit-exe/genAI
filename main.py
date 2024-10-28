import yaml
from agents.industry_research import industry_research
from agents.use_case_generation import generate_use_cases
from agents.asset_collection import find_datasets
from agents.final_proposal import generate_final_report

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Step 1: Industry Research
company_name = "Example Company"
company_insights = industry_research(company_name)

# Step 2: Use Case Generation
use_cases = generate_use_cases(company_insights)

# Step 3: Resource Asset Collection
datasets = find_datasets(use_cases)

# Step 4: Final Proposal
final_report = generate_final_report(company_insights, use_cases, datasets)

# Save report to file
with open("outputs/report.md", "w") as report_file:
    report_file.write(final_report)

print("Report generated and saved in outputs/report.md.")
