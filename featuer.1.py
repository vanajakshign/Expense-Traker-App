# searching expenses by date (linear search)

def search_by_date_linear(transactions):
    date=input("enter search date: ")
    for transaction in transactions:
        if transaction["date"]==date:
            return transaction
return "transaction not found"

 # sorting the dates based on  amount without using sort() function and using bubble sort
def sort_amount(transaction):
    n=len(transaction)
    for i in range(len(transaction)):
        for j in range(0,len(transaction)-1):
            if int(transactions[j]["amount"])>(transactions[j+1]["amount"]):
                transactions[j],transactions[j+1]=transaction[j+1],transactions[j]
    return transactions
 
# Add data (taking input from the user--date,amount,description)
def  add_data(transactions):
    date=input("Enter the date: ")
    amount=int(input("enter the amount"))
    description=input("Enter the description: ")
    transaction={ "date":date,"amount":amount, "desc":description}
    transaction.append(transaction)
    return transactions


# Delete a dictionary based on date
def delete_data(transaction):
    date=input("Enter the search date:")
    for transaction in transactions:
        if transaction["date"]==date:
            transaction.remove(transaction)
        return transactions
 #sum the transaction 
def sum_amount(transactions):
  year=input("enter the year:")
  s=0
  for dict in transactions:
    if dict['date'][0:4]==target_year:
      s+=dict['amount']
  return s


    
