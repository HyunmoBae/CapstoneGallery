#함수
def deposit(balance, money): 
    print("입금완료 잔액 {0} 원입니다.".format(balance+money))
    return balance + money

def m_minus(balance,money):
    if balance >= money:
        print("출금완료. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금할수 없습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

balance = 0 #최초금액
balance = deposit(balance, 1000) 
balance = m_minus(balance,500)
print(balance)   


    
