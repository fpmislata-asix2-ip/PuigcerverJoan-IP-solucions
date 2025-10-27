people = int(input())
cookies = int(input())

def would_people_fight_for_cookies(people, cookies):
    return cookies % people != 0
        
is_there_fight = would_people_fight_for_cookies(people, cookies) 
if is_there_fight:
    print("Let's fight!")
else:
    print("Let's eat!")