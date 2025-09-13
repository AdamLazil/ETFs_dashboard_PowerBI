# Sample of used DAX measures

### Performance

performance_YTD =
VAR LastDate = MAX('price_merged_data'[date])
VAR StartofYear = DATE(YEAR(LastDate), 1, 1)
RETURN
PRODUCTX(
FILTER(
'price_merged_data',
'price_merged_data'[isin] = SELECTEDVALUE('price_merged_data'[isin]) &&
'price_merged_data'[date] >= StartofYear &&
'price_merged_data'[date] <= LastDate
),
1 + 'price_merged_data'[Change %]
) - 1

### CAGR (Compaund Annual Growth Rate)

CAGR =
VAR FirstDate = MIN('price_merged_data'[date])
VAR LastDate = MAX('price_merged_data'[date])
VAR Years = DATEDIFF(FirstDate, LastDate, YEAR)
VAR TotalReturn =
PRODUCTX(
FILTER('price_merged_data',
'price_merged_data'[isin] = SELECTEDVALUE('price_merged_data'[isin])
),
1 + 'price_merged_data'[Change %]
) - 1
RETURN
IF(Years > 0, (1 + TotalReturn) ^ (1 / Years) - 1, BLANK())

### Volatility

Volatility_Annual =
SQRT(252) \* STDEVX.P(
FILTER(
'price_merged_data',
'price_merged_data'[isin] = SELECTEDVALUE('price_merged_data'[isin])
),
'price_merged_data'[Change %]
)
