import employee_info as EMP
from employee_info import employee_data as EMPDATA #to simplify array list and not copy the whole thing here



def test_get_employees_by_age_range():
    upper = 33
    lower = 29
    expected = [EMPDATA[0], EMPDATA[4]]
    result = EMP.get_employees_by_age_range(lower, upper)
    assert(result == expected)

def test_calculate_average_salary():
    expected = 60166.67 # remb to use round off function in another file and use exact value here
    result = EMP.calculate_average_salary()
    assert(result == expected)
 


def test_get_employees_by_dept_engg():
    targetDept = "Engineering"
    expected = [EMPDATA[3], EMPDATA[4]] #need to change value here for different testing
    result = EMP.get_employees_by_dept(targetDept)
    assert(result == expected)


def test_get_employees_by_dept_marketing():
    targetDept = "Marketing"
    expected = [EMPDATA[1], EMPDATA[2]] #need to change value here for different testing
    result = EMP.get_employees_by_dept(targetDept)
    assert(result == expected)
