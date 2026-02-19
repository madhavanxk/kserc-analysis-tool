"""
KSERC Regulatory Constants
==========================
Static values from KSERC orders used across heuristics.
Source: Table D.571 - Escalation Rate based on actual inflationary index for FY 2024-25

Update these values each tariff year.
"""

# =============================================================================
# INFLATION INDICES (Table D.571)
# =============================================================================

# CPI - Industrial Workers (Base: 2001=100)
CPI = {
    '2021-22': 356.06,
    '2022-23': 377.62,
    '2023-24': 397.25,
    '2024-25': 410.64,
}

# Annual CPI increase (%)
CPI_INCREASE_PCT = {
    '2021-22': 5.13,
    '2022-23': 6.05,
    '2023-24': 5.19,
    '2024-25': 3.37,
}

# WPI (2011-12 series)
WPI = {
    '2021-22': 139.4,
    '2022-23': 152.5,
    '2023-24': 151.4,
    '2024-25': 154.90,
}

# Annual WPI increase (%)
WPI_INCREASE_PCT = {
    '2021-22': 12.97,
    '2022-23': 9.4,
    '2023-24': -0.72,
    '2024-25': 2.31,
}

# Weighted inflation: CPI (70%) + WPI (30%)
WEIGHTED_INFLATION_PCT = {
    '2021-22': 7.48,
    '2022-23': 7.06,
    '2023-24': 3.41,
    '2024-25': 3.05,
}

# =============================================================================
# O&M BASE YEAR (from MYT Order 2022)
# =============================================================================

# Base year O&M for SBU-G as approved in TU order dated 14.06.2022
OM_BASE_YEAR_SBU_G = 156.16  # Rs Cr (2021-22)

# Component ratios (MYT Order 2022, Table 4.23)
OM_COMPONENT_RATIOS = {
    'employee': 0.7703,   # 77.03%
    'ag':       0.0432,   # 4.32%
    'rm':       0.1865,   # 18.65%
}

# =============================================================================
# CURRENT FISCAL YEAR
# =============================================================================

CURRENT_FY  = '2024-25'
PREVIOUS_FY = '2023-24'

# =============================================================================
# NON-TARIFF INCOME BASELINE (Table 4.61, MYT Order 2022)
# =============================================================================

# MYT approved NTI (Other Income) for SBU-G (Rs Cr)
NTI_BASELINE_SBU_G = {
    '2022-23': 10.30,
    '2023-24': 10.81,
    '2024-25': 11.35,
    '2025-26': 11.92,
    '2026-27': 12.52,
}

# =============================================================================
# LOAN SUMMARY (Table 5.3, Petition 2024-25)
# =============================================================================

LOAN_OPENING_SBU_G      = 1273.68   # Rs Cr (01/04/2024)
LOAN_ADDITIONS_SBU_G    = 278.14    # Rs Cr
LOAN_REPAYMENTS_SBU_G   = 296.27    # Rs Cr
LOAN_CLOSING_SBU_G      = 1255.55   # Rs Cr (31/03/2025)
LOAN_AVERAGE_SBU_G      = 1264.62   # Rs Cr
LOAN_INTEREST_ACTUAL    = 111.74    # Rs Cr (from audited accounts)
LOAN_AVG_RATE_SBU_G     = 8.84      # % weighted average
# =============================================================================

GPF_INTEREST_RATE    = 7.10   # % (confirmed)
SBU_G_GPF_RATIO      = 5.40   # % (same as employee strength ratio)

# Company-wide GPF balances by year (Rs Cr)
GPF_OPENING_BALANCE = {
    '2022-23': 2852.52,
    '2023-24': 3274.32,
    '2024-25': 3364.32,
    '2025-26': 3454.32,
    '2026-27': 3544.32,
}
GPF_CLOSING_BALANCE = {
    '2022-23': 3274.32,
    '2023-24': 3364.32,
    '2024-25': 3454.32,
    '2025-26': 3544.32,
    '2026-27': 3634.32,
}
GPF_TOTAL_INTEREST = {
    '2022-23': 217.50,
    '2023-24': 235.67,
    '2024-25': 242.06,
    '2025-26': 248.45,
    '2026-27': 254.84,
}

# SBU-G employee strength ratio (used for allocation)
SBU_G_EMPLOYEE_RATIO = 5.40   # %

# Total company-wide Master Trust bond interest by year (Rs Cr)
MT_BOND_TOTAL_COMPANY = {
    '2022-23': 610.80,
    '2023-24': 570.08,
    '2024-25': 529.36,
    '2025-26': 488.64,
    '2026-27': 447.92,
}

# MYT approved SBU-G share of bond interest (Rs Cr)
MT_BOND_APPROVED_SBU_G = {
    '2022-23': 32.98,
    '2023-24': 30.78,
    '2024-25': 28.59,
    '2025-26': 26.39,
    '2026-27': 24.19,
}

# Opening GFA excl. land SBU-G (derived from MYT WC requirement 2024-25)
# WC req = O&M/12 + 1% GFA → 78.00 = 14.85 + GFA*0.01 → GFA ≈ 6315 Cr
OPENING_GFA_EXCL_LAND_SBU_G = 6315.0   # Rs Cr (as on 01.04.2024)

# =============================================================================
# INTEREST ON WORKING CAPITAL (Table 4.45, MYT Order 2022)
# =============================================================================

# SBI EBLR as fixed by KSERC for MYT period 2023-24 to 2026-27
SBI_EBLR_RATE = 7.55          # % (effective from 15.06.2022)
IWC_RATE      = 9.55          # % (EBLR + 2% per Regulation 32(2))

# MYT approved IWC amounts for SBU-G (Table 4.46)
IWC_APPROVED_SBU_G = {
    '2022-23': 5.54,
    '2023-24': 6.87,
    '2024-25': 7.45,
    '2025-26': 7.81,
    '2026-27': 8.21,
}

# MYT approved working capital requirement for SBU-G (Table 4.46)
WC_REQUIREMENT_SBU_G = {
    '2022-23': 64.01,
    '2023-24': 71.90,
    '2024-25': 78.00,
    '2025-26': 81.81,
    '2026-27': 85.93,
}
