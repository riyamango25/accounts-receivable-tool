from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

"""
LangChain Tool: Accounts Receivable Risk Analysis
"""

class AccountsReceivableInput(BaseModel):
    receivables: list[float] = Field(description="Receivables over years")
    revenue: list[float] = Field(description="Revenue over years")
    ageing_long_term_percentage: float = Field(description="Receivables > 90 days")

def accounts_receivable_risk(
    receivables: list[float],
    revenue: list[float],
    ageing_long_term_percentage: float
) -> str:

    result = []

    receivable_growth = (receivables[-1] - receivables[0]) / receivables[0]
    revenue_growth = (revenue[-1] - revenue[0]) / revenue[0]

    if receivable_growth > revenue_growth:
        result.append("Receivables growing faster than revenue (red flag).")
    else:
        result.append("Receivables growth aligned with revenue.")

    ratio = receivables[-1] / revenue[-1]

    if ratio > 0.5:
        result.append("Receivables-to-revenue ratio above 50%.")
    elif ratio > 0.4:
        result.append("Receivables-to-revenue ratio between 40–50%.")
    else:
        result.append("Receivables-to-revenue ratio healthy.")

    if ageing_long_term_percentage > 30:
        result.append("High ageing receivables (write-off risk).")
    else:
        result.append("Ageing profile healthy.")

    return " | ".join(result)

accounts_receivable_tool = StructuredTool.from_function(
    name="accounts_receivable_risk_tool",
    description="Analyzes receivable trends, ratios, and ageing risk",
    func=accounts_receivable_risk,
    args_schema=AccountsReceivableInput
)