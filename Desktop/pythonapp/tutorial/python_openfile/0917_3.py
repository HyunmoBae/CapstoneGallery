#pickle
import pickle

#profile_file = open("profile.pickle","wb") #바이너리 형식으로 저장
#profile = {"이름":"홍길동","나이":20,"학과":"융합복합학과"}

#print(profile)
#pickle.dump(profile,profile_file)
#profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)

print(profile)
profile_file.close()