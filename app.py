import sys
import json
import requests


def print_match(value):
    """Finds the specific match seeking numbers in a list

     Prints the firts and last name of all players whose
     the sum of the heights in inches are equal to value

    Parameters:
    value -- positive integer  must be greater than 50 and less than 180

    Excepcions:
    ValueError -- if (type(value) != int or type(value) != float)
    
    """
    try:
        value = int(value)

        if 50 < value < 180:
            # Catch the json from internet
            url = requests.get("https://mach-eight.uc.r.appspot.com/")
            text = url.text

            #Convert in a diccionary
            data = json.loads(text) 

            flag = False
            count = 0

            #Slicing of the array inside diccionary
            for i in range(len(data["values"])):
                for j in range(count, len(data["values"])):

                    #Avoid the same index
                    if j == i:
                        continue

                    if int(data['values'][i]["h_in"]) + int(data['values'][j]["h_in"]) == value:
                        flag = True
                        print("-" + data['values'][i]["first_name"] + " " + data['values'][i]["last_name"], end=" " * 6)
                        print(data['values'][j]["first_name"] + " " + data['values'][j]["last_name"])
                
                #Increase the count for avoid past index
                count = count + 1

            # When there are not matches
            if not flag:
                print("No matches found")
        else:
            print("The number ingressed is not in the range")

    except:
        print("Input an Integer value")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_match(sys.argv[1])

