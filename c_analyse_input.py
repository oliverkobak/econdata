#!/usr/bin/python
"""
    @author     Oliver Kobak
    @desc       Complete analysis of a given query
"""
import json

class AnalyseInput(object):

    def __init__(self):
        self.analysed_query = []
        self.all_subjects = []
        self.all_variables = []
        self.space_subjects = {}
        self.space_variables = {}
        self.last_variable = ""
        self.backward = False
        self.first_is_variable = False

        # Get all countries from a json file
        with open("countries.json", 'r') as json_file:
            self.subjects = json.load(json_file)

        # Get all variables from a json file
        with open("variables.json", 'r') as json_file:
            self.variables = json.load(json_file)

        # Get all operators from a json file
        with open("operators.json", 'r') as json_file:
            self.operators = json.load(json_file)

        # Find and store countries with spaces in name 
        with open("countries_with_space.json", 'r') as json_file:
            self.subjects_space = json.load(json_file)

        self.compute()

    # List of all possible subjects
    def create_list_of_subjects(self):
        for key, value in self.subjects.items():
            for v in value:
                for word in v.split():
                    self.all_subjects.append(word)

    # List of all possible variales
    def create_list_of_variables(self):
        for key, value in self.variables.items():
            for v in value:
                for word in v.split():
                    self.all_variables.append(word)

    # List of all subjects with space in name
    def create_list_of_subjects_with_space(self):
        for key, value in self.subjects.items():
            for v in value:
                if ' ' in v:
                    self.space_subjects[key] = v.split()

    # List of all variables with space in name
    def create_list_of_variables_with_space(self):
        for key, value in self.variables.items():
            for v in value:
                if ' ' in v:
                    self.space_variables[key] = v.split()

    # Method for finding subjects, variables and operators in a query
    def query_check(self, query):
        for i in range(0, len(query)):
            if query[i] in self.all_subjects:
                self.find_subject(query, i, 'country')
            elif query[i] in self.all_variables:
                self.find_variables(query, i, 'variable')
            elif query[i] in self.operators:
                self.find_operator(query, i, 'operator')

    # Method for finding a subject in a query
    def find_subject(self, query, i, keyword):
        for subject in self.space_subjects:
            if query[i] == self.space_subjects[subject][0]:
                if query[i+1] == self.space_subjects[subject][1]:
                    self.analysed_query.append({'type':keyword, 'key': subject})
            else:
                for key, value in self.subjects.items():
                    if query[i] in value:
                        self.analysed_query.append({'type':keyword, 'key': key})
                        return

    # Method for finding a variable in a query
    def find_variables(self, query, i, keyword):
        for variable in self.space_variables:
            if query[i] == self.space_variables[variable][0]:
                if query[i+1] == self.space_variables[variable][1]:
                    self.analysed_query.append({'type':keyword, 'key': variable})
            else:
                for key, value in self.variables.items():
                    if query[i] in value:
                        self.analysed_query.append({'type':keyword, 'key': key})
                        return

    # Method for finding an operator in a query
    def find_operator(self, query, i, keyword):
        for operator in self.operators:
            if query[i] == operator:
                    self.analysed_query.append({'type':keyword, 'key': operator})

    # Method for finding a variable forward
    # This method is called when the first element in a query is a country
    def search_variable_forward(self, analysed_query, position):
        for i in range(position, len(analysed_query), 1):
            if analysed_query[i]['type'] == 'variable':
                return analysed_query[i]['key']

    # Method for finding a variable backward
    # This method is called when the first element in a query is a variable 
    def search_variable_backward(self, analysed_query, position):
        for i in range(position, -1, -1):
            if analysed_query[i]['type'] == 'variable':
                return analysed_query[i]['key']

    # Determins the directon of the variable searching
    def search_backward(self, analysed_query):
        # Query starts with an operator e.g. '(' and the next element is a variable or starst with a variable
        if (analysed_query[0]['type'] == 'operator' and analysed_query[1]['type'] == 'variable') or analysed_query[0]['type'] == 'variable':
           self.backward = True
           self.first_is_variable = True

    def check_variable_after_variable(self, analysed_query, i):
        try:
            # The next element is a variable so there are two variables after each other
            if analysed_query[i+1]['type'] == 'variable':
                self.backward = True
        except IndexError:
            self.last_variable = analysed_query[i]['key']

    # Finding variables for each subject
    def organize_query(self, analysed_query):
        self.search_backward(analysed_query)

        for i in range(0, len(analysed_query)):
            if self.backward == False:
                if analysed_query[i]['type'] == 'country':
                    analysed_query[i]['variable'] = self.search_variable_forward(analysed_query, i)
                elif analysed_query[i]['type'] == 'variable':
                    self.check_variable_after_variable(analysed_query, i)
            else:
                if analysed_query[i]['type'] == 'country':
                    analysed_query[i]['variable'] = self.search_variable_backward(analysed_query, i)
                elif analysed_query[i]['type'] == 'variable':
                    analysed_query[i-1]['variable'] = analysed_query[i]['key']
        if self.last_variable != "":
            analysed_query[-2]['variable'] = self.last_variable

    # Main method for complete analysis of a query
    def analyse_query(self, query):
        self.query_check(query)
        self.organize_query(self.analysed_query)

    # Preparation for a query analysis
    def compute(self):
        self.create_list_of_subjects()
        self.create_list_of_variables()
        self.create_list_of_subjects_with_space()
        self.create_list_of_variables_with_space()
