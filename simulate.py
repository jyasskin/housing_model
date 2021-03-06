import model


def new_simulation():
    '''
    New version of the simulation with far more people with minimum score
    of 1 to simulate the fact that SF has a lot of renters who are not picky
    on what the accept (lots of single people with low housing needs)
    runs model 2 times with 10,000 renters first with 5k houses then with
    1k (luxury) score 5 houses added for a total of 6k houses
    '''
    renter_min_scores = {1: 4000, 2: 2000, 3: 2000, 4: 1000, 5: 1000}
    house_scores = {1: 1000, 2: 1000, 3: 1000, 4: 1000, 5: 1000}
    mod = model.HousingModel(renter_min_scores, house_scores)
    mod.generate_csv('normal.csv')
    house_scores[5] += 1000  # simulating with more luxury apartments
    lux_mod = model.HousingModel(renter_min_scores, house_scores)
    lux_mod.generate_csv('more_luxury.csv')

def old_simulation():
    '''
    older version of the simulation similar to what we used at hackathon
    runs model 2 times with 15,000 renters first with 9k houses with a
    somewhat normal distribution of the 5 housing scores, then with
    3k (luxury) score 5 houses added for a total of 12k houses
    '''
    renter_min_scores = {1: 3000, 2: 3000, 3: 3000, 4: 3000, 5: 3000}
    house_scores = {1: 1000, 2: 2000, 3: 3000, 4: 2000, 5: 1000}
    mod = model.HousingModel(renter_min_scores, house_scores)
    mod.generate_csv('normal.csv')
    house_scores[5] += 3000  # simulating with more luxury apartments
    lux_mod = model.HousingModel(renter_min_scores, house_scores)
    lux_mod.generate_csv('more_luxury.csv')



def user_input():
    renters = {}
    houses = {}
    for dic, name in [renters, 'renters with minimum housing score'], \
                     [houses, 'housing units with score']:
        for score in [1, 2, 3, 4, 5]:
            dic[score] = input('input number of %s %s: ' % (name, score))
    while True:
        mod = model.HousingModel(renters, houses)
        if input('Type 1 to print renter info, or type 0 to output to CSV '):
            mod.renter_dict()
        else:
            filename = input('enter filename in quotes ')
            mod.generate_csv(filename)
        if not input('Type 1 to simulate building more housing, 0 to exit '):
            break
        for score in [1, 2, 3, 4, 5]:
            houses[score] += input('%s units with score %s. # of units to add:'
                                   % (houses[score], score))


if __name__ == '__main__':
    user_input()
