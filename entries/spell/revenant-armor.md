+++
id = "ref/spell/revenant-armor"
kind = "spell"
title = "Revenant Armor"
aon = "SpellDisplay.aspx?ItemName=Revenant%20Armor"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "revenant_armor", path = "json/spells8.json" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "23"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (one suit of armor)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one suit of armor" },
]
duration = "1 day/level or 1 hour/level; see below"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Antipaladin, Paladin, Shaman, Spiritualist, Witch\
4: Arcanist, Cleric, Magus, Medium, Occultist, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, F (one suit of armor)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level or 1 hour/level; see below
Saving throw: none
Spell resistance: no
Target: one suit of armor
:::

This spell endows a suit of armor with a singular purpose realized only after its wearer goes
unconscious or is killed; whenever the wearer of a suit of armor warded by revenant armor is brought
below 0 hit points or otherwise rendered unconscious (but not paralyzed or held) in combat, the
armor is immediately brought to life as a Medium animated object. This animated suit of armor still
contains the unconscious (or dead) body of its former wearer and moves with a shambling gait at a
speed of 20 feet. This animated object has average hit points and, if the armor is made from metal,
it has the metal animated object extraordinary ability (plus
[additional abilities](ref/monster/animated-object) based on the type of metal). Once animated, the
revenant armor remains standing (and stands if knocked prone, doing so without provoking attacks of
opportunity), and prevents the wearer of the armor from being considered helpless. If an ally of the
wearer is within range of the armor, she can direct it to move, though it refuses to go anywhere
that requires a skill check. If grappled or otherwise restrained, it can attempt to break free with
a Strength score equal to your caster level and a CMB equal to 1 + your caster level + the armor's
Strength modifier. If the armor's wearer is reduced to dust, made conscious, or removed from the
armor, the spell ends.
