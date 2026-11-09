+++
id = "ref/spell/magic-aura-greater"
kind = "spell"
title = "Greater Magic Aura"
source_ids = ["core-rulebook", "ultimate-intrigue", "adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_aura_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-aura" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "219"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (a woolen handkerchief)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature, or one object weighting up to 20 lbs./level" },
]
duration = "1 day/level (D)"
saving_throw = "none; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Mesmerist, Occultist, Skald\
4: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a woolen handkerchief)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature, or one object weighting up to 20 lbs./level
Duration: 1 day/level (D)
Saving throw: none; see text
Spell resistance: no
Subschool: Glamer
Descriptors: glamer
:::

### Greater Magic Aura

If cast on an object, this spell functions as [magic aura](ref/spell/magic-aura), except that if you
have identified the unique spellcasting signatures of a specific individual with
[greater detect magic](ref/spell/detect-magic-greater) or a similar spell, you can make the magic
aura appear to have been created by that individual. Alternatively, you can simply obscure all
identifiers, making it more difficult to determine who cast the spell. In either case, if the object
is the subject of a greater detect magic spell, any Spellcraft check made to identify the unique
spellcasting identifiers of the aura automatically produce the result you chose unless the observer
disbelieves the spell with a successful Will save (as with magic aura, however, detect spells don't
grant a save to disbelieve).

If cast on a creature, you can make that creature register to detect spells (and spells with similar
capabilities) as though it were the subject of any number of spells that you specify, when the spell
is cast. Alternatively, you can make the creature register as nonmagical, hiding all spell effects
that he is currently affected by from such scrutiny. If you choose to make the creature register as
being the subject of one or more spells, you can also alter the unique spellcasting identifiers of
those spell auras, in the same fashion as described for objects.

If the target is a creature, you can also alter how the creature registers to arcane sight, making
the creature appear to have or not have spellcasting or
[spell-like abilities](ref/umr/spell-like-abilities), whether those abilities are arcane, divine, or
psychic in nature, and the strength of the most powerful spell or spell-like ability they currently
have available for use. Similarly, you can alter the way the target appears when viewed with greater
detect magic, causing the last spell that he cast to seem to be any spell of your choice.
