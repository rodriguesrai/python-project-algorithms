from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("hello", 2) == "oll_eh"

    with pytest.raises(TypeError):
        encrypt_message("hello", "2")

    with pytest.raises(TypeError):
        encrypt_message(123, 2)

    assert encrypt_message("hello", 6) == "olleh"
