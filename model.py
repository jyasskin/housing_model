import classes
import random
import math
import numpy as np
import house_match as hm
import csv
import generators as gen


class HousingModel(object):

    def __init__(self, renter_min_scores, house_scores):
        self.houses = gen.generate_houses(house_scores)
        self.renters = gen.generate_renters(renter_min_scores)
        hm.stable_match(self.renters, self.houses)

    def mean_rent(self):
        '''returns the mean rent paid by people with housing'''
        return np.mean([r.paying for r in self.renters if r.matched])

    def median_rent(self):
        '''returns the median rent paid by people with housing'''
        return np.median([r.paying for r in self.renters if r.matched])

    def renter_dict(self, dict_writer=None):
        '''
        creates dictionary of each renter with max rent they can pay,
        the minimum housing score they can accept, the rent they actually pay,
        and the score to the apartment they rent or 'None' if they are unhoused
        '''
        for renter in sorted(self.renters, key=lambda x: x.willingness_to_pay):
            dic = {'max_rent': renter.willingness_to_pay,
                   'min_score': renter.min_score, 'rent': renter.paying,
                   'apt_score': (renter.renting.score if renter.matched
                                 else 'Null')}
            if dict_writer:
                dict_writer.writerow(dic)
            else:
                print dic

    def generate_csv(self, filename):
        f = open(filename, 'w')
        fieldnames = ['min_score', 'max_rent', 'rent', 'apt_score']
        dw = csv.DictWriter(f, fieldnames)
        dw.writeheader()
        self.renter_dict(dict_writer=dw)
        f.close()


def test(renter_min_scores={1: 30, 2: 30, 3: 30, 4: 30, 5: 30},
         house_scores={1: 15, 2: 20, 3: 30, 4: 20, 5: 15},
         filename='output.csv'):

    mod = HousingModel(renter_min_scores, house_scores)
    print mod.mean_rent()
    print mod.mean_rent()
    mod.renter_dict()
    mod.generate_csv(filename)

if __name__ == '__main__':
    test()
