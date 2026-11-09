+++
id = "ref/spell/awaken-construct"
kind = "spell"
title = "Awaken Construct"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "awaken_construct", path = "json/spells.json" },
]
[[sources]]
publication = "occult-adventures"
page = "158"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "24 hours"
components = "V, S, DF, M (herbs and oils worth 2,000 gp per HD of target)"
range = "touch"
effects = [
  { label = "Target", value = "mindless construct touched" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Occultist\
6: Psychic, Shaman\
7: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 24 hours
Components: V, S, DF, M (herbs and oils worth 2,000 gp per HD of target)
Range: touch
Duration: instantaneous
Saving throw: Will negates
Spell resistance: no
Target: mindless construct touched
:::

You amplify the animating force of a construct to more closely resemble a true soul, granting the
construct human-like sentience. To do so, you must succeed at a Spellcraft check (DC = 15 + the
construct's current Hit Dice). If the construct's master (if any) is present, this is an opposed
Spellcraft check. You have no special empathy or connection with a creature you awaken - it is a
free-willed creature. Golems previously under another creature's control, either as shield guardians
or a golem crafter's creations, break all connections with that creature.

Roll 3d6 to determine the Intelligence score of the awakened construct, and increase its Charisma
score by 2d6. It gains feats and skill points according to its new Intelligence score, and the skill
points are assigned appropriately for its function, as determined by the GM.

An awakened construct speaks one language that its creator spoke, plus one additional language that
its creator knew per point of the construct's Intelligence bonus (if any). Its alignment is
determined by the GM, but is usually within one step of its creator's alignment. This spell doesn't
function on a construct with an Intelligence score.
