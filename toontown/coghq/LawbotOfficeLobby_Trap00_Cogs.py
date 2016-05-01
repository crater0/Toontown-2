from SpecImports import *
import random
CogParent = 10000
CogParent1 = 100021
BattlePlace1 = 100020
BattlePlace2 = 100022
BattleCellId = 0
BattleCellId1 = 1
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1,
                'pos': Point3(0, 0, 0)},
 BattleCellId1: {'parentEntId': BattlePlace2,
                 'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent1,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId1,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent1,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId1,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent1,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId1,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4, 5])},
 {'parentEntId': CogParent1,
  'boss': 0,
  'level': random.choice([10, 11, 12]),
  'battleCell': BattleCellId1,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': random.choice([1, 2, 3, 4])}]
ReserveCogData = []
