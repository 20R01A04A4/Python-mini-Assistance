while True:
    project=input('Enter Usernanme:')
    if project == 'sai':
        password=input('Enter password:')
        if password == 'sai':
            print('welcome sai☻')
            import winsound
            winsound.PlaySound("welcome", winsound.SND_FILENAME)
            print('Welcome',project,'I am your Mini Assistant how can i help you☻')
            while True:
                print('1.song')
                print('2.show calender')
                print('3.calculator')
                print('4.send a message')
                print('5.open personal links   ')
                print('6.Tell me a joke   ')
                print('7.If you have any other quries ASK TO CHATGPT: PRESS 8 TO ENTER:')
                hi = input('>')
                if hi =='1':
                    print('playing song from playlist☻')
                    import winsound
                    winsound.PlaySound("song", winsound.SND_FILENAME)
                    print('1) mehabooba  '
                          '2) khaleja  '
                          '3) pathan  '
                          '4) Exit')
                    import winsound
                    sg = input('>')
                    if sg == '1':
                        winsound.PlaySound("mehabooba", winsound.SND_FILENAME)
                    if sg == '2':
                        winsound.PlaySound("khaleja", winsound.SND_FILENAME)
                    if sg == '3':
                        winsound.PlaySound("pathan", winsound.SND_FILENAME)
                        if sg=='4':
                            break
                elif hi=='4':
                    import pywhatkit as pwt

                    msg = input('what messege do you want to send:')
                    msg2 = int(input('At what hour:'))
                    msg4 = int(input('At what minute:'))
                    msg3 = input('enter phone number:')
                    pwt.sendwhatmsg('+91' + msg3, msg, msg2, msg4)
                    print('hi')
                elif hi=='2':
                    cal=input('which year:')
                    cal2=input('which month:')
                    import calendar
                    year = int(cal)
                    month =int(cal2)
                    print(calendar.month(year, month))
                elif hi=='3':
                    print('Type add for additions:')
                    print('Type sub for subractions:')
                    print('Type mul for multiplications:')
                    print('Type div for divisions:')
                    print('Type sqr for square roots:')
                    print('Type fact for factorials:')
                    print('Type mod for modulations:')
                    print('Type pow for power:')
                    print('Type sin for sine functions:')
                    print('Type log for logirthms:')
                    print('press exit for exit')
                    while True:
                        import itertools
                        import math

                        cal = input('>')
                        if cal == 'add':
                            print('now you can add numbers:')
                            print('press "  = and enter  " to equate all numbers')
                            lst = []
                            for n in itertools.count():
                                number = input('')
                                if number == '=':
                                    break
                                lst.append(int(number))
                            print(sum(lst))
                        if cal == 'sub':
                            print('you can subract only two numbers at a Time:')
                            num1 = int(input())
                            num2 = int(input())
                            print(num1 - num2)
                        if cal == 'mul':
                            print('Now you can multiple numbers:')
                            print('press "  = and enter  " to equate all numbers')
                            numbers = []
                            for k in itertools.count():
                                mul = input()
                                if mul == '=':
                                    break
                                numbers.append(int(mul))
                            product = 1
                            for num in numbers:
                                product *= num
                            print(product)
                        if cal == 'div':
                            div = int(input())
                            div2 = int(input())
                            print(div / div2)
                        if cal == 'sqr':
                            sqr = int(input())
                            print(math.sqrt(sqr))
                        if cal == 'fact':
                            fact = int(input())
                            print(math.factorial(fact))
                        if cal == 'mod':
                            mod = int(input())
                            print(math.modf(mod))
                        if cal == 'pow':
                            pow = int(input('Enter base:'))
                            pow2 = int(input('Enter power'))
                            print(math.pow(pow, pow2))
                        if cal == 'sin':
                            sin = int(input())
                            print(math.sin(math.radians(sin)))
                        if cal == 'log':
                            lo = int(input('give base:'))
                            log2 = int(input('Enter pow:'))
                            print(math.log(lo, log2))
                        if cal == 'exit':
                            break
                elif hi=='5':
                    while True:
                        import webbrowser

                        print('NOTE:PRESS ctrl w AFTER USAGE...')
                        print('1) My resume  ')
                        print('2) open instagram   ')
                        print('3) open whatsapp   ')
                        print('4) open youtube with less adds   ')
                        print('5) open youtube directly   ')
                        print('6) open google  ')
                        per = input('>')
                        if per == '1':
                            webbrowser.open('file:///C:/Users/ramse/OneDrive/Documents/Desktop/RESUME.pdf')
                        elif per == '2':
                            webbrowser.open('https://www.instagram.com/ramsetty_saikrishna/saved/all-posts/?hl=en')
                        elif per == '3':
                            webbrowser.open('https://web.whatsapp.com/')
                        elif per == '4':
                            webbrowser.open('https://search.brave.com/search?q=youtube&source=web')
                        elif per == '5':
                            webbrowser.open('https://www.youtube.com/')
                        elif per == '6':
                            webbrowser.open('https://www.google.com/')
                        else:
                            break
                elif hi=='6':
                    import pyjokes
                    print(pyjokes.get_joke(language="en", category="neutral"))

                elif hi=='7':
                    import webbrowser
                    webbrowser.open('https://chat.openai.com/')
                else:
                    print('As iam mini please choose from below list only..')
        else:print('Please Enter a valid password:')
    else:
        print('Enter Username currectly:')