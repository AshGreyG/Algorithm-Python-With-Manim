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
            self.size = len(correct) - 1
            self.inner_str = correct
    
        for char_correct in correct[:index + has_signed - 1:-1] :
            self.storage.append(int(char_correct))

    def to_string(self) -> str :
        ''' return the string style of BigInteger object
            - return:  
        '''
        return self.inner_str

def test_valid() -> None :
    ''' test for valid checking
        - Such as "++12+12", "^^12" are not valid
    '''
    test_1 = BigInteger("++12+")
    test_2 = BigInteger("000012")

    print(test_1.to_string(), 
          test_2.to_string(),
          sep="\n")

if __name__ == "__main__" :
    test_valid()