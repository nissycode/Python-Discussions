num = int(input("Input Score (Int): "))

if num >=0:
    if num <=10:
        print("BEGINNER LEARNER")
    else:
        if num <= 30:
            print("MID LEARNER")
        else:
            if num <=60:
                print("FAIR LEARNERS")
            else:
                if num <=100:
                    print("EXCELLENT LEARNERS")
else:
    print("Negative Number")