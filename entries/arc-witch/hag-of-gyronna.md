+++
id = "ref/arc-witch/hag-of-gyronna"
kind = "archetype"
title = "Hag of Gyronna"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Hag%20of%20Gyronna"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hag_of_gyronna", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "people-of-the-river"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "patron" },
  { anchor = "spells" },
  { anchor = "curdle-thoughts", level = 2 },
  { anchor = "sunder-hope", level = 8 },
  { anchor = "hag-crony", level = 12 },
]
trades = [
  { replaces = "2nd-level hex", feature = "hex", levels = [2], by = ["curdle-thoughts"] },
  { replaces = "8th-level hex", feature = "hex", levels = [8], by = ["sunder-hope"] },
  { replaces = "12th-level hex", feature = "hex", levels = [12], by = ["hag-crony"] },
]
+++

Only female witches dare dedicate themselves to the [Angry Hag](ref/faith/gyronna), and those who do
so are feared for their ability to bend minds and sow discord. Some say these witches can watch
their enemies from afar and can even corrupt the minds of the most innocent or loyal, including
newborn babes and cherished pets.

## Patron {#patron}

A hag of Gyronna must choose [Deception](ref/patron/deception), [Trickery](ref/patron/trickery),
[Vengeance](ref/patron/vengeance), or [Water](ref/patron/water) as her witch patron.

## Spells {#spells}

A hag of Gyronna replaces several of her patron spells with the following: 2nd—_doom_, 6th—_obscure
object_, 10th—_commune_, 14th—_repulsion_, 18th—_shapechange_.

## Curdle Thoughts (Su) {#curdle-thoughts}

At 2nd level, a hag of Gyronna can insert negative emotions into the mind of a single target. She
gains a +2 bonus on Diplomacy and Bluff checks to sow suspicion, hatred, or other forms of
animosity. In addition, a hag of Gyronna can choose to increase the save DC of any spell with the
fear descriptor she casts by 2. She can increase a spell's DC in this way a number of times per day
equal to 1/2 her witch level. This ability replaces the witch's 2nd-level hex.

## Sunder Hope (Su) {#sunder-hope}

At 8th level, a hag of Gyronna can violently dismiss her curses to counter magical boons and impose
her own capricious whims. Once per day, after the hag of Gyronna has successfully affected a
creature within 30 feet with a mind-affecting spell,
[spell-like ability](ref/umr/spell-like-abilities), or hex with a duration of longer than 1 round,
she can choose to dismiss the mind-affecting effect as an immediate action. If she dismisses this
effect in response to another creature targeting her victim with a beneficial spell or ability, the
witch's effect is dismissed and the caster of the beneficial spell or ability must succeed at a Will
save (DC = 10 + 1/2 the witch's level + her Intelligence modifier) or the spell or ability is wasted
to no effect and the targeted victim takes 1d4 points of
[Wisdom damage](ref/rule/ability-damage-drain). At 14th and 20th levels, a hag of Gyronna can use
this ability an additional time per day. This ability replaces the witch's 8th-level hex.

## Hag Crony (Su) {#hag-crony}

At 12th level, a hag of Gyronna gains a blessing from the Angry Hag in the form of an alliance with
a night hag (_Pathfinder RPG Bestiary_ 215). Once per week, the hag of Gyronna can as a full-round
action summon the night hag from the Shadow Plane. The night hag serves the hag of Gyronna to the
best of its ability as long as the witch's commands are consistent with the night hag's alignment
and goals, but flees back to its native plane after a number of rounds equal to the witch's level or
upon losing half or more of its hit points. The night hag may provide the hag of Gyronna with other
favors or gifts at the GM's discretion. At 15th and 18th levels, a hag of Gyronna can call upon her
hag crony an additional time per week. This ability replaces the witch's 12th-level hex.
