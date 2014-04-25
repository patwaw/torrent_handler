'''
	search.py

	ThePirateBay browser.
	Requirements: ThePirateBay library
'''

from tpb import TPB
from tpb import CATEGORIES, ORDERS
import argparse
import sys

class Search(object):
	def __init__(self, domain):
		if domain != None:
			self.domain = domain
		else:
			self.domain = "https://thepiratebay.se"
		self.tpb = TPB(self.domain)
	def list_categories(self):
		print """List of category codes:
ALL - 0
AUDIO:
	All - 100
	Music - 101
	Audio books - 102
	Sound clips - 103
	Flac - 104
	Other - 199
VIDEO:
	All - 200
	Movies - 201
	Movies DVDR - 202
	Music videos - 203
	Movie clips - 204
	TV shows - 205
	Handheld - 206
	HD movies - 207
	HD TV shows - 208
	3D - 209
	Other - 299
APPLICATIONS:
	All - 300
	Windows - 301
	Mac - 302
	Unix - 303
	Handheld - 304
	iOS - 305
	Android - 306
	Other - 399
GAMES:
	All - 400
	PC - 401
	Mac - 402
	PSX - 403
	Xbox 360 - 404
	Wii - 405
	Handheld - 406
	iOS - 407
	Android - 408
	Other - 499
PORN:
	All - 500
	Movies - 501
	Movies DVDR - 502
	Pictures - 503
	Games - 504
	HD Movies - 505
	Movie clips - 506
	Other - 599
OTHER:
	E-books - 601
	Comics - 602
	Pictures - 603
	Covers - 604
	Physibles - 605
	Other - 699
"""
		sys.exit(0)

	def list_orders(self):
		print """List of sorting codes:
NAME:
    Descending = 1
    Ascending = 2

UPLOADED:
    Descending = 3
    Ascending = 4

SIZE:
    Descending = 5
    Ascending = 6

SEEDERS:
    Descending = 7
    Ascending = 8

LEECHERS:
    Descending = 9
    Ascending = 10

UPLOADER:
    Descending = 11
    Ascending = 12

TYPE:
    Descending = 13
    Ascending = 14

			  """
		sys.exit(0)


	def search(self, category_number=0, query='', order_number=1, limit=0):
		self.query = query
		self.limit = limit
		self.categories = {  
						0   : CATEGORIES.ALL,
						100 : CATEGORIES.AUDIO.ALL,
						101 : CATEGORIES.AUDIO.MUSIC,
						102 : CATEGORIES.AUDIO.AUDIO_BOOKS,
						103 : CATEGORIES.AUDIO.SOUND_CLIPS,
						104 : CATEGORIES.AUDIO.FLAC,
						199 : CATEGORIES.AUDIO.OTHER,
						200 : CATEGORIES.VIDEO.ALL,
						201 : CATEGORIES.VIDEO.MOVIES,
						202 : CATEGORIES.VIDEO.MOVIES_DVDR,
						203 : CATEGORIES.VIDEO.MUSIC_VIDEOS,
						204 : CATEGORIES.VIDEO.MOVIE_CLIPS,
						205 : CATEGORIES.VIDEO.TV_SHOWS,
						206 : CATEGORIES.VIDEO.HANDHELD,
						207 : CATEGORIES.VIDEO.HD_MOVIES,
						208 : CATEGORIES.VIDEO.HD_TV_SHOWS,
						209 : CATEGORIES.VIDEO.THREE_DIMENSIONS,
						299 : CATEGORIES.VIDEO.OTHER,
						300 : CATEGORIES.APPLICATIONS.ALL,
						301 : CATEGORIES.APPLICATIONS.WINDOWS,
						302 : CATEGORIES.APPLICATIONS.MAC,
						303 : CATEGORIES.APPLICATIONS.UNIX,
						304 : CATEGORIES.APPLICATIONS.HANDHELD,
						305 : CATEGORIES.APPLICATIONS.IOS,
						306 : CATEGORIES.APPLICATIONS.ANDROID,
						399 : CATEGORIES.APPLICATIONS.OTHER,
						400 : CATEGORIES.GAMES.ALL,
						401 : CATEGORIES.GAMES.PC,
						402 : CATEGORIES.GAMES.MAC,
						403 : CATEGORIES.GAMES.PSX,
						404 : CATEGORIES.GAMES.XBOX360,
						405 : CATEGORIES.GAMES.WII,
						406 : CATEGORIES.GAMES.HANDHELD,
						407 : CATEGORIES.GAMES.IOS,
						408 : CATEGORIES.GAMES.ANDROID,
						499 : CATEGORIES.GAMES.OTHER,

						601 : CATEGORIES.OTHER.EBOOKS,
						602 : CATEGORIES.OTHER.COMICS,
						603 : CATEGORIES.OTHER.PICTURES,
						604 : CATEGORIES.OTHER.COVERS,
						605 : CATEGORIES.OTHER.PHYSIBLES,
						699 : CATEGORIES.OTHER.OTHER 
						}
		self.orders = {
						1  : ORDERS.NAME.DES,
						2  : ORDERS.NAME.ASC,
						3  : ORDERS.UPLOADED.DES,
						4  : ORDERS.UPLOADED.ASC,
						5  : ORDERS.SIZE.DES,
						6  : ORDERS.SIZE.ASC,
						7  : ORDERS.SEEDERS.DES,
						8  : ORDERS.SEEDERS.ASC,
						9  : ORDERS.LEECHERS.DES,
						10 : ORDERS.LEECHERS.ASC,
						11 : ORDERS.UPLOADER.DES,
						12 : ORDERS.UPLOADER.ASC,
						13 : ORDERS.TYPE.DES,
						15 : ORDERS.TYPE.ASC
						}

		try:
			self.category = self.categories[category_number]
		except KeyError:
			print "Provide correct category code."
			sys.exit(2)

		try:
			self.order = self.orders[order_number]
		except KeyError:
			print "Provide correct sorting code."
			sys.exit(3)

		if self.limit == 0:
			for torrent in self.tpb.search(self.query, category=self.category).order(self.order):
				print torrent.title, " - ", torrent.user
				print "Seeders: ", torrent.seeders
				print "Leechers: ", torrent.leechers
				print torrent.magnet_link
		sys.exit(0)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="TPB search")
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-sc", "--sortingcodes", action='store_true')
	group.add_argument("-lc", "--listcategories", action='store_true')
	parser.add_argument("-d", "--domain", type=str)
	parser.add_argument("-q", "--query", type=str)
	parser.add_argument("-c", "--category", type=int)
	parser.add_argument("-s", "--sort", type=int)
	parser.add_argument("-l", "--limit", type=int)
	args = parser.parse_args()
	query = args.query
	domain = args.domain
	category = args.category
	sort = args.sort
	search = Search(domain)
	# limit = args.limit
	if args.sortingcodes == True:
		search.list_orders()
	if args.listcategories == True:
		search.list_categories()
	search.search(category_number=category, query=query, order_number=sort)
	sys.exit(0)