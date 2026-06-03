from __future__ import annotations
def format_percentage(x:float) ->str:
    return f"{x:.1%}"   # converts decimal to percentage 
def format_currency(x:float) ->str:
    abs_value=abs(x)
    sign = "-" if x<0 else ""
    if abs_value>=1_000_000_000_000:
        return f"{sign}${abs_value/1_000_000_000_000:.2f}T"
    if abs_value>=1_000_000_000:
        return f"{sign}${abs_value/1_000_000_000:.2f}B"
    
    if abs_value>=1_000_000:
        return f"{sign}${abs_value/1_000_000:.2f}M"
    return f"{sign}${abs_value:,.2f}"

def revenue_cagr(start:float,end:float,years: int) ->float:
    if start <=0 or end <=0:
        raise ValueError("start and end reveune must be positive")
    if years <=0:
        raise ValueError("years should not be 0 or negative ")
    return (end/start)**(1/years)-1
def margin(fcf:float,revenue:float) ->float:
    if revenue ==0:
        raise ValueError("Revenue cannot be zero when calculating margin")
    return fcf/revenue