Live Sports AI: Production Bayesian Engine with TML and Multi-Agentic AI for NHL, NBA, NFL, and MLB In-Game Predictions
-------------------------------------

This post shares a production-ready Bayesian engine for live NHL predictions (will be extended to NBA, NFL, MLB) and explains why it can outperform many "black-box" prediction tools in the market. The intent is to stay business-friendly while still being technically honest about what is going on under the hood.

What this engine actually does
===============================

At a high level, the code builds a probabilistic "digital twin" of an NHL game that updates in real time as events happen (shots, goals, hits, penalties, etc.).  
Instead of just saying "Team A is 63% to win," it decomposes that into player-level event rates and team-level effects, then recombines them for actionable betting and product decisions.

**Key capabilities:**
- **Player-level forecasts:** probability a player records at least 1 goal, assist, point, hit, etc. in the next X minutes.
- **Team win probabilities:** probability the home team ends the game with more goals than the away team.
- **Betting intelligence:** conversion of all probabilities into fair decimal odds, American odds, and expected value (Expected Value) versus market prices.

This engine is designed to run in production with tight latency constraints, using modern Bayesian libraries (PyMC with JAX/NumPyro) and heavy low-level optimization (Numba) to keep it fast.

The core mathematical model
==========================

Under the hood, most on-ice events are modeled as Poisson processes.  
Intuitively, a Poisson process answers questions like: "Given a rate of λ events per game, what is the probability that a player records 0, 1, 2, … goals in a future window?"

Player event model
""""""""""""""""""""

For each player i and event type e (goals, assists, penalties, hits, etc.), the engine learns a log-rate:

.. figure:: lsm1.png
   :scale: 70%

- `ability_i,e`: player's latent skill, with priors informed by historical per-game averages (on log scale) and regularized so noisy recent data cannot explode the estimate.
- `team_effect_team(i)`: combined impact of team defense, goalie quality, momentum (goals, shots, takeaways, hits), fatigue (time on ice, hits absorbed, penalties), and home/away adjustments.
- `star_bonus_i`: extra boost for flagged star players, capturing the fact that stars disproportionately generate events.

Given λ_i,e, the probability that player i records k events of type e over a future window with effective rate λ_i,e^future is:

.. figure:: lsm2.png
   :scale: 70%

- The “future” rate scales elapsed vs remaining time; for example, if a player generated 1.0 expected goals per 10 minutes, the engine rescales that to the next 5–20 minutes depending on period, game state, and event type.

- For rare events (especially goals), the model also supports zero-inflation (extra mass at zero) to better match empirical NHL distributions, though the current configuration may use a standard Poisson likelihood with a zero-inflation parameter available for tuning.

Team goals and win probability
===============================

Team goals are constructed by summing the player-level goal intensities by team:

.. figure:: lsm3.png
   :scale: 70%


These team goal intensities then drive:
- Full distributions of final goals for each team.
- Win probability P(Team A goals > Team B goals) via Monte Carlo over posterior samples.

**This is critical:** win probability is not a black-box output; it is an aggregation of player-level and team-level structure that can be inspected and explained.

From probabilities to betting metrics
=====================================

For any event with model-implied probability p, the engine computes:
- Fair decimal odds: O_fair = 1 / p.
- Fair American odds (approx.):  
  - If p > 0.5, favorite: A = -(p/(1-p)) × 100.
  - If p ≤ 0.5, underdog: A = ((1-p)/p) × 100.
- Expected Value (EV) versus market decimal odds O_mkt:  

.. figure:: lsm4.png
   :scale: 70%
