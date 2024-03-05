import pickle

# example_dict = {
#     "url" :"https://oauth2.googleapis.com/token?client_id=143443373358-kok70q3su8jc4qo8uhrr4d6dhdp6gaqp.apps.googleusercontent.com&client_secret=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&grant_type=refresh_token&refresh_token=1//0gjKKAQijzHNPCgYIARAAGBASNwF-L9IrQmoyLNxwURme1-_d739S_o67owFxg2yeLwo9zpd8_n09ATe-CQF-wVyH77QSAS4vxKA"
# }

# pickle_out = open('data.pickle',"wb")
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()

pickle_in = open("data.pickle", "rb")
example_dict = pickle.load(pickle_in)
print(example_dict,"example_dict")
print(example_dict["url"])