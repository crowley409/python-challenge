def analyze_election_data(file_path):
    total_votes = 0
    candidate_votes = {}
    candidates = set()

    with open(file_path, "r") as file:
        next(file)

        for line in file:
            voter_id, county, candidate = line.strip().split(",")

            total_votes += 1

            candidates.add(candidate)

            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    candidate_percentages = {c: votes / total_votes * 100 for c, votes in candidate_votes.items()}

    winner = max(candidate_votes, key=candidate_votes.get)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates:
        print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    with open("election_results.txt", "w") as output_file:
        output_file.write("Election Results\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("-------------------------\n")
        for candidate in candidates:
            output_file.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Winner: {winner}\n")
        output_file.write("-------------------------\n")

if __name__ == "__main__":
    file_path = "election_data.csv"
    analyze_election_data(file_path)