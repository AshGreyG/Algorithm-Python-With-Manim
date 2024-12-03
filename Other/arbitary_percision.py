class BigInteger(object) :
    # __slots__ = ("inner_str", "storage", "is_positive", "size")

    def __init__(self, input : str) -> None :
        ''' constructor of BigInteger
            - @input: The original string of BigInteger, may be incorrect. \n
                Like "+++00123", "0123^126" (cannot be corrected).
        '''
        has_signed = 0              # 1 when input[0] == "+" or "-", 0 when not.
        index = -1                  # -1 when thek input is equal to zero, other positive number when not.
        correct = ""
        self.storage = []
        self.inner_str = "It is the default string, "\
                         "if this sentence appears, "\
                         "then there may be somthing wrong with your input string."
        self.size = 0

        for i in range(0, len(input)) :
            char = input[i]
            try :
                wrong_condition = [
                    (char == "-" or char == "+") and i != 0,
                    char != "-" and char != "+" and char < "0" and char > "9"
                ]
                if any(wrong_condition) :
                    raise Exception("Invalid Argument")
                if char >= "1" and char <= "9" and index == -1 :
                    index = i
            except Exception :
                print(input + "\n" + ' ' * i + "^ Invalid " + char + " character.")
                return
        
        if (input[0] == "+" or input[0] == "-") and index != -1 :
            correct = input[0] + input[index:]
        elif input[0] != "+" and input[0] != "-" and index != -1:
            correct = input[index:]
        elif index == -1 :
            correct = "0"

        if correct[0] == "+" :
            has_signed = 1
            self.is_positive = True
            self.size = len(correct) - 1
            self.inner_str = correct
        elif correct[0] == "-" :
            has_signed = 1
            self.is_positive = False
            self.size = len(correct) - 1
            self.inner_str = correct
        else :
            has_signed = 0
            self.is_positive = True
            self.size = len(correct)
            self.inner_str = "+" + correct  # If there is no sign, then we consider the BigInteger is postive by default.

        if has_signed == 0 :
            no_sign_correct = correct[::-1]
        else :
            no_sign_correct = correct[:0:-1]

        for char_correct in no_sign_correct :

            # - When has_signed = 1 : +123
            #                         ^ notice that has_signed - 1 is not achievable

            # 2024-12-03 21:53 A important bug : when has_signed == 0, correct[:-1:-1] will return empty list []

            self.storage.append(int(char_correct))
    

    def __str__(self) -> str :
        ''' React with built-in *print() function
            - while using *print() function to print the BigIntegr object, 
            *print() function will print the inner string or string style 
            of the BigInteger object
        '''
        return self.inner_str

    def __len__(self) -> int :
        ''' React with built-in *len() function
            - while using *len() function to get the length of the BigInteger 
              object, it will return the size
        '''
        return self.size


    
    def __eq__(self, another : "BigInteger") -> bool:
        ''' Overload the == operator
            - @another: Another BigInteger object that needs to be judged if equal
            - return: The boolean value of a == b
        '''
        if self.size != another.size :
            return False
        elif self.is_positive != another.is_positive :
            return False
        else :
            for i in range(0, self.size) :
                if self.storage[i] != another.storage[i] :
                    return False
            return True

    def __ne__(self, another : "BigInteger") -> bool:
        ''' Overload the != operator
            - @another: Another BigInteger object that needs to be judged if not equal
            - return: The boolean value of a != b
        '''
        return not(self == another)

    def __ls__(self, another: "BigInteger") -> bool :
        ''' Overload the < operator
            - @another: Another BigInteger object that needs to be judged if equal
            - return: The boolean value of a < b
        '''
        sip = self.is_positive
        aip = another.is_positive
        ses = self.size
        ans = another.size

        if sip and aip and ses < ans :
            return True
        elif sip and aip and ses > ans :
            return False
        elif not sip and not aip and ses < ans :
            return False
        elif not sip and not aip and ses > ans :
            return True
        elif sip and not aip :
            return False
        elif not sip and aip :
            return True
        elif ses == ans :
            for i in range()
        
    
    def __add__(self, aonther: "BigInteger") -> "BigInteger":
        ''' Overload the + operator
            - @another: Another BigInteger object that needs to be added
            - return: The result of a + b
        '''
        new = BigInteger()

    def to_string(self) -> str :
        ''' Return the string style of BigInteger object
            - return: The inner string or string style of the BigInteger object
        '''
        return self.inner_str


# -------------- TEST -------------- 

def test_valid() -> None :
    ''' test for valid checking
        - Such as "++12+12", "^^12" are not valid
    '''

    print(BigInteger("++12+"), 
          BigInteger("000012"),
          BigInteger("-00012012"),
          BigInteger("+01289012903"),
          BigInteger("1230"),
          sep="\n")

def test_comparision() -> None :
    ''' test for comparision
        - Such as a == b, a > b, a < b, a != b, a <= b, a >= b
    '''

    def print_result(a : BigInteger, b : BigInteger) -> None :
        print(f"{a} V.S {b}",
               "--------------",
              f"a == b : {a == b}",
              f"a != b : {a != b}",
               "--------------",
              sep="\n")


    print_result(BigInteger("-1234"), BigInteger("+1234"))
    print_result(BigInteger("123"), BigInteger("+123"))
    
def test_len() -> None :
    ''' test for built-in funcion *len()
        - Such as len(BigInteger("123"))
    '''
    print("---len---",
          len(BigInteger("123")),
          len(BigInteger("+1234")),
          len(BigInteger("++++1230")),
          "--------",
          sep="\n")
 

if __name__ == "__main__" :
    test_valid()
    test_comparision()
    test_len()