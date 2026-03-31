wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def departments(wards): 
    staff = {} 
    for dept, docs in wards.items(): 
        """ print(dept, docs) """
        jobs = []
        for doc in docs: 
            if dept in staff: 
                jobs.append(dept)
            else: 
                staff[doc] = {
                    "job" == jobs
                }
        print(staff)

departments(wards)