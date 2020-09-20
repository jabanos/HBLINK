#           Configuracion by EA7JCL & BLASMAKERS &  EA5GVK.ES)
BRIDGES = {
 'LORO': [
     {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 9990,    'ACTIVE': True, 'TIMEOUT': 1, 'TO_TYPE': 'NONE',  'ON': [9990], 'OFF': [], 'RESET': [9990]},
     {'SYSTEM': 'LORO',    'TS': 2, 'TGID': 9990, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE',  'ON': [], 'OFF': [], 'RESET': []},
 ]
}

'''
list the names of each system that should bridge unit to unit (individual) calls.
'''
UNIT = ['MASTER-1']

'''
This is for testing the syntax of the file. It won't eliminate all errors, but running this file
like it were a Python program itself will tell you if the syntax is correct!
'''

if __name__ == '__main__':
    from pprint import pprint
    pprint(BRIDGES)
