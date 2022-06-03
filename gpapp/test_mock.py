#coding:utf-8
import unittest
from gpapp.views import *


def test_api_result(monkeypatch):

    def mockreturn():
        return {"wikipedia":"""Tokyo /to.kjo/ (東京, Tōkyō, /toːkʲoː/ , litt. « Capitale de l'est »), anciennement Edo (江戸), officiellement Métropole de Tokyo (東京都, Tōkyō-to), est de facto la capitale actuelle du Japon. Elle est la plus peuplée des préfectures du Japon, avec plus de 14 831 421 habitants intra-muros en 2018 et 42 794 714 dans l'agglomération, et forme l'aire urbaine la plus peuplée au monde.
Située sur la côte est de l'île principale de l'archipel japonais, Honshū, Tokyo est l'une des quarante-sept préfectures du Japon. Principal centre politique de l'archipel depuis le XVIIe siècle, la ville accueille la plupart des institutions du pays : la résidence principale de l'empereur du Japon, du Premier ministre, le siège de la Diète (le parlement japonais), du Cabinet, les ministères qui le constituent ainsi que toutes les ambassades étrangères.""", "wikipedia2":"https://fr.wikipedia.org/wiki/Tokyo", "map":'https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyBVHZn0r4ew-nmCvlI1v27fbfJcKtA31TM&center=Tokyo%2C+Japan&zoom=15&size=400x400&markers=Tokyo%2C+Japan'}
 
    mocker.patch.object(views, 'request', mockreturn)
 
    expected_value = {"wikipedia":"""Tokyo /to.kjo/ (東京, Tōkyō, /toːkʲoː/ , litt. « Capitale de l'est »), anciennement Edo (江戸), officiellement Métropole de Tokyo (東京都, Tōkyō-to), est de facto la capitale actuelle du Japon. Elle est la plus peuplée des préfectures du Japon, avec plus de 14 831 421 habitants intra-muros en 2018 et 42 794 714 dans l'agglomération, et forme l'aire urbaine la plus peuplée au monde.
Située sur la côte est de l'île principale de l'archipel japonais, Honshū, Tokyo est l'une des quarante-sept préfectures du Japon. Principal centre politique de l'archipel depuis le XVIIe siècle, la ville accueille la plupart des institutions du pays : la résidence principale de l'empereur du Japon, du Premier ministre, le siège de la Diète (le parlement japonais), du Cabinet, les ministères qui le constituent ainsi que toutes les ambassades étrangères.""", "wikipedia2":"https://fr.wikipedia.org/wiki/Tokyo", "map":'https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyBVHZn0r4ew-nmCvlI1v27fbfJcKtA31TM&center=Tokyo%2C+Japan&zoom=15&size=400x400&markers=Tokyo%2C+Japan'}
    assert api_result("tokyo") == expected_value

if __name__ == "__main__":
	unittest.main()