"""
main.py test
"""
import pytest

import main
import numeric_input
from person import Person
from ticket import Ticket


@pytest.fixture
def mock_functions(monkeypatch):
    """Monkeypatch to replace the functions 'login', 'transfer_money', 'select_menu' and 'create_ticket' in main"""

    def dummy_login():
        """Dummy function to replace the function 'login' in main"""
        pass

    def dummy_transfer():
        """Dummy function to replace the function 'transfer_money' in main"""
        pass

    def dummy_select_menu():
        """Dummy function to replace the function 'select_menu' in main"""
        print('Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden')
        return input('')

    def dummy_ticket():
        """Dummy function to replace the function 'create_ticket' in main"""
        pass

    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'transfer_money', dummy_transfer)
    monkeypatch.setattr(main, 'select_menu', dummy_select_menu)
    monkeypatch.setattr(main, 'create_ticket', dummy_ticket)


def test_main_exit(capsys, monkeypatch, mock_functions):
    """Test the main function with the exit option"""
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_money(capsys, monkeypatch, mock_functions):
    """Test the main function with the money transaction option"""
    inputs = iter(['A', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_ticket(capsys, monkeypatch, mock_functions):
    """Test the main function with the ticket creation option"""
    inputs = iter(['B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_ticket_joker_setter():
    """Test the setter of the joker property"""
    ticket = Ticket(0, [1, 2, 3, 4, 5, 6])
    try:
        ticket.joker = 'a'
    except ValueError:
        pass
    assert ticket.joker == 0


def test_ticket_number_setter():
    """Test the setter of the numbers property"""
    ticket = Ticket(0, [1, 2, 3, 4, 5, 6])
    ticket.numbers = [1, 2, 3, 4, 5, 6]
    assert ticket.numbers == [1, 2, 3, 4, 5, 6]


def test_person_givenname_setter():
    """Test the setter of the givenname property"""
    person = Person('name', 'password', 0)
    person.givenname = 'newname'
    assert person.givenname == 'newname'


def test_person_password_setter():
    """Test the setter of the password property"""
    person = Person('name', 'password', 0)
    person.password = 'newpassword'
    assert person.password == 'newpassword'


def test_person_balance_setter():
    """Test the setter of the balance property"""
    person = Person('name', 'password', 0)
    person.balance = 10
    assert person.balance == 10


def test_numeric_input_read_int(monkeypatch):
    """Test the read_int function with valid input"""
    inputs = iter(['5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert numeric_input.read_int('prompt', 0, 10) == 5


def test_numeric_input_read_float(monkeypatch):
    """Test the read_float function with valid input"""
    inputs = iter(['5.5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert numeric_input.read_float('prompt', 0, 10) == 5.5


def test_money_transfer():
    """Test the transfer_money function"""
    person1 = Person('name1', 'password1', 10)
    person2 = Person('name2', 'password2', 10)
    main.transfer_money(person1)
    assert person1.balance == 9
    assert person2.balance == 11


def test_money_select_transaction(monkeypatch):
    """Test the select_transaction function"""
    inputs = iter(['A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert main.select_transaction() == 'A'
