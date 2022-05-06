from sample_test import *


#Passed test cases

def test_validate_email():
    validate_phone("akanksha@gmail.com")


def test_validate_phone_number():
    validate_phone("1345627890")



def test_validate_ingredient_list():
    validate_ingredient_count(["potato","chicken"])


#Failed cases

def test_validate_ingredient_list():
    validate_ingredient_count([])



def test_validate_phone_number():
    validate_phone("13450")
