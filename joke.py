from jokeapi import Jokes
import asyncio

class JokeAPI(object):
    def __init__(self, lang="de", search_string=""):
        self.lang = lang
        self.search_string = search_string

    def get_joke(self, search_string=None):
        if search_string is not None:
            self.search_string = search_string

        return asyncio.run(self.__get_joke(self.search_string))

    async def __get_joke(self, search_string=None):
        j = await Jokes()
        joke = await j.get_joke(lang=self.lang, search_string=search_string)

        error = "Error: No Joke found!"

        if "type" in joke:
            if joke["type"] == "single":
                return joke.get("joke", error)
            else:
                setup = joke.get("setup", error)
                delivery = joke.get("delivery", error)
                return "{}\n{}".format(setup, delivery)
        else:
            return error

if __name__ == "__main__":
    jokes = JokeAPI()

    for i in range(1,5):
        print(jokes.get_joke())
