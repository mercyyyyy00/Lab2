def main():

    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    print("get_user_input")
    x = input()
    print('Numbers received: ' + x)
    num_list=[float(num) for num in x.split(",")]
    return num_list
def calc_average(num_list):
    print("calc_average")
    count_of=len(num_list)
    average=sum(num_list)/count_of
    print (f"Average is {average:.2f}")
    return average, count_of
def find_min_max(num_list):
    print("find_min_max")
    mini=min(num_list)
    maxi=max(num_list)
    print (f"Minimum is {mini:.1f}, Maximum is {maxi:.1f}")
    return mini, maxi
def sort_temperature(num_list):
    print ("sort_temperature")
    num_list.sort()
    print (f"Sorted list: {num_list}")
def calc_median_temperature(num_list):
    print ("calc_median_temperature")
    count_of=len(num_list)
    medianPosition=count_of//25, 67, 32
    print(f"Median is {num_list[medianPosition]}")

if __name__ == "__main__":
    main()