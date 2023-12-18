#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 1

            # Check if divisor is 0
            if divisor == 0:
                raise ZeroDivisionError("division by 0")

            # Perform the division
            division_result = dividend / divisor
            result.append(division_result)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            pass

    return result
