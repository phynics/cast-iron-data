+++
id = "ref/spell/harrowing"
kind = "spell"
title = "Harrowing"
aon = "SpellDisplay.aspx?ItemName=Harrowing"
source_ids = ["inner-sea-world-guide", "the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "harrowing", path = "json/spells5.json" },
]
[[sources]]
publication = "inner-sea-world-guide"
page = "295"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, F (a Harrow deck)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level or until fulfilled"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Arcanist, Bard, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (a Harrow deck)
Range: touch
Duration: 1 day/level or until fulfilled
Saving throw: none
Spell resistance: no
Target: one creature
:::

You use a Harrow deck to tell a fortune for yourself or someone else. If you cast harrowing on
another creature, you must remain adjacent to the target for the duration of the casting time. A
harrowing must describe one set of events or course of action (for example, "hunting down the pirate
king," or "traveling to Viperwall to search for a magic sword") that the target of the spell intends
to undertake at some point during the spell's duration.

If you have access to a Harrow deck, draw nine cards when this spell is cast. If you do not have a
Harrow deck, you can simulate the draws by rolling a d6 and a d10 for each of the nine cards, as
detailed in the [deck description](ref/eq-misc/harrow-deck). Record the ability score and alignment
associated with each card. Each of these cards grants a luck bonus or a penalty on a specific type
of d20 check; the magnitude of the penalty or bonus depends upon how closely that particular card's
alignment matches the target creature's alignment. If the card and target's alignments are
identical, that card provides a +2 luck bonus on the associated suit's check. If the card and
target's alignments are of the opposite alignment (see below), the card inflicts a -1 penalty on
that associated check. If the card has any other alignment, it provides a +1 luck bonus on the
associated suit's check.

While penalties persist on all associated checks for as long as the harrowing persists, the bonuses
are one-use bonuses that the harrowed character can "spend" at any time to modify that card's
associated check. You can spend a bonus to modify an appropriate roll after the die is rolled, but
cannot spend the bonus once you know the result of the roll. Since all of the bonuses granted by a
harrowing are luck bonuses, they do not stack with each other. Penalties, on the other hand, do
stack. Once you spend all of the bonuses granted by a harrowing, or once the spell's duration ends,
the spell ends and the penalties are removed.

A single creature can only be under the effects of one harrowing at a time. If it is subjected to a
second harrowing while a previous harrowing is still in effect, the new harrowing automatically
fails.

#### Suit

|Suit|Associated Check|
| --- | --- |
|Hammer (Str)|Attack rolls (ranged and melee)|
|Key (Dex)|Reflex saving throws|
|Shield (Con)|Fortitude saving throws|
|Book (Int)|Skill checks|
|Star (Wis)|Will saving throws|
|Crown (Cha)|Any d20 roll|

#### Alignment

|Alignment|Opposition|
| --- | --- |
|LG|CE|
|NG|NE|
|CG|LE|
|LN|CN|
|N|LG, LE, CG, or CE (pick one when spell is cast)|
|CN|LN|
|LE|CG|
|NE|NG|
|CE|LG|
