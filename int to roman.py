#! /usr/bin/env python





def intToRoman(num: int) -> str:

        romans = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X": 10,
            "XL" : 40,
            "L" : 50,
            "XC": 90,
            "C" : 100,
            "CD": 400,
            "D": 500,
            "CM" : 900,
            "M" : 1000
        }
        # Getting a list of both our keys and values 
        value_list = list(romans.values())
        key_list = list(romans.keys())

        string = str(num)
        solution = ''
        components = []

        # Getting the place values for each digit
        for i in range(len(string)):
            sub = string[i] + ((len(string)-(i+1))*'0')
            components.append(int(sub))
        

        for j in components:
            if j in value_list:
                solution += key_list[value_list.index(j)]
            else:
                if j == 0:
                    continue
                smaller_than_j = [i for i in value_list if i < j] # smaller than j 
                temp = smaller_than_j[-1] # The maximum of the smaller than j list
                if len(smaller_than_j) == 1:
                    solution += key_list[temp-1]*j
                else:
                    if temp * 2  == j or temp * 3 == j:
                        smaller_num = smaller_than_j[-1]
                        solution += key_list[value_list.index(temp)]
                        while temp < j:
                            solution += key_list[value_list.index(smaller_num)]
                            temp += smaller_num
                    else:
                        smaller_num = smaller_than_j[-3]
                        solution += key_list[value_list.index(temp)]
                        while temp < j:
                            solution += key_list[value_list.index(smaller_num)]
                            temp += smaller_num

                    
                
        return solution



print(intToRoman(564))










