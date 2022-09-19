import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

with open("test.txt","w",encoding="utf8") as test_file:
    test_file.write("테스트 문장입니다.")

with open("test.txt","r",encoding="utf8") as test_file:
    print(test_file.read())