#In this project we build a simple,practical backend-style object that uses ALL important dunder methods

""" 
A PaginatedResult object 
 1. its a list because backend responses often work like sequences
 2. show useful output when prited (__str__)
 3. show debug output(__repr__)
 4. support slicing/indexing (__getitem__)
 5. support len(result)
 6. support for row in result
 7. support id in a result in a custom meaning
 
"""

class PaginatedResult:
    def __init__(self,data,page,page_size,):
        self.data = data   #full data ie users in our case
        self.page = page   # which page number you want its a single page in ours
        self.page_size = page_size # how many items per page 
        
        
    # printable and user friendly
    def __str__(self):
        return f"page {self.page} with {len(self)} items"
    
    # developer friendly debugging 
    def __repr__(self):
        return f"PaginatedResult(page={self.page},page_size={self.page_size},total_items={len(self.data)})"
    
    # number of items in this page
    def __len__(self):
        start = (self.page -1) * self.page_size # { this gives us the formula page 1 --> 0-1 item, page 2 --> 2-3 ..}
        end = start + self.page_size
        return len(self.data[start:end])
    
    #allow indexing and slicing 
    def __getitem__(self,index):
        start = (self.page -1) * self.page_size
        end = start + self.page_size
        page_data = self.data[start:end]
        return page_data[index]
    
    #allow iteration
    def __iter__(self):
        start = (self.page -1) * self.page_size
        end = start + self.page_size
        return iter(self.data[start:end])
    
    #custom membership ("is their anobject with this id?")
    def __contains__(self,user_id):
        return any(item["id"]== user_id for item in self.data)

#data for simulation
users = [
    {"id": 1, "name": "Kaila"},
    {"id": 2, "name": "Mark"},
    {"id": 3, "name": "Stacy"},
    {"id": 4, "name": "Liu"},
    {"id": 5, "name": "Aya"},
]

#make a page with data = users, its a single page 1 and it has 2 items only that is page size
page1 = PaginatedResult(users,page=1,page_size=2)

#tests

print(page1) # outputs a user friendly info ie: page 1 with 2 items
len(page1) # outputs 2 since page size is 2
page1[0] # {"id":1, "name": "kaila"}
for user in page1:
    print(user["name"]) # Kaila , Mark
    
1 in page1 # True since we have a user with id = 1
