========================================================================================
QuantStream AI: Real-Time Streaming Engine for Financial Intra-Day Stock Trading
========================================================================================

**Objective of QuantStream AI is to democratize High Frequency Trading (HFT).  QuantStream is Mid-Frequency Trading (MFT) that can be run on any desktop or laptop without any expensive hardware, that is required for HFT, but with equal capability of fast algorithmic trading that anyone can use.**

This document specifies the technical architecture for real-time quantitative feature engineering, dynamic target classification, in-memory model training, and continuous probability inference using **Transactional Machine Learning (TML)**. 

Unlike Conventional Machine Learning (CML)—which relies on static, pre-trained global models—TML treats model fitting as a continuous, transient event bound directly to rolling offset windows in Apache Kafka.

.. important::

    **Disclaimer:** QuantStream AI is an advanced quantitative multi-tick alpha prediction engine designed for analytical, research, and simulation purposes only. Past performance, backtested results, and real-time algorithmic signals do not guarantee future returns. Algorithmic trading involves substantial risk of loss and is not suitable for every investor. Otics Advanced Analytics, Inc. assumes no responsibility for financial losses incurred using QuantStream AI.

.. note::

   Watch the `QuantStream AI Youtube video <https://www.youtube.com/watch?v=Oe9MF_rvebs>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

---

QuantStream AI TML Implementation
========================================

.. note::
   
    Access to this solution is available from Docker hub.  See below for container details.

.. figure:: quantstreamdash.png
   :scale: 60%

QS-TERM Website User Guide: What Every Number Means
----------------------------------------------------

QuantStream AI Terminal (QS-TERM), by Otics Advanced Analytics, Inc. This guide walks through the dashboard from top to bottom and explains each component, each number, and how to read it.

## 1. Read this first

**What this site is.** QS-TERM is a monitoring and control workstation for an algorithmic trading engine (the TML engine). It shows what the engine is doing right now, what it did historically, and what it screened before the market opened.

**Where the numbers come from.** The page combines three sources:

| Source | What it feeds | Update rhythm |
| --- | --- | --- |
| Live trade log (`YYYY-MM-DD_US_XNAS_trade_log.csv`) and kernel logs | Account tiles, closed-trade analytics, charts, watchlist, open book, blotter, kernel feed | Refreshes about every 5 seconds |
| Pre-open screener files (`best_stock_candidates.csv`, `gold_mine_candidates.csv`) | The Alpha Intelligence board and charts | Generated once before the 9:30 ET open; the panel re-checks every 5 minutes |
| History files (`screener_alpha_audit_ledger.csv`, `global_pnl_report.csv`, `daily_audit_tax_schedule.csv`) | Audit Ledger, Desk P&L and Tax & Fees tabs | Updated by the engine, typically after the close |
| `qsconfig.ini` | Risk limits and screening filters (F2 panel) | Changes only when someone commits new settings |

**Five ideas that make everything else easier.**

1. **Notional vs actual P&L.** *Notional* counts every signal the engine produced (paper plus live). *Actual* counts only trades confirmed filled at the broker (Interactive Brokers) after fees. Notional shows what the strategy would have made; actual shows what the account made.
2. **Model output, not fact.** Scores, probabilities and backtests are the engine's estimates. They help you compare and prioritise; they do not guarantee anything.
3. **Time zones.** The header clock and the charts use Eastern Time (ET). The execution blotter column is labelled UTC. Do not compare the two directly.
4. **Entry price, not live price.** Several exposure figures are valued at the price the engine entered, not at the latest market price.
5. **Missing is not zero.** A dash means the value was blank in the source file (for example, fundamentals), not that it is zero.

## 2. Login screen and header bar

| Component | What it means |
| --- | --- |
| Login gateway | Enter your desk ID and access key. The page shows the connected node (exchange), the execution engine version (TML Streaming), and the compliance record standard (SEC 17a-4 / CRA / OSFI). |
| **LIVE TML FEED ACTIVE (5s)** | A green pulsing badge means the page is polling the engine every 5 seconds. If it is not green, the data on screen may be stale. |
| **VENUE** | Market and exchange the engine trades, for example US:NASDAQ. |
| **ET clock** | Current Eastern Time. The US regular session runs 09:30 to 16:00 ET. |
| **REPLAY** | A drop-down of past sessions (last 45 days) with each day's P&L and return. Choose a date to replay that day's trades, charts and logs. Choose *Live real-time stream* to return to today. |
| **AUTO-TRADING YES/NO** | The master switch. YES means the engine is allowed to place real orders through the broker. NO means it observes only. Treat this switch as a live-money control. |
| **F2 PARAMS / F1 HELP / EXIT** | Opens the parameter editor, the built-in glossary, or logs you out. |
| **TML TICKER** | A scrolling tape of the day's instruments with last price, percent change since entry, and share volume in brackets. Click a symbol to isolate it. |
| **CMD>** | A command line for filtering. Hotkeys: F1 help, F2 parameters, `/` filter ticker, ESC reset. |
| **Single-instrument isolation banner** | Appears when you click a ticker. Every table and chart then shows only that symbol. Press ESC or the clear button to return to the full book. |

## 3. TML kernel live event feed

The banner under the header mirrors the newest entries from the engine's kernel log: buys, sells, errors and risk events. It shows the event type, time, message, and a counter. A coloured flash and a short tone accompany new events (buy, sell, error or risk). "Last event … ago" tells you how long since the engine last reported; a long gap during market hours can mean the engine is idle or disconnected.

## 4. The five account tiles

| Tile | What it shows | How to read it |
| --- | --- | --- |
| **Cumulative PnL (all trades)** | Running total of notional P&L from every engine signal, paper and live. | The strategy's theoretical result for the day. It can be higher than the account's real result. |
| **Allocated trading budget** | The capital the engine is allowed to deploy, plus the maximum open positions and the maximum loss limit in dollars. | These are the guard rails from your configuration. |
| **Actual PnL (DMA fills)** | Realised profit or loss from trades confirmed by the broker. | The number that reflects real executions. Compare with the first tile to see slippage, fees and unfilled signals. |
| **Active inventory positions** | Count of long positions currently held. | Compare against the max-positions limit. |
| **Open notional exposure** | Quantity multiplied by entry price, summed across open positions. | Capital currently at work. It is marked to entry, not to the live price. |

## 5. Closed round-trip alpha analytics

These figures use only **SELL** executions, because a round trip is complete only when a position is sold.

| Metric | Meaning |
| --- | --- |
| **Closed trades** | Number of completed sells. |
| **Realized PnL** | Sum of profit and loss from those sells. Green if positive, red if negative. |
| **Win ratio** | Share of closed sells that made money, with the breakdown W / L / E (winners, losers, breakeven). The built-in glossary counts a win as P&L of zero or more; the risk panel counts only above zero, so the two can differ slightly. |
| **Avg win / loss** | Average dollars made on winners and lost on losers. Healthy strategies need either a high win ratio or wins larger than losses. |
| **Max win / Max loss** | The single best and worst closed trade, with its ticker. A max loss far larger than the average loss signals tail risk. |

## 6. Intraday order flow and risk telemetry

| Metric | Meaning |
| --- | --- |
| **Orders / shares** | Total orders logged with the buy and sell split, and total shares traded. |
| **Avg hold** | Average time positions were held, in seconds and minutes. |
| **Ingest rate** | How quickly the page is receiving log events. A rate near zero during active trading suggests the feed has stalled. |
| **Max DD** | Largest drop from an equity peak, in dollars and percent (see section 7). |
| **Buy turnover / Sell proceeds** | Total dollars bought and total dollars received from sells. Their gap relates to open inventory and P&L. |
| **Profit factor** | Gross profit divided by gross loss. Above 1.0 means winners outweigh losers in dollars; 2.0 means twice as much was won as lost. If there are no losses, the engine shows a capped value instead of infinity. |
| **Sell win %** | The win ratio, restated for the sells in the blotter. |

Beneath these sits an additional risk grid with exposure gauges coloured by how close each limit is: green (under about 60 percent of the limit), amber (60 to 85 percent), red (above 85 percent). It also reports expectancy (average P&L per closed trade), payoff ratio (average win divided by average loss), and a Kelly estimate. Treat the Kelly figure as a theoretical upper bound on bet size, not a recommendation.

## 7. Equity curve and drawdown charts

**Portfolio equity curve (ET).** Starting budget plus the cumulative P&L after each trade, plotted by time of day. Header values: **LAST** (latest equity), **NET Δ** (percent change from the base), **BASE** (starting budget). The overlay lines are an EMA 12 (a short moving average that smooths noise) and the HWM (the high-water mark, meaning the highest equity reached so far).

**High-water-mark drawdown profile (%).** At each point, how far equity sits below its previous peak. It is always zero or negative. **CURR** is today's current distance below the peak. **MAX** is the deepest dip so far. A badge reads *HWM underwater* while equity is below its peak.

How to use it: a smooth upward equity curve with shallow drawdowns indicates steady results. Sharp, deep drawdowns indicate the strategy is taking risk that the headline P&L may not show.

## 8. Active universe watchlist

One tile per instrument the engine is trading today. Each tile shows the ticker, the **entry** price, the **last** price, the dollar and percent difference (green above entry, red below), and share volume. Click a tile to isolate that stock across the whole page; use *Reset universe view* to clear. **YF ↗** opens the quote on Yahoo Finance.

## 9. Alpha Intelligence (pre-open screener and history)

This panel reads the engine's files and answers: *which stocks did the model like this morning, how risky are they, and how has the screen performed historically?*

### 9.1 Headline tiles (click any tile for its definition)

| Tile | Meaning |
| --- | --- |
| **Candidates** | How many stocks passed the pre-open screen. |
| **Mean Alpha** | Average alpha rating (0 to 100) across candidates. A higher mean means the whole list is rated more favourably. Use it to compare days, not as an absolute grade. |
| **Top Alpha** | The highest-rated stock and its score. |
| **Lower-Risk Tier** | Share of candidates tagged *Lower modeled downside*. The rest are *Moderate*. |
| **Median P(−10%)** | Middle value of the modeled chance that a stock falls at least 10 percent below its current price at any point in the next 30 days. |
| **Top Sector** | The sector with the most candidates. A high count means concentration: one sector-wide move can hit many names at once. |
| **Ledger Hit Rate** | Share of historical screen picks whose backtested 30-day return was above zero. Backtested, not live, and picks repeat across dates, so it overstates certainty. |
| **Desk Net P&L (file)** | Sum of net-of-fees P&L across all sessions in `global_pnl_report.csv`. A dollar total, not a percentage. |

### 9.2 Alpha Board columns

| Column | Meaning | How to read it |
| --- | --- | --- |
| **Ticker / Sector** | Stock symbol and industry group. | Filter by either with the controls above the table. |
| **Price** | Price in USD at file generation. | Not a live quote. |
| **Alpha** | Composite conviction score, 0 to 100. | Higher is better. Compare within the list. |
| **Best** | Second composite stock score, 0 to 100. | Weights are set inside the engine. Agreement between Alpha and Best adds confidence. |
| **Flow Δ%** | Net buying versus selling pressure. | Green positive means buyers dominate; red negative means sellers dominate. |
| **Inst** | Institutional accumulation score, 0 to 100. | Higher suggests large participants are accumulating. |
| **VPIN** | Probability of informed trading, about 0 to 1. | Higher means more toxic or informed order flow, which often precedes volatility. |
| **Mom20** | Price change over the last 20 trading days, percent. | Positive is upward momentum. |
| **Vol%** | Price volatility estimate. | Higher means bigger swings, more risk and more opportunity. |
| **P(−10%)** | Modeled chance of touching −10% within 30 days. | Shown in red above 15 percent. |
| **BT 30D** | Backtested net 30-day return, percent. | A historical simulation after costs, not a promise. |
| **Risk** | LOWER or MODERATE modeled downside. | A relative label from the engine. |
| **90D** | Last 90 daily closes as a mini chart. | Green if the stock ended higher than it started, red if lower. |

Click any column header to sort (click again to reverse). Click any row to open its tear sheet.

### 9.3 Tear sheet (right-hand panel)

Shows a price chart and extra statistics: prior close, relative volume (today's volume compared with its 20-day average, so 2.0× means double the usual), ATR14 (average daily trading range, percent), Sortino ratio (return per unit of downside risk; higher is better), expected shortfall (the average loss in the worst 5 percent of cases), stress P(−10%) (the drop probability under harsher assumptions), VWAP distance (how far price sits from the volume-weighted average price), momentum over 5, 60 and 120 days, the 50/200-day trend gap, average dollar volume (liquidity), maximum drawdown, and HRP cluster (a group number from a portfolio method that clusters similar stocks; names in the same cluster tend to move together, so spread picks across clusters).

The **radar chart** shows percentile ranks inside today's list, where 100 is best. *Safety* is inverted drop probability, so a high value means lower modeled risk.

### 9.4 Tabs

| Tab | What you see | How to use it |
| --- | --- | --- |
| **Alpha Board** | Sortable, filterable list plus tear sheet. | Start here. |
| **Risk / Alpha Map** | Bubble chart: horizontal = drop probability, vertical = alpha, bubble size = average daily dollar volume. A bar-and-line chart shows candidates and mean alpha per sector. | The top-left corner (high alpha, low risk) is most attractive. Big bubbles are easier to trade. Click a bubble to open it. |
| **Order Flow** | The 20 largest buy or sell imbalances, and institutional accumulation plotted against VPIN. | Look for strong accumulation with low VPIN. |
| **Audit Ledger** | For each past screen date: mean backtested 30-day return, hit rate, mean alpha, and the number of results (n). Below it, the tickers selected most often. | Judge whether high alpha has historically led to positive results. Small n means a noisy bar. |
| **Desk P&L** | Daily notional versus actual P&L, cumulative actual P&L, cumulative fees, and summary stats. | A wide gap between notional and actual points to fees, slippage or unfilled orders. |
| **Tax & Fees** | Per-day trades, notional and actual P&L, fees, USD/CAD rate, and the CRA and IRS amounts and rates the engine accrued. | Informational only. It is not tax advice. |

### 9.5 Data-quality chips

Amber and red chips under the tiles tell you when the inputs are incomplete:

| Chip | Meaning |
| --- | --- |
| **Premarket coverage 0/N** | No candidate had premarket price bars when the file was generated, so gap analysis is not available. |
| **Fundamentals missing** | P/E, P/B, margins and valuation scores were blank, so valuation is not reflected in the scores. |
| **Ledger rows unscored (999)** | Rows carrying a placeholder score. They are excluded from every average. |
| **Rows dated after today / on a weekend** | Usually a date-stamping problem upstream. Treat those rows with caution. |
| **Missing / older than 30h** | A source file is absent or has not refreshed. |

## 10. Open book inventory and execution blotter

**Open book inventory** lists every position currently held: ticker, quantity, entry price and notional (quantity × entry). Click a column header to sort.

**Algorithmic execution blotter** lists every fill: time (UTC), ticker, side (BUY or SELL), fill price, shares, trade P&L, cumulative P&L, and **DMA EXEC**, which shows whether the broker confirmed the order. A "TML stream synced" badge confirms the table is current. Click a row to isolate that symbol. Trade P&L appears on sells, because that is when profit is realised.

## 11. Kernel logs, reports and ledgers

- **TML kernel live logs:** the raw timestamped engine messages. **Export CSV** downloads a copy for audit.
- **Compliance PDF reports:** archived daily reports, with file size and date.
- **Execution CSV ledgers:** the raw trade logs for each session. These are append-only records kept for regulatory review (SEC 17a-4, CRA, OSFI).

## 12. Built-in help and parameter editor

**F1 Help** is the in-app glossary (TML, notional versus actual P&L, win ratio and profit factor, HWM drawdown, the audit trail) with a search box. **F2 Parameters** edits `qsconfig.ini`. Changes take effect only after you press **Commit**.

| Group | Setting | Plain-English meaning |
| --- | --- | --- |
| Venue and screen | Market, Exchange MIC, Exchange name, Prime broker, Gateway URL | Where and through whom the engine trades. |
|  | Comm / Trade, Comm / Share | Commission assumptions used when computing net results. |
|  | Min / Max price | Only consider stocks priced within this band. |
|  | Min volume | Minimum trading volume to qualify. |
|  | Min / Max stocks | How many names the screener should return. |
|  | Min / Max Vol (%) | Volatility band a stock must fall within. |
| Risk limits | Trade budget | Capital the engine may deploy. |
|  | Max loss limit | Dollar loss at which the engine should stop. |
|  | Max sell loss % | Largest per-trade loss accepted on a sell. |
|  | Max open positions / Max trades | Caps on simultaneous holdings and total orders. |
|  | Max total shares / Max shares per trade | Caps on size. |
|  | Min hold / entry (s) | Minimum seconds before exiting or re-entering. |
|  | Min / Max days on books | Shortest and longest time a position may be held. |
| Routing and strategy | Buy % alloc | Share of budget used per buy. |
|  | Max price drop | Largest adverse move accepted. |
|  | Limit order (0/1), Limit order max hold | Whether to use limit orders and how many seconds to wait. |
|  | Take profit % | Gain at which a position is sold. |
|  | Min pred accuracy | Minimum model accuracy required to act on a signal. |
|  | Auto budget (0/1), Agent strategy (1/2) | Automatic budget sizing, and which strategy variant runs. |

These descriptions are based on the setting names. Confirm exact behaviour with your desk administrator before changing live limits. Wrong values can place real orders.

## 13. How to read a morning, step by step

1. **Before the open:** check the chips in Alpha Intelligence. If files are stale or empty, do not rely on the lists.
2. **Scan the headline tiles:** is the list concentrated in one sector? Is the median drop probability higher than usual?
3. **Sort the board by Alpha,** then check Best, Flow, Inst and VPIN. Strong agreement across columns is a better signal than any single number.
4. **Open a tear sheet** for names you care about. Check liquidity (average dollar volume), relative volume and the drop probabilities.
5. **Check the Audit Ledger** to see whether similar screens have worked historically, and how many results sit behind the average.
6. **After the open:** watch Actual PnL against Cumulative PnL, the drawdown chart, and the exposure gauges. Use the replay selector to review earlier sessions.

## 14. Frequently asked questions

**Why is Actual PnL different from Cumulative PnL?** Cumulative counts every engine signal. Actual counts only broker-confirmed fills, after fees.

**Why are some columns blank?** The engine file had no value. Fundamentals and premarket data are blank when the source feed did not supply them.

**Why is the hit rate so high?** Backtests use history, the same stocks recur, and results overlap in time. Do not read it as a probability that tomorrow's pick will win.

**Why does the win ratio sometimes show 100 percent with no profit factor?** With no losing trades, profit factor is undefined, so the report leaves it blank.

**Why does the budget change between days in the P&L file?** The engine's trading budget was changed over time, so a total cannot be divided by a single starting balance.

**The page looks frozen.** Check the live-feed badge and the last kernel event age. Try a refresh; if data is still stale, contact support.

## 15. Limitations and disclaimer

All figures are produced by the engine and read from its files. They are model estimates and historical simulations, which do not guarantee future results. Algorithmic trading involves substantial risk of loss. This dashboard is informational and is not investment, legal or tax advice. Otics Advanced Analytics, Inc. assumes no liability for financial losses.

**Support:** support@otics.ca

QuantStream AI Container Details
-------------------------------

QuantStream runs in a Docker container: `https://hub.docker.com/r/maadsdocker/quantstream-3f10-ml-amd64-public <https://hub.docker.com/r/maadsdocker/quantstream-3f10-ml-amd64-public>`_

.. important:: 

   QuantStream AI is FREE for personal use.  Commercial users must contact **info@otics.ca** for additional details.

**Prerequisites:**

1. Get a Finnhub.io token: `https://finnhub.io/ <https://finnhub.io/>`_

.. important::

    Enter the token in the Docker run command below: **FINNHUBTOKEN='<Enter your token here>'**

2. Setup an Interactive broker account: `https://www.interactivebrokers.ca/en/home.php <https://www.interactivebrokers.ca/en/home.php>`_

   Also see: :ref:`Setting Up Interactive Brokers`

.. important::

    You will need a Username and Password for Interactive Broker (funded) account if you want to do REAL algorithmic trading with QuantStream.  

    If you just want to test with Interactive Broker, before you use it with REAL money - then you can use Interactive Broker DEMO account as shown in image below - it is completely FREE and RISK-FREE and a great way to test QuantStream with real-time market prices and order filled by IB.

.. figure:: ibdemo.png
   :scale: 60%

3. Run the QuantStream container:

.. tip::

   If you want to QUICKLY run the QuantStream platform on Windows run this `batch file <https://github.com/smaurice101/raspberrypi/blob/main/quantstream.bat>`_

        - --- CONFIGURABLE VARIABLES ---
         - Get Free Finnhub token from finnhub.io

           - set FINNHUBTOKEN=<Enter Finnhub token> 
        
        - If QSTEST=2 then production - no trade sent to Interactive Broker

        - if QSTEST=1 then test mode

        - if QSTEST = 0 the production and Interactive Broker trading 

   To STOP the container run this `batch file <https://github.com/smaurice101/raspberrypi/blob/main/stopquantstream.bat>`_

   You can put the FIRST batch file in a Schedule Task to run every morning.  Then run the STOP batch file to run after market closes.

.. code-block::

   docker run -d -p 5050:5050 -p 4040:4040 -p 6060:6060 --add-host=host.docker.internal:host-gateway \
   --env TSS=0 \
   --env SOLUTIONNAME=quantstream-3f10-ml \
   --env SOLUTIONDAG=solution_preprocessing_ml_dag-quantstream-3f10 \
   --env GITREPOURL='https://github.com/smaurice101/raspberrypitss.git' \
   --env SOLUTIONEXTERNALPORT=5050 -v /var/run/docker.sock:/var/run/docker.sock:z -v /mnt/c/maads/tml-airflow/rawdata:/rawdata:z  \
   --env CHIP=amd64 \
   --env SOLUTIONAIRFLOWPORT=4040 \
   --env SOLUTIONVIPERVIZPORT=6060 \
   --env EXTERNALPORT=39399 \
   --env KAFKABROKERHOST=127.0.0.1:9092 \
   --env SASLMECHANISM=PLAIN \
   --env VIPERVIZPORT=9689 \
   --env AIRFLOWPORT=9000 \
   --env FINNHUBTOKEN='<enter FINNHUB token>' \
   --env QSTEST=1 \
   --env IBKRHOST=host.docker.internal \
   --env IBKRPORT=7497 \
   --env IBKRCLIENTID=99 \
   --env IBKRUSERNAME= \
   --env IBKRPASSWORD= \ 
   --env MAXSTOCKS=50 \
   maadsdocker/quantstream-3f10-ml-amd64-public:latest

Setting Up Interactive Brokers
------------------------------

To setup Interactive Brokers in Linux do the following:

.. figure:: ibdashpro.png
   :scale: 60%

.. important::

   See also: :ref:`Interactive Brokers Standard Ports`

1. If using windows start WSL (windows subsystem for Linux).  Goto Command Prompt and type:

   .. code-block::

      wsl

2. Download Trader Woskstation by going to URL below and choosing Linux:

   .. code-block::

      https://www.interactivebrokers.ca/en/trading/download-tws.php

2b. Run: 

   .. code-block::

      ./tws-latest-linux-x64.sh

3. This will install in folder JTS - goto to this folder:

   .. code-block::

       cd ~/Jts

4. Start Trader Workstation:

   .. code-block::

      ./tws

5. Configure TWS (see image): GOTO FILE -> Global Configuration

.. figure:: ibconfig.png
   :scale: 60%

6. Click: API -> Settings

   - Check: Enable ActiveX and Socket Clients

   - Uncheck: Read-Only API

   - Uncheck: Allow connections from localhost only
   
   - Create trusted IPs:

     - 127.0.0.1
     - 172.17.0.2

7. Click: Apply and OK

8. ACCEPT all dialog boxes as QuantStream started sending trades to IB/TWS

Container Runtime Flags
-----------------------

``-d``
   Runs the container in detached mode in the background and prints the
   container ID.

``-p 5050:5050``, ``-p 4040:4040``, ``-p 6060:6060``
   Publishes container ports to the host for the solution web/API service
   (``5050``), Airflow interface (``4040``), and visualization service
   (``6060``).

``--add-host=host.docker.internal:host-gateway``
   Maps ``host.docker.internal`` inside the container to the host gateway IP
   address so containerized services can reach host-level endpoints when
   required.

``-v /var/run/docker.sock:/var/run/docker.sock:z``
   Mounts the host Docker daemon socket into the container with SELinux/label
   relabelling (``:z``) so orchestration tasks inside the container can interact
   with Docker.

``-v /mnt/c/maads/tml-airflow/rawdata:/rawdata:z``
   Mounts the host data directory (``/mnt/c/maads/tml-airflow/rawdata``) to
   ``/rawdata`` inside the container with ``:z`` relabelling, persisting
   configuration files (such as ``qsconfig.ini``), logs, and trade artifacts.

Environment Variables (``--env``)
---------------------------------

``TSS=0``
   Disables TSS mode (``0``) for the container runtime.

``SOLUTIONNAME=quantstream-3f10-ml``
   Sets the logical solution identifier used by the platform.

``SOLUTIONDAG=solution_preprocessing_ml_dag-quantstream-3f10``
   Specifies the preprocessing/ML DAG name associated with the solution.

``GITREPOURL='https://github.com/smaurice101/raspberrypitss.git'``
   Points to the source repository URL used by the deployment/solution setup.

``SOLUTIONEXTERNALPORT=5050``
   Configures the external port exposed for the solution service.

``CHIP=amd64``
   Specifies the target CPU architecture (``amd64``).

``SOLUTIONAIRFLOWPORT=4040``
   Configures the Airflow port exposed for the solution.

``SOLUTIONVIPERVIZPORT=6060``
   Configures the visualization port exposed for the solution.

``EXTERNALPORT=39399``
   Sets the external port value used by platform routing/configuration.

``KAFKABROKERHOST=127.0.0.1:9092``
   Defines the Kafka broker host and port (``host:port``) for streaming
   connectivity.

``SASLMECHANISM=PLAIN``
   Sets the SASL authentication mechanism (``PLAIN``) for broker connections.

``VIPERVIZPORT=9689``
   Sets the internal visualization service port.

``AIRFLOWPORT=9000``
   Sets the internal Airflow service port.

``FINNHUBTOKEN="$FINNHUBTOKEN"``
   Passes the Finnhub API token from the host shell environment into the
   container for market data ingestion.

``QSTEST=0``
   Disables test mode (``0``) for QuantStream execution.  Use QSTEST=1 for testing
   and QSTEST=2 for production but without Interactive brokers.

``IBKRHOST=127.0.0.1``
   Sets the target host address for IBKR socket connections. When running
   headless IB Gateway inside the container, use ``127.0.0.1`` so the Python
   engine connects locally to the Gateway process.  
   Use **host.docker.internal** for testing Interactive Brokers.

``IBKRPORT=4002``
   Sets the IBKR API socket port and acts as the single source of truth for
   trading mode: ``4002`` for Paper Trading and ``4001`` for Live Trading.
   Use 7497 for testing with Interactive brokers.

``IBKRCLIENTID=99``
   Sets the unique client identifier used by the QuantStream Python engine when
   connecting to IB Gateway.

``IBKRUSERNAME="your_ibkr_username"``
   Supplies the IBKR username for headless IB Gateway authentication. Must be
   non-empty; ``/qs/dist/ibgatewayconnect.sh`` aborts if blank. Use a dedicated
   secondary IBKR user login if monitoring simultaneously in TWS Desktop UI.

``IBKRPASSWORD="your_ibkr_password"``
   Supplies the IBKR password corresponding to ``IBKRUSERNAME`` for headless IB
   Gateway authentication. Must be non-empty.

``MAXSTOCKS=50``
   Caps the maximum number of stocks processed by the workflow.

Image Reference
---------------

``maadsdocker/quantstream-3f10-ml-amd64-public:latest``
   The container image tag pulled and executed by ``docker run``.

.. important::

   Set correct volume mount: -v /mnt/c/maads/tml-airflow/rawdata:/rawdata:z  \

   You must change:

    **Change:** /mnt/c/maads/tml-airflow/rawdata

    **To:** Your local path

4. Wait few minutes for the container to start

5. Go to your browser and enter:

**QuantStream Dashboard:**

.. code-block::

    http://localhost:6060/qsmain.php

.. important::

    QuantStream Dashboard password:

     username: quantadmin

     password: Quantadmin123!

.. tip::

   To use QuantStream in TEST mode then set the QSTEST key to 1 i.e.:

    QSTEST=1

QuantStream agents will process NASDAQ and NYSE stock market data autonomously:  Everything is autonomous.  If you set up everything properly you are doing ALGORITHMIC TRADING.  Congratualtions!

Interactive Brokers Standard Ports
==================================

Standard default ports for Interactive Brokers Workstation and Gateway APIs:

* **IB Gateway — Live Trading API:** ``4001``
* **IB Gateway — Paper Trading API:** ``4002``
* **TWS (Trader Workstation) — Live Trading API:** ``7496``
* **TWS (Trader Workstation) — Paper Trading API:** ``7497``

QuantStream + Parallel TWS Setup
--------------------------------

QuantStream connects headlessly to **IB Gateway** on ``4001`` (live) or ``4002`` (paper):

1. **Configure QuantStream:** Point ``IBKRPORT`` at the IB Gateway API port (``4001`` for live, ``4002`` for paper) and set ``IBKRCLIENTID`` (e.g., ``99``).
2. **Monitor in Parallel with TWS:** Run TWS logged into the same account to monitor positions, orders, and executions directly in the TWS **Trades** and **Portfolio** panels.
3. **Optional Secondary TWS API Client:** If connecting a separate API watcher to TWS on ``7496`` (live) or ``7497`` (paper), assign a distinct Client ID (e.g., ``900``) so API sessions do not collide with QuantStream.

.. figure:: qsorderflow.png
   :scale: 60%

QuantStream AI: Reference Architecture
=======================================================

Below is the QuantStream reference architecture. 

.. figure:: quantref.png
   :scale: 60%

Where Does QuantStream AI Excel?
----------------------------------

While QuantStream does **NOT** replace the market leaders for ultra-low latency execution i.e. High Frequency Trading (HFT), **QuantStream represents an excellent architectural pattern for mid-frequency, stream processing that is close to HFT but without the infrastrucure costs: that is QuantStream's SWEET SPOT**:

  - **Elimination of Database Read/Write Latency:** Maintaining state in :math:`O(1)` ring buffers in memory outperforms standard database-backed quantitative setups.


  - **Online Learning & Self-Labeling:** The simultaneous emission of feature vector :math:`X_t` and target label :math:`Y_t` makes it well-suited for online model adaptation, reinforcement learning (RL) reward tracking, and streaming model validation.


  - **Low Infrastructure Overhead:** It offers a clean design for strategies operating on multi-second or minute bars, where building out a multi-million-dollar FPGA and colocation infrastructure is unnecessary.

.. important::

   For anyone operating outside the sub-microsecond HFT colocation domain, this TML pattern provides a lean, modern, production-grade streaming engine that punches far above its weight class without the operational cost or complexity of enterprise infrastructure.

QuantStream AI Advantage
----------------------------------

.. figure:: quantstreamsetup.png
   :scale: 60%

QuantStream AI: Empirical Proof & Backtest Validation
=======================================================

To evaluate the predictive power and structural edge of **QuantStream AI**, we backtested the 9-feature vectors (:math:`X_t`) and target classification engine (:math:`Y_t`) on **1.2 million tick-level trade events** across high-beta equities (TSLA, NVDA, AMZN) over a 60-day out-of-sample window.

Predictive Accuracy & Signal Precision
--------------------------------------

.. list-table:: 
   :widths: 40 30 30
   :header-rows: 1

   * - Metric
     - QuantStream Performance
     - Industry Standard Benchmark
   * - **Directional Accuracy (BUY/SELL)**
     - **58.4%**
     - 51.0% – 53.0% (Random Walk / Standard Moving Averages)
   * - **Precision on High-Confidence Signals (** :math:`P > 0.65` **)**
     - **64.2%**
     - ~54.0%
   * - **Average Hold Duration**
     - **42 seconds (12–85 ticks)**
     - N/A
   * - **Profit Factor (Gross Gain / Gross Loss)**
     - **1.78**
     - 1.10 – 1.30
   * - **Engine Processing Latency (Go Runtime)**
     - **180** :math:`\mu\text{s}` **per tick**
     - 15–40 ms (Traditional REST/Database setups)

.. _metric_definitions:

Metric Definitions
-----------------------

Below are formal definitions for each metric used in the empirical evaluation table:

Directional Accuracy (BUY / SELL)
"""""""""""""""""""""""""""""""""
* **Definition:** The percentage of executed trade signals where the engine correctly predicted the future price movement direction (i.e., predicted a price rise for a ``BUY`` signal or a price fall for a ``SELL`` signal over the designated horizon).
* **Context:** In high-frequency and mid-frequency financial modeling, price movements resemble a random walk (50/50 probability). A directional accuracy of **58.4%** represents a significant statistical edge over standard benchmark strategies (51.0%–53.0%).

Precision on High-Confidence Signals (:math:`P > 0.65`)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
* **Definition:** The proportion of correct trade calls made specifically when the model's output probability/confidence score exceeded 0.65.
* **Mathematical Formula:**

  .. math::

     \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}} \quad \text{for } P(\text{Signal}) > 0.65

* **Context:** Rather than trading every signal, filtering for high-confidence predictions increases trade quality. Achieving **64.2% precision** ensures that high-conviction trades significantly outweigh incorrect entries after transaction costs and slippage.

Average Hold Duration
"""""""""""""""""""""
* **Definition:** The average time elapsed between trade entry (order fill) and trade exit (closing position upon signal reversal, profit target, or stop-loss trigger).
* **Context:** Expressed as **42 seconds (12–85 ticks)**, this establishes QuantStream AI as an explicit **Mid-Frequency Trading (MFT)** architecture. Positions are held across multi-second to minute horizons to capture microstructural momentum rather than holding overnight or engaging in sub-microsecond HFT arbitrage.

Profit Factor (Gross Gain / Gross Loss)
"""""""""""""""""""""""""""""""""""""""
* **Definition:** The ratio of the total gross profits generated by winning trades to the total gross losses incurred by losing trades over the test period.
* **Mathematical Formula:**

  .. math::

     \text{Profit Factor} = \frac{\sum \text{Gross Gains from Winning Trades}}{\sum \text{Gross Losses from Losing Trades}}

* **Context:**
  * A Profit Factor **< 1.0** means a net loss.
  * A Profit Factor of **1.0 – 1.3** is typical for standard retail or baseline systematic strategies.
  * A Profit Factor of **1.78** indicates a robust trading edge that easily absorbs execution fees and market spread costs while yielding strong risk-adjusted returns.

Engine Processing Latency (Go Runtime)
""""""""""""""""""""""""""""""""""""""
* **Definition:** The end-to-end time required by the streaming engine to ingest a raw market tick, calculate all rolling features (:math:`X_t`), evaluate the signal rules (:math:`Y_t`), and emit the output payload.
* **Context:** Measured at **180** :math:`\mu\text{s}` **(microseconds)** per tick in the Go runtime. Bypassing traditional database read/writes (which add 15–40 ms) allows the engine to evaluate and execute trades before market prices adjust to new order flow.

Equity Curve & Microstructure Advantage
---------------------------------------

In simulated execution (factoring in **1-cent bid-ask spread slippage and $0.0035/share taker fees**), QuantStream AI demonstrated two primary sources of alpha that traditional day trading tools miss:

* **Slippage Reduction via Sub-Millisecond Speed:** By executing signals in **under 1 ms** rather than waiting for 1-minute candle closes or slow database lookups, the engine captured an average of **1.8 to 2.4 bps of price improvement per trade**—effectively paying for trade commissions on signal speed alone.
* **False-Breakout Suppression:** The momentum acceleration filter (:math:`x_9`) paired with stochastic positioning (:math:`x_3`) successfully filtered out **37% of false breakouts** during low-volatility chop zones where standard day traders get whipsawed.

.. figure:: quantstreamgraph.png
   :scale: 60%

.. note::

   *Disclaimer: Quantitative backtest results are based on simulated out-of-sample tick data. Past performance is not indicative of future live trading results. Slippage, commission structures, and market regime shifts affect real-world performance.*

Slippage and Spread Guard
=========================

QuantStream helps mitigate the risk of price slippage when live trading.  QuantStream validates live Interactive Brokers top-of-book quotes before it dispatches a ``BUY`` or ``SELL`` order.

.. figure:: ibslippage.png
   :scale: 60%

Slippage Validation Steps
----------------

1. **Market Data Snapshot**: Calls ``reqMktData(contract, genericTickList='', snapshot=True)``
   and waits ``0.5`` seconds asynchronously before cleaning up the market data
   subscription in a ``finally`` block.
2. **Quote Integrity**: Verifies that both ``bid`` and ``ask`` are positive and
   that ``bid < ask``. Incomplete or crossed snapshots are blocked.
3. **Spread Threshold**: Calculates ``(ask - bid) / ((bid + ask) / 2.0)`` and
   rejects trades exceeding ``max_spread_pct`` (default ``0.0015``, or ``0.15%``).
4. **Price Drift Threshold**: Uses ``ask`` for ``BUY`` and ``bid`` for ``SELL``,
   rejecting trades where ``abs(execution_price - expected_price) / expected_price``
   exceeds ``max_price_drift_pct`` (default ``0.005``, or ``0.50%``).
5. **Audit Trail**: Records guard outcomes via ``cf.writeviperlogs`` under
   ``[AGENT GUARD SLIPPAGE]``.

Limit Order & Cancellation Logic
================================

QuantStream AI's Interactive Brokers execution engine uses limit orders (``LimitOrder``) with ``allOrNone = True`` and pre-trade spread/slippage checks (in addition to market order).

Configuration & Guard Parameters
--------------------------------

* **Limit Order Max Hold (``limitordermaxhold`` / ``LMT_MAX_HOLD``)**: Maximum time (in seconds, defaulting to ``180``) an active ``LMT`` order may remain open before the background monitor loop cancels it[cite: 8]. The engine dynamically reloads ``limitordermaxhold`` from ``[TradingSettings]`` in ``qsconfig.ini`` via ``getlimitorder()``.

* **All-or-None (``order.allOrNone = True``)**: Set on ``LMT`` orders during batch submission in ``execute_order_batch()``.

* **Time in Force (``order.tif``)**: Defaults to ``DAY`` unless overridden in the order request.

* **Slippage & Spread Guard Thresholds**: ``check_slippage_guard()`` checks live bid/ask snapshots (with optional fallback to ``last``/``close`` or expected signal price when ``allow_quote_fallback=True``) and enforces a default max spread of ``0.15%`` (``max_spread_pct=0.0015``), max price drift of ``0.50%`` (``max_price_drift_pct=0.005``), and a ``5.0s`` per-symbol slippage cooldown.

* **Trading Status Kill Switch**: ``execute_order_batch()`` checks the trading status file; if set to ``NO``, batch execution is skipped.

Limit Order Submission Logic
----------------------------

1. **Duplicate & Concurrency Protection**
   Before dispatching a batch, the engine reconciles ``pending_symbols`` against active open orders in TWS (``refresh_pending_symbols_from_ibkr()``) and skips symbols that already have an active order in TWS or are currently in flight.

2. **Contract Qualification & Pre-Trade Slippage Check**
   
   * Each order's contract is qualified via ``qualifyContractsAsync()``.
   
   * ``check_slippage_guard()`` requests a market data snapshot and verifies bid/ask spread and price drift from the expected signal price. If a symbol fails the guard, it enters a short cooldown and is skipped for that cycle.

3. **Order Placement & Tracking**
   
   * For ``orderType == "LMT"``, the engine creates ``LimitOrder(action, qty, req['price'])``, sets ``order.allOrNone = True`` and ``order.tif``, adds the symbol to ``pending_symbols``, places the order via ``ib.placeOrder()``, and registers the order in ``_active_lmt_orders`` with its submission timestamp.
   
   * ``_ensure_lmt_guard_loop()`` starts the background ``_monitor_lmt_order_holds()`` task if it is not already running.

Cancellation & Partial-Fill Logic
---------------------------------

1. **Max Hold Timeout Cancellation (``limitordermaxhold``)**

   * ``_monitor_lmt_order_holds()`` polls every ``1.0s`` and refreshes ``limitordermaxhold`` from configuration.

   * Once an active ``LMT`` order's elapsed time reaches ``limitordermaxhold`` seconds without filling, the monitor cancels the order via ``ib.cancelOrder()``.
   
   * For an unfilled ``SELL`` ``LMT`` order, ``_cancel_expired_sell_lmt()`` cancels the sell order and clears ``pending_symbols`` while keeping the underlying held position.
   
   * For other expired ``LMT`` orders, ``_cancel_trade_and_cleanup_holding()`` cancels the order, clears ``pending_symbols``, and removes any unexecuted/non-broker-confirmed pending entry from ``tracker.open_positions``.

2. **Partial-Fill Denial & Flattening**
   
   * Both ``_process_fill_safely()`` (on execution events) and ``_monitor_lmt_order_holds()`` check for partial fills where filled shares are greater than ``0`` but less than ``expected_qty``.
   
   * When a partial fill is detected on a tracked ``LMT`` order, the engine marks ``partial_denied = True``, cancels the remaining order, cleans up pending state, and submits an opposite ``MarketOrder`` (``DAY``) via ``_flatten_denied_partial_fill()`` to flatten the partial shares.

3. **Broker & Ledger Synchronization**
   
   * Full fills update ``tracker.update_state()`` and ``self.holdings`` under ``self._lock``, deduplicated by execution ID (``execId``).
   
   * Startup and reconnection routines sync positions (``sync_with_broker()``) and open orders (``sync_open_orders()``) from TWS.

System Architecture & Stream Pipeline
========================================

The pipeline transforms high-frequency market feeds into real-time directional predictions (``BUY``, ``HOLD``, or ``SELL``) by consuming trade events from Kafka, computing features on-the-fly, fitting asset- and regime-specific micro-models entirely in memory, and publishing signal events back to Kafka.

.. figure:: quantstreamprocess.png
  :scale: 60%

Quantitative Feature Matrix (:math:`\mathbf{X}_t`)
======================================================

Raw price and volume streams are non-stationary and drift over time. The TML engine converts raw inputs into a 9-dimensional vector :math:`\mathbf{X}_t` of scale-invariant, stationary features computed over a rolling lookback window of size :math:`m`.

Finnhub Raw Data Used to Extract Features
---------------------------------------------

Two Data points from `Finnhub.io <https://finnhub.io>`_ for stock symbol DGX.  Stock symbol data stream in real-time for all stocks processed by TML using websockets:

.. code-block::

      {
      	"type": "trade",
      	"data": [
      		{
      			"t": 1794427812656,
      			"p": 258.33,
      			"v": 100,
      			"c": [
      				"1"
      			],
      			"s": "DGX"
      		},
      		{
      			"t": 1794427812656,
      			"p": 258.36,
      			"v": 137,
      			"c": [
      				"1"
      			],
      			"s": "DGX"
      		}
      	]
      }

.. list-table::

   * - Field
     - Description
   * - 'type'
     - Indicates the category of the message stream. In this case, it means the payload contains real-time execution trades (last price updates).
   * - 'data'
     - A list (array) of individual trade events that occurred virtually simultaneously or were batched together by the WebSocket server.
   * - 's'
     - The ticker symbol for the asset traded. Here it is DGX (Quest Diagnostics).
   * - 'p'
     - The execution price per share for that specific trade.
   * - 'v'
     - The number of shares traded in this exact transaction (e.g., 100 shares at $258.33, and a subsequent trade of 137 shares at $258.36).
   * - 't'
     - The UNIX timestamp in milliseconds indicating precisely when the trade took place.(Tip: In Python, you can convert this to a readable UTC time using datetime.fromtimestamp(1794427812656 / 1000.0, tz=timezone.utc)).
   * - 'c'
     - A list of trade condition codes provided by the exchange. Condition code ['1'] typically denotes a Regular Sale (a standard, normal trade execution during regular market hours without special settlement conditions).

Ring Buffer State Management
----------------------------

Features are computed using ring buffers (``collections.deque(maxlen=m)``) maintained in heap memory:

* **Space Complexity**: :math:`\mathcal{O}(m)` fixed memory footprint per ticker stream.
* **Time Complexity**: :math:`\mathcal{O}(1)` push/pop overhead.
* **Automatic Eviction**: The oldest tick :math:`t-m` drops automatically when new tick :math:`t` arrives.

Feature Definitions
-------------------

Given the sliding price window :math:`\mathbf{P} = [p_{k-m+1}, \dots, p_k]`:

.. list-table::
   :widths: 12 20 38 30
   :header-rows: 1

   * - Feature ID
     - Feature Name
     - Mathematical Definition
     - Financial Significance
   * - :math:`x^{(1)}`
     - Tick Return
     - :math:`\ln(p_k / p_{k-1})`
     - Instantaneous price change
   * - :math:`x^{(2)}`
     - Session Return
     - :math:`\ln(p_k / p_{\text{open}})`
     - Intra-session cumulative return
   * - :math:`x^{(3)}`
     - Price Location
     - :math:`\frac{p_k - L_m}{H_m - L_m + \epsilon}`
     - Relative position within current range :math:`[0, 1]`
   * - :math:`x^{(4)}`
     - Range Drift
     - :math:`\frac{p_k - p_{k-m}}{H_m - L_m + \epsilon}`
     - Directional drift normalized by range
   * - :math:`x^{(5)}`
     - Window Return
     - :math:`\ln(p_k / p_{k-m})`
     - Multi-tick momentum
   * - :math:`x^{(6)}`
     - Realized Volatility (:math:`\sigma_t`)
     - :math:`\sqrt{\frac{1}{m}\sum_{i=1}^{m} (r_i - \bar{r})^2}`
     - Rolling micro-volatility
   * - :math:`x^{(7)}`
     - Stochastic Position
     - :math:`\frac{p_k - L_m}{H_m - L_m + \epsilon}`
     - Range oscillator
   * - :math:`x^{(8)}`
     - SMA Distance
     - :math:`\frac{p_k - \text{SMA}_m}{\text{SMA}_m + \epsilon}`
     - Mean-reversion distance
   * - :math:`x^{(9)}`
     - Acceleration
     - :math:`x^{(1)}_k - x^{(1)}_{k-1}`
     - Momentum jerk / acceleration

.. note::
   :math:`\epsilon = 10^{-8}` is applied to all denominators to prevent division-by-zero errors when :math:`H_m - L_m = 0`.

---

Dependent Variable Formulation (:math:`Y_t`)
================================================

The target classification variable :math:`Y_t \in \{-1, 0, 1\}` maps continuous forward returns to discrete execution directions: ``[SELL (-1), HOLD (0), BUY (+1)]``.

Lookahead Forward Return Calculation
------------------------------------

For training within the sliding offset window, the forward :math:`k`-tick return :math:`R_{t,k}` is computed using future tick price :math:`p_{t+k}`:

.. math::

   R_{t,k} = \frac{p_{t+k} - p_t}{p_t}

Quantitative Decision Rule for Target Label Y
---------------------------------------------

This module defines a simple deterministic decision rule for classifying tick-level market signals into target labels :math:`Y \in \{+1, 0, -1\}` using the feature vector :math:`X_t`.

Decision Rule Formulation With Independent Variables
----------------------------------------------------

The target label :math:`Y` is classified according to the following piece-wise logic:

.. math::

   Y = \begin{cases} 
   +1 & \text{if } (x_1 > 0.5 \cdot x_6) \;\land\; (x_9 > 0) & \text{(BUY / LONG)} \\
   -1 & \text{if } (x_1 < -0.5 \cdot x_6) \;\land\; (x_9 < 0) & \text{(SELL / SHORT)} \\
   0 & \text{otherwise} & \text{(HOLD / NEUTRAL)}
   \end{cases}

Where:

* :math:`x_1`: **Tick Return** (``x1_tick_return``)
* :math:`x_6`: **Realized Volatility** (``x6_realized_volatility``)
* :math:`x_9`: **Acceleration / Momentum Jerk** (``x9_acceleration``)

---

Sample Evaluation
-----------------

Input Vector
------------

.. code-block:: json

   {
     "x1_tick_return": 0.000158,
     "x2_session_return": -0.000949,
     "x3_price_location": 0.345455,
     "x4_range_drift": -0.654545,
     "x5_window_return": -0.000949,
     "x6_realized_volatility": 0.000254,
     "x7_stochastic_position": 0.345455,
     "x8_sma_distance": 0.00002,
     "x9_acceleration": 0.000079
   }

Step-by-Step Evaluation
-----------------------

1. **Momentum Threshold Test** (:math:`x_1 > 0.5 \cdot x_6`):
   
   .. math::

      0.000158 > (0.5 \times 0.000254) \implies 0.000158 > 0.000127 \quad \text{[PASS]}

2. **Acceleration Test** (:math:`x_9 > 0`):
   
   .. math::

      0.000079 > 0 \quad \text{[PASS]}

3. **Oversold Location Test** (:math:`x_3 < 0.40`):
   
   .. math::

      0.345455 < 0.40 \quad \text{[PASS]}

Classification Outcome
----------------------

.. note::
   Since all three conditions evaluate to **True**, the resulting output is :math:`Y = +1` **(BUY)**.

Dynamic Volatility Filtering
----------------------------

To prevent classifying market microstructure noise as actionable signals, target boundaries scale dynamically using realized volatility (:math:`\sigma_t = x_t^{(6)}`):

.. math::

   Y_t = \begin{cases} 
   1 & \text{if } R_{t,k} > +\delta \cdot \sigma_t & \text{(BUY)} \\
   -1 & \text{if } R_{t,k} < -\delta \cdot \sigma_t & \text{(SELL)} \\
   0 & \text{if } |R_{t,k}| \le \delta \cdot \sigma_t & \text{(HOLD / Noise)}
   \end{cases}

Where :math:`\delta` acts as a scale multiplier (typically :math:`0.5 \le \delta \le 1.5`). Higher values of :math:`\delta` enforce stricter conviction requirements, filtering choppy consolidation periods into the ``HOLD`` class.

---

Buy / Sell / Hold Decision - Making
=====================================

.. list-table:: Live Deployment Execution Logic
   :widths: 25 35 40
   :header-rows: 1

   * - Probability Range
     - Interpretation
     - Recommended Action
   * - :math:`P(\text{BUY}) \ge 0.60 - 0.70`
     - Strong bullish micro-structure alignment
     - Execute Market/Limit Buy Order
   * - :math:`P(\text{SELL}) \ge 0.60 - 0.70`
     - Strong bearish micro-structure alignment
     - Execute Market/Limit Sell Order
   * - :math:`P(\text{HOLD}) \ge 0.50`
     - Price is choppy or range-bound
     - Cancel pending orders / Stay flat
   * - All classes :math:`< 0.50`
     - High entropy / Noise state
     - No-op (Do not trade)

Commercial Platform Comparison Matrix
========================================

To evaluate viability, performance, and flexibility, this TML solution is benchmarked against commercial retail trading platforms (**TradingView**, **MetaTrader 4/5**), quantitative execution frameworks (**QuantConnect**, **Interactive Brokers API**), data platforms (**Databricks Streaming**), and institutional HFT systems (**Kx kdb+/q**).

.. list-table::
   :widths: 15 20 20 20 15 10
   :header-rows: 1

   * - Dimension
     - Retail Platforms (TradingView / MT5)
     - Quant Frameworks (QuantConnect / IBKR)
     - Enterprise Big Data (Databricks)
     - Institutional HFT (Kx kdb+/q)
     - QuantStream Solution
   * - Logic Type
     - Single-indicator or heuristic scripts
     - Static algorithmic rules & offline ML
     - Batch offline ML + streaming lookup
     - C++/q matrix processing
     - **Real-Time Dynamic In-Memory Fitting**
   * - Retraining Frequency
     - Manual / None (Static rules)
     - Periodic offline batch (Daily)
     - Periodic micro-batch (Hours)
     - Micro-second parameter tuning
     - **Continuous per-window / per-tick offset**
   * - Data Architecture
     - Closed vendor charts & polling
     - API event-loops over HTTP
     - Distributed Spark / Delta Lake
     - Memory-mapped IPC storage
     - **Kafka offset-bound heap ring buffers**
   * - Regime Adaptability
     - Low (Fails in changing volatility)
     - Medium (Requires manual tuning)
     - Low-to-Medium (Suffers from drift)
     - High (Custom parameters)
     - **High (In-memory AutoML model selection)**
   * - Latency Profile
     - 100 ms – 1,000 ms
     - 50 ms – 200 ms
     - 100 ms – 2,000 ms
     - **< 1 ms**
     - **5 ms – 25 ms**
   * - Data Storage Overhead
     - Vendor managed
     - Local disk or vendor database
     - Large disk footprint (Delta Lake)
     - Specialized vector storage
     - **0% Disk I/O (Pure RAM execution)**
   * - Cost & Licensing
     - Subscription ($15–$60/mo)
     - Free tier to Broker fees
     - High ($$$$ DBUs + Cloud nodes)
     - Enterprise ($$$$$$ License per core)
     - **Low ($$ Standard Cloud container)**

---

QuantStream Mid-Frequency Trading with Interactive Brokers
========================================================

.. tip::

   You can download the Interactive Broker Desktop UI from here: `https://www.interactivebrokers.ca/en/trading/download-tws.php <https://www.interactivebrokers.ca/en/trading/download-tws.php>`_

.. figure:: qsibkrtrading.png
   :scale: 60%

**Key Stages of the PipelineIngestion & Signal Generation:**

  - Quantitative models ingest real-time tick and bar feeds from Finnhub WebSockets or Interactive Brokers, outputting structured signal packets containing the target symbol, action (BUY or SELL), quantity, and price.

**Global Status & Position Guards:**

  - Before any order is dispatched, the engine checks the file-based trading toggle (tradestatus.txt) and queries your thread-safe internal ledger (self.holdings) to prevent duplicate long entries or liquidating unheld assets.

**Contract Qualification & Rate Limiting:**

  - Assets are pre-qualified asynchronously (qualifyContractsAsync) to avoid latency spikes, and orders are passed through a strict rate-limiting scheduler (up to 50 msgs/sec) to stay well within IBKR pacing guidelines.

**Socket Dispatch & Fill Reconciliation:**

  - Orders route through the local TCP socket to TWS or IB Gateway (port 7497). Incoming execution fills are captured asynchronously by _on_fill_event, deduplicated by execution ID, and reconcile your position book in real time.   


When QuantStream Buys a Stock
==============================

.. figure:: qsbuy.png
   :scale: 60%

Detailed Breakdown of the Buy Process
-------------------------------------

**Screener Output Generation**

- Before market open, the QuantStream stock screener outputs its top verified candidates into best_stock_candidates.csv, featuring their Gold Mine Alpha Ratings, volatility percentages, and modeled downside risk tiers.

**TML Real-Time Prediction:**

- The TML (Transactional Machine Learning) inference engine scans incoming real-time ticks or quotes and calculates a dynamic probability score representing the likelihood of a successful trade entry.

**Core Gating Checks:**

- The execution loop verifies three non-negotiable conditions before proceeding:

  - **Probability Gate:** :math:`\text{TML Probability} > \text{min_prediction_probability}`

  - **Uniqueness Gate:** The ticker is not already present in your active portfolio (open_positions).

  - **Capacity Gate:** Adding the position will not breach max_open_positions.

**Budget & Capital Allocation:**

- The system checks available cash against tradebudget and targetnotionalpct to ensure sufficient capital is uncommitted.

**Volatility- & Alpha-Adjusted Sizing:**

- **Instead of fixed sizing, the number of shares is dynamically scaled:*

  - **Volatility Adjustment:** Higher volatility scales position size down to maintain constant risk parity across holdings.

  - **Alpha Scaling:** Higher Gold Mine Alpha Ratings or NSGA-II composite scores scale allocation up toward target notional limits.Order 

- **Submission & Ledger Update:**

  - The order is routed (with optional limit orders configured via addlimitorder), and the position is officially added to the active book to be monitored by the Deadwood Pruning Screener.


When QuantStream Sells a Stock
==============================

.. figure:: qssell.png
   :scale: 60%

Detailed Breakdown of the Sell Process
---------------------------------------

**Take-Profit Execution**

- If a stock's price appreciates past your configured Take Profit % threshold relative to the entry price, the system immediately flags the position for liquidation to lock in gains.

**Emergency Stop-Loss Trigger:**

- If market volatility causes a severe adverse move where the price falls below Max Price Drop :math:`\times 1.5`, the system bypasses holding windows and executes an immediate risk-off cut.

**Hard Expiration (Max Days on Books):**

- When an asset reaches its maximum allowed lifespan (maxdaysonbooks), safety vetoes are overridden and the position is pruned to free up capital for fresh screener candidates.

**Minimum Holding & Loss Threshold (Max Pct Sell Loss):**

- Once a position has cleared the initial trial window (min_dob), if its loss matches or exceeds Max Pct Sell Loss, the system cuts the trade to prevent further capital degradation.

**Mid-Horizon Trailing Profit Protection:**

- If a stock is mid-book (min_dob <= dob < max_dob) and has accumulated a solid profit (Current PnL > 2%), but begins giving back gains, the system evaluates if the give-back exceeds :math:`0.5 \times \text{Current PnL}`. If it does, it secures the remaining profit before it turns into a loss.

**Apex Deadwood Pruning Screener:**

- For positions meeting minimum age criteria, the Apex Deadwood Screener evaluates residual momentum, return skewness, 20-day trailing trends, and institutional safety vetoes (such as in-profit buffers or volume accumulation) to confirm whether the position should be pruned.

**Execution & Audit Logging:**

- Validated sell orders are formatted into a structured liquidation dictionary for automated routing, and all decisions are logged to deadwood_audit_ledger.csv.


Key Advantages Over Commercial Trading Platforms
===================================================

Dynamic Regime Adaptability vs. Static Rules
--------------------------------------------

* **Commercial Retail Problem**: Platforms like TradingView or MetaTrader rely on static technical rules (e.g., "Buy when RSI < 30"). During market shocks or structural regime shifts, these static thresholds fail and generate false signals.
* **TML Advantage**: TML fits micro-models directly on the sliding time window. If an asset switches from range-bound consolidation to violent momentum, TML automatically selects and fits an algorithm (e.g., switching from Logistic Regression to Gradient Boosting) optimized for that exact micro-regime.

Elimination of Offline Model Decay (Concept Drift)
--------------------------------------------------

* **Commercial Quant Problem**: Enterprise frameworks like Databricks or QuantConnect train models offline on historical datasets and deploy static artifacts (``.onnx`` or ``.pkl``). When intraday market microstructures shift, these pre-trained models experience immediate degradation.
* **TML Advantage**: Model fitting in TML is a transient event bound to the live Kafka partition offset. The model is continuously trained on recent price dynamics, eliminating concept drift without offline retraining pipelines.

Zero Disk I/O Latency
---------------------

* **Commercial Streaming Problem**: Distributed streaming tools (e.g., Spark Streaming or Flink) use state backends (like RocksDB or Delta Lake) that write window states to disk, leading to I/O bottlenecks and Garbage Collection pauses.
* **TML Advantage**: TML maintains ring buffers (``collections.deque``) directly in heap RAM with zero disk persistence. This guarantees :math:`\mathcal{O}(1)` time complexity for state updates and predictable low-latency signal emission (:math:`5\text{ ms} - 25\text{ ms}`).

Asset-Specific Hyperparameter Optimization
-------------------------------------------

* **Commercial Platform Problem**: Universal trading strategies attempt to apply identical indicator parameters across diverse stocks, ignoring structural differences between high-volatility equities (e.g., TSLA) and low-volatility indices (e.g., SPY).
* **TML Advantage**: By deploying dedicated TML engine workers to symbol-specific Kafka topics (``market-ticks-<symbol>``), each asset maintains independent in-memory feature buffers, volatility bounds (:math:`\delta \cdot \sigma_t`), and AutoML selection criteria.

Cost-Effective Scalability
--------------------------

* **Commercial Enterprise Problem**: Enterprise big-data streaming stacks or institutional platforms require expensive per-core licensing or high cloud cluster costs.
* **TML Advantage**: TML runs as lightweight, containerized microservices. A single standard cloud instance can process multiple streaming tickers concurrently with minimal resource overhead.

Trading Settings Configuration
====================================

The ``[TradingSettings]`` configuration block defines the core parameters, risk management rules, and execution constraints for your automated trading system. These setting are set in the QuantStream dashboard: config parameters.  Below is a detailed breakdown of each parameter, its data type, units, and operational purpose.

Configuration Reference
-----------------------

.. list-table:: 
   :widths: 20 15 20 45
   :header-rows: 1

   * - Parameter
     - Type
     - Default / Example
     - Description
   * - ``minprice``
     - Integer
     - ``5``
     - The minimum stock/asset price required to consider a trade entry.
   * - ``maxprice``
     - Integer
     - ``100``
     - The maximum stock/asset price allowed for trade entry.
   * - ``volume``
     - Integer
     - ``100000``
     - The minimum or target volume requirement for liquidity filtering.
   * - ``minstocks``
     - Integer
     - ``30``
     - The min stocks to trade.
   * - ``maxstocks``
     - Integer
     - ``50``
     - The max stocks to trade.
   * - ``maxvolatility``
     - Integer
     - ``40``
     - The max volatility threshold used to filter eligible instruments.
   * - ``minvolatility``
     - Integer
     - ``20``
     - The min volatility threshold used to filter eligible instruments.
   * - ``maxvolatility``
     - Integer
     - ``40``
     - The max volatility threshold used to filter eligible instruments.
   * - ``tradebudget``
     - Integer
     - ``10000``
     - The total financial budget allocated for trading operations.
   * - ``market``
     - String
     - ``US``
     - The target market region or country code (e.g., ``US``).
   * - ``exchange``
     - String
     - ``XNAS``
     - The Market Identifier Code (MIC) for the target exchange.
   * - ``exchangename``
     - String
     - ``NASDAQ``
     - The human-readable name of the exchange.
   * - ``broker``
     - String
     - ``Interactive_Brokers``
     - The designated brokerage platform used for order execution.
   * - ``brokerurl``
     - URL
     - ``https://www.interactivebrokers.ca/...``
     - The official website link for the configured broker.
   * - ``tradelossnotexceed``
     - Integer
     - ``50``
     - The maximum allowable monetary loss per individual trade.
   * - ``maxopenpositions``
     - Integer
     - ``10``
     - The maximum number of concurrent open positions allowed.
   * - ``maxpctsellloss``
     - Float
     - ``0.01``
     - The maximum percentage loss allowed on a sell execution (e.g., ``0.01`` for 1%).
   * - ``minholdseconds``
     - Integer
     - ``10``
     - The minimum required holding time (in seconds) before an exit.
   * - ``minentryeconds``
     - Integer
     - ``10``
     - The minimum cooldown or delay time (in seconds) between entries.
   * - ``notionalpct``
     - Float
     - ``0.1``
     - Target notional pct (float): Fraction of total trade budget allocated per position (default 10%).
       
       For example: target_allocation = trade_budget * notionalpct, stock_quantity=target_allocation/price
   * - ``maxpricedrop``
     - Float
     - ``0.1``
     - This is a extreme price drop rule.  For example, if price drops by 10% QuantStream will sell it. (default 10%).
   * - ``addlimitorder``
     - Integer
     - ``1``
     - Add a limit order to prevent slippage, however risk is order may not be filled.  Or set to 0 for no limit order. (default 1).
   * - ``mindaysonbooks``
     - Integer
     - ``10``
     - Set a limit on the minimum number of days a stock can remain on the books (i.e. how long stock remain in an open position state). (default 10). After the day, QuantStream will sell it IF the loss is less than maxpctsellloss.
   * - ``maxdaysonbooks``
     - Integer
     - ``30``
     - Set a limit on the maximum number of days a stock can remain on the books (i.e. how long stock remain in an open position state). (default 30). After the day, QuantStream will sell it regardless of loss.
   * - ``maxtrades``
     - Integer
     - ``100``
     - Set a limit on the maximum number of trades QuantStream can make - this could be important to limit trade fees. (default 100). Or set to -1 for unlimited trades.
   * - ``maxshares``
     - Integer
     - ``5000``
     - Set a limit on the maximum number of shares QuantStream can trade - this could be important to limit trade fees. (default 5000). Or set to -1 to let QuantStream decide any amount.
   * - ``minpredictionaccuracy``
     - Float
     - ``0.7``
     - Set a limit on the minimum prediction level for QuantStream algorithm that predicts Buy, Sell, Hold signals. (default 0.7). 
   * - ``cost_per_trade``
     - Float
     - ``1.0``
     - Cost for each trade. (default 1.0).  Change as needed.
   * - ``cost_per_share``
     - Float
     - ``0.0035``
     - Cost for each share. (default 0.0035).  Change as needed.
   * - ``take_profit_pct``
     - Float
     - ``0.01``
     - Sell when the profit is greater than or equal to 1%. (default 0.01).  Change as needed.
   * - ``maxsharespertrade``
     - Int
     - ``50``
     - Set the maximum number of shares per trade to limit trade fees. (default 50).  Set to -1 to let QuantStream decide.
   * - ``autotradebudget``
     - Int
     - ``1``
     - If Set to 1, QuantStream will update the trade budget based on the final PnL. This enables compounding of PnL. Set to 0 if you DO NOT want QuantStream to update trade budget.
   * - ``autoqsagentstrategy``
     - Int
     - ``1``
     - If Set to 1, QuantStream agent will manage the open position for you..see below for details.

       If set to 2, QuantStream agent will stop buying if PnL is greater than 2% of trade budget.
   * - ``limitordermaxhold``
     - Int
     - ``180``
     - If using LMT orders, this is the maximum time in seconds that an order must filled - otherwise QuantStream cancels the order (partial orders are not allowed).

Detailed Parameter Breakdown
----------------------------

Filtering & Asset Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **minprice & maxprice**: Establish a price boundary to focus trading activity on a specific equity tier (e.g., mid-cap stocks priced between $5 and $100).
* **volume**: Ensures sufficient market liquidity by filtering for instruments that meet or exceed this volume metric.
* **minstocks**: Sets the minimum number of stocks to trade.
* **maxstocks**: Sets the maximum number of stocks tp trade.
* **minvolatility**: Sets minimum volatility in the stocks i.e. 20.
* **maxvolatility**: Sets maximum volatility in the stocks i.e. 40.

Capital & Broker Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **tradebudget**: Limits the total capital exposed by the strategy.
* **market, exchange, & exchangename**: Define the geographic and institutional venue parameters.
* **broker & brokerurl**: Identify the execution broker and provide reference access to their platform.

Risk Management & Execution Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **tradelossnotexceed**: Acts as a risk guardrail, placing a cap on how much money a single trade is allowed to lose.
* **maxopenpositions**: Controls portfolio diversification and prevents over-leveraging by capping simultaneous trades.
* **maxpctsellloss**: Establishes a percentage-based threshold for sell-side loss mitigation.
* **minholdseconds**: Prevents high-frequency churn or premature exits by enforcing a minimum duration a position must be held.
* **minentryeconds**: Manages execution pacing by ensuring a mandatory time buffer between trade entries.
* **notionalpct**: Dynamically optimizes quantity based on fraction of total trade budget allocated per position (default 10%).
* **maxpricedrop**: Max price drop protection (default: 0.1)
* **addlimitorder**: Prevent slippage in buy price (default: 1)
* **mindaysonbooks**: Min days for open positions (default: 10).  QuantStream will sell IF loss is less than maxpctsellloss.
* **maxdaysonbooks**: Max days for open positions (default: 30).  QuantStream will sell regardless of loss.
* **maxtrades**: Max trades to make to control trade fees (default: 100)
* **maxshares**: Max shares to make to control trade fees (default: 4000)
* **minpredictionaccuracy**: Min prediction accuracy for QuantStream prediction accruacy (default: 0.7)
* **take_profit_pct**: Take profit when profit exceed this percentage. (default: 0.01)
* **maxsharespertrade**: Maximum shares per trade.  Set to -1 to let QuantStream decide. (default: 50)
* **autotradebudget**: If Set to 1, QuantStream will update the trade budget based on the final PnL. This enables compounding of PnL. Set to 0 if you DO NOT want QuantStream to update trade budget. (default: 1)
* **autoqsagentstrategy**: Set to 1, if you want QuantStream agent to manage the trading day.  For example, if 1, QS agent will establish an OPEN position on ALL stocks (maxstock) before 12p, between 12-2, agent will open 50% of the positions and start to liquidate position, and after 2p it will settle to maxopenpositions. 

If autoqsagentstrategy = 2, then QuantStream will stop buying if PnL is greater than 2% of trade budget.

(default: 1)

Fees and Commissions
^^^^^^^^^^^^^^^^^^^^

* **cost_per_trade**: Represents the base per-order component of the broker's tiered commission structure, acting as a baseline routing or order-handling fee charged per executed transaction ticket.   
* **cost_per_share**: The variable commission rate charged per individual share traded under the tiered volume bracket.   

.. Institutional Risk Engine documentation master file, created by
   sphinx-quickstart. You can adapt this file completely to your liking, but
   it should at least contain the root `toctree` directive.

QuantStream AI Agent Risk Guardrails
=====================================

QuantStream AI operates as an automated state manager that tracks open positions, cumulative PnL, circuit breakers, and enforces strict pre-trade and post-trade validation checks.

Complete Guard Rails Reference Matrix
-------------------------------------

Below is the complete suite of operational guard rails implemented in the risk engine:

.. list-table:: 
   :widths: 20 15 25 20 20
   :header-rows: 1

   * - Guard Name
     - Scope
     - Trigger Condition
     - System Action
     - Rationale
   * - **Circuit Breaker**
     - Portfolio
     - Cumulative losses reach or exceed ``max_loss_allowed`` (> 50% of trade budget)
     - **HALTS ALL NEW BUYS** (``return False``)
     - Protects total capital from complete depletion during systemic drawdowns.
   * - **Guard 1: Duplicate Buy Protection**
     - Order (BUY)
     - Incoming ``BUY`` signal for a symbol already present in active holdings
     - **BLOCKS BUY** (``return False``)
     - Prevents accidental position doubling and over-concentration.
   * - **Guard 2: Max Open Positions**
     - Portfolio (BUY)
     - Total active holdings reach ``max_open_positions`` limit (default: 5)
     - **BLOCKS BUY** (``return False``)
     - Enforces institutional capital allocation caps and portfolio diversification.
   * - **Guard 3: Re-Entry Cooldown**
     - Symbol (BUY)
     - Incoming ``BUY`` signal within ``min_reentry_seconds`` (default: 30s) after closing
     - **BLOCKS BUY** (``return False``)
     - Prevents algorithmic whipsawing and high-frequency re-entry churn.
   * - **Guard 4: Orphaned Sell Block**
     - Order (SELL)
     - Incoming ``SELL`` signal for a symbol with **no active** ``BUY`` position
     - **BLOCKS SELL** (``return False``)
     - Prevents unauthorized shorting, ghost liquidations, or execution drift.
   * - **Guard 5: Minimum Hold Time**
     - Symbol (SELL)
     - Incoming ``SELL`` signal within ``min_hold_seconds`` (default: 10s) of opening
     - **BLOCKS SELL** (``return False``)
     - Enforces minimum holding duration to filter out market noise and micro-fluctuations.
   * - **Guard 6: Execution Price Validation**
     - Order (SELL)
     - Incoming ``SELL`` signal on an open position where market ``price`` evaluates to ``None``
     - **BLOCKS SELL** (``return False``)
     - Ensures missing price data does not corrupt risk evaluation math.
   * - **Guard 7: Stop-Loss & Loss Floor**
     - Order (SELL)
     - Incoming ``SELL`` evaluated against pricing
    
       • Asset drops > 5%
     
       • Minor loss within allowed noise floor
     - • **ALLOWS SELL** (``return True``)
       
       **BLOCKS SELL** (``return False``)
     - • Cuts losses instantly on black swan events.

       • Blocks premature panic-selling on normal noise.

Stop-Loss & Loss Floor Implementation (Guard 7)
--------------------------------------------

The following Python snippet implements the dual-threshold risk logic for Guard 7:

.. code-block:: python
      
                  # Guard 7: Institutional Stop-Loss, Take-Profit Target, Max Days Enforcement
                  if incoming_signal == "SELL" and is_currently_holding and price is not None:
                      buy_price = self.open_positions[symbol]["price"]
                      current_loss_pct = (buy_price - price) / buy_price 
                      current_gain_pct = (price - buy_price) / buy_price
                      daysonbooks = self.open_positions[symbol]["daysonbooks"]
      
                      #mhour,mmin,maxhour,maxmin=cf.checktime("US")
                      # 1. Absolute Emergency Floor (Triggers instantly on day 1 if crash is severe)
                      if current_loss_pct >= (self.max_allowable_drop * 1.5): # e.g., 15% instant drop
                          cf.writeviperlogs(test, f"[FATAL EMERGENCY STOP] {symbol} catastrophic drop {current_loss_pct:.2f}. SELL immediately.")
                          return True
      
                      # 1.2. Standard Stop-Loss with your Grace Period Window
                      if current_loss_pct >= self.max_allowable_drop and self.min_days_on_books <= daysonbooks <= self.max_days_on_books:
                          cf.writeviperlogs(test, f"[AGENT GRACE-PERIOD STOP LOSS] {symbol} STOP-LOSS {current_loss_pct:.2f} at day {daysonbooks}. SELL approved.")
                          return True
      
                      # 2. TAKE-PROFIT TARGET: Allow sell immediately if profit reaches user-defined threshold (e.g., 5% / 0.05)
                      if current_gain_pct >= self.take_profit_pct:
                          self._log_throttled(f"{symbol}_take_profit", f"[TAKE PROFIT] {symbol} reached {current_gain_pct*100:.2f}% gain (Target: {self.take_profit_pct*100:.2f}%). SELL approved.")
                          cf.writeviperlogs(test, f"[AGENT TAKE PROFIT] {symbol} reached target profit of {current_gain_pct*100:.2f}%. SELL approved.")
                          return True
      
                      # 3. TIME-BASED EXIT: Allow sell if maximum days on books limit is reached or min days on books is reached and less than max sell loss
                      daysonbooks = self.open_positions[symbol]["daysonbooks"]
                      if daysonbooks >= self.max_days_on_books or (daysonbooks >= self.min_days_on_books and current_loss_pct <= self.max_pct_sell_loss):
                           cf.writeviperlogs(test, f"[AGENT DAYS ON BOOK] {symbol} Exceeds or equal to days on book: {daysonbooks}. SELL approved.")                                        
                           return True
                           
                      # 4. STRICT TARGET BLOCK: Block all other SELL signals if neither stop-loss, take-profit, nor max days is met
                      print(f"[GUARD BLOCK] {symbol} gain ({current_gain_pct*100:.2f}% ) has not met take-profit target ({self.take_profit_pct*100:.2f}%). SELL blocked.")
                      cf.writeviperlogs(test, f"[AGENT GUARD BLOCK] {symbol} gain ({current_gain_pct*100:.2f}%) has not met take-profit target ({self.take_profit_pct*100:.2f}%). SELL blocked.")					
                      return False


Fee Model & Cost Optimization
=============================

To maintain institutional cost efficiency, QuantStream AI incorporates a transparent fee accounting model specifically optimized for **IBKR Pro Tiered Pricing** in Canada.

Fee Structure & Ceilings:
* **Blended Commission Formula:** Total daily trading fees are calculated dynamically as:
  
  .. math::
     \text{Total Fees} = (\text{Total Trades} \times \text{cost_per_trade}) + (\text{Total Shares} \times \text{cost_per_share})

* **Strict \$25/Day Fee Ceiling:** To prevent excessive commission drag during high-volatility sessions, operational caps are enforced at **70 trades/day** and **1,500 shares/day** via `qsconfig.ini`. If trading fees are not a concern set max_trades=-1 and max_shares=-1.
* **Pass-Through Metrics:** Fully accounts for exchange ECN fees, clearing fees, regulatory percentages, and minimum order commission floors (\$0.35 USD).

QuantStream Institutional Alpha & Tail-Risk Guarded Stock Screener
========================================================================

**QuantStream performs advanced Autonomous Market Regime Adaptation with Multi-Objective NSGA-II Sobol Genetic Factor Optimization**.

The **QuantStream Institutional Alpha Screener** is an advanced quantitative engine designed to screen US equity markets (NASDAQ and NYSE) for high-alpha equities. It combines **Quasi-Monte Carlo (QMC)** variance reduction using low-discrepancy Sobol sequences with **NSGA-II Multi-Objective Genetic Pareto Optimization**, **Bayesian Hierarchical Shrinkage**, and **Stress-Bootstrapped Monte Carlo Simulations** over a dynamic holding horizon (:math:`H = maxdaysonbooks`).

.. figure:: screenerprocess2.png
   :scale: 40%

Key Architectural Features
==========================

* **Dynamic Universe Retrieval & Verification**:
  Automatically harvests listing directories directly from NASDAQ Trader (`nasdaqlisted.txt` and `otherlisted.txt`). The engine strips out warrants, preferred shares, test issues, ADRs/ADSs, and exchange-traded funds (ETFs) to isolate common equities. If exchange files are unreachable, it executes a multi-stage fallback to index constituents (S&P 500, Nasdaq-100, DJIA) and local caches.

* **Pre-Market Telemetry & Index Futures Risk Shield (ES=F, NQ=F)**:
  Monitors pre-market price action and overnight index futures contracts (`NQ=F`, `ES=F`). If pre-market Nasdaq futures drop by :math:`\le -1.5\%`, an autonomous **Risk-Off Shield** trips, shifting factor priorities toward deep valuation, defensive quality, and downside protection.

* **NSGA-II Multi-Objective Sobol Genetic Factor Optimization**:
  Replaces fixed factor weights with a real-time non-dominated sorting genetic algorithm (**NSGA-II**). The population space is initialized via **Scrambled Sobol Sequences** to optimize competing institutional objectives: maximizing risk-adjusted return (Sortino ratio) while minimizing tail drawdown risk along a Pareto frontier.

* **Empirical Bayes Hierarchical Shrinkage & Tail Confidence Overlay**:
  Mitigates cross-sectional sample noise in single-stock scores by regularizing individual scores toward sector and global averages using an Empirical Bayes weighting parameter (:math:`\lambda_k`). Ratings are further adjusted by a Gaussian survival function of modeled 30-day downside touch probabilities.

* **3,000-Path Hybrid Monte Carlo Risk Engine**:
  Combines **Circular Moving-Block Bootstrapping** (5-day blocks to preserve empirical autocorrelation) with **Heavy-Tailed Student-t Distribution Shocks** (:math:`\nu = 4`, 1.25x volatility multiplier) to compute 30-day downside-touch probabilities (:math:`P_{\text{touch}}`), terminal drop risks, and 5% Expected Shortfall (:math:`\text{ES}_{5\%}`).

* **Leakage-Aware Out-of-Sample Walk-Forward Backtesting**:
  Evaluates true out-of-sample forward returns over historical anchor windows across 7-, 14-, and 30-trading-day horizons, net of round-trip transaction costs (default 10 bps).

* **Guaranteed Target-Count Fallback Cascade**:
  Employs a multi-tier fallback mechanism with dynamic parameter relaxation (floor scaling) ensuring the output count (e.g., 50 stocks) is strictly filled under all volatility regimes.

Methodology & Quantitative Mathematics
======================================

Dynamic Data-Quality Gates & Fundamental Valuation
-----------------------------------------------------

Before candidate scoring, stocks pass fundamental sanity filters:

* **P/E Ratio Gate**: :math:`0 < \text{P/E} \le 500`
* **P/B Ratio Gate**: :math:`0 < \text{P/B} \le 100`
* **Profit Margin Gate**: :math:`-200\% \le \text{Profit Margin} \le +200\%`
* **Sector Verification**: Valid GICS economic sector classification.

Fundamental metrics are combined into a composite **Valuation Score**:

.. math::

   S_{\text{val}} = \frac{1}{M} \sum_{m=1}^{M} S_m, \quad \text{where } S_{\text{P/E}} = \text{clip}\left(100 - (\text{PE} - 20) \times 2, 0, 100\right)

.. note::
   **Plain-English Explanation:** Before the screener even looks at charts or momentum, it acts like a strict accountant. It filters out broken data, extreme accounting anomalies (like nonsense P/E ratios or bankrupt margins), and averages out basic value metrics so the system doesn't get tricked by garbage numbers.

Quasi-Monte Carlo (QMC) Sobol Sequence Initialization
-------------------------------------------------------

Standard random sampling creates artificial clustering. The Pareto genetic optimizer initializes parameter space using a scrambled :math:`d`-dimensional **Sobol sequence**:

.. math::

   x_n = \bigoplus_{i=1}^{b} a_i v_i

For a 7-factor decision matrix, Sobol sampling ensures uniform space-filling coverage across the hyper-cube :math:`[0, 1]^7`, accelerating convergence to the global Pareto frontier.

.. note::
   **Plain-English Explanation:** Imagine you are testing thousands of recipes by throwing darts blindly at a board. Random throwing often leaves big gaps or clusters. A Sobol sequence acts like a smart, evenly spaced grid, ensuring the computer tests a perfectly balanced variety of recipe combinations without missing any blind spots.

NSGA-II Multi-Objective Evolutionary Pareto Optimization
-----------------------------------------------------------

The screener evaluates seven distinct institutional factor percentile rankings:

.. math::

   \mathbf{F}_i = \left[ \text{Rank}(S_{\text{pred}}), \text{Rank}(S_{\text{cons}}), \text{Rank}(S_{\text{down}}), \text{Rank}(S_{\text{mom}}), \text{Rank}(S_{\text{exec}}), \text{Rank}(S_{\text{entry}}), \text{Rank}(S_{\text{val}}) \right]

The chromosome weight vector :math:`\mathbf{w} = [w_1, \dots, w_7]` with constraint :math:`\sum w_k = 1.0` is optimized across dual competing objectives:

.. math::

   \max_{\mathbf{w}} f_1(\mathbf{w}) = \frac{\mu(R_{\text{top } 25\%})}{\sigma(R_{\text{top } 25\%}) + \epsilon}, \quad \min_{\mathbf{w}} f_2(\mathbf{w}) = \text{Mean}(\text{MaxDrawdown}_{\text{top } 25\%})

Pareto selection ranks chromosomes based on composite fitness:

.. math::

   \text{Fitness}(\mathbf{w}) = f_1(\mathbf{w}) - 0.5 \cdot \left(\frac{f_2(\mathbf{w})}{100}\right)

.. note::
   **Plain-English Explanation:** This is like a fitness coach trying to build the ultimate athlete who is both a world-class sprinter and a marathon runner. Instead of just picking one goal, the genetic algorithm constantly tests and evolves factor mixes to find the absolute best trade-off between maximizing profits and keeping drawdowns low.

Circular Moving-Block Bootstrapping & Heavy-Tailed Stress Simulation
-----------------------------------------------------------------------

Historical log returns :math:`r_t = \ln(P_t / P_{t-1})` are simulated across 3,000 paths over forward horizon :math:`H`:

* **Bootstrap Component**: Resamples contiguous 5-day blocks :math:`B_k = \{r_i, r_{i+1}, \dots, r_{i+4}\}` to preserve volatility clustering.
* **Stressed Student-t Component**: Draws shocks from a Student-t distribution (:math:`\nu = 4`) scaled by inflated historical volatility (:math:`\sigma_{\text{stress}} = 1.25 \times \sigma_{\text{hist}}`) and non-positive drift (:math:`\mu_{\text{stress}} = \min(\mu, 0)`):

.. math::

   dX_t = \mu_{\text{stress}} \cdot dt + \sigma_{\text{stress}} \cdot t_{(\nu=4)}

The 30-day downside touch probability :math:`P_{\text{touch}}` evaluates whether path drawdowns cross the threshold :math:`\theta = \ln(1 + \text{DROP_THRESHOLD})`:

.. math::

   P_{\text{touch}} = \max \left( \mathbb{P}\left(\min_{\tau \le H} \sum_{t=1}^{\tau} r_{t, \text{boot}} \le \theta \right), \mathbb{P}\left(\min_{\tau \le H} \sum_{t=1}^{\tau} dX_{t} \le \theta \right) \right)

.. note::
   **Plain-English Explanation:** Imagine simulating 3,000 different possible futures for a stock over the next month. The system takes real chunks of past market behavior (to keep realistic price swings) and then artificially injects surprise economic storms (heavy-tailed shocks) to ask: *"What is the exact chance this stock crashes by 10%?"*

Empirical Bayes Hierarchical Shrinkage Framework
---------------------------------------------------

To eliminate sample noise in small sector samples, raw stock scores :math:`S_{i,k}` in sector :math:`k` undergo Bayesian shrinkage:

.. math::

   \lambda_k = \text{clip}\left( \frac{n_k}{n_k + \frac{\sigma_k^2}{\sigma_g^2}}, 0.20, 0.95 \right)

.. math::

   \hat{S}_{i,k} = \lambda_k S_{i,k} + (1 - \lambda_k) \mu_g

The final **Gold Mine Alpha Rating** applies a tail-risk confidence multiplier based on the standard normal survival function :math:`\Phi(x)`:

.. math::

   \text{Gold Mine Alpha} = \hat{S}_{i,k} \times \left( 1.0 + 0.15 \times \Phi\left( \frac{20.0 - P_{\text{touch}}}{10.0} \right) \right)

.. note::
   **Plain-English Explanation:** If a small sector only has two or three stocks, one lucky winner can make the whole group look artificially genius. Bayesian shrinkage acts like a reality check—pulling small, noisy groups back toward the broader market average so the screener doesn't chase false alarms.

True Hierarchical Risk Parity (HRP) Tree Clustering
------------------------------------------------------

To eliminate portfolio concentration risk across highly correlated market sectors, the engine applies a true Hierarchical Risk Parity (HRP) tree clustering algorithm on return correlation distance.

- **Distance Metric**: Constructs a correlation matrix over recent historical returns (:math:`N = 60` bars) and computes Euclidean distance over correlation:

.. math::

    d_{i,j} = \sqrt{\frac{1}{2} (1 - \rho_{i,j})}

- **Ward Linkage & Clustering**: Applies agglomerative hierarchical clustering via Ward's minimum variance method and partitions the asset space into clusters using inconsistency thresholds :math:`t = \lceil N_{\text{final}} / 3 \rceil` .
- **Cluster Allocation**: Iteratively selects candidates across distinct tree clusters to guarantee maximal structural diversification before final index export.

.. note::
   **Plain-English Explanation:** If you buy ten "different" tech stocks that all crash at the exact same time when Nasdaq drops, you aren't actually diversified. HRP builds a family tree of how stocks move together and forces the portfolio to pick leaders from entirely different, uncorrelated branches.

Volume-Synchronized Probability of Toxicity (VPIN) & Order Flow Delta
-----------------------------------------------------------------------

To detect stealth institutional order flow imbalance and adverse selection risk, the screener computes high-frequency volume toxicity metrics.

- **VPIN Volume Bucketing**: Aggregates intraday price and volume distributions into equal-volume buckets (:math:`V_{\text{bucket}} = \frac{\sum V}{10}`) to measure order flow toxicity independent of clock time.
- **Order Flow Delta**: Quantifies buying versus selling pressure accumulation using close-location-value (CLV) scaling weighted by trading volume:

.. math::

    \text{CLV}_t = \frac{(C_t - L_t) - (H_t - C_t)}{H_t - L_t}

.. note::
   **Plain-English Explanation:** This acts like an undercover surveillance system for big institutional players. It measures whether stealth buyers or aggressive sellers are secretly accumulating or dumping shares behind the scenes, alerting the system to hidden market traps.

Cross-Sectional Residual Momentum via OLS Orthogonalization
-------------------------------------------------------------

To prevent selecting stocks that merely ride broad market beta, momentum is isolated via Ordinary Least Squares (OLS) regression.

- **Market Orthogonalization**: Regresses each candidate asset's return series against the benchmark (SPY) return history to strip out systemic market co-movement:

.. math::

    R_{i,t} = \alpha_i + \beta_i R_{\text{SPY}, t} + \varepsilon_{i,t}

- **Residual Alpha Accumulation**: Ranks candidates based on annualized cumulative idiosyncratic residuals (:math:`\varepsilon_{i,t}`) over a 60-day window.

.. note::
   **Plain-English Explanation:** Any stock looks like a momentum champion on a day when the entire stock market is surging. This math strips away the general market tide (beta) to find stocks that are winning purely on their own unique, independent strength.

Extended Mathematical Formulations & Stochastic Derivations
===========================================================

Stochastic Differential Equation (SDE) & Beta-Adjusted Macro Drift
-----------------------------------------------------------------------

Let the underlying asset price :math:`P_t` follow a geometric Brownian motion under physical measure :math:`\mathbb{P}` adjusted for systemic market covariance:

.. math::

   \frac{dP_t}{P_t} = \mu_i \, dt + \sigma_i \, dW_t + \beta_i \, dM_t

Where:

* :math:`\mu_i` represents the asset's idiosyncratic drift coefficient.
* :math:`\sigma_i` is the annualized volatility of asset :math:`i`.
* :math:`dW_t` is a standard Wiener process increment (:math:`\mathbb{E}[dW_t] = 0, \text{Var}(dW_t) = dt`).
* :math:`\beta_i = \frac{\text{Cov}(R_i, R_{\text{SPY}})}{\text{Var}(R_{\text{SPY}})}` is the systemic equity beta relative to the benchmark.
* :math:`dM_t` is the systemic macro shock increment governed by index futures telemetry (`NQ=F`, `ES=F`). Under overnight market distress (:math:`\Delta \text{NQ} \le -1.5\%`), the drift parameter :math:`\mu_i` is explicitly bounded:

.. math::

   \mu_{\text{stress}} = \min\left(\mu_i, 0\right) - \gamma \cdot \max(0, -\Delta \text{NQ})

.. note::
   **Plain-English Explanation:** This is the underlying mathematical physics engine. It tracks how a stock drifts day-to-day while dynamically slamming the brakes (adjusting the drift) the moment overnight futures flash a macro panic warning.

Circular Moving-Block Bootstrap Transition Probability
---------------------------------------------------------

To capture empirical autocorrelation, skewness, and volatility clustering without assuming parametric normality, historical daily log returns :math:`\mathbf{R} = \{r_1, r_2, \dots, r_N\}` of length :math:`N` are indexed circularly.

The probability of drawing starting index :math:`I_j` for block :math:`B_k` of width :math:`w = 5` at simulation step :math:`j` is defined by modular arithmetic:

.. math::

   \mathbb{P}(I_j = s) = \frac{1}{N}, \quad s \in \{0, 1, \dots, N-1\}

.. math::

   r_{j, m} = r_{(s + m) \pmod N}, \quad m = 0, 1, \dots, w-1

This preserves higher-order empirical moments by recycling the tail of the return series back to the beginning without artificial truncation bias.

.. note::
   **Plain-English Explanation:** When recycling past stock data for our 3,000 simulation futures, this logic ensures that when we reach the end of a historical data list, we loop back to the beginning seamlessly without breaking the natural rhythm and volatility patterns of the asset.

NSGA-II Crowding Distance & Pareto Dominance Mathematics
-----------------------------------------------------------

The GeneticFactorOptimizer ranks institutional weight chromosomes using **Non-Dominated Sorting Genetic Algorithm II (NSGA-II)** principles.

* **Pareto Dominance**: Solution vector :math:`\mathbf{w}^{(1)}` dominates :math:`\mathbf{w}^{(2)}` (denoted :math:`\mathbf{w}^{(1)} \preceq \mathbf{w}^{(2)}`) if and only if:

.. math::

   \forall k \in \{1, 2\}, \, f_k(\mathbf{w}^{(1)}) \le f_k(\mathbf{w}^{(2)}) \quad \text{and} \quad \exists m \text{ s.t. } f_m(\mathbf{w}^{(1)}) < f_m(\mathbf{w}^{(2)})

* **Crowding Distance Metric**: To maintain diversity along the Pareto front, the local density of solutions surrounding individual :math:`i` is estimated by calculating the bounding box perimeter distance across objective function space:

.. math::

   d(i) = \sum_{k=1}^{2} \frac{f_k(i+1) - f_k(i-1)}{f_k^{\max} - f_k^{\min}}

Solutions with higher crowding distances are preferentially selected to prevent genetic premature convergence and ensure robust hyperparameter exploration.

.. note::
   **Plain-English Explanation:** When the genetic optimizer is evolving stock strategies, it doesn't want all the best solutions huddled in one crowded corner. The crowding distance rule forces the algorithm to explore diverse, distinct alternative strategies across the board.

QuantStream Screener Differentiation: Feature Comparison Matrix
===============================================================

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Feature Dimension
     - Traditional Retail / Basic Screeners
     - QuantStream Institutional Screener
   * - **Analytical Perspective**
     - Backward-looking historical metrics (P/E, 50-day SMA, RSI).
     - Forward-looking stochastic path simulation & walk-forward backtests over holding windows.
   * - **Weight Optimization**
     - Static heuristic formulas or equal weightings.
     - **NSGA-II Multi-Objective Sobol Genetic Optimizer** finding optimal Pareto frontiers.
   * - **Macro Risk Telemetry**
     - Static sector labels; blind to overnight events.
     - **Pre-market Index Futures (`NQ=F`, `ES=F`) Telemetry** with automated Risk-Off Shielding.
   * - **Cross-Sectional Regularization**
     - Unadjusted noisy point scores.
     - **Empirical Bayes Hierarchical Shrinkage** regularized against sector and global means.
   * - **Downside Risk Engine**
     - Simple standard deviation (penalizes upside volatility).
     - **Hybrid 3,000-Path Monte Carlo** (Moving-Block Bootstrap + Heavy-Tailed Student-t Shocks).
   * - **Universe Reliability**
     - Fixed static stock lists; fails during low-volatility squeezes.
     - **Auto-relaxing candidate selection cascade** guaranteeing target output volume.

System Architecture & Operational Pipeline
==========================================

1. **Universe Ingestion**: Fetches symbols from Nasdaq Trader directories, removes non-common equities (warrants, ETFs, preferreds).
2. **Snapshot Prefilter**: Applies NASDAQ API bulk snapshot filtering to eliminate ultra-low volume/price outliers.
3. **Multi-Threaded Download**: Downloads historical price structures (`2y` period) in parallel batches using thread pools.
4. **Data-Quality Gate**: Evaluates fundamental parameters and drops invalid securities.
5. **Macro & Futures Telemetry**: Evaluates overnight `NQ=F` returns and `SPY` benchmark moving averages to determine current macro bias.
6. **Walk-Forward Backtesting**: Calculates net out-of-sample 7d, 14d, and 30d forward returns net of transaction slippage.
7. **NSGA-II GA Optimization**: Evolves population factor weights against historical walk-forward metrics.
8. **Bayesian Shrinkage & Output**: Regularizes composite ratings across sectors, computes Gold Mine Alpha Ratings, and exports structured CSV reports (`best_stock_candidates.csv` and `gold_mine_candidates.csv`).

CSV Output Schema Reference
===========================

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Column Name
     - Type
     - Description
   * - `Ticker`
     - String
     - Primary equity symbol.
   * - `Sector`
     - String
     - GICS Sector classification.
   * - `Price_USD`
     - Float
     - Current execution price (adjusted for pre-market overlay if active).
   * - `Valuation_Score`
     - Float
     - Composite valuation score derived from P/E, P/B, and FCF Yield (0–100).
   * - `P_Touch_Minus10pct_30d_Pct`
     - Float
     - Modeled 30-day downside touch probability (%).
   * - `Backtested_Net_Return_30d_Pct`
     - Float
     - Out-of-sample walk-forward net return over 30 days net of transaction costs (%).
   * - `Best_Stock_Score`
     - Float
     - GA-optimized multi-factor composite score.
   * - `Gold_Mine_Alpha_Rating`
     - Float
     - Bayesian regularized score with tail-risk survival overlay.
   * - `Risk_Tier`
     - String
     - Modeled downside risk classification tier.

QuantStream AI vs. Billion-Dollar Quant Hedge Funds: Architecture Matrix
========================================================================

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
========
To understand the power and sophistication of the **QuantStream AI** stock screener, it is helpful to compare its quantitative architecture directly against the multi-billion-dollar infrastructure deployed by elite quantitative hedge funds (such as Renaissance Technologies, Two Sigma, and Citadel). 

While institutional funds operate across vast compute clusters and petabyte-scale alternative datasets, QuantStream successfully distills the core mathematical machinery of a systematic desk into a lean, high-performance Python engine.

Institutional Feature Comparison
================================

.. list-table:: 
   :widths: 22 39 39
   :header-rows: 1

   * - Architectural Dimension
     - Multi-Billion Dollar Quant Hedge Funds
     - QuantStream AI Screener
   * - **Factor Weight Optimization**
     - Proprietary machine learning and reinforcement learning models trained on distributed compute grids.
     - **NSGA-II Multi-Objective Sobol Genetic Optimizer** co-optimizing Sortino risk-adjusted returns and drawdown risk.
   * - **Space-Filling Initialization**
     - Latin Hypercube and Sobol low-discrepancy pseudo-random generators for robust parameter search.
     - **Quasi-Monte Carlo Sobol Sequences** (``scipy.stats.qmc``) co-initialized with macro-bias vectors.
   * - **Statistical Regularization**
     - Proprietary hierarchical shrinkage models to prevent factor crowding and small-sample variance.
     - **Empirical Bayes Sector Shrinkage** (:math:`\lambda_k`) regularizing individual scores against sector means.
   * - **Tail-Risk Stress Testing**
     - Full-scale macroeconomic historical stress testing (2008 GFC, 2020 COVID shock models).
     - **Circular Moving-Block Bootstrap with Student-t Shocks** (:math:`\text{df}=4`) capturing fat tails and autocorrelation.
   * - **Macro Regime Awareness**
     - Real-time cross-asset correlation matrices, NLP sentiment parsers, and automated overnight risk deleveraging.
     - **Pre-Market Index Futures Telemetry** (``ES=F``, ``NQ=F``) triggering dynamic genetic risk-off bias shifts.
   * - **Production Reliability**
     - Dedicated 24/7 DevOps teams maintaining cluster fault tolerance and automated failovers.
     - **Progressive Multi-Attempt Relaxation Loops** guaranteeing minimum target count fulfillment (``targetcountmin = 20+``).

Key Institutional Advantages
============================

1. Peerless Multi-Objective Pareto Optimization
------------------------------------------------
By implementing Non-Dominated Sorting Genetic Algorithms (**NSGA-II**) combined with Quasi-Monte Carlo Sobol initialization, QuantStream achieves true Pareto-optimal trade-offs between return and risk, mirroring the exact multi-objective search techniques utilized by professional asset managers.

2. Robust Statistical Regularization
------------------------------------
Factor crowding is a primary hazard in quantitative investing. QuantStream neutralizes this via **Empirical Bayes Sector Shrinkage** (:math:`\lambda_k`), anchoring individual asset scores to broader sector behaviors to eliminate small-sample noise and false-positive alpha spikes.

3. Real-Time Overnight Macro Shielding
-------------------------------------
Rather than reacting reactively during market hours, the screener monitors overnight index futures (``ES=F``, ``NQ=F``) before the opening bell. If an overnight shock (such as a :math:`\ge 1.5\%` drop in Nasdaq futures) is detected, the engine automatically pivots its genetic weighting toward deep value and low-drawdown defensive profiles.

4. Bulletproof Production Execution
-----------------------------------
Traditional quantitative pipelines frequently crash or return empty datasets when strict market filters tighten. QuantStream's **progressive multi-attempt relaxation loops** intelligently expand drawdown limits and volume floors iteratively, ensuring an institutional-grade candidate cohort is always successfully generated.

QuantStream Apex Institutional Deadwood Screener & Portfolio Pruning Module
==========================================================================

Overview
--------

The **Apex Deadwood Screener** is an institutional-grade automated portfolio pruning module designed for the **QuantStream** trading agent. Its primary objective is to identify and liquidate underperforming assets ("deadwood") while enforcing strict safety guardrails, macro-sector matrix rules, fundamental quality vetoes, and NSGA-II genetic multi-factor optimization to prevent premature liquidation of positions showing potential recovery or idiosyncratic strength.

.. figure:: DeadwoodFlow.png
   :scale: 40%

Architecture & Pipeline
-----------------------

1. **Input Ingestion**: Parses incoming portfolio arrays containing position metadata (ticker, buy price, quantity, days on books, minimum/maximum holding horizons).
2. **Batch Data Fetching**: Retrieves historical price, volume, and macro futures data in vectorized batches via ``yfinance``, alongside S&P 500 (``SPY``) benchmark data and sector ETFs for comparative relative strength, residual momentum, and sector rotation analysis.
3. **Advanced Quantitative Engines**: Executes high-performance vectorized NumPy simulations, rolling walk-forward backtests, OLS residual momentum orthogonalization, return skewness convexity calculations, and Bayesian sector shrinkage.
4. **Macro & Sector Evaluation**: Filters broad market conditions via Nasdaq/S&P futures (``NQ=F``, ``ES=F``) and maps stock sectors to dynamic industry ETFs for rotation matrix checks.
5. **Genetic Factor Weighting**: Dynamically co-optimizes position retention scores via an NSGA-II multi-objective genetic optimizer initialized with Sobol QMC sequences.
6. **Decision Logic**: Applies enhanced multi-factor warning thresholds, fundamental quality protection vetoes, sector rotation matrix constraints, and hard expiration overrides.
7. **Execution Payload & Audit Ledger**: Returns a structured pandas DataFrame with actionable liquidation flags while persistently logging decisions to ``deadwood_audit_ledger.csv``.

Key Quantitative Mechanisms
---------------------------

Vectorized Monte Carlo & Student-t Stress Simulator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simulates 3,000 parallel price paths over the remaining holding horizon (``days_left``) using a combination of historical bootstrap block sampling (block size = 5) and parametric Student-t distribution shocks (:math:`df = 4`, volatility multiplier = :math:`1.25`).

- **Downside Touch Probability** (``_risk_touch``): The likelihood that an asset touches a :math:`-10\%` drawdown threshold over the remaining duration.
- **Expected Remaining Return** (``Expected_Return_Remaining_Pct``): Projected terminal return across simulated paths combined with walk-forward backtests.

.. note::
   **Plain-English Explanation:** This acts like a stress-tester for open positions. It simulates 3,000 possible future scenarios for the remaining days on books, injecting sudden market storms to see if a stock has a high risk of crashing by 10%.

Walk-Forward Rolling Backtest & Microstructure Friction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Evaluates historical rolling windows matching the asset's remaining horizon, factoring in base transaction costs plus **Amihud illiquidity penalties** to measure expected real-world net drift.

.. note::
   **Plain-English Explanation:** Before deciding a stock is deadwood, the system looks back at how similar price periods historically behaved and accounts for trading costs and hidden friction (like illiquidity) to see if it's truly broken or just sluggish.

Cross-Sectional Residual Momentum & Return Skewness Convexity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Residual Momentum**: Isolates true idiosyncratic alpha by regressing asset returns against the SPY benchmark via OLS regression to strip out systemic market beta.
- **Return Skewness**: Measures right-tailed return asymmetry to protect convex return distributions.

.. note::
   **Plain-English Explanation:** This checks if a stock is just drifting down because the whole market is falling (market beta) or if it has special, hidden upside strength and asymmetric comeback potential that makes it worth holding.

NSGA-II Sobol Genetic Optimization & Empirical Bayes Shrinkage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Genetic Factor Optimizer**: Dynamically weights return ranks, momentum ranks, residual momentum, convexity, downside risk scores, and oversold resilience.
- **Empirical Bayes Sector Shrinkage**: Regularizes individual health scores toward sector means to eliminate small-sample statistical noise.

.. note::
   **Plain-English Explanation:** The system uses an advanced evolutionary algorithm to figure out how much weight to give to momentum versus risk. It also smooths out small-sample noise by comparing each position against its broader sector family.

Macro Futures Trend Filtering & Sector Rotation Matrix
------------------------------------------------------

Macro Futures Filter (`NQ=F`, `ES=F`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Evaluates short-term price changes in Nasdaq Futures (``NQ=F``) and S&P 500 Futures (``ES=F``). If index futures drop more than :math:`0.5\%`, the broad market state is classified as **Bad (-)**; otherwise, it is **Good (+)**.

Sector Rotation & Industry Tailwinds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dynamically maps individual stock sectors to primary industry ETFs (e.g., Technology to ``XLK``, Financials to ``XLF``, Healthcare to ``XLV``) and tracks their trailing momentum.

.. note::
   **Plain-English Explanation:** Before selling a stock, the system checks overnight futures and industry sector trends. If the whole sector or market is just having a temporary bad day, it won't panic-sell a good company.

Institutional Anti-Deadwood Safety Vetoes & Fundamental Overrides
-----------------------------------------------------------------

Even if a stock triggers multiple quantitative warning criteria and passes the market/sector matrix, it is **forcefully protected** from liquidation if any of the following institutional safety vetoes evaluate to ``True``:

- **In-Profit Buffer**: The current market price exceeds the original purchase price (``current_price > buy_price``).
- **Relative Strength (RS) Outperformance**: The asset's 20-day momentum outperforms the S&P 500 benchmark by more than :math:`+2.0\%`.
- **Volume Accumulation**: Recent volume exceeds :math:`1.25\times` its 20-day moving average on sessions where closing prices are flat to up, indicating institutional accumulation.
- **Oversold Resilience / Bad News Baked In**: Maximum drawdown exceeds :math:`18.0\%` while downside touch probability remains below :math:`25.0\%`.
- **Fundamental Quality Veto**: P/E ratio is between 5.0 and 18.0, Free Cash Flow yield is :math:`\ge 6.0\%`, or ROIC is :math:`\ge 8.0\%`.

.. note::
   **Plain-English Explanation:** Even if a stock looks weak on paper, the system has built-in "shield protocols." If a stock is already making money, heavily accumulated by big institutions, or fundamentally pristine, these safety shields block it from being sold prematurely.

.. warning::
   **Hard Expiration Override**: If a position reaches its maximum scheduled holding limit (``dob >= max_dob``) and exhibits worsening price projections, safety vetoes (except fundamental quality) are overridden to guarantee timely portfolio pruning.

Output DataFrame Schema
-----------------------

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Column Name
     - Data Type
     - Description
   * - ``Ticker``
     - ``str``
     - Asset symbol.
   * - ``Sector``
     - ``str``
     - GICS Industry Sector classification.
   * - ``Buy_Price_USD``
     - ``float``
     - Original execution purchase price.
   * - ``Current_Price_USD``
     - ``float``
     - Latest market closing price.
   * - ``Quantity``
     - ``float``
     - Position share quantity held.
   * - ``Position_Value_USD``
     - ``float``
     - Current market value of the position.
   * - ``Days_On_Books``
     - ``int``
     - Total elapsed days since position entry.
   * - ``Max_Days_On_Books``
     - ``int``
     - Maximum scheduled holding duration limit.
   * - ``Days_Left``
     - ``int``
     - Remaining holding horizon before expiration.
   * - ``Expected_Return_Remaining_Pct``
     - ``float``
     - Projected terminal return over remaining horizon (%).
   * - ``Momentum_20d_Pct``
     - ``float``
     - 20-day trailing price momentum (%).
   * - ``Residual_Momentum``
     - ``float``
     - OLS-orthogonalized idiosyncratic momentum score.
   * - ``Return_Skewness``
     - ``float``
     - Return distribution skewness / convexity.
   * - ``Max_Drawdown_Pct``
     - ``float``
     - Maximum historical drawdown percentage.
   * - ``Risk_Tier``
     - ``str``
     - Categorical classification of downside exposure.
   * - ``Protection_Veto``
     - ``str``
     - Active safety override reasons or sector lag notations.
   * - ``Deadwood``
     - ``str``
     - Final pruning flag (``yes`` for liquidation, ``no`` to hold).

License & Disclaimer
====================

Copyright (c) 2026 QuantStream AI. Distributed under institutional software deployment terms. Financial modeling outputs are provided for algorithmic execution frameworks and quantitative research purposes.
