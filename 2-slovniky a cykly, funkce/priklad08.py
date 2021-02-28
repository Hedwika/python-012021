def verif(number):
    number = number.replace(" ", "")
    if len(number) == 13:
        if number.startswith("+420"):
            try:
                number = int(number)
                return True
            except ValueError:
                return False
        else:
             return False
    elif len(number) == 9:
        try:
            number = int(number)
            return True
        except ValueError:
            return False
    else:
        return False


def price(message):
    one_message_price = 3
    message_length = int(len(message))
    number_of_messages = round((message_length/180))
    if (message_length % 180) != 0:
        number_of_messages = number_of_messages + 1
    return one_message_price * number_of_messages


numberInput = input("Zadejte své telefonní číslo: ")
print(verif(numberInput))
if verif(numberInput):
    messageInput = input("Zadejte zprávu, kterou chcete poslat: ")
    print(f"Cena za vaši zprávu je {price(messageInput)} Kč.")