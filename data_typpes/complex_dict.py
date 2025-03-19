data = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "address": {"city": "New York", "zip": "10001"},
        "skills": ["Python", "AWS", "Terraform"]
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "address": {"city": "San Francisco", "zip": "94105"},
        "skills": ["Java", "Docker"]
    }
}



for key, val in data.items():
    print(f'\n{key} : {val}')
    for k, v in val.items():
        print(f'{k} : {v}')
        if k == "address":
            for k1, v1 in v.items():
                print(f'{k1} : {v1}')
        if k == "skills":
            for skill in v:
                print(skill)
