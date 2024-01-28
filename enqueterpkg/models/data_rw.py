"""CSV file handling model"""

import collections
import csv
import os
import pathlib

class DataRW(object):
    
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = []
        if not os.path.exists(data_file):
            pathlib.Path(data_file).touch()
        self.read_data()
            
    def read_data(self):
        """Read data file.
        
        Returns:
            Returns users recommend data (dict)
        """
        with open(self.data_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                self.data.append(row)
        #         self.data[row['RECOMMEND']] = int(row['COUNT'])
        #     self.data = sorted(self.data, reverse=True, key=lambda x:int(x[1]))
        return self.data
    
    def stored_data(self):
        return self.data

    def update(self, recommend):
        """Count +1 if user like it"""
        update_data = []
        for data in self.data:
            print(data)
            if recommend == data['RECOMMEND']:
                data['COUNT'] = int(data['COUNT']) + 1
            print(data)
            update_data.append(data)
        
        self.data = update_data
    
    def write_data(self, new_recommend):
        """Wtie new recommend data."""
        not_add = False

        for data in self.data:
            if new_recommend.title() == data['RECOMMEND']:
                not_add = True
        
        if not not_add:
            self.data.append({'RECOMMEND': new_recommend.title(), 'COUNT': 1})

        with open(self.data_file, 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['RECOMMEND', 'COUNT'])
            writer.writeheader()
            writer.writerows(self.data)

            # for data in self.data:
            #     for recommend, count in data.items():
            #         writer.writerow({
            #             'RECOMMEND': recommend,
            #             'COUNT': count
            #         })
