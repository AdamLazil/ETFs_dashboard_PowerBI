# Sample of used DAX measures

This project uses several DAX measures to evaluate the performance and risk of ETF funds.  
Below is a categorized list of the most important measures.

---

## 📈 Performance Metrics

### CAGR (Compaund Annual Growth Rate)

```DAX
CAGR :=
VAR StartValue =
    CALCULATE(
        FIRSTNONBLANK(price_merged_data[Price], 1),
        ALL(price_merged_data)
    )
VAR EndValue =
    CALCULATE(
        LASTNONBLANK(price_merged_data[Price], 1),
        ALL(price_merged_data)
    )
VAR Years =
    DATEDIFF(
        MIN(price_merged_data[Date]),
        MAX(price_merged_data[Date]),
        YEAR
    )
RETURN
    (EndValue / StartValue) ^ (1 / Years) - 1
```

### Annual Return

```DAX
Performance_1Y :=
PRODUCTX(
    FILTER(
        price_merged_data,
        price_merged_data[Date] > EDATE(MAX(price_merged_data[Date]), -12)
    ),
    1 + price_merged_data[Change %]
) - 1

```

### Performance 3Y

```DAX
Performance_3Y :=
VAR LastDate = MAX(price_merged_data[Date])
VAR StartDate = EDATE(LastDate, -36)
RETURN
PRODUCTX(
    FILTER(
        price_merged_data,
        price_merged_data[Date] > StartDate &&
        price_merged_data[Date] <= LastDate
    ),
    1 + price_merged_data[Change %]
) - 1
```

## 💣 Risk Metrics

### Volatility (Annualizied Standard Deviation)

```DAX
AnnualizedVolatility :=
VAR DailyStd =
    STDEVX.P(
        VALUES(price_merged_data[Date]),
        price_merged_data[Change %]
    )
RETURN
    DailyStd * SQRT(252)
```

### Maximum Drawdown

```DAX
MaxDrawdown :=
VAR CumReturn =
    CALCULATE(
        PRODUCTX(
            FILTER(
                ALL(price_merged_data),
                price_merged_data[Date] <= MAX(price_merged_data[Date])
            ),
            1 + price_merged_data[Change %]
        )
    )
VAR Peak =
    MAXX(
        FILTER(
            ALL(price_merged_data),
            price_merged_data[Date] <= MAX(price_merged_data[Date])
        ),
        PRODUCTX(
            FILTER(
                price_merged_data,
                price_merged_data[Date] <= EARLIER(price_merged_data[Date])
            ),
            1 + price_merged_data[Change %]
        )
    )
RETURN
    MINX(VALUES(price_merged_data[Date]), (CumReturn / Peak) - 1)
```

## 📊 Risk-adjusted Metrics

## Sharpe Ratio

```DAX
SharpeRatio :=
DIVIDE(
    [CAGR] - 0.02,   -- Risk-free rate (2%)
    [AnnualizedVolatility]
)
```

### Variance of Returns

```DAX
Variance_Returns :=
VAR Mean =
    AVERAGEX(
        VALUES(price_merged_data[Date]),
        price_merged_data[Change %]
    )
RETURN
    AVERAGEX(
        VALUES(price_merged_data[Date]),
        (price_merged_data[Change %] - Mean) ^ 2
    )
```

## 🏆 Ranking Metrics

### Top 3 Funds by CAGR

```DAX
Top3_ISIN_List :=
CONCATENATEX(
    TOPN(
        3,
        Data_Visual,
        [CAGR],
        DESC
    ),
    transformed_data_table[ISIN],
    UNICHAR(10)   -- newline for better formatting
)
```
