# To debug, you should import websim as dr
# Also, you should type: valid = dr.GetData_m_b("USA:TOP3000")
import numpy as np
import random
totdi , totii = random.randint(600,800),random.randint(2000,3000)

inputs = ["open",
          "close",
          "high",
          "low",
          "vwap",
          "volume",
          "returns",
          "adv20",
          "sharesout",
          "cap",
          "split",
          "dividend",
          "market",
          "country",
          "exchange",
          "sector",
          "industry",
          "subindustry",
          "accounts_payable",
          "accum_depre",
          "assets",
          "assets_curr",
          "assets_curr_oth",
          "bookvalue_ps",
          "capex",
          "cash",
          "cash_st",
          "cashflow",
          "cashflow_dividends",
          "cashflow_fin",
          "cashflow_invst",
          "cashflow_op",
          "cogs",
          "cost_of_revenue",
          "current_ratio",
          "debt",
          "debt_lt",
          "debt_lt_curr",
          "debt_st",
          "depre",
          "depre_amort",
          "EBIT",
          "EBITDA",
          "employee",
          "enterprise_value",
          "eps",
          "equity",
          "goodwill",
          "income",
          "income_beforeextra",
          "income_tax",
          "income_tax_payable",
          "interest_expense",
          "inventory",
          "inventory_turnover",
          "invested_capital",
          "liabilities",
          "liabilities_cur_oth",
          "liabilities_curr",
          "liabilities_oth",
          "operating_expense",
          "operating_income",
          "operating_margin",
          "ppent",
          "ppent_net",
          "preferred_dividends",
          "pretax_income",
          "quick_ratio",
          "rad",
          "receivable",
          "retained_earnings",
          "return_assets",
          "return_equity",
          "revenue",
          "sales",
          "sales_growth",
          "sales_ps",
          "SGA_expense",
          "working_capital",
          "est_bookvalue_ps",
          "est_capex",
          "est_cashflow_fin",
          "est_cashflow_invst",
          "est_cashflow_op",
          "est_cashflow_ps",
          "est_dividend_ps",
          "est_ebit",
          "est_ebitda",
          "est_eps",
          "est_epsa",
          "est_epsr",
          "est_fcf",
          "est_fcf_ps",
          "est_ffo",
          "est_ffoa",
          "est_grossincome",
          "est_netdebt",
          "est_netprofit",
          "est_netprofit_adj",
          "est_ptp",
          "est_ptpr",
          "est_rd_expense",
          "est_sales",
          "est_sga",
          "est_shequity",
          "est_tbv_ps",
          "est_tot_assets",
          "est_tot_goodwill",
          "etz_eps",
          "etz_eps_delta",
          "etz_eps_ret",
          "etz_eps_tsrank",
          "etz_revenue",
          "etz_revenue_delta",
          "etz_revenue_ret",
          "rel_num_all",
          "rel_num_comp",
          "rel_num_cust",
          "rel_num_part",
          "rel_ret_all",
          "rel_ret_comp",
          "rel_ret_cust",
          "rel_ret_part",
          "snt_bearish",
          "snt_bearish_tsrank",
          "snt_bullish",
          "snt_bullish_tsrank",
          "snt_buzz",
          "snt_buzz_bfl",
          "snt_buzz_ret",
          "snt_ratio",
          "snt_ratio_tsrank",
          "snt_social_value",
          "snt_social_volume",
          "snt_value",
          "news_prev_vol",
          "news_curr_vol",
          "news_mov_vol",
          "news_ratio_vol",
          "news_open_vol",
          "news_close_vol",
          "news_tot_ticks",
          "news_atr14",
          "news_prev_day_ret",
          "news_prev_close",
          "news_open",
          "news_open_gap",
          "news_spy_last",
          "news_ton_high",
          "news_ton_low",
          "news_ton_last",
          "news_eod_high",
          "news_eod_low",
          "news_eod_close",
          "news_spy_close",
          "news_post_vwap",
          "news_pre_vwap",
          "news_main_vwap",
          "news_all_vwap",
          "news_eod_vwap",
          "news_max_up_amt",
          "news_max_up_ret",
          "news_max_dn_amt",
          "news_max_dn_ret",
          "news_session_range",
          "news_session_range_pct",
          "news_ls",
          "news_indx_perf",
          "news_pct_30sec",
          "news_pct_1min",
          "news_pct_5_min",
          "news_pct_10min",
          "news_pct_30min",
          "news_pct_60min",
          "news_pct_90min",
          "news_pct_120min",
          "news_mins_1_pct_up",
          "news_mins_2_pct_up",
          "news_mins_3_pct_up",
          "news_mins_4_pct_up",
          "news_mins_5_pct_up",
          "news_mins_7_5_pct_up",
          "news_mins_10_pct_up",
          "news_mins_20_pct_up",
          "news_mins_1_pct_dn",
          "news_mins_2_pct_dn",
          "news_mins_3_pct_dn",
          "news_mins_4_pct_dn",
          "news_mins_5_pct_dn",
          "news_mins_7_5_pct_dn",
          "news_mins_10_pct_dn",
          "news_mins_20_pct_dn",
          "news_mins_1_chg",
          "news_mins_2_chg",
          "news_mins_3_chg",
          "news_mins_4_chg",
          "news_mins_5_chg",
          "news_mins_7_5_chg",
          "news_mins_10_chg",
          "news_range_stddev",
          "news_mins_20_chg",
          "news_cap",
          "news_pe_ratio",
          "news_dividend_yield",
          "news_short_interest",
          "news_high_exc_stddev",
          "news_low_exc_stddev",
          "news_vol_stddev",
          "news_atr_ratio",
          "news_eps_actual"
          ]

def GetData(string):
    for i in range(len(inputs)):
        if string == inputs[i]:
            SampleData = np.random.uniform(0, 1, totdi * totii)
            SampleData = np.reshape(SampleData, (totdi, totii))
            return SampleData
    print("Error: GetData(" + string + ") -> There is no " + string)
    return None

#test