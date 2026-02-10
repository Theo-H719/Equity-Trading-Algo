import pandas as pd   
from datetime import timedelta

# 1. THE NEWS CALENDAR
news_events = [
    '2025-03-19 14:00', '2025-05-07 14:00', '2025-06-18 14:00', # FOMC
    '2025-03-12 08:30', '2025-04-10 08:30', '2025-05-13 08:30', # CPI
    '2025-03-07 08:30', '2025-04-04 08:30', '2025-05-02 08:30'  # NFP
]

def code_step_1_masking(df, event_list):
    # Ensure index is datetime
    df.index = pd.to_datetime(df.index)
    
    # 1. Detect your data's timezone (e.g., UTC)
    data_tz = df.index.tz
    if data_tz is None:
        # If your data had no TZ, we'd have no error. 
        # Since you got the error, data_tz is definitely not None.
        pass

    # 2. Make the news list match your data's timezone exactly
    # This keeps your option data pure and "Aware"
    event_ts = pd.to_datetime(event_list).tz_localize(data_tz)
    
    # Start with everything marked as 'Normal'
    df['is_news_noise'] = False
    
    for event in event_ts:
        start = event - timedelta(minutes=5)
        end = event + timedelta(minutes=45)
        
        # Mark the noise
        df.loc[start:end, 'is_news_noise'] = True
        
    print(f"Masking Complete. {df['is_news_noise'].sum()} rows marked as News Noise.")
    return df

# ==========================================
# USAGE
# ==========================================
df = pd.read_parquet('/content/drive/MyDrive/MATH_SIGNALS_FULL_YEAR.parquet') 
df = code_step_1_masking(df, news_events)

# Verification
print(f"Data Timezone: {df.index.tz}")
print(df['is_news_noise'].value_counts())



# 3. Train the new model 
print("🎯 Training Specialist Model (4 States, Full Covariance)...")
specialist_model = GaussianHMM(
    n_components=4, 
    covariance_type="full", 
    n_iter=1000, 
    random_state=42
)
specialist_model.fit(X_scaled)

# 4. Save the new tools
joblib.dump(specialist_model, 'specialist_hmm_model.pkl')
joblib.dump(scaler, 'specialist_scaler.pkl')
print("✅ New Model and Scaler Saved.")
