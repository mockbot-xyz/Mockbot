# Core Features & Settings

Mockbot operates primarily through Twitch Chat commands using the prefix `!mockbot`. Don't worry, you don't need to be a programmer to configure it! If you are a channel operator (like a Mod) or have been added as a "Trusted User", you can type these directly into chat to change how the bot behaves on the fly.

## Standard Commands

These are the commands you'll use most often to control how chatty Mockbot is.

| Type This in Chat | What Does It Do? |
|---|---|
| `!mockbot speak` | **Make the bot talk immediately.** It will look at what your chat has been talking about recently, generate a fresh sentence, and send it. If TTS is on, it will also read it out loud! |
| `!mockbot start` or `!mockbot stop` | **Turn the automatic talking on or off.** When started, the bot will jump in and talk by itself after a certain amount of time or chat messages pass. |
| `!mockbot lines 20` | **Set how many real chatter messages need to go by** before Mockbot decides it's time to speak again. (In this example, it waits for 20 messages). |
| `!mockbot time 300` | **Set the cooldown timer.** This forces the bot to wait *at least* this many seconds (e.g. 300 seconds = 5 minutes) before talking automatically again. |
| `!mockbot trust Firestarman` | **Give someone permission to control the bot.** The user `Firestarman` can now use all of these `!mockbot` commands, as well as create timers and custom commands. |
| `!mockbot join #mychannel` | *(Bot Host Only)* Tells the background program to connect the bot to a new Twitch channel. |

!!! tip "Finding the Sweet Spot"
    If your chat is moving really fast, you might want to increase `!mockbot lines` so the bot doesn't spam too frequently! If your chat is slower, keeping the lines low but the `time` higher works great.

## PubSub Integrations (Bits & Points)

"PubSub" is just a fancy term for Twitch's live event system. Mockbot can "listen" for when someone Cheers bits or redeems a Channel Point reward, and automatically generate a chat message reaction!

*   **Type `!mockbot bits on`**: The bot will now react automatically when someone cheers!
*   **Type `!mockbot points on`**: The bot will now react automatically when someone redeems Channel Points!

*(You can turn these off at any time by typing `!mockbot bits off`)*
