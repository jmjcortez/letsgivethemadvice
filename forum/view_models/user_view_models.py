class VoterViewModel(object):

    def __init__(self, voter):
        self.email = voter.user.email
        self.username = voter.user.username
        self.times_voted = voter.user.times_voted


class VoterListViewModel(object):

    def __init__(self, voters_list):

        voters = []

        for voter in voters_list:
            voters.append({
                'email': voter.user.email,
                'username': voter.user.username,
                'times_voted': voter.times_voted
            })

        self.voters = voters
    
