+++
id = "ref/carried/core-rulebook/skills/acrobatics"
kind = "skill"
title = "Acrobatics"
source_ids = ["core-rulebook"]
section = ["Skills"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Skills/Acrobatics", path = "core_rulebook/skill/acrobatics.json" },
]

[fields]
kind = "none"
+++

::: statblock
Key Ability: Dex
Trained Only: Yes
Armor Check Penalty: Yes
:::

_You can keep your balance while traversing narrow or treacherous surfaces. You can also dive, flip,
jump, and roll to avoid attacks and overcome obstacles._

## Check {#check}

You can use Acrobatics to move on narrow surfaces and uneven ground without falling. A successful
check allows you to move at half speed across such surfaces—only one check is needed per round. Use
the following table to determine the base DC, which is then modified by the Acrobatics skill
modifiers noted below. While you are using Acrobatics in this way, you are considered flat-footed
and lose your Dexterity bonus to your AC (if any). If you take damage while using Acrobatics, you
must immediately make another Acrobatics check at the same DC to avoid falling or being knocked
prone.

### Surface Width {#surface-width}

::: table
head = [
  [
    { text = "Surface Width", header = true },
    { text = "Base Acrobatics DC", header = true },
  ],
]
body = [
  [
    { text = "Greater than 3 feet wide" },
    { text = "0\\*" },
  ],
  [
    { text = "1–3 feet wide" },
    { text = "5\\*" },
  ],
  [
    { text = "7–11 inches wide" },
    { text = "10" },
  ],
  [
    { text = "2–6 inches wide" },
    { text = "15" },
  ],
  [
    { text = "Less than 2 inches wide" },
    { text = "20" },
  ],
]
foot = [
  [
    { text = "\\* No Acrobatics check is needed to move across these surfaces unless the modifiers to the surface (below) increase the DC to 10 or higher.", colspan = 2 },
  ],
]
:::

In addition, you can move through a threatened square without provoking an attack of opportunity
from an enemy by using Acrobatics. When moving in this way, you move at half speed. You can move at
full speed by increasing the DC of the check by 10. You cannot use Acrobatics to move past foes if
your speed is reduced due to carrying a medium or heavy load or wearing medium or heavy armor. If an
ability allows you to move at full speed under such conditions, you can use Acrobatics to move past
foes. You can use Acrobatics in this way while prone, but doing so requires a full-round action to
move 5 feet, and the DC is increased by 5. If you attempt to move through an enemy's space and fail
the check, you lose the move action and provoke an attack of opportunity.

### Situation {#situation}

::: table
head = [
  [
    { text = "Situation", header = true },
    { text = "Base Acrobatics DC\\*", header = true },
  ],
]
body = [
  [
    { text = "Move through a threatened area" },
    { text = "Opponent's Combat Maneuver Defense" },
  ],
  [
    { text = "Move through an enemy's space" },
    { text = "5 + opponent's Combat Maneuver Defense" },
  ],
]
foot = [
  [
    { text = "\\* This DC is used to avoid an attack of opportunity due to movement. This DC increases by 2 for each additional opponent avoided in 1 round.", colspan = 2 },
  ],
]
:::

### Long Jump {#long-jump}

|Long Jump|Acrobatics DC|
| --- | --- |
|5 feet|5|
|10 feet|10|
|15 feet|15|
|20 feet|20|
|Greater than 20 feet|+5 per 5 feet|

### High Jump {#high-jump}

|High Jump|Acrobatics DC|
| --- | --- |
|1 foot|4|
|2 feet|8|
|3 feet|12|
|4 feet|16|
|Greater than 4 feet|+4 per foot|

Finally, you can use the Acrobatics skill to make jumps or to soften a fall. The base DC to make a
jump is equal to the distance to be crossed (if horizontal) or four times the height to be reached
(if vertical). These DCs double if you do not have at least 10 feet of space to get a running start.
The only Acrobatics modifiers that apply are those concerning the surface you are jumping from. If
you fail this check by 4 or less, you can attempt a DC 20 Reflex save to grab hold of the other side
after having missed the jump. If you fail by 5 or more, you fail to make the jump and fall (or land
prone, in the case of a vertical jump). Creatures with a base land speed above 30 feet receive a +4
racial bonus on Acrobatics checks made to jump for every 10 feet of their speed above 30 feet.
Creatures with a base land speed below 30 feet receive a –4 racial bonus on Acrobatics checks made
to jump for every 10 feet of their speed below 30 feet. No jump can allow you to exceed your maximum
movement for the round. For a running jump, the result of your Acrobatics check indicates the
distance traveled in the jump (and if the check fails, the distance at which you actually land and
fall prone). Halve this result for a standing long jump to determine where you land.

When you deliberately fall any distance, even as a result of a missed jump, a DC 15 Acrobatics skill
check allows you to ignore the first 10 feet fallen, although you still end up prone if you take
damage from a fall. See the falling rules for further details.

Many conditions can affect your chances of success with Acrobatics checks. The following modifiers
to target DCs apply to all Acrobatics skill checks. The modifiers stack with one another, but only
the most severe modifier for any one condition applies.

### Acrobatics Modifiers {#acrobatics-modifiers}

::: table
head = [
  [
    { text = "Acrobatics Modifiers", header = true },
    { text = "DC Modifier", header = true },
  ],
]
body = [
  [
    { text = "Slightly obstructed (gravel, sand)" },
    { text = "+2" },
  ],
  [
    { text = "Severely obstructed (cavern, rubble)" },
    { text = "+5" },
  ],
  [
    { text = "Slightly slippery (wet)" },
    { text = "+2" },
  ],
  [
    { text = "Severely slippery (icy)" },
    { text = "+5" },
  ],
  [
    { text = "Slightly sloped (\\<45°)" },
    { text = "+2" },
  ],
  [
    { text = "Severely sloped (\\>45°)" },
    { text = "+5" },
  ],
  [
    { text = "Slightly unsteady (boat in rough water)" },
    { text = "+2" },
  ],
  [
    { text = "Moderately unsteady (boat in a storm)" },
    { text = "+5" },
  ],
  [
    { text = "Severely unsteady (earthquake)" },
    { text = "+10" },
  ],
  [
    { text = "Move at full speed on narrow or uneven surfaces" },
    { text = "+5\\*" },
  ],
]
foot = [
  [
    { text = "\\* This does not apply to checks made to jump.", colspan = 2 },
  ],
]
:::

## Action {#action}

None. An Acrobatics check is made as part of another action or as a reaction to a situation.

## Special {#special}

If you have 3 or more ranks in Acrobatics, you gain a +3 dodge bonus to AC when fighting defensively
instead of the usual +2, and a +6 dodge bonus to AC when taking the total defense action instead of
the usual +4.

If you have the Acrobatic feat, you get a bonus on Acrobatics checks (see Feats).
