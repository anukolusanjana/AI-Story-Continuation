import pytest
from model import generate_story

def test_empty_prompt_rejected():
    with pytest.raises(ValueError):
        generate_story("   ")

def test_long_prompt_rejected():
    with pytest.raises(ValueError):
        generate_story("x" * 4001)

def test_invalid_length_rejected():
    with pytest.raises(ValueError):
        generate_story("A story begins", 5, 0.8)

def test_invalid_temperature_rejected():
    with pytest.raises(ValueError):
        generate_story("A story begins", 50, 2.0)
