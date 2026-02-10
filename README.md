# Equity-Trading-Algo

Specialist HMM: Volatility Harvesting

This project implements a Hidden Markov Model (HMM) strategy designed to harvest volatility anomalies in SPY data while maintaining strict risk compliance.

- The Development Journey
The project followed a multi-stage evolution from raw anomaly detection to a risk-hardened execution engine. Paid Option Data was used from DataBento, for the year 2024, to use as an in sample:

Data Sanitization (News Masking): We implemented a timezone-aware masking system to exclude trading during high-impact news events (FOMC, CPI, NFP), ensuring strategy returns are based on structural market stress rather than event-driven binary noise.

State Discovery (The HMM Specialist): Initially modeled with 6 states, we refined the data into a 4-state "Specialist Model" using Full Covariance Gaussian HMMs to identify regimes where "specialist stress" creates predictable reversals or momentum.

Strategy Engineering (Lead-Lag & Short Alpha): We identified a "Stress Cliff" (Z-score > 0.5) where overextended jumps in specific HMM states provided a statistically significant edge for shorting.

Institutional Risk Management: To meet strict risk requirements ($5k daily limit), we engineered a "Bulletproof Engine" featuring a daily circuit breaker (max 3 losses) and an anti-layering (anti-martingale) lockout to prevent multiple entries on the same move.

- Final Performance Audit
The final engine was subjected to a full-year out sample backtest audit for 2025 (including blackswan events):

Daily Compliance: Passed with zero $5k daily breaches.
Overall RR Ratio:  3.04
Avg Win: 3.28% | Avg Loss: 1.08%
Yearly Return: 204.8%
Max Total Drawdown: 15.07%
