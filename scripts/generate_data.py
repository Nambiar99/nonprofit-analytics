import pandas as pd
import numpy as np
from pathlib import Path

SEED = 35
N_DONORS = 5000
N_DONATIONS = 25000
N_CAMPAIGNS = 20

START_DATE = pd.Timestamp("2023-01-01")
END_DATE = pd.Timestamp("2025-12-31")

PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR  = PROJECT_ROOT / "data"

rng = np.random.default_rng(SEED)

country_records = [
	("United States", "US", "North America", "USD", 1.00),
	("Canada", "CA", "North America", "CAD", 1.36),
	("Mexico", "MX", "North America", "MXN", 17.10),
	("United Kingdom", "GB", "Europe", "GBP", 0.79),
	("Germany", "DE", "Europe", "EUR", 0.92),
	("France", "FR", "Europe", "EUR", 0.92),
	("Italy", "IT", "Europe", "EUR", 0.92),
	("Spain", "ES", "Europe", "EUR", 0.92),
	("Netherlands", "NL", "Europe", "EUR", 0.92),
	("Switzerland", "CH", "Europe", "CHF", 0.88),
	("Sweden", "SE", "Europe", "SEK", 10.50),
	("Norway", "NO", "Europe", "NOK", 10.80),
	("Denmark", "DK", "Europe", "DKK", 6.90),
	("Poland", "PL", "Europe", "PLN", 4.00),
	("Ireland", "IE", "Europe", "EUR", 0.92),
	("Portugal", "PT", "Europe", "EUR", 0.92),
	("India", "IN", "Asia", "INR", 84.00),
	("Japan", "JP", "Asia", "JPY", 150.00),
	("China", "CN", "Asia", "CNY", 7.20),
	("Singapore", "SG", "Asia", "SGD", 1.35),
	("South Korea", "KR", "Asia", "KRW", 1380.00),
	("Australia", "AU", "Oceania", "AUD", 1.55),
	("New Zealand", "NZ", "Oceania", "NZD", 1.70),
	("Brazil", "BR", "South America", "BRL", 5.50),
	("Argentina", "AR", "South America", "ARS", 1000.00),
	("Chile", "CL", "South America", "CLP", 950.00),
	("Colombia", "CO", "South America", "COP", 4100.00),
	("South Africa", "ZA", "Africa", "ZAR", 18.00),
	("Nigeria", "NG", "Africa", "NGN", 1600.00),
	("Kenya", "KE", "Africa", "KES", 130.00),
	("Egypt", "EG", "Africa", "EGP", 50.00),
	("Ghana", "GH", "Africa", "GHS", 15.00),
	("Morocco", "MA", "Africa", "MAD", 10.00),
	("United Arab Emirates", "AE", "Asia", "AED", 3.67),
	("Saudi Arabia", "SA", "Asia", "SAR", 3.75),
	("Turkey", "TR", "Asia", "TRY", 35.00),
	("Thailand", "TH", "Asia", "THB", 35.00),
	("Malaysia", "MY", "Asia", "MYR", 4.45),
	("Philippines", "PH", "Asia", "PHP", 56.00),
	("Indonesia", "ID", "Asia", "IDR", 15800.00),
]

countries = pd.DataFrame(country_records, columns=["country", "country_code", "continent", "currency", "exchange_rate"])
countries.to_csv(OUTPUT_DIR / "countries.csv", index=False)

country_indices = rng.choice(
	len(countries),
	size=N_DONORS,
	p=np.array([
		0.25, 0.06, 0.025, 0.08, 0.045,
		0.035, 0.02, 0.02, 0.025, 0.015,
		0.012, 0.01, 0.01, 0.012, 0.012,
		0.008, 0.07, 0.015, 0.02, 0.015,
		0.02, 0.008, 0.025, 0.006, 0.008,
		0.008, 0.025, 0.015, 0.012, 0.008,
		0.008, 0.008, 0.015, 0.012, 0.01,
		0.008, 0.008, 0.008, 0.008, 0.008
	]) / np.sum([
		0.25, 0.06, 0.025, 0.08, 0.045,
		0.035, 0.02, 0.02, 0.025, 0.015,
		0.012, 0.01, 0.01, 0.012, 0.012,
		0.008, 0.07, 0.015, 0.02, 0.015,
		0.02, 0.008, 0.025, 0.006, 0.008,
		0.008, 0.025, 0.015, 0.012, 0.008,
		0.008, 0.008, 0.015, 0.012, 0.01,
		0.008, 0.008, 0.008, 0.008, 0.008
	])
)
donors = pd.DataFrame({
	"donor_id": [f"D{i:05d}" for i in range(1, N_DONORS + 1)],
	"donor_type": rng.choice(["Individual", "Organization"], size=N_DONORS, p=[0.9, 0.10]),
	"country": countries.iloc[country_indices]["country"].to_numpy(),
	"country_code": countries.iloc[country_indices]["country_code"].to_numpy(),
	"acquisition_channel": rng.choice(["Website", "Social Media", "Referral", "Email", "Events"], size=N_DONORS, p=[0.40, 0.20, 0.15, 0.15, 0.10])
})

donors["recurring_donor"] = rng.choice([True, False], size=N_DONORS, p=[0.30, 0.70])

campaign_names = [
	"Clean Water Initiative",
	"Education for All",
	"Emergency Food Relief",
	"Global Health Access",
	"Children's Future Fund",
	"Disaster Recovery Program",
	"Women Empowerment Project",
	"Rural Development Initiative",
	"Climate Action Fund",
	"Medical Aid Program",
	"Refugee Support Campaign",
	"Digital Education Access",
	"Hunger-Free Communities",
	"Community Housing Project",
	"Child Nutrition Program",
	"Ocean Conservation Fund",
	"Renewable Energy Access",
	"Mental Health Awareness",
	"Wildlife Protection Fund",
	"Global Emergency Response"
]

categories = [
	"Water & Sanitation",
	"Education",
	"Food Security",
	"Healthcare",
	"Education",
	"Disaster Relief",
	"Community Development",
	"Community Development",
	"Environment",
	"Healthcare",
	"Humanitarian Aid",
	"Education",
	"Food Security",
	"Community Development",
	"Healthcare",
	"Environment",
	"Environment",
	"Healthcare",
	"Environment",
	"Disaster Relief"
]

campaign_start_dates = pd.to_datetime(
	rng.choice(
		pd.date_range(START_DATE, END_DATE - pd.Timedelta(days=90)),
		size=N_CAMPAIGNS,
		replace=True
	)
)
campaign_durations = rng.integers(90, 366, size=N_CAMPAIGNS)

campaign_end_dates = [
	min(start + pd.Timedelta(days=int(duration)), END_DATE)
	for start, duration in zip(campaign_start_dates, campaign_durations)
]
campaigns = pd.DataFrame({
	"campaign_id": [f"C{i:03d}" for i in range(1, N_CAMPAIGNS + 1)],
	"campaign_name": campaign_names,
	"category": categories,
	"start_date": campaign_start_dates,
	"end_date": campaign_end_dates
})

donor_indices = np.concatenate([rng.permutation(N_DONORS), rng.choice(N_DONORS, N_DONATIONS - N_DONORS)])
rng.shuffle(donor_indices)
selected_donors = donors.iloc[donor_indices].reset_index(drop=True)
campaign_indices = rng.choice(N_CAMPAIGNS, size=N_DONATIONS)
selected_campaigns = campaigns.iloc[campaign_indices].reset_index(drop=True)
date_offsets = np.array([
	rng.integers(0, max(1, (end-start).days + 1))
	for start, end in zip(selected_campaigns["start_date"], selected_campaigns["end_date"])
])
donation_dates = selected_campaigns["start_date"].to_numpy() + pd.to_timedelta(date_offsets, unit="D")
donation_types = np.where(
	selected_donors["recurring_donor"].to_numpy(),
	rng.choice(["Recurring", "One-time"], size=N_DONATIONS, p=[0.75, 0.25]),
	"One-time"
)
donation_amounts_usd = rng.lognormal(mean=3.5, sigma=1.0, size=N_DONATIONS)
organization_mask = (selected_donors["donor_type"].to_numpy() == "Organization")
donation_amounts_usd = np.maximum(np.round(donation_amounts_usd, 2), 5.00)
donation_countries = selected_donors["country"].to_numpy()
donation_currency = pd.Series(donation_countries).map(countries.set_index("country")["currency"]).to_numpy()
exchange_rates = pd.Series(donation_countries).map(countries.set_index("country")["exchange_rate"]).to_numpy()
donation_amounts_local = np.round(donation_amounts_usd * exchange_rates, 2)
payment_methods = rng.choice(
	["Credit Card", "Debit Card", "Bank Transfer", "PayPal"],
	size=N_DONATIONS,
	p=[0.40, 0.25, 0.20, 0.15]
)
donations = pd.DataFrame({
	"donation_id": [f"TXN{i:07d}" for i in range(1, N_DONATIONS + 1)],
	"donor_id": selected_donors["donor_id"],
	"campaign_id": selected_campaigns["campaign_id"],
	"donation_date": donation_dates,
	"amount": donation_amounts_local,
	"currency": donation_currency,
	"amount_usd": donation_amounts_usd,
	"payment_method": payment_methods,
	"donation_type": donation_types,
	"country": donation_countries
})

donations["donation_date"] = pd.to_datetime(donations["donation_date"])
donations = donations.sort_values("donation_date").reset_index(drop=True)

first_donation = donations.groupby("donor_id")["donation_date"].min()
registration_offsets = rng.integers(0, 366, size=N_DONORS)
donors["first_donation_date"] = donors["donor_id"].map(first_donation)
donors["registration_date"] = donors["first_donation_date"] - pd.to_timedelta(registration_offsets, unit="D")
lifetime_donations = donations.groupby("donor_id")["amount_usd"].sum()
donors["lifetime_donations_usd"] = donors["donor_id"].map(lifetime_donations).fillna(0).round(2)
donors["donor_segment"] = pd.cut(
	donors["lifetime_donations_usd"],
	bins=[-np.inf, 250, 1000, 5000, np.inf],
	labels=["Small", "Medium", "Major", "Principal"]
).astype(str)

actual_campaign_donations = donations.groupby("campaign_id")["amount_usd"].sum()
campaigns["actual_raised_usd"] = campaigns["campaign_id"].map(actual_campaign_donations).fillna(0).round(2)

achievement_ratios = rng.uniform(0.65, 1.30, size=N_CAMPAIGNS)
campaigns["findraising_goal_usd"] = np.round(campaigns["actual_raised_usd"] / achievement_ratios, 2)
campaigns["achievement_percentage"] = np.round(campaigns["actual_raised_usd"] / campaigns["findraising_goal_usd"] * 100, 2)

donations.to_csv(OUTPUT_DIR / "donations.csv", index=False)
donors.to_csv(OUTPUT_DIR / "donors.csv", index=False)
campaigns.to_csv(OUTPUT_DIR / "campaigns.csv", index=False)
countries.to_csv(OUTPUT_DIR / "countries.csv", index=False)

print("Data Generation Complete")
print("=" * 30)
for filename, df in {
	"donations.csv": donations,
	"donors.csv": donors,
	"campaigns.csv": campaigns,
	"countries.csv": countries
}.items():
	print(f"{filename}: {len(df):,} records")

print(f"Total donations (USD): ${donations["amount_usd"].sum():,.2f}")
print(f"Unique donors: {donations["donor_id"].nunique()}")
print(f"Unique countries: {donations["country"].nunique()}")
print(f"Recurring donations: {(donations["donation_type"] == "Recurring").mean() * 100:.2f}%")
print(f"Files saved to: {OUTPUT_DIR}")




