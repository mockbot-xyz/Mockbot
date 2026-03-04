# Core Features & Settings

Mockbot operates primarily through Twitch Chat commands using the prefix `!mockbot`. If you are a channel operator (like a Mod) or have been added as a "Trusted User", you can type these directly into chat to change how the bot behaves on the fly.

## Standard Commands

These are the commands you'll use most often to control how chatty Mockbot is.

| Type This in Chat | What Does It Do? |
|---|---|
| `!mockbot speak` | **Make the bot talk immediately.** It will look at what your chat has been talking about recently, generate a fresh sentence, and send it. If TTS is on, it will also read it out loud. |
| `!mockbot start` or `!mockbot stop` | **Turn the automatic talking on or off.** When started, the bot will jump in and talk by itself after a certain amount of time or chat messages pass. |
| `!mockbot lines 20` | **Set how many real chatter messages need to go by** before Mockbot decides it's time to speak again. (In this example, it waits for 20 messages). |
| `!mockbot time 300` | **Set the cooldown timer.** This forces the bot to wait *at least* this many seconds (e.g. 300 seconds = 5 minutes) before talking automatically again. |
| `!mockbot trust Firestarman` | **Give someone permission to control the bot.** The user `Firestarman` can now use all of these `!mockbot` commands, as well as create timers and custom commands. |
| `!mockbot join #mychannel` | *(Bot Host Only)* Tells the background program to connect the bot to a new Twitch channel. |

!!! tip "Finding the Sweet Spot"
    If your chat is moving fast, you may want to increase `!mockbot lines` so the bot does not spam too frequently. If your chat is slower, keeping the lines low but the `time` higher is recommended.

## PubSub Integrations (Bits & Points)

"PubSub" refers to Twitch's live event system. Mockbot can "listen" for when someone Cheers bits or redeems a Channel Point reward on your channel.

### 1. Setting Up Permissions
For Mockbot to actually "see" your stream's Cheers and Point redemptions, the Twitch Account you connected the bot to inside `settings.conf` **must have the right permissions**.

When generating your `tmi_token` OAuth password, make sure you checked these two boxes:
*   `bits:read` (Allows the bot to see cheers)
*   `channel:read:redemptions` (Allows the bot to see channel points)

### 2. Turn It On In Chat
Once your bot has permission, you can turn the features on or off directly from your Twitch chat:

*   **Type `!mockbot bits on`**: The bot will now monitor cheers. When someone Cheers, it will automatically drop a message: *"Thank you Firestarman for the 100 bits!"*
*   **Type `!mockbot points on`**: The bot will now monitor your Channel Point redemptions.

*(You can turn these off at any time by typing `!mockbot bits off`)*

### 3. The Power of Channel Points
Mockbot's channel points integration allows you to trigger commands via redemptions. **If you name a Twitch Channel Point Reward the exact same name as a Bot Command, the bot will execute it.**

For example:
1. You go to your Twitch Creator Dashboard and create a new Channel Point Reward.
2. You name the reward: `!speak`
3. Whenever a viewer redeems that reward, Mockbot will automatically generate and send a Markov message, just as if they typed `!speak` in chat.

This works for all custom commands and Funtoon grammar. You could attach a "Russian Roulette Time Out" command directly to a Channel Point reward.
