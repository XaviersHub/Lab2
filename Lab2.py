def main():
    print("ET0735 (DevOps for AIot)")
    display_main_menu()
    lst = get_user_input()
    calc_average_temp(lst)
    find_min_max(lst)
    sort_temp(lst)

def display_main_menu():
    print("display_main_menu")
    

def get_user_input():
    user = input("Enter an input float: ").split(",")
    print(user)
    user = [float(i) for i in user]
    print(user)
    return user

def calc_average_temp(lst):
    total = sum(lst)
    avg = total/len(lst)
    print(avg)
    return avg

def find_min_max(lst):
    min_temp = min(lst)
    max_temp = max(lst)
    lst = [min_temp,max_temp]
    return lst

def sort_temp(lst):
    print("Sorting temp in ascending order")
    lst = lst.sort()
    print(lst)  
    return lst

def calc_median_temp():
    lst = sort_temp()
    print("Calculating median temperature")
    lst = statistics.median(lst)
    return lst




if __name__  == "__main__":
    main()


