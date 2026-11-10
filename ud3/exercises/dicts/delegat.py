def read_votes():
    votes = []

    vot = input()
    while vot.strip() != "":
        votes.append(vot)
        vot = input()

    return votes

def count_votes(vote_list):
    vote_count = {}
    for vot in vote_list:
        # vote_count[vot] = vote_count.get(vot, 0) + 1
        
        if vot in vote_count:
            vote_count[vot] += 1
        else:
            vote_count[vot] = 1
    return vote_count


def max_vote(vote_dict):
    return max(vote_dict.values())


def elected_students(vote_count_dict, max_vote_value):
    elected = []
    for name, votes in vote_count_dict.items():
        if votes == max_vote_value:
            elected.append(name)
    return elected
            

if __name__ == "__main__":
    votes = read_votes()
    #print(votes) # ["vot1", "vot2", ...]
    vote_count = count_votes(votes)
    print(vote_count) # {"vot1": 5, "vot2": 1, ...}
    max_vote_count = max_vote(vote_count)
    print(max_vote_count) # 5
    students = elected_students(vote_count, max_vote_count)
    print(students) # ["vot1"]