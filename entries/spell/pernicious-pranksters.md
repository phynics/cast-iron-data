+++
id = "ref/spell/pernicious-pranksters"
kind = "spell"
title = "Pernicious Pranksters"
aon = "SpellDisplay.aspx?ItemName=Pernicious%20Pranksters"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pernicious_pranksters", path = "json/spells7.json" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "18"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 3 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Occultist", level = 3 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (three drops of honey rolled in a sycamore leaf)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "fey pranksters" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Bard, Occultist, Skald\
5: Arcanist, Druid, Hunter, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (three drops of honey rolled in a sycamore leaf)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: fey pranksters
Subschool: Summoning
:::

You summon intangible forces of whimsy to perform a variety of tricks and pranks upon your foes.
Each round on your turn (including the round you cast this spell), these incorporeal pranksters
perform a single dirty trick, disarm, steal, or trip combat maneuver against one of your foes within
the spell's range. The whimsical forces have a bonus on combat maneuver checks equal to your caster
level + your primary spellcasting ability score modifier (Intelligence for wizards, Charisma for
sorcerers, etc.). Unless the target of the combat maneuver can see invisible creatures or forces,
the spell gains an additional +4 bonus on combat maneuver checks.

The whimsical forces choose a random foe to target with their pranks on and randomly determine which
combat maneuver to use. You can attempt to convince them to take a particular course of action with
a DC 20 Bluff, Diplomacy, or Intimidate check as a standard action. If successful, you determine
their target and the type of combat maneuver they use for that round.
