import requests

class JokeAPI(object):
    def __init__(self, category="Any", language="en", blacklist=None, response_format="json", joke_type="single", search_string="", min_range_id=0, max_range_id=1368, amount_of_jokes=1):
        self.__BASE_URL = "https://v2.jokeapi.dev/joke/"
        self.__categories = ["Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"]
        self.__languages = ["en", "de", "cs", "es", "fr", "pt"]
        self.__blacklist_flags = ["nsfw", "religious", "political", "racist", "sexist", "explicit"]
        self.__response_formats = ["json", "xml", "yaml", "plain text"]
        self.__joke_types = ["single", "twopart"]
        self.__search_min_id_range = 0
        self.__search_max_id_range = 1368

        self.setCategory(category)
        self.setLanguage(language)
        self.setBlacklist(blacklist)
        self.setResponseFormat(response_format)
        self.setJokeType(joke_type)
        self.setSearchString(search_string)
        self.setMinRangeId(min_range_id)
        self.setMaxRangeId(max_range_id)
        self.setAmountOfJokes(amount_of_jokes)

    def setCategory(self, category):
        if self.__checkCategory(category):
            if isinstance(category, str):
                self.category = category
            else:
                self.category = ",".join(category).replace(" ", "")
        else:
            self.category = None

    def getCategory(self):
        return self.category

    def setLanguage(self, language):
        if self.__checkLanguage(language):
            self.language = language
        else:
            self.language = None

    def getLanguage(self):
        return self.language

    def setBlacklist(self, blacklist):
        if self.__checkBlacklist(blacklist):
            if isinstance(blacklist, str):
                self.blacklist = blacklist
            else:
                self.blacklist = ",".join(blacklist).replace(" ", "")
        else:
            self.blacklist = None

    def getBlacklist(self):
        return self.blacklist

    def setResponseFormat(self, response_format):
        if self.__checkResponseFormat(response_format):
            self.response_format = response_format
        else:
            self.response_format = None

    def getResponseFormat(self):
        return self.response_format

    def setJokeType(self, joke_type):
        if self.__checkJokeType(joke_type):
            self.joke_type = joke_type
        else:
            self.joke_type = None

    def getJokeType(self):
        return self.joke_type

    def setSearchString(self, search_string):
        if self.__checkSearchString(search_string):
            self.search_string = search_string
        else:
            self.search_string = None

    def getSearchString(self):
        return self.search_string

    def setMinRangeId(self, min_range_id):
        if self.__checkIdRangeMin(min_range_id):
            self.min_range_id = min_range_id
        else:
            self.min_range_id = None

    def getMinRangeId(self):
        return self.min_range_id

    def setMaxRangeId(self, max_range_id):
        if self.__checkIdRangeMax(max_range_id):
            self.max_range_id = max_range_id
        else:
            self.max_range_id = None

    def getMaxRangeId(self):
        return self.max_range_id

    def setAmountOfJokes(self, amount_of_jokes):
        if self.__checkAmountOfJokes(amount_of_jokes):
            self.amount_of_jokes = amount_of_jokes
        else:
            self.amount_of_jokes = None

    def getAmountOfJokes(self):
        return self.amount_of_jokes

    def __checkCategory(self, category):
        if isinstance(category, str):
            if category == "Any":
                return True
            else:
                return False
        elif isinstance(category, list):
            if category in self.getCategories():
                return True
            else:
                return False
        else:
            return False
    
    def __checkLanguage(self, language):
        if isinstance(language, str):
            if language in self.getLanguages():
                return True
            else:
                return False
        else:
            return False
    
    def __checkBlacklist(self, blacklist):
        if isinstance(blacklist, str) and "," in blacklist:
            blacklist = blacklist.split(",")

        if isinstance(blacklist, str):
            if blacklist in self.getBlacklistFlags():
                return True
            else:
                return False
        elif isinstance(blacklist, list):
            if blacklist in self.getBlacklistFlags():
                return True
            else:
                return False
        else:
            return False
    
    def __checkResponseFormat(self, response_format):
        if isinstance(response_format, str):
            if response_format in self.getResponseFormats():
                return True
            else:
                return False
        else:
            return False
    
    def __checkJokeType(self, joke_type):
        if isinstance(joke_type, str):
            if joke_type in self.getJokeTypes():
                return True
            else:
                return False
        else:
            return False
    
    def __checkSearchString(self, search_string):
        if isinstance(search_string, str):
            return True
        else:
            return False
    
    def __checkIdRangeMin(self, id_range_min):
        if isinstance(id_range_min, int) and (self.getMinOfSearchIdRange() <= id_range_min < self.getMaxOfSearchIdRange()):
            return True
        else:
            return False
        
    def __checkIdRangeMax(self, id_range_max):
        if isinstance(id_range_max, int) and (self.getMinOfSearchIdRange() < id_range_max <= self.getMaxOfSearchIdRange()):
            return True
        else:
            return False
    
    def __checkAmountOfJokes(self, amount_of_jokes):
        if isinstance(amount_of_jokes, int):
            if 1 <= amount_of_jokes <= self.getMaxOfSearchIdRange():
                return True
            else:
                return False
        else:
            return False

    def getBaseUrl(self):
        return self.__BASE_URL
    
    def getCategories(self):
        return self.__categories
    
    def getLanguages(self):
        return self.__languages
    
    def getBlacklistFlags(self):
        return self.__blacklist_flags
    
    def getResponseFormats(self):
        return self.__response_formats
    
    def getJokeTypes(self):
        return self.__joke_types
    
    def getMinOfSearchIdRange(self):
        return self.__search_min_id_range
    
    def getMaxOfSearchIdRange(self):
        return self.__search_max_id_range
    
    def get_jokes(self, category="Any", language="en", blacklist=None, response_format="json", joke_type="single", search_string="", min_range_id=0, max_range_id=1368, amount_of_jokes=1):
        self.setCategory(category)
        self.setLanguage(language)
        self.setBlacklist(blacklist)
        self.setResponseFormat(response_format)
        self.setJokeType(joke_type)
        self.setSearchString(search_string)
        self.setMinRangeId(min_range_id)
        self.setMaxRangeId(max_range_id)
        self.setAmountOfJokes(amount_of_jokes)

        url = self.getBaseUrl() + self.getCategory()
        params = {
            "format": self.getResponseFormat(),
            "blacklistFlags": self.getBlacklist(),
            "type": self.getJokeType(),
            "lang": self.getLanguage(),
            "amount": self.getAmountOfJokes()
        }

        try:
            response = requests.get(url, params=params, timeout=8)
            response.raise_for_status()

            if response.ok or response.status_code == 200:
                return response.text
            else:
                print("Failed to retrieve jokes. Status code: {}.".format(response.status_code))
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

if __name__ == "__main__":
    joke = JokeAPI()
    print(joke.get_jokes())
