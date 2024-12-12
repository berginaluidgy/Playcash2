
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, LikeEvent, GiftEvent

# Remplacer 'username' par le nom d'utilisateur TikTok

client = TikTokLiveClient(unique_id="@themsmartymar")

# Écoute des événements de commentaires
@client.on("comment")
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname}: {event.comment}")

# Écoute des événements de likes
@client.on("like")
async def on_like(event: LikeEvent):
    print(f"{event.user.nickname} a envoyé {event.like_count} likes!")

# Écoute des événements de cadeaux
@client.on("gift")
async def on_gift(event: GiftEvent):
    print(f"{event.user.nickname} a envoyé un cadeau : {event.gift.name}")

# Connexion au live
client.run()
