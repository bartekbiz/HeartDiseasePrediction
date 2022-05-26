def change_y_n(input):
    if input == 'y':
        return 'Yes'
    else:
        return 'No'


print('Hi, I am going to predict if you have a heart disease.\n')


while True:
    print('You will be asked 17 questions but answer only using available options.\n')

    try:
        BMI = float(input('What is your BMI? - should be typed with dot "." not ",".'))

        Sex = input('Are you male or female? - type "male" or "female".')
        assert Sex in ['male', 'female']
        Sex = Sex.title()

        AgeCategory = int(input('What is your age? - type integer number.'))

        if int(AgeCategory) <= 24:
            AgeCategory = '18-24'
        elif 25 <= int(AgeCategory) <= 29:
            AgeCategory = '25-29'
        elif 30 <= int(AgeCategory) <= 34:
            AgeCategory = '30-34'
        elif 35 <= int(AgeCategory) <= 39:
            AgeCategory = '35-39'
        elif 40 <= int(AgeCategory) <= 44:
            AgeCategory = '40-44'
        elif 45 <= int(AgeCategory) <= 49:
            AgeCategory = '45-49'
        elif 50 <= int(AgeCategory) <= 54:
            AgeCategory = '50-54'
        elif 55 <= int(AgeCategory) <= 59:
            AgeCategory = '55-59'
        elif 60 <= int(AgeCategory) <= 64:
            AgeCategory = '60-64'
        elif 65 <= int(AgeCategory) <= 69:
            AgeCategory = '65-69'
        elif 70 <= int(AgeCategory) <= 74:
            AgeCategory = '70-74'
        elif 75 <= int(AgeCategory) <= 79:
            AgeCategory = '75-79'
        elif int(AgeCategory) >= 80:
            AgeCategory = '80 or older'
        else:
            raise Exception

        race_options = ['white', 'black', 'asian', 'american', 'hispanic', 'other']
        Race = input('What is your race? - choose from: white, black, asian, american indian/alaskan native '
                     '(type american), hispanic, other')
        assert str(Race) in race_options
        if Race == 'american':
            Race = 'American Indian/Alaskan Native'
        else:
            Race = Race.title()

        SleepTime = float(input('How many hours on average do you sleep? - should be typed with dot "." not ",".'))

        gen_health_options = ['excellent', 'vg', 'good', 'fair', 'poor']
        GenHealth = input('How can you define your general health? - choose from: '
                          'excellent, very good (type vg), good, fair, poor')
        assert GenHealth in gen_health_options
        if GenHealth == 'vg':
            GenHealth = 'Very good'
        else:
            GenHealth = GenHealth.title()

        Smoking = input('Have you smoked at least 100 cigarettes in your entire life? '
                        '[Note: 5 packs = 100 cigarettes] - type y or n (for Yes or No).')
        assert str(Smoking) in ['y', 'n']
        Smoking = change_y_n(Smoking)

        AlcoholDrinking = input('Do you have more than 14 drinks of alcohol (men) or more than 7 (women) in a week?'
                                '- type y or n (for Yes or No).')
        assert str(AlcoholDrinking) in ['y', 'n']
        AlcoholDrinking = change_y_n(AlcoholDrinking)

        Stroke = input('Have you ever had a stroke? - type y or n (for Yes or No).')
        assert str(Stroke) in ['y', 'n']
        Stroke = change_y_n(Stroke)

        PhysicalHealth = int(input('For how many days during the past 30 days was your physical health not good?'
                                   '- type integer number.'))

        MentalHealth = int(input('For how many days during the past 30 days was your mental health not good?'
                                 '- type integer number.'))

        DiffWalking = input('Do you have serious difficulty walking or climbing stairs? - type y or n (for Yes or No).')
        assert str(DiffWalking) in ['y', 'n']
        DiffWalking = change_y_n(DiffWalking)

        PhysicalActivity = input('Have you played any sports (running, biking, etc.) in the past month?'
                                 '- type y or n (for Yes or No).')
        assert str(PhysicalActivity) in ['y', 'n']
        PhysicalActivity = change_y_n(PhysicalActivity)

        diabetic_options = ['y', 'n', 'nb', 'yp']
        Diabetic = input('Have you ever had diabetes? - choose from: y, n, "no, borderline diabetes" (type "nb"),'
                         '"yes, during pregnancy" (type "yp")')
        assert str(Diabetic) in diabetic_options
        if Diabetic == 'y':
            Diabetic = 'Yes'
        elif Diabetic == 'n':
            Diabetic = 'No'
        elif Diabetic == 'nb':
            Diabetic = 'No, borderline diabetes'
        elif Diabetic == 'yp':
            Diabetic = 'Yes (during pregnancy)'
        else:
            raise Exception

        Asthma = input('Do you have asthma? - type y or n (for Yes or No).')
        assert str(Asthma) in ['y', 'n']
        Asthma = change_y_n(Asthma)

        KidneyDisease = input('Do you have kidney disease? - type y or n (for Yes or No).')
        assert str(KidneyDisease) in ['y', 'n']
        KidneyDisease = change_y_n(KidneyDisease)

        SkinCancer = input('Do you have skin cancer? - type y or n (for Yes or No).')
        assert str(SkinCancer) in ['y', 'n']
        SkinCancer = change_y_n(SkinCancer)

        break

    except Exception as e:
        print('There occured an error: {}\n'.format(e))


dict_data = {'HeartDisease': 'No', 'BMI': BMI, 'Smoking': Smoking, 'AlcoholDrinking': AlcoholDrinking,
             'Stroke': Stroke,
             'PhysicalHealth': PhysicalHealth, 'MentalHealth': MentalHealth, 'DiffWalking': DiffWalking,
             'Sex': Sex,
             'AgeCategory': AgeCategory, 'Race': Race, 'Diabetic': Diabetic, 'PhysicalActivity': PhysicalActivity,
             'GenHealth': GenHealth, 'SleepTime': SleepTime, 'Asthma': Asthma, 'KidneyDisease': KidneyDisease,
             'SkinCancer': SkinCancer}

print('\nPreparing your prediction...')

import heart as h

prediction = h.predict_input_heart(dict_data)

result = '''
\nRandomForest model which predicts well about 86% of the time,
predicts that you have about {}% chance of having a heart disease.
    
LogisticRegression model which predicts well about 91% of the time,
predicts that you {} have a heart disease.
'''.format(prediction[0] * 100, 'fortunately do not' if prediction[1] == 0 else 'unfortunately')

print(result)
