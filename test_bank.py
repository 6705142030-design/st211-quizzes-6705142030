import pytest
from bank import BankAccount

def test_deposit_increases_balance():
    account = BankAccount(100)
    result = account.deposit(50)
    assert result == 150

def test_withdraw_decreases_balance():
    account = BankAccount(100)
    result = account.withdraw(30)
    assert result == 70

def test_deposit_negative_raises_error():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw_too_much_raises_error():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(200)