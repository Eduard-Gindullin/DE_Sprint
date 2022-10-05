number = int(input('Введите число от 0 до 2000: '))
if number < 0:
    print("Ваше число должно быть больше 0")
elif number > 2000:
    print("Ваше число слишком большое")
else: 
    def roman(number):
        
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thous = ["","M","MM","MMM","MMMM"]
    
        t = thous[number // 1000]
        h = hunds[number // 100 % 10]
        te = tens[number // 10 % 10]
        o =  ones[number % 10]
        return t+h+te+o
   # print(roman.text)