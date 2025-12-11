    cursor.execute(query, (user_id,))
        rows = cursor.fetchall()

        if not rows:
            print("No expenses found.\n")
            return

        print("\nSorted Expenses:\n")
        for r in rows:
            print(f"ID: {r[0]} | Amount: ₹{r[1]} | Category: {r[2]} | Desc: {r[3]} | Date: {r[4]}")
        print()
