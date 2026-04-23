import os
from datetime import datetime

FILE_NAME = "expenses.txt"

def add_expense():
    category = input("Category (Food/Travel/Shopping/Other): ").strip()
    description = input("Description: ").strip()
    amount = input("Amount (Rs): ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open(FILE_NAME, "a") as f:
        f.write(f"{date},{category},{description},{amount}\n")
    
    print(f"✅ Expense of Rs {amount} added successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("❌ No expenses found!\n")
        return
    
    print("\n📋 ALL EXPENSES:")
    print("-" * 60)
    print(f"{'Date':<20} {'Category':<12} {'Description':<15} {'Amount':>8}")
    print("-" * 60)
    
    total = 0
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No expenses recorded yet.")
            return
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4:
                date, category, desc, amount = parts
                print(f"{date:<20} {category:<12} {desc:<15} Rs {amount:>6}")
                total += float(amount)
    
    print("-" * 60)
    print(f"{'TOTAL':>50} Rs {total:.2f}")
    print()

def summary_by_category():
    if not os.path.exists(FILE_NAME):
        print("❌ No expenses found!\n")
        return
    
    categories = {}
    with open(FILE_NAME, "r") as f:
        for line in f.readlines():
            parts = line.strip().split(",")
            if len(parts) == 4:
                _, category, _, amount = parts
                categories[category] = categories.get(category, 0) + float(amount)
    
    print("\n📊 SUMMARY BY CATEGORY:")
    print("-" * 30)
    for cat, total in categories.items():
        print(f"  {cat:<15}: Rs {total:.2f}")
    print("-" * 30)
    print(f"  {'GRAND TOTAL':<15}: Rs {sum(categories.values()):.2f}\n")

def delete_all():
    confirm = input("⚠️  Delete ALL expenses? (yes/no): ")
    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("✅ All expenses deleted!\n")
    else:
        print("Cancelled.\n")

def main():
    print("=" * 40)
    print("   💰 EXPENSE TRACKER - SoftGrowTech")
    print("=" * 40)
    
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary by Category")
        print("4. Delete All Expenses")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            delete_all()
        elif choice == "5":
            print("👋 Thank you! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()