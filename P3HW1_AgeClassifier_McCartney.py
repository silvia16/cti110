
#CTI110
#Silvia
#Age Classifier

age_person=int(input("Enter age "))



if age_person <=1:
    print ("The person is an infant")
    
elif age_person >1 and age_person <=13:
    print ("The person is a child")

elif age_person >=13 and age_person <=20:
    print("The person is teenager")
elif age_person>=20:
    print ("The person is adult")
