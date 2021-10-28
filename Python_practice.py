#practice with if statements
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

#practice with interactive if-else statements
temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#practice with nested if-else statements
#what is the score?
score = int(input("What is your test score? "))

#Determine grade
if score >= 90:
    print('your grade is an A.')
elif score >= 80:
    print("your grade is a B.")
elif score >= 70:
    print("your grade is a C.")
elif score >= 60:
    print("your grade is a D.")
else:
    print("your grade is an F.")

#3.2.9  module
counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

#3.2.10
x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
        for value in county_dict.values():
            print(value)

#3.2.11
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What s the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("what is the total number of votes in the election? "))
message_to_candidate = (
    f"you received {candidate_votes:,} number of votes. "
    f"the total number of votes in the election was {total_votes:,}. "
    f"you received {candidate_votes / total_votes *100:.2f}% of the total votes. ")
print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters. ")

