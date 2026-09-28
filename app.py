import tkinter as tk


# ==========================================================
# COLORS AND FONTS
# ==========================================================

BG = "#EEF2F5"
DARK = "#17212B"
DARK2 = "#202D38"
CARD = "#FFFFFF"
TEXT = "#17212B"
MUTED = "#66737F"
ACCENT = "#2F80A8"
ACCENT_DARK = "#23627F"
BORDER = "#D6DEE5"
GREEN = "#287D4F"
ORANGE = "#C47A22"
RED = "#C0392B"

FONT = "Times New Roman"


# ==========================================================
# MAIN APP
# ==========================================================

app = tk.Tk()

app.title("Smart Money Decision Assistant")
app.geometry("950x700")
app.minsize(850, 620)
app.configure(bg=BG)


# ==========================================================
# COMMON FUNCTIONS
# ==========================================================

def create_header(window, title, subtitle):

    header = tk.Frame(
        window,
        bg=DARK,
        height=135
    )

    header.pack(
        fill="x"
    )

    header.pack_propagate(False)

    tk.Label(
        header,
        text=title,
        font=(FONT, 25, "bold"),
        bg=DARK,
        fg="white"
    ).pack(
        pady=(25, 2)
    )

    tk.Label(
        header,
        text=subtitle,
        font=(FONT, 11),
        bg=DARK,
        fg="#B9C6D0"
    ).pack()


def create_card(window):

    card = tk.Frame(
        window,
        bg=CARD,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    card.pack(
        fill="both",
        expand=True,
        padx=70,
        pady=30
    )

    return card


def create_entry(card):

    entry = tk.Entry(
        card,
        font=(FONT, 13),
        bg="#FAFBFC",
        fg=TEXT,
        relief="solid",
        bd=1,
        highlightthickness=0
    )

    entry.pack(
        fill="x",
        ipady=9,
        pady=(7, 20)
    )

    return entry


def show_message(result, text, color=TEXT):

    result.config(
        text=text,
        fg=color
    )


# ==========================================================
# FEATURE 1
# SUBSCRIPTION LEAK DETECTOR
# ==========================================================

def open_subscription():

    window = tk.Toplevel(app)

    window.title("Subscription Leak Detector")
    window.geometry("850x720")
    window.minsize(750, 600)
    window.configure(bg=BG)

    create_header(
        window,
        "SUBSCRIPTION LEAK DETECTOR",
        "See what your subscriptions are really costing you."
    )

    # ------------------------------------------------------
    # SCROLLABLE AREA
    # ------------------------------------------------------

    canvas = tk.Canvas(
        window,
        bg=BG,
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
        window,
        orient="vertical",
        command=canvas.yview
    )

    scroll_frame = tk.Frame(
        canvas,
        bg=BG
    )

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=scroll_frame,
        anchor="nw",
        width=810
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # ------------------------------------------------------
    # SUBSCRIPTION DATA
    # ------------------------------------------------------

    subscriptions = []

    # ------------------------------------------------------
    # CARD
    # ------------------------------------------------------

    card = tk.Frame(
        scroll_frame,
        bg=CARD,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    card.pack(
        fill="x",
        padx=45,
        pady=30
    )

    tk.Label(
        card,
        text="SUBSCRIPTION DETAILS",
        font=(FONT, 17, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(25, 5)
    )

    tk.Label(
        card,
        text="Enter each subscription one at a time.",
        font=(FONT, 11),
        bg=CARD,
        fg=MUTED
    ).pack(
        anchor="w",
        padx=35,
        pady=(0, 20)
    )

    # ------------------------------------------------------
    # NAME
    # ------------------------------------------------------

    tk.Label(
        card,
        text="Subscription Name",
        font=(FONT, 11, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35
    )

    name_entry = create_entry(card)

    # ------------------------------------------------------
    # COST
    # ------------------------------------------------------

    tk.Label(
        card,
        text="Monthly Cost (₹)",
        font=(FONT, 11, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35
    )

    cost_entry = create_entry(card)

    # ------------------------------------------------------
    # ADD ANOTHER
    # ------------------------------------------------------

    tk.Label(
        card,
        text="Do you want to add another subscription? (yes/no)",
        font=(FONT, 11, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35
    )

    more_entry = create_entry(card)

    instruction = tk.Label(
        card,
        text="Press Enter to move to the next step.",
        font=(FONT, 10),
        bg=CARD,
        fg=MUTED
    )

    instruction.pack(
        anchor="w",
        padx=35,
        pady=(0, 25)
    )

    # ------------------------------------------------------
    # RESULT AREA
    # ------------------------------------------------------

    result_card = tk.Frame(
        scroll_frame,
        bg=CARD,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    result_card.pack(
        fill="x",
        padx=45,
        pady=(0, 25)
    )

    tk.Label(
        result_card,
        text="YOUR RESULT",
        font=(FONT, 16, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(
        pady=(20, 5)
    )

    result = tk.Label(
        result_card,
        text="Enter your subscription details above.",
        font=(FONT, 11),
        bg=CARD,
        fg=MUTED,
        justify="center"
    )

    result.pack(
        pady=(0, 25)
    )

    # ------------------------------------------------------
    # POTENTIAL SAVINGS
    # ------------------------------------------------------

    savings_card = tk.Frame(
        scroll_frame,
        bg=CARD,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    savings_card.pack(
        fill="x",
        padx=45,
        pady=(0, 30)
    )

    tk.Label(
        savings_card,
        text="POTENTIAL SAVINGS",
        font=(FONT, 16, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(20, 5)
    )

    savings_result = tk.Label(
        savings_card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=TEXT,
        justify="center"
    )

    savings_result.pack(
        pady=(5, 25)
    )

    # ------------------------------------------------------
    # FUNCTION TO SHOW SUMMARY
    # ------------------------------------------------------

    def show_summary():

        total_monthly = sum(
            cost for name, cost in subscriptions
        )

        total_yearly = total_monthly * 12

        most_expensive = max(
            subscriptions,
            key=lambda x: x[1]
        )

        percentage = (
            most_expensive[1] / total_monthly
        ) * 100

        if total_yearly >= 15000:
            health = (
                "● High recurring subscription spending."
            )
            health_color = RED

        elif total_yearly >= 10000:
            health = (
                "● Moderate recurring subscription spending."
            )
            health_color = ORANGE

        else:
            health = (
                "● Recurring spending is relatively low."
            )
            health_color = GREEN

        summary = (
            f"Total monthly cost: ₹{total_monthly:.2f}\n"
            f"Total yearly cost: ₹{total_yearly:.2f}\n\n"
            f"Most expensive: {most_expensive[0]}\n"
            f"Monthly cost: ₹{most_expensive[1]:.2f}\n"
            f"Yearly cost: ₹{most_expensive[1] * 12:.2f}\n"
            f"Share of yearly spending: {percentage:.1f}%"
        )

        result.config(
            text=summary,
            fg=TEXT
        )

        health_label = tk.Label(
            result_card,
            text=health,
            font=(FONT, 11, "bold"),
            bg=CARD,
            fg=health_color
        )

        health_label.pack(
            pady=(0, 20)
        )

        # --------------------------------------------------
        # CANCELLATION SECTION
        # --------------------------------------------------

        cancel_question = tk.Label(
            savings_card,
            text="Do you want to cancel any subscription? (yes/no)",
            font=(FONT, 11, "bold"),
            bg=CARD,
            fg=TEXT
        )

        cancel_question.pack(
            anchor="w",
            padx=35,
            pady=(0, 7)
        )

        cancel_entry = tk.Entry(
            savings_card,
            font=(FONT, 13),
            bg="#FAFBFC",
            fg=TEXT,
            relief="solid",
            bd=1
        )

        cancel_entry.pack(
            fill="x",
            padx=35,
            ipady=9
        )

        cancel_result = tk.Label(
            savings_card,
            text="",
            font=(FONT, 11),
            bg=CARD,
            fg=TEXT,
            justify="center"
        )

        cancel_result.pack(
            pady=15
        )

        def process_cancel_choice(event=None):

            choice = cancel_entry.get().strip().lower()

            if choice == "no":

                cancel_result.config(
                    text="No cancellation selected.",
                    fg=MUTED
                )

                cancel_entry.config(
                    state="disabled"
                )

            elif choice == "yes":

                cancel_entry.delete(0, tk.END)

                cancel_question.config(
                    text="Enter the subscription name to check:"
                )

                cancel_entry.focus_set()

                cancel_entry.bind(
                    "<Return>",
                    cancel_subscription
                )

            else:

                cancel_result.config(
                    text="Please enter yes or no.",
                    fg=RED
                )

        def cancel_subscription(event=None):

            cancel_name = cancel_entry.get().strip()

            found = False

            for name, cost in subscriptions:

                if name.lower() == cancel_name.lower():

                    savings = cost * 12

                    cancel_result.config(
                        text=(
                            f"Cancelling {name} could save "
                            f"₹{savings:.2f} per year."
                        ),
                        fg=GREEN
                    )

                    found = True
                    break

            if not found:

                cancel_result.config(
                    text="Subscription not found.",
                    fg=RED
                )

        cancel_entry.bind(
            "<Return>",
            process_cancel_choice
        )

        canvas.update_idletasks()

        canvas.yview_moveto(1)

    # ------------------------------------------------------
    # PROCESS SUBSCRIPTION
    # ------------------------------------------------------

    def process_subscription(event=None):

        name = name_entry.get().strip()

        if name == "":

            result.config(
                text="Please enter a subscription name.",
                fg=RED
            )

            name_entry.focus_set()
            return

        try:

            monthly = float(
                cost_entry.get()
            )

            if monthly < 0:

                result.config(
                    text="Monthly cost cannot be negative.",
                    fg=RED
                )

                cost_entry.focus_set()
                return

        except ValueError:

            result.config(
                text="Please enter a valid monthly cost.",
                fg=RED
            )

            cost_entry.focus_set()
            return

        subscriptions.append(
            (name, monthly)
        )

        yearly = monthly * 12

        result.config(
            text=(
                f"{name}\n\n"
                f"Monthly cost: ₹{monthly:.2f}\n"
                f"Yearly cost: ₹{yearly:.2f}"
            ),
            fg=TEXT
        )

        more_entry.focus_set()

    # ------------------------------------------------------
    # PROCESS YES / NO
    # ------------------------------------------------------

    def process_more(event=None):

        choice = more_entry.get().strip().lower()

        if choice == "yes":

            name_entry.delete(0, tk.END)
            cost_entry.delete(0, tk.END)
            more_entry.delete(0, tk.END)

            name_entry.focus_set()

            result.config(
                text="Enter the next subscription.",
                fg=MUTED
            )

        elif choice == "no":

            name_entry.config(
                state="disabled"
            )

            cost_entry.config(
                state="disabled"
            )

            more_entry.config(
                state="disabled"
            )

            show_summary()

        else:

            result.config(
                text="Please enter yes or no.",
                fg=RED
            )

            more_entry.focus_set()

    # ------------------------------------------------------
    # ENTER NAVIGATION
    # ------------------------------------------------------

    name_entry.bind(
        "<Return>",
        lambda event: cost_entry.focus_set()
    )

    cost_entry.bind(
        "<Return>",
        process_subscription
    )

    more_entry.bind(
        "<Return>",
        process_more
    )

    name_entry.focus_set()


# ==========================================================
# FEATURE 2
# WHERE IS MY MONEY GOING?
# ==========================================================

def open_spending():

    window = tk.Toplevel(app)

    window.title("Where Is My Money Going?")
    window.geometry("750x650")
    window.configure(bg=BG)

    create_header(
        window,
        "WHERE IS MY MONEY GOING?",
        "See which category takes most of your money."
    )

    card = create_card(window)

    categories = [
        "Food",
        "Shopping",
        "Travel",
        "Bills",
        "Entertainment",
        "Other"
    ]

    expenses = {}
    index = [0]

    tk.Label(
        card,
        text="MONTHLY SPENDING",
        font=(FONT, 17, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(pady=(30, 5))

    instruction = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=MUTED
    )

    instruction.pack(
        pady=(0, 25)
    )

    category_label = tk.Label(
        card,
        text="",
        font=(FONT, 14, "bold"),
        bg=CARD,
        fg=TEXT
    )

    category_label.pack()

    entry = create_entry(card)

    result = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=TEXT,
        justify="center"
    )

    result.pack(
        pady=25
    )

    def show_category():

        if index[0] < len(categories):

            category_label.config(
                text=categories[index[0]] + " expenses (₹)"
            )

            instruction.config(
                text=f"{index[0] + 1} of {len(categories)}"
            )

            entry.delete(0, tk.END)
            entry.focus_set()

        else:

            total = sum(expenses.values())

            if total == 0:
                label.config(text="SPENDING SUMMARY")
                instruction.config(text="")
                entry.pack_forget()
                result.config(
                    text=(
                        "No spending was entered.\n\n"
                        "Enter at least one expense to see your spending breakdown."
                    ),
                    fg=ORANGE
                )
                return

            highest = max(
                expenses,
                key=expenses.get
            )

            amount = expenses[highest]

            percentage = (
                amount / total
            ) * 100

            if percentage >= 50:

                health = (
                    "Consider reviewing this category."
                )
                color = RED

            elif percentage >= 30:

                health = (
                    "This category takes a significant share."
                )
                color = ORANGE

            else:

                health = (
                    "Your spending is fairly distributed."
                )
                color = GREEN

            breakdown = "\n".join(
                f"{cat}: {(value / total) * 100:.1f}%"
                for cat, value in expenses.items()
            )

            category_label.config(
                text="SPENDING INSIGHT"
            )

            instruction.config(
                text=""
            )

            entry.pack_forget()

            result.config(
                text=(
                    f"Total monthly spending: ₹{total:.2f}\n\n"
                    f"Highest spending: {highest}\n"
                    f"Amount: ₹{amount:.2f}\n"
                    f"Share: {percentage:.1f}%\n\n"
                    f"SPENDING BREAKDOWN\n"
                    f"{breakdown}\n\n"
                    f"{health}"
                ),
                fg=color
            )

    def next_field(event=None):

        try:

            value = float(
                entry.get()
            )

            if value < 0:

                result.config(
                    text="Expenses cannot be negative.",
                    fg=RED
                )

                return

            expenses[
                categories[index[0]]
            ] = value

            index[0] += 1

            show_category()

        except ValueError:

            result.config(
                text="Please enter a valid number.",
                fg=RED
            )

    entry.bind(
        "<Return>",
        next_field
    )

    show_category()


# ==========================================================
# FEATURE 3
# HIDDEN COST CALCULATOR
# ==========================================================

def open_hidden_cost():

    window = tk.Toplevel(app)

    window.title("Hidden Cost Calculator")
    window.geometry("750x650")
    window.configure(bg=BG)

    create_header(
        window,
        "HIDDEN COST CALCULATOR",
        "See the real cost behind the advertised price."
    )

    card = create_card(window)

    fields = [
        "Advertised Product Price",
        "Accessories",
        "Warranty",
        "Maintenance",
        "Other Fees"
    ]

    values = {}
    index = [0]

    tk.Label(
        card,
        text="ACTUAL COST CHECK",
        font=(FONT, 17, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(pady=(30, 5))

    instruction = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=MUTED
    )

    instruction.pack(
        pady=(0, 25)
    )

    label = tk.Label(
        card,
        text="",
        font=(FONT, 14, "bold"),
        bg=CARD,
        fg=TEXT
    )

    label.pack()

    entry = create_entry(card)

    result = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=TEXT,
        justify="center"
    )

    result.pack(
        pady=25
    )

    def show_field():

        if index[0] < len(fields):

            label.config(
                text=fields[index[0]] + " (₹)"
            )

            instruction.config(
                text=f"{index[0] + 1} of {len(fields)} • Press Enter"
            )

            entry.delete(0, tk.END)
            entry.focus_set()

        else:

            price = values["Advertised Product Price"]

            extra = (
                values["Accessories"] +
                values["Warranty"] +
                values["Maintenance"] +
                values["Other Fees"]
            )

            actual = price + extra

            percentage = (
                extra / price
            ) * 100

            if percentage >= 30:

                insight = (
                    "Hidden costs are very high."
                )
                color = RED

            elif percentage >= 20:

                insight = (
                    "Hidden costs are quite high."
                )
                color = ORANGE

            elif percentage >= 10:

                insight = (
                    "Additional costs are significant."
                )
                color = ORANGE

            else:

                insight = (
                    "Additional costs are relatively low."
                )
                color = GREEN

            label.config(
                text="ACTUAL COST"
            )

            instruction.config(
                text=""
            )

            entry.pack_forget()

            result.config(
                text=(
                    f"Advertised price: ₹{price:.2f}\n\n"
                    f"Additional costs: ₹{extra:.2f}\n"
                    f"Actual estimated cost: ₹{actual:.2f}\n\n"
                    f"Extra costs: {percentage:.1f}%\n\n"
                    f"{insight}"
                ),
                fg=color
            )

    def next_field(event=None):

        try:

            value = float(
                entry.get()
            )

            if value < 0:

                result.config(
                    text="Please enter a positive number.",
                    fg=RED
                )

                return

            values[
                fields[index[0]]
            ] = value

            index[0] += 1

            if (
                index[0] == 1
                and values["Advertised Product Price"] == 0
            ):

                result.config(
                    text="Product price must be greater than zero.",
                    fg=RED
                )

                index[0] -= 1
                return

            show_field()

        except ValueError:

            result.config(
                text="Please enter a valid number.",
                fg=RED
            )

    entry.bind(
        "<Return>",
        next_field
    )

    show_field()


# ==========================================================
# FEATURE 4
# CAN I AFFORD THIS?
# ==========================================================

def open_affordability():

    window = tk.Toplevel(app)

    window.title("Can I Afford This?")
    window.geometry("750x650")
    window.configure(bg=BG)

    create_header(
        window,
        "CAN I AFFORD THIS?",
        "Understand how a purchase affects your budget."
    )

    card = create_card(window)

    fields = [
        "Monthly Income",
        "Monthly Expenses",
        "Current Savings",
        "Purchase Price"
    ]

    values = {}
    index = [0]

    tk.Label(
        card,
        text="AFFORDABILITY CHECK",
        font=(FONT, 17, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(pady=(30, 5))

    instruction = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=MUTED
    )

    instruction.pack(
        pady=(0, 25)
    )

    label = tk.Label(
        card,
        text="",
        font=(FONT, 14, "bold"),
        bg=CARD,
        fg=TEXT
    )

    label.pack()

    entry = create_entry(card)

    result = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=TEXT,
        justify="center"
    )

    result.pack(
        pady=25
    )

    def show_field():

        if index[0] < len(fields):

            label.config(
                text=fields[index[0]] + " (₹)"
            )

            instruction.config(
                text=f"{index[0] + 1} of {len(fields)} • Press Enter"
            )

            entry.delete(0, tk.END)
            entry.focus_set()

        else:

            income = values["Monthly Income"]
            expenses = values["Monthly Expenses"]
            savings = values["Current Savings"]
            purchase = values["Purchase Price"]

            remaining = income - expenses

            label.config(
                text="AFFORDABILITY RESULT"
            )

            instruction.config(
                text=""
            )

            entry.pack_forget()

            if income <= 0:

                result.config(
                    text="Monthly income must be greater than zero.",
                    fg=RED
                )

                return

            if remaining <= 0:

                result.config(
                    text=(
                        "Your current expenses are equal to or "
                        "higher than your income.\n\n"
                        "Consider improving your monthly cash flow "
                        "before making this purchase."
                    ),
                    fg=RED
                )

                return

            ratio = (
                purchase / remaining
            ) * 100

            savings_ratio = 0

            if savings > 0:

                savings_ratio = (
                    purchase / savings
                ) * 100

            if ratio <= 50:

                decision = (
                    "Relatively affordable"
                )
                color = GREEN

            elif ratio <= 100:

                decision = (
                    "Think carefully before buying"
                )
                color = ORANGE

            else:

                decision = (
                    "May put pressure on your budget"
                )
                color = RED

            savings_text = (
                "Your savings can cover this purchase."
                if savings >= purchase
                else
                "Your savings cannot fully cover this purchase."
            )

            result.config(
                text=(
                    f"Money left after expenses: ₹{remaining:.2f}\n\n"
                    f"Purchase uses {ratio:.1f}% of your "
                    f"remaining monthly money.\n\n"
                    f"{decision}\n\n"
                    f"{savings_text}\n"
                    f"Savings usage: {savings_ratio:.1f}%"
                ),
                fg=color
            )

    def next_field(event=None):

        try:

            value = float(
                entry.get()
            )

            if value < 0:

                result.config(
                    text="Please enter a positive number.",
                    fg=RED
                )

                return

            values[
                fields[index[0]]
            ] = value

            index[0] += 1

            show_field()

        except ValueError:

            result.config(
                text="Please enter a valid number.",
                fg=RED
            )

    entry.bind(
        "<Return>",
        next_field
    )

    show_field()


# ==========================================================
# FEATURE 5
# EMI REALITY CHECKER
# ==========================================================

def open_emi():

    window = tk.Toplevel(app)

    window.title("EMI Reality Checker")
    window.geometry("750x650")
    window.configure(bg=BG)

    create_header(
        window,
        "EMI REALITY CHECKER",
        "See what the EMI really costs you."
    )

    card = create_card(window)

    fields = [
        "Product Price",
        "Down Payment",
        "Annual Interest Rate (%)",
        "Number of Months"
    ]

    values = {}
    index = [0]

    tk.Label(
        card,
        text="EMI CHECK",
        font=(FONT, 17, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(pady=(30, 5))

    instruction = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=MUTED
    )

    instruction.pack(
        pady=(0, 25)
    )

    label = tk.Label(
        card,
        text="",
        font=(FONT, 14, "bold"),
        bg=CARD,
        fg=TEXT
    )

    label.pack()

    entry = create_entry(card)

    result = tk.Label(
        card,
        text="",
        font=(FONT, 11),
        bg=CARD,
        fg=TEXT,
        justify="center"
    )

    result.pack(
        pady=25
    )

    def show_field():

        if index[0] < len(fields):

            label.config(
                text=fields[index[0]]
            )

            instruction.config(
                text=f"{index[0] + 1} of {len(fields)} • Press Enter"
            )

            entry.delete(0, tk.END)
            entry.focus_set()

        else:

            price = values["Product Price"]
            down = values["Down Payment"]
            rate = values["Annual Interest Rate (%)"]
            months = int(values["Number of Months"])

            label.config(
                text="EMI SUMMARY"
            )

            instruction.config(
                text=""
            )

            entry.pack_forget()

            if price <= 0:

                result.config(
                    text="Product price must be greater than zero.",
                    fg=RED
                )

                return

            if down < 0 or down >= price:

                result.config(
                    text=(
                        "Down payment must be less than "
                        "the product price."
                    ),
                    fg=RED
                )

                return

            if months <= 0:

                result.config(
                    text="Number of months must be greater than zero.",
                    fg=RED
                )

                return

            loan = price - down

            monthly_rate = (
                rate / (12 * 100)
            )

            if rate == 0:

                emi = loan / months

            else:

                emi = (
                    loan *
                    monthly_rate *
                    (1 + monthly_rate) ** months
                ) / (
                    (1 + monthly_rate) ** months - 1
                )

            total_payment = emi * months

            interest = (
                total_payment - loan
            )

            total_cost = (
                down + total_payment
            )

            if interest >= 10000:

                insight = (
                    "You will pay a significant amount in interest."
                )
                color = RED

            elif interest >= 5000:

                insight = (
                    "The interest cost is considerable."
                )
                color = ORANGE

            else:

                insight = (
                    "The interest cost is relatively low."
                )
                color = GREEN

            result.config(
                text=(
                    f"Loan amount: ₹{loan:.2f}\n"
                    f"Monthly EMI: ₹{emi:.2f}\n\n"
                    f"Total interest: ₹{interest:.2f}\n"
                    f"Total repayment: ₹{total_payment:.2f}\n\n"
                    f"Total amount paid: ₹{total_cost:.2f}\n\n"
                    f"{insight}"
                ),
                fg=color
            )

    def next_field(event=None):

        try:

            value = float(
                entry.get()
            )

            if value < 0:

                result.config(
                    text="Please enter a positive number.",
                    fg=RED
                )

                return

            values[
                fields[index[0]]
            ] = value

            index[0] += 1

            show_field()

        except ValueError:

            result.config(
                text="Please enter a valid number.",
                fg=RED
            )

    entry.bind(
        "<Return>",
        next_field
    )

    show_field()


# ==========================================================
# MAIN DASHBOARD
# ==========================================================

header = tk.Frame(
    app,
    bg=DARK,
    height=175
)

header.pack(fill="x")
header.pack_propagate(False)


tk.Label(
    header,
    text="SMART MONEY",
    font=(FONT, 31, "bold"),
    bg=DARK,
    fg="white"
).pack(pady=(25, 0))


tk.Label(
    header,
    text="Decision Assistant",
    font=(FONT, 17),
    bg=DARK,
    fg="#C4D0D9"
).pack(pady=(2, 0))


# KEEP THIS TAGLINE STYLE

tk.Label(
    header,
    text="See beyond the price. Decide with confidence.",
    font=("Arial", 11),
    bg=DARK,
    fg="#AEB6BF"
).pack(pady=(10, 0))


# ==========================================================
# DASHBOARD CONTENT
# ==========================================================

content = tk.Frame(
    app,
    bg=BG
)

content.pack(
    fill="both",
    expand=True,
    padx=85,
    pady=24
)


tk.Label(
    content,
    text="Your Money Tools",
    font=(FONT, 19, "bold"),
    bg=BG,
    fg=TEXT
).pack()


tk.Label(
    content,
    text="Choose a tool to understand your spending and make better decisions.",
    font=(FONT, 10),
    bg=BG,
    fg=MUTED
).pack(pady=(3, 18))


# ==========================================================
# DASHBOARD BUTTONS
# ==========================================================

buttons_frame = tk.Frame(
    content,
    bg=BG
)

buttons_frame.pack(fill="x")


button_style = {
    "font": (FONT, 12, "bold"),
    "bg": CARD,
    "fg": TEXT,
    "activebackground": "#DCE8EF",
    "activeforeground": TEXT,
    "relief": "solid",
    "bd": 1,
    "cursor": "hand2",
    "padx": 15,
    "pady": 14
}


def add_dashboard_button(parent, text, command, row, column):

    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=30,
        height=2,
        **button_style
    )

    button.grid(
        row=row,
        column=column,
        padx=8,
        pady=7,
        sticky="nsew"
    )

    def on_enter(event):
        button.config(
            bg="#E8F0F4",
            fg=ACCENT_DARK
        )

    def on_leave(event):
        button.config(
            bg=CARD,
            fg=TEXT
        )

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button


buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)


add_dashboard_button(
    buttons_frame,
    "Subscription Leak Detector",
    open_subscription,
    0,
    0
)

add_dashboard_button(
    buttons_frame,
    "Where Is My Money Going?",
    open_spending,
    0,
    1
)

add_dashboard_button(
    buttons_frame,
    "Hidden Cost Calculator",
    open_hidden_cost,
    1,
    0
)

add_dashboard_button(
    buttons_frame,
    "Can I Afford This?",
    open_affordability,
    1,
    1
)


# The fifth tool stays centered instead of stretching across the screen.
emi_button = add_dashboard_button(
    buttons_frame,
    "EMI Reality Checker",
    open_emi,
    2,
    0
)

emi_button.grid_configure(
    column=0,
    columnspan=2,
    padx=150
)


# ==========================================================
# FOOTER
# ==========================================================

tk.Label(
    app,
    text="Smart financial decisions start with understanding the real cost.",
    font=(FONT, 10),
    bg=BG,
    fg=MUTED
).pack(pady=(0, 15))


# ==========================================================
# START APP
# ==========================================================

app.mainloop()