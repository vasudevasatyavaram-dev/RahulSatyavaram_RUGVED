class RugvedSystems:
#1
    def triple_and(self, isBlack, isExpensive, isFast):
        return isBlack and isExpensive and isFast
    
#2 
    def sort(self, strs):
        stringList = list(strs)
        length = len(strs)
        for i in range(length-1):
            for j in range(0, length-1-i):
                if stringList[j] < stringList[j+1]:
                    stringList[j], stringList[j+1] = stringList[j+1], stringList[j]
        strs = "".join(stringList)

        initial = 0
        for i in range(1, length):
            if strs[i] != strs[initial]:
                print(f'{strs[initial]} appeared {i-initial} times')
                initial = i
        print(f'{strs[initial]} appeared {length-initial} times')
        return strs

#3
    def hillNumber(self, number):
        lastDigit = number % 10
        num = number // 10
        secondLast = num % 10
        if num == 0:
            return True
        increased = False
        while num > 0 and secondLast < lastDigit:
            if secondLast == lastDigit:
                return False  # no repeats
            increased = True
            lastDigit = secondLast
            num = num // 10
            secondLast = num % 10
        if not increased:
            return False  # must have increasing phase before decreasing
        while num > 0:
            if secondLast == lastDigit or secondLast > lastDigit:
                return False  # must strictly decrease, and no repeats
            lastDigit = secondLast
            num = num // 10
            secondLast = num % 10
        return True


#4
    def selectionSort(self, arr):
        length = len(arr)
        for i in range(length):
            min = i
            for j in range(i,length):
                if(arr[j]<arr[min]):
                    min = j
            lst = list(arr)
            lst[i], lst[min] = lst[min], lst[i]
        return "".join(arr)

#5
    def fibonacci(self, num):
        if num <=1:
            return num
        else:
            return self.fibonacci(num-1) + self.fibonacci(num-2)
        
    num = input("enter an integer")
    print(fibonacci(num))

#6
    def anagram(self, st1, st2):
        return sort(st1)==sort(st2) #sort function is above for question number 2

#7
    def fibonacciSequence(self, n):
        a = 0
        b = 1
        if n>=0:
            print(a, end=" ")
        if n>=1:
            print(b, end=" ")
        if n>=2:
            for i in range(2,n+1):
                a, b = b, a+b
                print(b, end=" ")

#8
    def equalString1(self,strs,num):
        if len(strs)%num!=0:
            print("Not Possible")
        else:
            divisible = len(strs)//num
            sub = [strs[i:i+divisible] for i in range(0,len(strs),divisible)]
            for i in range(len(sub)-1):
                print(sub[i])
                if(sub[i]!=sub[i+1]):
                    print("Not Possible")
                    break
            else:
                print(sub[i])
                print("Success")

#9
    def ceaserCipher(self, shift, strs):
        result = ""
        for char in strs:
            if char.islower():
                result += chr((ord(char)-ord('a')+shift)%26+ord('a'))
            elif char.isupper():
                result += chr((ord(char)-ord('A')+shift)%26+ord('A'))
            else:
                result += char

#10
    def luhns(self, num):
        sum = 0
        length = len(num)
        lst = list(reversed(list(num)))
        i = 0
        while i < length:
            sum += int(lst[i])
            i += 1
            if i < length:
                double = int(lst[i]) * 2
                if double >= 10:
                    double -= 9  
                sum += double
                i += 1
        if sum % 10 == 0:
            print("Valid Credit Card")
        else:
            print("Invalid Credit Card")

#11
    def coleman(self, text):
        length = len(text)   
        letters = 0
        sentences = 0
        words = 1    

        for i in range(length):
            if text[i].isalpha():
                letters += 1
            if text[i] in '.!?':
                sentences += 1
            if text[i] == ' ':
                words += 1

        L = (letters / words) * 100   # Letters per 100 words
        S = (sentences / words) * 100 # Sentences per 100 words

        CLI = 0.0588 * L - 0.296 * S - 15.8
        print(f'The grade level is {CLI}')

#12
#Diamond
    def diamond(self, num):
        for i in range(num):
            for j in range(num-i-1):
                print(" ", end="")
            for j in range(i+1):
                print("* ", end="")
            print()
        for i in range(num-1):
            for j in range(i+1):
                print(" ", end="")
            for j in range(num-i-1):
                print("* ", end="")
            print()

#Butterfly
    def butterfly(self, num):
        if num == 1:
            print("*")
            return

        for i in range(1, num + 1):
            print("*" * i, end="")
            print(" " * (2 * (num - i)), end="")
            print("*" * i)

        for i in range(num, 0, -1):
            print("*" * i, end="")
            print(" " * (2 * (num - i)), end="")
            print("*" * i)

#13
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, c):
        self.color = c
    def get_color(self):
        return self.color
    @abstractmethod
    def get_area(self):
        pass

class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side
    def get_area(self):
        return self.side * self.side

#14
def first_repeating(arr):
    d = {}
    for i, val in enumerate(arr):
        if val in d:
            return val
        d[val] = i
    return None

#15
def rotate90(mat):
    n = len(mat)
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[n-j-1][i]
            mat[n-j-1][i] = mat[n-i-1][n-j-1]
            mat[n-i-1][n-j-1] = mat[j][n-i-1]
            mat[j][n-i-1] = temp

def spiralOrder(mat):
    res = []
    left, right = 0, len(mat[0])-1
    top, bottom = 0, len(mat)-1
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            res.append(mat[top][i])
        top += 1
        for i in range(top, bottom+1):
            res.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                res.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(mat[i][left])
            left += 1
    return res
