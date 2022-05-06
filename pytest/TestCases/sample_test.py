def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('/')[5]
    return f'<a target="_blank" href="{link}">{text}</a>'

def validate_phone(phone_number):
    if len(phone_number)<10:
        raise ValueError("Phone number cannot be less than 10")



def validate_email(email):
    if str(email).endswith(".com")==False:
        raise ValueError("Enter valid email")


def validate_ingredient_count(ingred_list):
    if len(ingred_list)==0:
        raise ValueError("Ingredients cannot be zero!")

