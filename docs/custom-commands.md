# Custom Commands & Grammar

Mockbot features a **Custom Command Engine**, inspired by the Twitch bot *Funtoon*. It allows you to build randomized chat responses and text games.

## Creating Basic Commands

You can create, edit, or delete static commands directly from chat:

*   **`!addc !<command_name> <response>`**: Creates a new command.
    *   *Example:* `!addc !lurk I am going to lurk now!`
*   **`!editc !<command_name> <new_response>`**: Modifies an existing command.
*   **`!delc !<command_name>`**: Deletes a custom command.

## Making Commands Interactive (Variables)

Commands can be configured to react to user input. Mockbot uses "Tags" (words wrapped in `<{ }>` brackets). When your command fires, Mockbot replaces these tags with corresponding variables.

*   **`<{sender}>`**: Automatically swaps to the username of the person who typed the command.
*   **`<{input}>`**: Automatically swaps to anything the user typed *after* the command.
*   **`<{streamer}>`**: Automatically swaps to the name of the channel the command was used in.

!!! tip "Example: A Slap Command"
    You type: `!addc !slap <{sender}> slaps <{input}>!`
    
    If `firestarman` types `!slap the wall`, the bot outputs: `firestarman slaps the wall!`

## Grammar Word Pools

Instead of typing the exact same text every time, you can tell the bot to randomly pick words from a "Word Pool". Pools are surrounded by hashtags like `#rule_name#`.

**Step 1: Fill up a Word Pool using `!grammar`:**

We are going to create a pool called "weapons".
*   Type: `!grammar add weapons a huge trout`
*   Type: `!grammar add weapons a folding chair`
*   Type: `!grammar add weapons the ban hammer`

**Step 2: Use the pool in a custom command:**

*   Type: `!addc !attack <{sender}> strikes <{input}> with #weapons#!`

Now, typing `!attack the boss` might result in `firestarman strikes the boss with a folding chair!` or `...with a huge trout!`. The output is randomized.

!!! note "Checking your pools"
    *   `!grammar list <rule>`: Show all the items you've added to a specific pool.
    *   `!grammar clear <rule>`: Deletes the pool entirely.

## Moderation Actions (Auto-Timeouts)

Custom commands can execute **real Twitch timeouts**. This can be used to create chat minigames.

### The Timeout Tag

To issue a timeout, include the hidden `{timeout:user:duration}` tag anywhere in your command's response. **The tag itself is completely invisible in chat.**

*   **Syntax**: `{timeout:username:seconds}`
*   **Usage with Inputs**: `{timeout:<{input}>:60}` (Times out whoever the sender targets message for 60s)
*   **Self-Timeout**: `{timeout:<{sender}>:10}` (Times out the person who typed the command for 10s)

### Security Rules

To prevent abuse, Mockbot will **ONLY** honor a `{timeout...}` tag if the user typing the command meets one of these rules:

1. They are a Channel Moderator.
2. They are the Broadcaster.
3. They are the Global Bot Owner.
4. **They are targeting themselves.** (Even non-mods can use commands that timeout *themselves*).

!!! example "Russian Roulette Game"
    Let's make a game using Word Pools (Grammar) and Timeouts!
    
    1. **Setup the outcomes (5 empty chambers, 1 bullet):**
        *   `!grammar add roulette <{sender}> survives the spin... this time.`
        *   `!grammar add roulette <{sender}> survives the spin... this time.`
        *   `!grammar add roulette <{sender}> survives the spin... this time.`
        *   `!grammar add roulette <{sender}> survives the spin... this time.`
        *   `!grammar add roulette <{sender}> survives the spin... this time.`
        *   `!grammar add roulette *BANG* <{sender}> was shot! {timeout:<{sender}>:60}`
    
    2. **Create the command:**
        *   `!addc !spin #roulette#`
    
    Now, when a viewer types `!spin`, they have a 1-in-6 chance of being timed out for 60 seconds automatically by the bot.
