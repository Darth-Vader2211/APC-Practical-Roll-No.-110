def create_account(name, account_no, balance):
    return {
        "name": name,
        "account_no": account_no,
        "balance": balance
    }


def get_balance(account):
    return account["balance"]