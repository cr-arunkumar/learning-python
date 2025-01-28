
import requests
import json 
try:
    my_ans=10/0
    print(my_ans)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

    # handling the multiple exceptions
    try:
        # my_input=int(input("Please enter a number: "))
        # print(my_i nput*2)
        pass
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    except TypeError as e:
        print(f"Math error: {e}")
    except Exception as e:
        print("An unexpected error occurred:",e)

def validate_age(age):
    if age < 18:
        raise ValueError("Age cannot be less than 18")
    return age
validate_age(29)
# reading a file 
try:
    file=open("./fundamentals/demo.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An unexpected error occurred:",e)
else:
    print("File successfully opened and read.")
finally:
    print("Finally block executed.")

print("----------------------------------------------------------------")

try:
    with open("fundamentals/demo.txt", "r") as file:
        content = file.read()
        print("my file content:- ",content)
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"I/O Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("File successfully opened and read.")


print("----------------------making api requests------------------------------------------")
api_url="https://jsonplaceholder.typicode.com/posts/4"

try:
    response = requests.get(api_url)
    if not response.ok:
        raise requests.exceptions.HTTPError(response.status_code)
    data = response.json()
    print("Data from the api request", json.dumps(data, indent=4))
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code}")
except requests.exceptions.ConnectionError:
    print("Network connection failed")
except ValueError:  # Bad JSON
    print("Invalid API response format")   


try:
  f = open("./fundamentals/demo.txt","w+")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

print("----------------------------------------------------------------")
