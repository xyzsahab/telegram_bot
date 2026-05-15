import asyncio
import random
import requests
import telegram

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = telegram.Bot(token=BOT_TOKEN)


async def send_image(image_url):
    try:
        response = requests.get(image_url)

        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=response.content
        )

        print("Image sent successfully")

    except Exception as e:
        print(f"Unable to send image: {e}")


async def send_message(message):
    try:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode="HTML"
        )

        print("Message sent successfully")

    except Exception as e:
        print(f"Unable to send message: {e}")


def hindi_quote():
    response = requests.get(
        "https://hindi-quotes.vercel.app/random"
    )

    data = response.json()

    return data["quote"]


def hindi_joke():
    response = requests.get(
        "https://hindi-jokes-api.onrender.com/jokes?api_key=YOUR_API_KEY"
    )

    data = response.json()

    return data["jokeContent"]


def would_you_rather():
    url = "https://would-you-rather.p.rapidapi.com/wyr/random"

    headers = {
        "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
        "x-rapidapi-host": "would-you-rather.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data[0]["question"]


def anime_quotes():
    anime_list = [
        "Naruto",
        "One Piece",
        "Attack on Titan",
        "My Hero Academia",
        "Dragon Ball",
        "Demon Slayer",
        "Death Note",
        "Bleach"
    ]

    url = "https://anime-quotes5.p.rapidapi.com/api.php"

    querystring = {
        "anime": random.choice(anime_list)
    }

    headers = {
        "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
        "x-rapidapi-host": "anime-quotes5.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    data = random.choice(response.json())

    asyncio.run(send_image(data["character_thumbnail_url"]))

    return (
        f"{data['anime']}\n"
        f"{data['character']}\n"
        f"{data['quote']}"
    )


def send(message):
    asyncio.run(send_message(message))


if __name__ == "__main__":
    completed = 0

    options = [1, 2, 3, 4]

    while completed != 3:
        try:
            selected = random.choice(options)

            if selected == 1:
                data = hindi_joke()

                send("😂 Hindi Joke")
                send(data)
                send("_" * 35)

            elif selected == 2:
                data = hindi_quote()

                send("✨ Quote of the Day")
                send(data)
                send("_" * 35)

            elif selected == 3:
                data = would_you_rather()

                send("🤔 Would You Rather")
                send(data)
                send("_" * 35)

            else:
                data = anime_quotes()

                send("🎌 Anime Quote")
                send(data)
                send("_" * 35)

            completed += 1

            options.remove(selected)

        except Exception as e:
            print(e)