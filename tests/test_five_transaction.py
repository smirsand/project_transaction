from src.five_transaction import five_transaction


def test_five_transaction():
    assert len(five_transaction()) == 5
    assert len(five_transaction()) != 4
    assert len(five_transaction()) != 6
