wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def departments(wards): 
    staff = {}
    for dept, docs in wards.items(): #for the items in the wards
        for doc in docs: #in all the doctors
            if doc not in staff: #if the doctors arent in the dictionary, add them
                staff[doc] = [dept] #format of dictionary, the doctor = [list of occupations]
            else: #when it is in the dictionary
                staff[doc].append(dept) #add all their occupations into the list by adding the depts
    print(staff) #print the new dictionary

departments(wards)