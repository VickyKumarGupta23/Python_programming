class  movie:
    '''This is movie store and looking movie store application demo '''
    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    def m1(self):
        print("The Movie name is:__",self.title)
        print("Hero of this movie is :__",self.hero)
        print("Heroine of the movie is:__",self.heroine)


list = []
while True:
    title = input("Enter the name of the Movie:__")
    hero = input('Enter the hero name: --')
    heroine = input("Enter the heroine name")

    m = movie(title,hero,heroine)
    list.append(m)
    print("Movie added Successfully********")
    option = input("Do you want more movie [Yes/NO]")
    if option.lower() == 'no':
        break
print('Here all the movie infor8mation those are added')
for movie_obj in list:
    movie_obj.m1()
    print()
