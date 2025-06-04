increase_sales_percent = 12.93720081
revenue_growth_percent = 18.33206078

answer = f"sales in our company went up {increase_sales_percent:.2f}%, and our revenue has grown by {revenue_growth_percent:.2f}%"

with open("file.csv", "a") as f:
    f.write(f"task1, {answer}\n")
