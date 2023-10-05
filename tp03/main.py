# ZeroDivisionError : UpperCamelCase
# zeroDivisionError : camelCase
# zero_division_error : snake_case
# zero-division-error : kebab case
import traceback


class DouzeDivisionError(ArithmeticError):

    def __init__(self) -> None:
        super().__init__("Division par 12 !")


def div(a,b):
    if b==12:
        # e = Exception("Division par 12 !")
        e = DouzeDivisionError()
        raise e
    r= a/b
    return r


def call_div(a,b):
    try:
        print("ouverture fichier")
        r = div(a,b)
    # except Exception as e:
    #     print("Erreur call_div",e)
    finally:    
        print("fermeture fichier")
    
    return r


def main():
    try:
        a = 2
        b = int(input("b:"))
        # c = a/b
        c = call_div(a,b    )

        print(c)
    except ZeroDivisionError as e   :
        print("ZeroDivisionError",e)
    except DouzeDivisionError as e:
        print("DouzeDivisionError",e)
        # traceback.print_exc()
    # except TypeError as e   :
    #     print("TypeError",e)
    # except ValueError as e   :
    #     print("ValueError",e)
    except Exception as e:
        print("Exception",e)
        pass
    else:
        print("pas d'erreur")
    print("la suite du code...")

if __name__=='__main__':
    main()
