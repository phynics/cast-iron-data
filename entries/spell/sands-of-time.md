+++
id = "ref/spell/sands-of-time"
kind = "spell"
title = "Sands of Time"
aon = "SpellDisplay.aspx?ItemName=Sands%20of%20Time"
source_ids = ["ultimate-magic", "osirion-land-of-the-pharaohs"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sands_of_time", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "236"
[[sources]]
publication = "osirion-land-of-the-pharaohs"
page = "27"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "touched creature or object" },
]
duration = "10 minutes/level or instantaneous (see text)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Cleric, Occultist, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Witch, Wizard\
4: Shaman
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level or instantaneous (see text)
Saving throw: none
Spell resistance: yes
Target: touched creature or object
:::

You temporarily age the target, immediately advancing it to the next age category. The target
immediately takes the age penalties to Strength, Dexterity, and Constitution for its new age
category, but does not gain the bonuses for that category. A creature whose age is unknown is
treated as if the spell advances it to middle age. Ageless or immortal creatures are immune to this
spell.

If you cast this on an object, construct, or undead creature, it takes 3d6 points of damage + 1
point per caster level (maximum +15) as time weathers and corrodes it. This version of the spell has
an instantaneous duration.
