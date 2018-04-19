import xml.etree.ElementTree as et
import threading
def getdata(f):
	xmltree = et.parse(f)
	root = xmltree.getroot()
	print root.tag
	a = []
	for child in root:
		a.append(int(child.text))
		print child.tag,child.text
	print a
	return a
def partition(l,r):
	pivot = a[l]
	i=l+1
	j=r
	while i<=j:
		while i<len(a) and pivot >= a[i]:
			i+=1
		while pivot < a[j]:
			j-=1
		if i<j:
			a[i],a[j] = a[j],a[i]
	a[j],a[l] = pivot,a[j]
	return j
def quicksort(l,r):
	if l<=r:
		mid = partition(l,r)
		print threading.current_thread().getName(),"this thread found mid = ",mid
		quicksort(l,mid-1)
		quicksort(mid+1,r)
		t1 = threading.Thread(target=quicksort,args=(l,mid-1))
		t1.start()
		t2 = threading.Thread(target=quicksort,args=(mid+1,r))
		t2.start()
		t1.join()
		t2.join()
a = getdata('input1.xml')
quicksort(0,len(a)-1)
print a
quicktest.py------------------------------------
import unittest
from a2_1 import *
class Mytest(unittest.TestCase):
	def testfun(self):
		try:
			a = getdata('input.xml')
			if a==None:
				self.fail('failed')
		except:
			self.fail('Failed... Cannot Load file')
	def testfun1(self):
		self.assertEqual(getdata('input1.xml'), [44, 21, 26,16,9])
unittest.main()
