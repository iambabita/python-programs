class animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species

        def __makesound__(self):
            print("Sound made by the animal.")


class dog:
    def __init__(self , name , breed):
        animal.__init__(self , name , species="Dog")
        self.breed = breed
   
    def make_sound(self):
            print("Bark!")

d = dog("dog" , "German shepered")
d.make_sound()
a = animal("Cat" , "siamese")
a.__makesound__()




        

        