from langchain.tools import tool
import yfinance as yf

@tool
def get_market_data(symbol: str):
    """
    Retrieve market data for a financial instrument.

    Args:
        symbol (str):
        Financial symbol like AAPL, MSFT, VTI, VOO

    Returns:
        dict:
        Market information  
    
    """

    instrument = yf.Ticker(symbol)
    info = instrument.info

    market_data = {

        "symbol":info.get("symbol"),
        "name":info.get("longName"),
        "instrument_type":info.get("quoteType"),
        "current_price":info.get("regularMarketOpen"),
        "currency": info.get("currency")
    }

    return market_data

if __name__=="__main__":

    result = get_market_data.invoke(
        {
            "symbol": "NVDA"
        }
    )

    print(result)