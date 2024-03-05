import pickle
file = 'token_data.pickle'
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar,'mycar')
print(type(mycar))