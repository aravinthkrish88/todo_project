import matplotlib.pyplot as plt

# Age groups and their populations (in billions)
age_groups = ['Learners (0-17)', 'Builders (18-34)', 'Growers (35-49)', 'Stabilizers (50-64)', 'Elders (65+)']
population = [2.1, 2.2, 1.5, 1.2, 1.1]

# Colors for the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = (0, 0.1, 0, 0, 0)  # Highlight Builders (18-34)

plt.figure(figsize=(8,8))
plt.pie(population, labels=age_groups, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)
plt.title('Global Population by Age Groups (2025 estimate)')
plt.show()

# Step 3: User Input and Age Group Identification

def get_age_group(age):
    if 0 <= age <= 17:
        return 'Learners (0-17)'
    elif 18 <= age <= 34:
        return 'Builders (18-34)'
    elif 35 <= age <= 49:
        return 'Growers (35-49)'
    elif 50 <= age <= 64:
        return 'Stabilizers (50-64)'
    elif age >= 65:
        return 'Elders (65+)'
    else:
        return 'Invalid age'

try:
    user_age = int(input("Enter your age: "))
    group = get_age_group(user_age)
    print(f"You belong to the '{group}' age group.")
except ValueError:
    print("Please enter a valid integer age.")

age_group_info = {
    'Learners (0-17)': 'You are in the learning phase, focus on building strong foundations.',
    'Builders (18-34)': 'You are in the prime career-building phase, keep upgrading your skills.',
    'Growers (35-49)': 'You are growing in your career and life, leadership skills are key.',
    'Stabilizers (50-64)': 'You have stability, share your knowledge and mentor others.',
    'Elders (65+)': 'You are a wise elder, your experience is invaluable to the community.'
}

# After getting the age group
if group in age_group_info:
    print(age_group_info[group])
else:
    print("No information available for your age group.")