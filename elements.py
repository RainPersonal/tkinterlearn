# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import tkinter.font as tf
def get_class_by_index(index):
	class_dic = {
    1:'碱金属',
	2:'碱土金属',
	3:'过渡金属',
	4:'弱金属',
	5:'非金属',
	6:'准金属',
	7:'卤素',
	8:'稀有气体',
	9:'镧系元素',
	10:'锕系元素'
	}
	return class_dic[index]

def get_screen_size(window):
    return window.winfo_screenwidth(),window.winfo_screenheight()
 
def get_window_size(window):
    return window.winfo_reqwidth(),window.winfo_reqheight()
 
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    # print(size)
    root.geometry(size)

color = ["#0078d7","#ee6fb9","#47a8e8","#f27575","#9b85dd","#4fb180","#ff7f46","#67c3ef","#74ce18","#eba95d","#a59b78"]
class ele_button():
	"""docstring for ele_button"""
	def __init__(self, root, dic, btnfont, func):
		super(ele_button, self).__init__()
		self.dic = dic
		self.btn = tk.Button(root, relief = 'groove', text = dic['index']+'\n'+dic['symbol'], padx=0,pady=0,width=4,height=2,bg=color[int(dic['class'])],font = btnfont, command=lambda:func(self.dic))
	

elements=[{'index': '1', 'symbol': 'H', 'zhName': '氢', 'enName': 'hydrogen', 'commonWeight': '1.008', 'standardWeight': '[1.0078, 1.0082]', 'row': '1', 'col': '1', 'class': 5},
 {'index': '2', 'symbol': 'He', 'zhName': '氦', 'enName': 'helium', 'commonWeight': '', 'standardWeight': '4.0026', 'row': '1', 'col': '18', 'class': 8},
 {'index': '3', 'symbol': 'Li', 'zhName': '锂', 'enName': 'lithium', 'commonWeight': '6.94', 'standardWeight': '[6.938, 6.997]', 'row': '2', 'col': '1', 'class': 1},
 {'index': '4', 'symbol': 'Be', 'zhName': '铍', 'enName': 'beryllium', 'commonWeight': '', 'standardWeight': '9.0122', 'row': '2', 'col': '2', 'class': 2},
 {'index': '5', 'symbol': 'B', 'zhName': '硼', 'enName': 'boron', 'commonWeight': '10.81', 'standardWeight': '[10.806, 10.821]', 'row': '2', 'col': '13', 'class': 6},
 {'index': '6', 'symbol': 'C', 'zhName': '碳', 'enName': 'carbon', 'commonWeight': '12.011', 'standardWeight': '[12.009, 12.012]', 'row': '2', 'col': '14', 'class': 5},
 {'index': '7', 'symbol': 'N', 'zhName': '氮', 'enName': 'nitrogen', 'commonWeight': '14.007', 'standardWeight': '[14.006, 04.008]', 'row': '2', 'col': '15', 'class': 5},
 {'index': '8', 'symbol': 'O', 'zhName': '氧', 'enName': 'oxygen', 'commonWeight': '15.999', 'standardWeight': '[15.999, 16.000]', 'row': '2', 'col': '16', 'class': 5},
 {'index': '9', 'symbol': 'F', 'zhName': '氟', 'enName': 'fluorine', 'commonWeight': '', 'standardWeight': '18.998', 'row': '2', 'col': '17', 'class': 7},
 {'index': '10', 'symbol': 'Ne', 'zhName': '氖', 'enName': 'neon', 'commonWeight': '', 'standardWeight': '20.180', 'row': '2', 'col': '18', 'class': 8},
 {'index': '11', 'symbol': 'Na', 'zhName': '钠', 'enName': 'sodium', 'commonWeight': '', 'standardWeight': '22.990', 'row': '3', 'col': '1', 'class': 1},
 {'index': '12', 'symbol': 'Mg', 'zhName': '镁', 'enName': 'magnesium', 'commonWeight': '24.305', 'standardWeight': '[24.304, 24.307]', 'row': '3', 'col': '2', 'class': 2},
 {'index': '13', 'symbol': 'Al', 'zhName': '铝', 'enName': 'aluminium', 'commonWeight': '', 'standardWeight': '26.982', 'row': '3', 'col': '13', 'class': 4},
 {'index': '14', 'symbol': 'Si', 'zhName': '硅', 'enName': 'silicon', 'commonWeight': '28.085', 'standardWeight': '[28.084, 28.086]', 'row': '3', 'col': '14', 'class': 6},
 {'index': '15', 'symbol': 'P', 'zhName': '磷', 'enName': 'phosphorus', 'commonWeight': '', 'standardWeight': '30.974', 'row': '3', 'col': '15', 'class': 5},
 {'index': '16', 'symbol': 'S', 'zhName': '硫', 'enName': 'sulfur', 'commonWeight': '32.06', 'standardWeight': '[32.059, 32.076]', 'row': '3', 'col': '16', 'class': 5},
 {'index': '17', 'symbol': 'Cl', 'zhName': '氯', 'enName': 'chlorine', 'commonWeight': '35.45', 'standardWeight': '[35.446, 35.457]', 'row': '3', 'col': '17', 'class': 7},
 {'index': '18', 'symbol': 'Ar', 'zhName': '氩', 'enName': 'argon', 'commonWeight': '', 'standardWeight': '39.948', 'row': '3', 'col': '18', 'class': 8},
 {'index': '19', 'symbol': 'K', 'zhName': '钾', 'enName': 'potassium', 'commonWeight': '', 'standardWeight': '39.098', 'row': '4', 'col': '1', 'class': 1},
 {'index': '20', 'symbol': 'Ca', 'zhName': '钙', 'enName': 'calcium', 'commonWeight': '', 'standardWeight': '40.078(4)', 'row': '4', 'col': '2', 'class': 2},
 {'index': '21', 'symbol': 'Sc', 'zhName': '钪', 'enName': 'scandium', 'commonWeight': '', 'standardWeight': '44.956', 'row': '4', 'col': '3', 'class': 3},
 {'index': '22', 'symbol': 'Ti', 'zhName': '钛', 'enName': 'titanium', 'commonWeight': '', 'standardWeight': '47.867', 'row': '4', 'col': '4', 'class': 3},
 {'index': '23', 'symbol': 'V', 'zhName': '钒', 'enName': 'vanadium', 'commonWeight': '', 'standardWeight': '50.942', 'row': '4', 'col': '5', 'class': 3},
 {'index': '24', 'symbol': 'Cr', 'zhName': '铬', 'enName': 'chromium', 'commonWeight': '', 'standardWeight': '51.996', 'row': '4', 'col': '6', 'class': 3},
 {'index': '25', 'symbol': 'Mn', 'zhName': '锰', 'enName': 'manganese', 'commonWeight': '', 'standardWeight': '54.938', 'row': '4', 'col': '7', 'class': 3},
 {'index': '26', 'symbol': 'Fe', 'zhName': '铁', 'enName': 'iron', 'commonWeight': '', 'standardWeight': '55.845(2)', 'row': '4', 'col': '8', 'class': 3},
 {'index': '27', 'symbol': 'Co', 'zhName': '钴', 'enName': 'cobalt', 'commonWeight': '', 'standardWeight': '58.933', 'row': '4', 'col': '9', 'class': 3},
 {'index': '28', 'symbol': 'Ni', 'zhName': '镍', 'enName': 'nickel', 'commonWeight': '', 'standardWeight': '58.693', 'row': '4', 'col': '10', 'class': 3},
 {'index': '29', 'symbol': 'Cu', 'zhName': '铜', 'enName': 'copper', 'commonWeight': '', 'standardWeight': '63.546(3)', 'row': '4', 'col': '11', 'class': 3},
 {'index': '30', 'symbol': 'Zn', 'zhName': '锌', 'enName': 'zinc', 'commonWeight': '', 'standardWeight': '65.38(2)', 'row': '4', 'col': '12', 'class': 3},
 {'index': '31', 'symbol': 'Ga', 'zhName': '镓', 'enName': 'gallium', 'commonWeight': '', 'standardWeight': '69.723', 'row': '4', 'col': '13', 'class': 4},
 {'index': '32', 'symbol': 'Ge', 'zhName': '锗', 'enName': 'germanium', 'commonWeight': '', 'standardWeight': '72.630(8)', 'row': '4', 'col': '14', 'class': 6},
 {'index': '33', 'symbol': 'As', 'zhName': '砷', 'enName': 'arsenic', 'commonWeight': '', 'standardWeight': '74.922', 'row': '4', 'col': '15', 'class': 6},
 {'index': '34', 'symbol': 'Se', 'zhName': '硒', 'enName': 'selenium', 'commonWeight': '', 'standardWeight': '78.971(8)', 'row': '4', 'col': '16', 'class': 5},
 {'index': '35', 'symbol': 'Br', 'zhName': '溴', 'enName': 'bromine', 'commonWeight': '79.904', 'standardWeight': '[79.901, 79.907]', 'row': '4', 'col': '17', 'class': 7},
 {'index': '36', 'symbol': 'Kr', 'zhName': '氪', 'enName': 'krypton', 'commonWeight': '', 'standardWeight': '83.798(2)', 'row': '4', 'col': '18', 'class': 8},
 {'index': '37', 'symbol': 'Rb', 'zhName': '铷', 'enName': 'rubidium', 'commonWeight': '', 'standardWeight': '85.468', 'row': '5', 'col': '1', 'class': 1},
 {'index': '38', 'symbol': 'Sr', 'zhName': '锶', 'enName': 'strontium', 'commonWeight': '', 'standardWeight': '87.62', 'row': '5', 'col': '2', 'class': 2},
 {'index': '39', 'symbol': 'Y', 'zhName': '钇', 'enName': 'yttrium', 'commonWeight': '', 'standardWeight': '88.906', 'row': '5', 'col': '3', 'class': 3},
 {'index': '40', 'symbol': 'Zr', 'zhName': '锆', 'enName': 'zirconium', 'commonWeight': '', 'standardWeight': '91.224(2)', 'row': '5', 'col': '4', 'class': 3},
 {'index': '41', 'symbol': 'Nb', 'zhName': '铌', 'enName': 'niobium', 'commonWeight': '', 'standardWeight': '92.906', 'row': '5', 'col': '5', 'class': 3},
 {'index': '42', 'symbol': 'Mo', 'zhName': '钼', 'enName': 'molybdenum', 'commonWeight': '', 'standardWeight': '95.95', 'row': '5', 'col': '6', 'class': 3},
 {'index': '43', 'symbol': 'Tc', 'zhName': '锝', 'enName': 'technetium', 'commonWeight': '', 'standardWeight': '', 'row': '5', 'col': '7', 'class': 3},
 {'index': '44', 'symbol': 'Ru', 'zhName': '钌', 'enName': 'ruthenium', 'commonWeight': '', 'standardWeight': '101.07(2)', 'row': '5', 'col': '8', 'class': 3},
 {'index': '45', 'symbol': 'Rh', 'zhName': '铑', 'enName': 'rhodium', 'commonWeight': '', 'standardWeight': '102.91', 'row': '5', 'col': '9', 'class': 3},
 {'index': '46', 'symbol': 'Pd', 'zhName': '钯', 'enName': 'palladium', 'commonWeight': '', 'standardWeight': '106.42', 'row': '5', 'col': '10', 'class': 3},
 {'index': '47', 'symbol': 'Ag', 'zhName': '银', 'enName': 'silver', 'commonWeight': '', 'standardWeight': '107.87', 'row': '5', 'col': '11', 'class': 3},
 {'index': '48', 'symbol': 'Cd', 'zhName': '镉', 'enName': 'cadmium', 'commonWeight': '', 'standardWeight': '112.41', 'row': '5', 'col': '12', 'class': 3},
 {'index': '49', 'symbol': 'In', 'zhName': '铟', 'enName': 'indium', 'commonWeight': '', 'standardWeight': '114.82', 'row': '5', 'col': '13', 'class': 4},
 {'index': '50', 'symbol': 'Sn', 'zhName': '锡', 'enName': 'tin', 'commonWeight': '', 'standardWeight': '118.71', 'row': '5', 'col': '14', 'class': 4},
 {'index': '51', 'symbol': 'Sb', 'zhName': '锑', 'enName': 'antimony', 'commonWeight': '', 'standardWeight': '121.76', 'row': '5', 'col': '15', 'class': 6},
 {'index': '52', 'symbol': 'Te', 'zhName': '碲', 'enName': 'tellurium', 'commonWeight': '', 'standardWeight': '127.60(3)', 'row': '5', 'col': '16', 'class': 6},
 {'index': '53', 'symbol': 'I', 'zhName': '碘', 'enName': 'iodine', 'commonWeight': '', 'standardWeight': '126.90', 'row': '5', 'col': '17', 'class': 7},
 {'index': '54', 'symbol': 'Xe', 'zhName': '氙', 'enName': 'xenon', 'commonWeight': '', 'standardWeight': '131.29', 'row': '5', 'col': '18', 'class': 8},
 {'index': '55', 'symbol': 'Cs', 'zhName': '铯', 'enName': 'caesium', 'commonWeight': '', 'standardWeight': '132.91', 'row': '6', 'col': '1', 'class': 1},
 {'index': '56', 'symbol': 'Ba', 'zhName': '钡', 'enName': 'barium', 'commonWeight': '', 'standardWeight': '137.33', 'row': '6', 'col': '2', 'class': 2},
 {'index': '57', 'symbol': 'La', 'zhName': '镧', 'enName': 'lanthanoids', 'commonWeight': '', 'standardWeight': '138.91', 'row': '8', 'col': '3', 'class': 9},
 {'index': '58', 'symbol': 'Ce', 'zhName': '铈', 'enName': 'cerium', 'commonWeight': '', 'standardWeight': '140.12', 'row': '8', 'col': '4', 'class': 9},
 {'index': '59', 'symbol': 'Pr', 'zhName': '镨', 'enName': 'praseodymium', 'commonWeight': '', 'standardWeight': '140.91', 'row': '8', 'col': '5', 'class': 9},
 {'index': '60', 'symbol': 'Nd', 'zhName': '钕', 'enName': 'neodymium', 'commonWeight': '', 'standardWeight': '144.24', 'row': '8', 'col': '6', 'class': 9},
 {'index': '61', 'symbol': 'Pm', 'zhName': '钷', 'enName': 'promethium', 'commonWeight': '', 'standardWeight': '', 'row': '8', 'col': '7', 'class': 9},
 {'index': '62', 'symbol': 'Sm', 'zhName': '钐', 'enName': 'samarium', 'commonWeight': '', 'standardWeight': '150.36(2)', 'row': '8', 'col': '8', 'class': 9},
 {'index': '63', 'symbol': 'Eu', 'zhName': '铕', 'enName': 'europium', 'commonWeight': '', 'standardWeight': '151.96', 'row': '8', 'col': '9', 'class': 9},
 {'index': '64', 'symbol': 'Gd', 'zhName': '钆', 'enName': 'gadolinium', 'commonWeight': '', 'standardWeight': '157.25(3)', 'row': '8', 'col': '10', 'class': 9},
 {'index': '65', 'symbol': 'Tb', 'zhName': '铽', 'enName': 'terbium', 'commonWeight': '', 'standardWeight': '158.93', 'row': '8', 'col': '11', 'class': 9},
 {'index': '66', 'symbol': 'Dy', 'zhName': '镝', 'enName': 'dysprosium', 'commonWeight': '', 'standardWeight': '162.50', 'row': '8', 'col': '12', 'class': 9},
 {'index': '67', 'symbol': 'Ho', 'zhName': '钬', 'enName': 'holmium', 'commonWeight': '', 'standardWeight': '164.93', 'row': '8', 'col': '13', 'class': 9},
 {'index': '68', 'symbol': 'Er', 'zhName': '铒', 'enName': 'erbium', 'commonWeight': '', 'standardWeight': '167.26', 'row': '8', 'col': '14', 'class': 9},
 {'index': '69', 'symbol': 'Tm', 'zhName': '铥', 'enName': 'thulium', 'commonWeight': '', 'standardWeight': '168.93', 'row': '8', 'col': '15', 'class': 9},
 {'index': '70', 'symbol': 'Yb', 'zhName': '镱', 'enName': 'ytterbium', 'commonWeight': '', 'standardWeight': '173.05', 'row': '8', 'col': '16', 'class': 9},
 {'index': '71', 'symbol': 'Lu', 'zhName': '镥', 'enName': 'lutetium', 'commonWeight': '', 'standardWeight': '174.97', 'row': '8', 'col': '17', 'class': 9},
 {'index': '72', 'symbol': 'Hf', 'zhName': '铪', 'enName': 'hafnium', 'commonWeight': '', 'standardWeight': '178.49(2)', 'row': '6', 'col': '4', 'class': 3},
 {'index': '73', 'symbol': 'Ta', 'zhName': '钽', 'enName': 'tantalum', 'commonWeight': '', 'standardWeight': '180.95', 'row': '6', 'col': '5', 'class': 3},
 {'index': '74', 'symbol': 'W', 'zhName': '钨', 'enName': 'tungsten', 'commonWeight': '', 'standardWeight': '183.84', 'row': '6', 'col': '6', 'class': 3},
 {'index': '75', 'symbol': 'Re', 'zhName': '铼', 'enName': 'rhenium', 'commonWeight': '', 'standardWeight': '186.21', 'row': '6', 'col': '7', 'class': 3},
 {'index': '76', 'symbol': 'Os', 'zhName': '锇', 'enName': 'osmium', 'commonWeight': '', 'standardWeight': '190.23(3)', 'row': '6', 'col': '8', 'class': 3},
 {'index': '77', 'symbol': 'Ir', 'zhName': '铱', 'enName': 'iridium', 'commonWeight': '', 'standardWeight': '192.22', 'row': '6', 'col': '9', 'class': 3},
 {'index': '78', 'symbol': 'Pt', 'zhName': '铂', 'enName': 'platinum', 'commonWeight': '', 'standardWeight': '195.08', 'row': '6', 'col': '10', 'class': 3},
 {'index': '79', 'symbol': 'Au', 'zhName': '金', 'enName': 'gold', 'commonWeight': '', 'standardWeight': '196.97', 'row': '6', 'col': '11', 'class': 3},
 {'index': '80', 'symbol': 'Hg', 'zhName': '汞', 'enName': 'merury', 'commonWeight': '', 'standardWeight': '200.59', 'row': '6', 'col': '12', 'class': 3},
 {'index': '81', 'symbol': 'Tl', 'zhName': '铊', 'enName': 'thallium', 'commonWeight': '204.38', 'standardWeight': '[204.38, 204.39]', 'row': '6', 'col': '13', 'class': 4},
 {'index': '82', 'symbol': 'Pb', 'zhName': '铅', 'enName': 'lead', 'commonWeight': '', 'standardWeight': '207.2', 'row': '6', 'col': '14', 'class': 4},
 {'index': '83', 'symbol': 'Bi', 'zhName': '铋', 'enName': 'bismuth', 'commonWeight': '', 'standardWeight': '208.98', 'row': '6', 'col': '15', 'class': 4},
 {'index': '84', 'symbol': 'Po', 'zhName': '钋', 'enName': 'polonium', 'commonWeight': '', 'standardWeight': '', 'row': '6', 'col': '16', 'class': 6},
 {'index': '85', 'symbol': 'At', 'zhName': '砹', 'enName': 'astatine', 'commonWeight': '', 'standardWeight': '', 'row': '6', 'col': '17', 'class': 7},
 {'index': '86', 'symbol': 'Rn', 'zhName': '氡', 'enName': 'radon', 'commonWeight': '', 'standardWeight': '', 'row': '6', 'col': '18', 'class': 8},
 {'index': '87', 'symbol': 'Fr', 'zhName': '钫', 'enName': 'francium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '1', 'class': 1},
 {'index': '88', 'symbol': 'Ra', 'zhName': '镭', 'enName': 'radium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '2', 'class': 2},
 {'index': '89', 'symbol': 'Ac', 'zhName': '锕', 'enName': 'actinoids', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '3', 'class': 10},
 {'index': '90', 'symbol': 'Th', 'zhName': '钍', 'enName': 'thorium', 'commonWeight': '', 'standardWeight': '232.04', 'row': '9', 'col': '4', 'class': 10},
 {'index': '91', 'symbol': 'Pa', 'zhName': '镤', 'enName': 'protactinium', 'commonWeight': '', 'standardWeight': '231.04', 'row': '9', 'col': '5', 'class': 10},
 {'index': '92', 'symbol': 'U', 'zhName': '铀', 'enName': 'uranium', 'commonWeight': '', 'standardWeight': '238.03', 'row': '9', 'col': '6', 'class': 10},
 {'index': '93', 'symbol': 'Np', 'zhName': '镎', 'enName': 'neptunium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '7', 'class': 10},
 {'index': '94', 'symbol': 'Pu', 'zhName': '钚', 'enName': 'plutonium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '8', 'class': 10},
 {'index': '95', 'symbol': 'Am', 'zhName': '镅', 'enName': 'americium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '9', 'class': 10},
 {'index': '96', 'symbol': 'Cm', 'zhName': '锔', 'enName': 'curium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '10', 'class': 10},
 {'index': '97', 'symbol': 'Bk', 'zhName': '锫', 'enName': 'berkelium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '11', 'class': 10},
 {'index': '98', 'symbol': 'Cf', 'zhName': '锎', 'enName': 'californium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '12', 'class': 10},
 {'index': '99', 'symbol': 'Es', 'zhName': '锿', 'enName': 'einsteinium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '13', 'class': 10},
 {'index': '100', 'symbol': 'Fm', 'zhName': '镄', 'enName': 'fermium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '14', 'class': 10},
 {'index': '101', 'symbol': 'Md', 'zhName': '钔', 'enName': 'mendelevium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '15', 'class': 10},
 {'index': '102', 'symbol': 'No', 'zhName': '锘', 'enName': 'nobelium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '16', 'class': 10},
 {'index': '103', 'symbol': 'Lr', 'zhName': '铹', 'enName': 'lawrencium', 'commonWeight': '', 'standardWeight': '', 'row': '9', 'col': '17', 'class': 10},
 {'index': '104', 'symbol': 'Rf', 'zhName': '𬬻', 'enName': 'rutherfordium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '4', 'class': 3},
 {'index': '105', 'symbol': 'Db', 'zhName': '𬭊', 'enName': 'dubnium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '5', 'class': 3},
 {'index': '106', 'symbol': 'Sg', 'zhName': '𬭳', 'enName': 'seaborgium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '6', 'class': 3},
 {'index': '107', 'symbol': 'Bh', 'zhName': '𬭛', 'enName': 'bohrium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '7', 'class': 3},
 {'index': '108', 'symbol': 'Hs', 'zhName': '𬭶', 'enName': 'hassium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '8', 'class': 3},
 {'index': '109', 'symbol': 'Mt', 'zhName': '鿏', 'enName': 'meitnerium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '9', 'class': 3},
 {'index': '110', 'symbol': 'Ds', 'zhName': '𫟼', 'enName': 'darmstadtium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '10', 'class': 3},
 {'index': '111', 'symbol': 'Rg', 'zhName': '𬬭', 'enName': 'roentgenium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '11', 'class': 3},
 {'index': '112', 'symbol': 'Cn', 'zhName': '鿔', 'enName': 'copernicium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '12', 'class': 3},
 {'index': '113', 'symbol': 'Nh', 'zhName': '鉨', 'enName': 'nihonium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '13', 'class': 4},
 {'index': '114', 'symbol': 'Fl', 'zhName': '𫓧', 'enName': 'flerovium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '14', 'class': 4},
 {'index': '115', 'symbol': 'Mc', 'zhName': '镆', 'enName': 'moscovium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '15', 'class': 4},
 {'index': '116', 'symbol': 'Lv', 'zhName': '𫟷', 'enName': 'livermorium', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '16', 'class': 4},
 {'index': '117', 'symbol': 'Ts', 'zhName': '石田', 'enName': 'tennessine', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '17', 'class': 7},
 {'index': '118', 'symbol': 'Og', 'zhName': '气奥', 'enName': 'oganesson', 'commonWeight': '', 'standardWeight': '', 'row': '7', 'col': '18', 'class': 8}]

if __name__ == '__main__':
	# for i in range(1,11):
	# 	print(get_class_by_index(i))
	# print(s2n('Na'))
	# print(n2s('皮'))
	def change_symbol(buttons):
		if buttons[-1]['text'] == '符号':
			buttons[-1]['text'] = '名称'
			mark = True
		else:
			buttons[-1]['text'] = '符号'
			mark = False
		for i in range(len(buttons)-1):
			if mark:
				buttons[i].btn['text'] = buttons[i].dic['index']+'\n'+buttons[i].dic['zhName']
			else:
				buttons[i].btn['text'] = buttons[i].dic['index']+'\n'+buttons[i].dic['symbol']
	window = tk.Tk()
	window.title('数据')
	max_width, max_height = get_screen_size(window)
	center_window(window, max_width*0.7, max_height*0.7)
	window.resizable(0,0)
	ftwindow = tf.Font(family='等线', size=15,weight=tf.BOLD,underline=0,overstrike=0)
	windowframe = ttk.Frame(window, relief='groove', borderwidth=5, width=50, height=50)
	buttons = []
	for i in elements:
		buttons.append(ele_button(windowframe, i, ftwindow, print))
		buttons[-1].btn.grid(row=int(i['row']),column=int(i['col']))
	buttons.append(tk.Button(windowframe, relief = 'groove',text = '符号', padx=0,pady=0,width=4,height=1,bg=color[0],font = ftwindow,command=lambda:change_symbol(buttons)))
	buttons[-1].grid(row=1,column=16,columnspan=2)
	tk.Label(windowframe, relief = 'flat', text = '*', padx=0,pady=0,width=4,height=2,font = ftwindow).grid(row=6,column=3)
	tk.Label(windowframe, relief = 'flat', text = '**', padx=0,pady=0,width=4,height=2,font = ftwindow).grid(row=7,column=3)
	tk.Label(windowframe, relief = 'flat', text = '*镧系', padx=0,pady=0,width=6,height=2,font = ftwindow).grid(row=8,column=1,columnspan=2)
	tk.Label(windowframe, relief = 'flat', text = '**锕系', padx=0,pady=0,width=6,height=2,font = ftwindow).grid(row=9,column=1,columnspan=2)
	windowframe.pack()
	classframe = ttk.Frame(window,relief='groove', borderwidth=5, width=50, height=50)
	for i in range(10):
		tk.Label(classframe, relief = 'flat', text = get_class_by_index(i+1), padx=0,pady=0,width=8,height=1,bg = color[i+1], font = ftwindow).grid(row=0,column=i)
	classframe.pack()
	window.mainloop()