#!/usr/bin/python
#Filename : contacts.py

import os
import cPickle as p

#build a contacts class ,which can add person and check person
class contacts:
	def __init__(self, name, number, contacts, exist):
		self.name = name
		self.number = number
		self.contacts = contacts
		self.exist = exist
	def tell(self):
		print 'name is :{0} , number is :{1} \n'.format(self.name, self.number)
	def add(self):
		self.name = raw_input('please enter the add name:')
		
		self.number = raw_input('please enter the add number:')
		self.contacts[self.name] = self.number  # () is not a dict ,using [] to assign a dict
	def research(self):
		self.check()
		self.name = raw_input('please enter the name you want to research:')
		for name, number in self.contacts.items():
			if self.name == name:
				#print 'person is already exist'
				self.number = self.contacts.get(self.name)
				self.tell()
				self.exist = True
		if self.exist == False:
			print 'the person isn\'t exist\n'

	def change(self):
		self.check()
		print 'please enter a new name:'
		self.name = raw_input()
		self.contacts.pop(self.name)
		print 'please enter a new number:'
		self.number = raw_input()
		#self.add()
		self.contacts[self.name] = self.number
	def remove(self):
		self.check()
		print 'please enter the name be delete:'
		self.name = raw_input()
		for name, number in self.contacts.items():
			if name == self.name:
				self.contacts.pop(self.name)
				print 'remove success'
			else:
				print '%s don\'t exist, can\'t be remove'
	def check(self):
		if self.contacts == {}:
			print 'no contacts exist\n'
			os._exit(1)
'''
		else:
			for name, number in self.contacts:
				if name == self.name:
					exist = True
#			self.again = 'yes'
'''
#1 enter a number or name
#name_in = raw_input('please enter a name:')
#number_in = raw_input('please enter a number:')

#2 create a contacts list
#contacts_list = []#list
contacts_list = {} #dict
filename = 'contacts.txt'

#check this file ####f = file(filename, 'w+') will error
if os.path.exists(filename):
	f = open(filename, 'r+')
	contacts_list = p.load(f)
	print contacts_list
#	person = contacts(name_in, number_in, contacts_list, exist)
else:
	f = open(filename, 'w+')

#person = contacts(name_in, number_in, contacts_list, exist)
person = contacts('', '', contacts_list, False)

command = raw_input('Do you want to add/change/remove/research the contacts ?\n')

#while person.again == 'yes'
if command == 'add':
	person.add()
elif command == 'change':
	person.change()
elif command == 'remove':
	person.remove()
elif command == 'research':
	person.research()
else:
	print 'command is error'
	os._exit(0)
	print 'conmand'
#		break


#check the contact is exist or not
#person.research()
'''
for name, number in person.contacts.items():
	if name == name_in:
#		print '%s is exist', name_in
		print 'person is already exist'
		person.tell()
		exist = True
#	else:
'''
'''
if person.flag == False:
	print '%s isn\'t exist' % name_in
#	contacts.append(name)
#	contacts_list.append(name)
#	contacts_list[person.name] = person.number# this is a method of dict add
	if raw_input('Do you want to add a person, yes or no:') == 'yes':
		person.add()
else:
	print '%s is already exist' % name_in
	if raw_input('Do you want to change a person, yes or no:') == 'yes':
		person.change()
'''
print person.contacts
f.close()

f = open(filename, 'w+')
p.dump(person.contacts, f)
f.close()

f = open(filename, 'r+')
print 'now the contacts :', p.load(f)
f.close




