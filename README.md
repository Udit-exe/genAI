# Market Research & Use Case Generation Agent

This project is a multi-agent system designed to conduct market research and generate AI/GenAI use cases tailored for a given company or industry. It consists of several agents, each responsible for a specific task, ultimately producing a structured report.

## Project Structure

- `agents/industry_research.py`: Collects industry and company-specific insights.
- `agents/use_case_generation.py`: Proposes relevant AI/ML use cases.
- `agents/asset_collection.py`: Finds dataset resources for each use case.
- `agents/final_proposal.py`: Compiles outputs into a final report.
- `outputs/`: Stores generated reports and optional demo video.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/market-research-use-case-agent.git
   cd market-research-use-case-agent
