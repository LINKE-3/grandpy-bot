#coding:utf-8
import unittest
from gpapp.views import *


class test_parser(unittest.TestCase):
	def setUp(self):
		self.valuea = "je suis là"
		self.valueb = "as tu entendu parler de tokyo"
		self.valuec = " "

	def test_parser_with_no_key_word(self):
		"""check if the parser work"""
		response = ""
		self.assertEqual(parser(self.valuea), response)

	def test_parser_with_key_word(self):
		"""check if the parser work with key word"""
		response = "entendu tokyo "
		self.assertEqual(parser(self.valueb), response)

	def test_parser_empty(self):
		"""check if the parser work with key word"""
		response = "le formulaire est vide"
		self.assertEqual(parser(self.valuec), response)

class test_api(unittest.TestCase):

	def setUp(self):
		self.valuea = " "
		self.valueb = "tokyo"

	def test_wiki_data_with_key_word(self):
		"""check wiki data"""
		response = "https://fr.wikipedia.org/wiki/Tokyo"
		self.assertEqual(wiki_search(self.valueb), response)

	def test_summarize(self):
		"""check wiki resume"""
		response = """Tokyo /to.kjo/ (東京, Tōkyō, /toːkʲoː/ , litt. « Capitale de l'est »), anciennement Edo (江戸), officiellement Métropole de Tokyo (東京都, Tōkyō-to), est de facto la capitale actuelle du Japon. Elle est la plus peuplée des préfectures du Japon, avec plus de 13 831 421 habitants intra-muros en 2018 et 42 794 714 dans l'agglomération, et forme l'aire urbaine la plus peuplée au monde.
Située sur la côte est de l'île principale de l'archipel japonais, Honshū, Tokyo est l'une des quarante-sept préfectures du Japon. Principal centre politique de l'archipel depuis le XVIIe siècle, la ville accueille la plupart des institutions du pays : la résidence principale de l'empereur du Japon, du Premier ministre, le siège de la Diète (le parlement japonais), du Cabinet, les ministères qui le constituent ainsi que toutes les ambassades étrangères."""
		self.assertEqual(wiki_summarize(self.valueb), response)

	def test_wiki_data_no_key_word(self):
		"""check wiki erreur"""
		response = []
		self.assertEqual(wiki_search_error(self.valuea), response)

	def test_print_url_map(self):
		"""display an url from google map api of a specific place"""
		response = 'https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyBVHZn0r4ew-nmCvlI1v27fbfJcKtA31TM&center=Tokyo%2C+Japan&zoom=15&size=400x400&markers=Tokyo%2C+Japan'
		self.assertEqual(google_map_search(self.valueb), response)

if __name__ == "__main__":
	unittest.main()