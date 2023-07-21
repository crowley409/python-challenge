def analyze_financial_records(file_path):
    total_months = 0
    net_total = 0
    prev_profit_loss = 0
    total_changes = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""

    with open(file_path, "r") as file:
        next(file)

        for line in file:
            date, profit_loss = line.strip().split(",")

            profit_loss = int(profit_loss)

            total_months += 1

            net_total += profit_loss

            if total_months > 1:
                change = profit_loss - prev_profit_loss
                total_changes += change

                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = date
                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = date

            prev_profit_loss = profit_loss

    average_change = total_changes / (total_months - 1)

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    with open("financial_analysis_results.txt", "w") as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("------------------\n")
        output_file.write(f"Total Months: {total_months}\n")
        output_file.write(f"Net Total: ${net_total}\n")
        output_file.write(f"Average Change: ${average_change:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

if __name__ == "__main__":
    file_path = "budget_data.csv"
    analyze_financial_records(file_path)