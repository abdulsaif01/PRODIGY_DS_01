"""
PRODIGY_DS_01 - Population Distribution Analysis
Task: Create a bar chart or histogram to visualize the distribution of a categorical 
or continuous variable (population distribution by country and age groups)

Author: Abdul Saif
Internship: Prodigy InfoTech - Data Science Track
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Create sample population data (World Population by Country - 2022)
countries_data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 
                'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico',
                'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam',
                'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand'],
    'Population_Millions': [1425.67, 1417.17, 338.29, 275.50, 235.82,
                           215.31, 218.54, 171.19, 144.71, 127.50,
                           123.95, 123.38, 115.56, 110.99, 98.19,
                           99.01, 85.04, 88.55, 83.37, 71.80],
    'Continent': ['Asia', 'Asia', 'North America', 'Asia', 'Asia',
                  'South America', 'Africa', 'Asia', 'Europe', 'North America',
                  'Asia', 'Africa', 'Asia', 'Africa', 'Asia',
                  'Africa', 'Asia', 'Asia', 'Europe', 'Asia']
}

df_countries = pd.DataFrame(countries_data)

# Create age distribution data for a sample population
np.random.seed(42)
age_groups = ['0-14', '15-24', '25-54', '55-64', '65+']
age_distribution = {
    'Age_Group': age_groups,
    'Population_Percentage': [25.4, 15.8, 41.2, 10.3, 7.3]
}

df_age = pd.DataFrame(age_distribution)

print("="*70)
print("TASK 01: POPULATION DISTRIBUTION ANALYSIS")
print("="*70)
print("\n1. Dataset Overview:")
print(f"   - Total countries analyzed: {len(df_countries)}")
print(f"   - Total population (millions): {df_countries['Population_Millions'].sum():.2f}")
print(f"\n2. Top 5 Most Populous Countries:")
print(df_countries.nlargest(5, 'Population_Millions')[['Country', 'Population_Millions']])

# Visualization 1: Bar Chart - Top 20 Countries by Population
plt.figure(figsize=(14, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(df_countries)))
bars = plt.bar(df_countries['Country'], df_countries['Population_Millions'], color=colors, edgecolor='black')

# Highlight top 3 countries
bars[0].set_color('#FF6B6B')  # China
bars[1].set_color('#4ECDC4')  # India
bars[2].set_color('#FFE66D')  # USA

plt.xlabel('Country', fontsize=12, fontweight='bold')
plt.ylabel('Population (Millions)', fontsize=12, fontweight='bold')
plt.title('World Population Distribution - Top 20 Countries (2022)', 
          fontsize=14, fontweight='bold', pad=20)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/population_by_country.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: population_by_country.png")
plt.close()

# Visualization 2: Histogram - Population Distribution
plt.figure(figsize=(12, 6))
plt.hist(df_countries['Population_Millions'], bins=15, color='#6C5CE7', 
         edgecolor='black', alpha=0.7)
plt.axvline(df_countries['Population_Millions'].mean(), color='red', 
            linestyle='--', linewidth=2, label=f'Mean: {df_countries["Population_Millions"].mean():.2f}M')
plt.axvline(df_countries['Population_Millions'].median(), color='green', 
            linestyle='--', linewidth=2, label=f'Median: {df_countries["Population_Millions"].median():.2f}M')

plt.xlabel('Population (Millions)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency (Number of Countries)', fontsize=12, fontweight='bold')
plt.title('Histogram: Distribution of Population Across Countries', 
          fontsize=14, fontweight='bold', pad=20)
plt.legend(fontsize=10)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/population_histogram.png', dpi=300, bbox_inches='tight')
print("✓ Saved: population_histogram.png")
plt.close()

# Visualization 3: Bar Chart - Population by Continent
plt.figure(figsize=(10, 6))
continent_pop = df_countries.groupby('Continent')['Population_Millions'].sum().sort_values(ascending=False)
colors_continent = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#95E1D3', '#F38181']
bars = plt.bar(continent_pop.index, continent_pop.values, color=colors_continent, edgecolor='black')

plt.xlabel('Continent', fontsize=12, fontweight='bold')
plt.ylabel('Total Population (Millions)', fontsize=12, fontweight='bold')
plt.title('Total Population Distribution by Continent', 
          fontsize=14, fontweight='bold', pad=20)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}M',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/claude/population_by_continent.png', dpi=300, bbox_inches='tight')
print("✓ Saved: population_by_continent.png")
plt.close()

# Visualization 4: Age Distribution
plt.figure(figsize=(10, 6))
colors_age = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#95E1D3', '#F38181']
bars = plt.bar(df_age['Age_Group'], df_age['Population_Percentage'], 
               color=colors_age, edgecolor='black')

plt.xlabel('Age Group', fontsize=12, fontweight='bold')
plt.ylabel('Population Percentage (%)', fontsize=12, fontweight='bold')
plt.title('Global Population Distribution by Age Group', 
          fontsize=14, fontweight='bold', pad=20)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/claude/age_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: age_distribution.png")
plt.close()

# Save datasets to CSV
df_countries.to_csv('/home/claude/population_data.csv', index=False)
df_age.to_csv('/home/claude/age_distribution_data.csv', index=False)

print("\n" + "="*70)
print("KEY INSIGHTS:")
print("="*70)
print(f"1. China and India lead with populations over 1.4 billion each")
print(f"2. Asia dominates with {continent_pop['Asia']:.1f}M total population")
print(f"3. The working-age population (25-54) represents {df_age.loc[2, 'Population_Percentage']}% globally")
print(f"4. Average country population: {df_countries['Population_Millions'].mean():.2f}M")
print(f"5. Population range: {df_countries['Population_Millions'].min():.2f}M - {df_countries['Population_Millions'].max():.2f}M")
print("="*70)
print("\n✓ All visualizations saved successfully!")
print("✓ Data files saved: population_data.csv, age_distribution_data.csv")
