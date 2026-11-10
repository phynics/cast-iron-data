+++
id = "ref/spell/detect-magic-greater"
kind = "spell"
title = "Greater Detect Magic"
aon = "SpellDisplay.aspx?ItemName=Detect%20Magic%2C%20Greater"
source_ids = ["core-rulebook", "adventurers-guide", "andoran-spirit-of-liberty", "ultimate-intrigue", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_magic_greater", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-magic" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "212"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Medium, Mesmerist, Occultist, Oracle, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Area: cone-shaped emanation
Duration: concentration, up to 1 min./level (D)
Saving throw: none
Spell resistance: no
:::

### Greater Detect Magic

This spell functions as _[detect magic](ref/spell/detect-magic),_ except that you can glean much
more information from the magical auras that you find, and those auras can be found after a much
greater length of time. You can detect a lingering aura for up to 1 day per caster level you have,
regardless of the aura's original strength.

Additionally, when you use a standard action to concentrate on this spell, you can also study a
creature within the spell's area and attempt a Spellcraft check in order to determine the last spell
that the creature cast by identifying lingering traces that the spell left in the caster's aura. The
DC to identify the spell is equal to 20 + the creature's caster level.

Finally, you are able to locate and analyze the signature flourishes in a magical aura that allow
you to match a spell to the person who cast it. In order to find these identifiers in a spell's
aura, you must spend 1 round focusing on that spell in particular, and succeed at an opposed
Knowledge (arcana) check against the caster (or a Knowledge \[arcana\] check with a DC equal to 15 +
the spell level if the caster wants her work to be identified and emphasizes these unique elements
rather than obscuring them). Once you learn a caster's set of identifiers, you can remember them as
easily as a face or a voice. You can recognize this signature if you succeed at a Spellcraft check
when later identifying a spell to determine whether or not that spell was cast by the same
individual. The spell greater magic aura can obfuscate this information, making it seem that someone
else cast the spell. Greater detect magic grants a saving throw against magic aura (but not greater
magic aura).
