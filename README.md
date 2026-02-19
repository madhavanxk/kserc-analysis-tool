# KSERC Truing-Up Analysis Tool

Automated first-cut analysis of KSEB truing-up petitions for the Kerala State Electricity Regulatory Commission (KSERC).

**Version:** Beta v1.0  
**Coverage:** SBU-G (Generation) only  
**Fiscal Year:** 2024-25

---

## What It Does

KSERC staff upload a KSEB truing-up petition PDF. The tool automatically:

1. Extracts all 10 SBU-G line items from the petition
2. Extracts 10 supporting Chapter 5 tables
3. Runs 15 regulatory heuristics
4. Produces a traffic light analysis (GREEN / YELLOW / RED)
5. Identifies excess claims and flags items requiring scrutiny

**Typical processing time:** Under 60 seconds for a 381-page petition.

---

## Line Items Covered

| # | Line Item | Heuristic(s) |
|---|-----------|-------------|
| 1 | Return on Equity (ROE) | ROE-01 |
| 2 | Depreciation | DEP-GEN-01 |
| 3 | Fuel Costs | FUEL-01 |
| 4 | O&M Expenses | OM-INFL-01, OM-NORM-01, OM-APPORT-01, EMP-PAYREV-01 |
| 5 | Interest & Finance Charges | IFC-LTL-01, IFC-WC-01, IFC-GPF-01, IFC-OTH-02 |
| 6 | Master Trust Bond Interest | MT-BOND-01 |
| 7 | Non-Tariff Income | NTI-01 |
| 8 | Intangible Assets | INTANG-01 |
| 9 | Other Expenses | OTHER-EXP-01 |
| 10 | Exceptional Items | EXC-01 |

---

## Installation (Local)

**Requirements:** Python 3.10+

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/kserc-analysis-tool.git
cd kserc-analysis-tool

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
```

The app opens automatically at `http://localhost:8501`.

---

## Running from Command Line (without UI)

```bash
python integration_pipeline.py KSEB_Petition.pdf --detailed
```

---

## File Structure

```
kserc-analysis-tool/
│
├── streamlit_app.py              # Main UI — run this
├── integration_pipeline.py       # End-to-end pipeline
├── pdf_parser_sbu_g.py           # PDF table extraction
├── data_mapper_sbu_g.py          # Maps extracted data to heuristic inputs
├── kserc_constants.py            # Regulatory constants (CPI, WPI, rates etc.)
│
├── roe_heuristics.py             # ROE-01
├── depreciation_heuristics.py    # DEP-GEN-01
├── fuel_heuristics.py            # FUEL-01
├── om_heuristics.py              # OM-INFL-01, OM-NORM-01, OM-APPORT-01, EMP-PAYREV-01
├── ifc_heuristics.py             # IFC-LTL-01, IFC-WC-01, IFC-GPF-01, IFC-OTH-02
├── master_trust_heuristics.py    # MT-BOND-01
├── nti_heuristics.py             # NTI-01
├── intangible_heuristics.py      # INTANG-01
├── other_items_heuristics.py     # OTHER-EXP-01, EXC-01
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Regulatory Constants

All constants are sourced from KSERC orders and published indices:

| Constant | Value | Source |
|----------|-------|--------|
| CPI 2024-25 | 410.64 | RBI / CSO — Table D.571 |
| WPI 2024-25 | 154.90 | RBI / CSO — Table D.571 |
| SBI EBLR | 7.55% | MYT Order 2022 |
| GPF Rate | 7.10% | Table 5.27, MYT Order 2022 |
| SBU-G Employee Ratio | 5.40% | Table 4.51, MYT Order 2022 |
| O&M Base Year | ₹156.16 Cr | TU Order 14.06.2022 |
| MT Bond Total 2024-25 | ₹529.36 Cr | Table 4.51, MYT Order 2022 |
| NTI Baseline 2024-25 | ₹11.35 Cr | Table 4.61, MYT Order 2022 |
| GPF Opening 2024-25 | ₹3364.32 Cr | Table 5.27, MYT Order 2022 |
| GPF Closing 2024-25 | ₹3454.32 Cr | Table 5.27, MYT Order 2022 |

All constants are visible and editable in the sidebar before each run.

---

## Updating for a New Year

When a new truing-up petition is filed:

1. Update `kserc_constants.py` with new CPI/WPI values (from RBI)
2. Update GPF opening/closing balances (shift by one year from Table 5.27)
3. Update loan opening balance and interest rate (from new petition Table 5.3)
4. All other MYT constants remain fixed until the next MYT order (2027)

Estimated update effort: **2-3 hours per year**.

---

## Known Limitations (v1.0)

- **SBU-G only** — SBU-T and SBU-D analysis not yet implemented
- **2024-25 petition format** — table layouts may differ in earlier petitions
- Table 5.1 and 5.22 not extractable (workaround: uses Table G10)
- O&M component table 5.37 not found in current petition (prudence checks use available data)
- Opening GFA derived from MYT WC requirement (not directly extracted)
- IFC-LTL normative calculation uses simplified model

---

## Important Disclaimer

This tool provides an automated first-cut analysis only. All recommendations must be reviewed and approved by authorised KSERC staff before being incorporated into regulatory orders. The tool does not replace professional regulatory judgement.

---

## Roadmap

- [ ] SBU-T (Transmission) module
- [ ] SBU-D (Distribution) module  
- [ ] Multi-year analysis (comparison across petitions)
- [ ] Year-agnostic constants config UI
- [ ] Automated data standardisation guidelines for petitioners
- [ ] Export to Word / PDF report

---

## Built For

Kerala State Electricity Regulatory Commission (KSERC)  
Thiruvananthapuram, Kerala, India

---

*For technical queries, contact the development team.*
