salary = input("gross salary of person? ")
gross_number_of_children = input ("Gross number of children? ")

try:
    salary = int(salary)
    gross_number_of_children = int(gross_number_of_children)

except ValueError:
    print("input only integers ")
    exit()

if salary < 1000:
    net_salary_of_person = (0.9+(gross_number_of_children*0.01))*salary
    print("this is your net salary: ", round(net_salary_of_person))

elif 1000 <= salary < 2000:
    net_salary_of_person = (0.88+(gross_number_of_children*0.01))*salary
    print("this is your net salary: ", round(net_salary_of_person))

elif 2000 <= salary < 4000:
    net_salary_of_person = (0.86+(gross_number_of_children*0.0055))*salary
    print("this is your net salary: ", round(net_salary_of_person))

else:
    net_salary_of_person = (0.82+(gross_number_of_children*0.005))*salary
    print("this is your net salary: ", round(net_salary_of_person))

