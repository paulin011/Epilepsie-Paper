# Heart-to-Wear – Organization Notes

## 1. Citation
Wolf, S. M., Seidel, P., Ockenga, T., & Schoder, D. (2024). **Heart-to-Wear: Assessing the Accuracy of Heart Rate Sensor Measurements of Wearable Devices in Uncontrolled Environments.** _HICSS 57_.

## 2. Study design (short)
- N = 10 healthy, right-handed adults
- Devices: Apple Watch Ultra, Garmin Enduro 2, Polar Pacer Pro
- Reference: Polar H10 chest strap
- Protocol: 6 × 20-min sessions per person
  - 3 indoor (stationary bike), 3 outdoor (real traffic cycling)
  - Each watch: 2 indoor + 2 outdoor sessions per person (counterbalanced)
  - Each watch worn once on dominant and once on non-dominant wrist

## 3. Data handling
- Standardized segments: always 20 min, ending 60s before recording stop
- Removes: attaching/removing transitions
- Apple Watch sampling: ~ every 5s → not 1Hz
- Garmin & Polar: 1Hz (per second)
- To compare Apple vs chest strap, they **downsample/aggregate** Polar H10:
  - For each Apple sample at time t, compute
  - `Xt = (1/s) * sum_{i=0}^{s-1} X_{t-i}`
    - s = seconds since last Apple measurement
    - X_{t-i} = Polar H10 at t-i seconds

## 4. Evaluation metrics
- Agreement vs Polar H10 (treated as ground truth)
- Metrics:
  - Lin’s Concordance Correlation Coefficient (CCC)
  - Bland–Altman analysis (mean difference + 95% limits of agreement)
- CCC interpretation (McBride 2005):
  - > 0.99: almost perfect
  - 0.95–0.99: substantial
  - 0.90–0.95: moderate
  - < 0.90: poor

## 5. Key numerical results
- Overall CCC (all scenarios combined):
  - Apple Watch Ultra: **0.998** → almost perfect
  - Garmin Enduro 2: **0.995** → almost perfect, but more dispersion than Apple
  - Polar Pacer Pro: **0.957** → substantial
- Wrist side effects:
  - Accuracy generally **worse on dominant wrist** for all watches
  - For Polar, dominant wrist indoors can drop to **poor** agreement
- Error patterns for Polar Pacer Pro:
  - Avg deviation ≈ 1 bpm but **variance high**
  - At 90–120 bpm, deviations up to **~70 bpm**
  - Strong deviations especially in the **first minute** after recording start
- Motion / artifacts:
  - Indoor dominant wrist: more hand movements → worse Polar accuracy
  - Outdoor bumps/road irregularities **do not significantly degrade** Apple/Garmin accuracy

## 6. Interpretation
- Apple Watch Ultra & Garmin Enduro 2:
  - Very high accuracy indoors and outdoors
  - Robust against typical outdoor cycling artifacts
  - Suitable for research / remote monitoring where cost is acceptable
- Polar Pacer Pro:
  - Substantial but clearly worse accuracy
  - Issues at low HR and on dominant wrist
  - Trade-off: lower cost vs lower reliability

## 7. Limitations
- Small sample: N=10 healthy, right-handed, physically fit
- Limited context:
  - Only cycling (indoor & outdoor)
  - Warm summer days → narrow temperature range
  - No explicit recording of external factors (e.g., bumps quantified, temperature, hydration)

## 8. Relevance for seizure / health monitoring
- Shows that **Apple and Garmin devices can provide highly accurate HR** even outdoors
- Suggests they could be reasonable platforms for:
  - HR-based seizure detection/prediction
  - Other anomaly detection (e.g., panic attacks)
- But: seizure patients, daily activities, and more varied environments still need dedicated validation.
