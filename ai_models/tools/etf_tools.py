from langchain.tools import tool

@tool

def get_etf_data(ticker: str):
    """
    Retrieve ETF information by ticker.

    Args:
        ticker (str):
        ETF symbol such as VOO, VTI, VWRA

    Returns:
        dict:
        ETF details  
    
    """

    etf_db = {
        "VOO": {
            "ticker":"VOO",
            "name":"Vanguard S&P 500 ETF",
            "expense_ratio":"0.03%",
            "category":"Large Blend",
            "investment_style":"Passive Index Investing"
        },
        "VTI":{
            "ticker":"VTI",
            "name":"Vanguard Total Stock Market ETF",
            "expense_ratio":"0.03%",
            "category":"Total Market",
            "investment_style":"Passive Index Investing"
        },
        "VWRA":{
            "ticker":"VWRA",
            "name":"Vanguard FTSE All World ETF",
            "expense_ratio":"0.22%",
            "category":"Global Equity",
            "investment_style":"Passive Index Investing"
        },
        "QQQM":{
            "ticker":"QQQM",
            "name":"Nasdaq Quality top100 shares",
            "expense_ratio":"0.34%",
            "category":"US Equities of Nasdaq Index",
            "investment_style":"Active Index Investing"
        },
        "SOXX":{
            "ticker":"SOXX",
            "name":"iShares Semiconductor ETF",
            "expense_ratio":"0.56%",
            "category":"US Semiconductor Equities",
            "investment_style":"Active Index Investing"
        }

    }

    return etf_db.get(
        ticker.upper(),
        {
            "error": f"ETF {ticker} not found"
        }
    )