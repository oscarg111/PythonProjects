# code that might throw error
try:
    a_dict = {"Key": "Value",
              "oscar": "gross"}
    print(a_dict["oscar"])

# catches errors
except FileNotFoundError:
    print("there was an error")
except KeyError as error_message:
    print(f"The key {error_message} not found")

# executes if no errors
else:
    print("works")

# executes no matter what
finally:
    print("everything finished")
# -------------------------------------------------------------------
height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Humans are not that tall stop lying")

bmi = weight / height**2
print(bmi)
