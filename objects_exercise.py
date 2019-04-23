class Person: 
    
    def __init__(self, name, email, phone, friends): 
        self.name = name 
        self.email = email 
        self.phone = phone
        self.friends = []
        self.greet_count = 0
        self.unique_greet_list = []

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greet_count += 1
        if other_person.name not in self.unique_greet_list:
            self.unique_greet_list.append(other_person.name)
        return     

    def greeting_count(self):
        print('{}\'s greeting count is {}'.format(self.name, self.greet_count))

    def num_unique_people_greeted(self):
        print('{} has greeted {} unique people'.format(self.name, len(self.unique_greet_list)))

    def contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone))

    def add_friend(self, other_person):
        return self.friends.append(other_person.name)

    def num_friends(self):
        return (len(self.friends))

#Instantiate Person Object
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", "")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", "")
dee_ann = Person("Dee Ann", "dee_ann@gmail.com", "555-555-555", "")

# print(jordan)

# #Instance methods
sonny.greet(jordan)
jordan.greet(sonny)
sonny.greet(dee_ann)

#printing unique counters
sonny.num_unique_people_greeted()
dee_ann.num_unique_people_greeted()
jordan.num_unique_people_greeted()

# #printing greeting count
sonny.greeting_count()
jordan.greeting_count()
dee_ann.greeting_count()

# #printing sonny's contact info
# sonny.contact_info()
# jordan.contact_info()

# class Vehicle:
    
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print('{} {} {}'.format(self.year, self.make, self.model))

# #Instantiate Vehicle Object
# car = Vehicle('Nissan', 'Leaf', '2015')

# car.print_info()

# jordan.friends.append(sonny)
# sonny.friends.append(jordan)

# print(len(jordan.friends))
# print(len(sonny.friends))

jordan.add_friend(sonny)
sonny.add_friend(jordan)

# print(len(jordan.friends))
# print(len(sonny.friends))

# print(jordan.num_friends())
