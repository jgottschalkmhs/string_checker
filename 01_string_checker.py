def string_checker(question, to_check):
  
  valid = False
  while not valid:

    response = input(question).lower()

    for item in to_check:
      if response == item:
        return response

    print("sorry that is not a valid response")

yes_no = ["yes", "no"]

mood = string_checker("Are you happy? ", yes_no)

