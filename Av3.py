#Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

#A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
#A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
#A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
#A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
#A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
#When the budget object is printed it should display:
#A title line of 30 characters where the name of the category is centered in a line of * characters.
#A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
#A line displaying the category total.
class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []


  def __str__(self):
    s = self.category.center(30, "*") + "\n"

    for item in self.ledger:
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      s += temp + "\n"

    s += "Total: " + str(self.get_balance())
    return s

  def deposit(self, amount, description=""):
    temp = {}
    temp['amount'] = amount
    temp['description'] = description
    self.ledger.append(temp)


  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      temp = {}
      temp['amount'] = 0 - amount
      temp['description'] = description
      self.ledger.append(temp)
      return True
    return False


  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance


  def transfer(self, amount, budget_cat):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_cat.category)
      budget_cat.deposit(amount, "Transfer from " + self.category)
      return True
    return False


  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True


def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    # Spaces
    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].category[i] + " "
      else:
        s += "   "
    # Spaces
    s += " "

  return s