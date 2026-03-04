# Twitch Interactions (Polls & Timers)

Mockbot has built-in support for native Twitch API polls and timed chat messages. No need to open your Creator Dashboard!

## Creating Twitch Polls

You can launch a native Twitch Poll directly from the chat UI without lifting a finger from your keyboard.

*   **Syntax**: `!poll <duration_in_minutes> <Question> | <Option 1> | <Option 2> | [Option 3...]`
*   **Example**: `!poll 5 What game should I play tonight? | Mario | Zelda | Halo`

!!! warning "Poll Rules"
    *   Minimum 2 options, maximum of 5 options. 
    *   Duration must be between **15 seconds** and **30 minutes**.

## Timed Message Pools (The "Shoutout" feature)

Timers are rotating lists of messages that the bot will broadcast automatically over time. This is perfect for dropping your Discord links, social media plugs, or reminders for people to subscribe!

1. **Create the timer:**
    *   *Type:* `!mockbot timer add socials 30`
    *   *What it does:* Creates a timer called "socials" that will go off every 30 minutes.
2. **Add messages to it:**
    *   *Type:* `!mockbot timer msg socials Join our community Discord at discord.gg/example!`
    *   *Type:* `!mockbot timer msg socials Follow me on Twitter at @example!`
    *   *What it does:* The bot will now cycle through these messages every 30 minutes!

If you need to check or delete your timers:

*   **List them:** `!mockbot timer list` (View all active rules)
*   **Delete one:** `!mockbot timer del socials` (Deletes the timer we just made)
