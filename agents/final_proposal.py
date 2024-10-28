def generate_final_report(insights, use_cases, datasets):
    report = f"**Industry**: {insights['industry']}\n"
    report += f"**Focus Areas**: {', '.join(insights['focus_areas'])}\n"
    report += f"**Trends**: {', '.join(insights['trends'])}\n\n"
    report += "**Proposed Use Cases**:\n"
    
    for use_case in use_cases:
        report += f"- {use_case}\n"
    
    report += "\n**Dataset Resources**:\n"
    for data in datasets:
        report += f"- [{data['use_case']}]({data['kaggle_link']})\n"
    
    return report

# Example Usage
final_report = generate_final_report(company_insights, use_cases, datasets)
print(final_report)
