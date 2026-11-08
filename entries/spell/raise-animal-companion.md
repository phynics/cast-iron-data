+++
id = "ref/spell/raise-animal-companion"
kind = "spell"
title = "Raise Animal Companion"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "raise_animal_companion", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/raise-dead" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 6 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 minute"
components = "V, S, DF, M (diamond worth 5,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Adept, Cleric, Oracle, Spiritualist, Warpriest\
6: Shaman, Witch
Casting time: 1 minute
Components: V, S, DF, M (diamond worth 5,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
Subschool: Healing
:::

## Raise Dead

**Sources:** PRPG Core Rulebook pg 329

You restore life to a deceased creature. You can raise a creature that has been dead for no longer
than 1 day per caster level. In addition, the subject's soul must be free and willing to return. If
the subject's soul is not willing to return, the spell does not work; therefore, a subject that
wants to return receives no saving throw.

Coming back from the dead is an ordeal. The subject of the spell gains two permanent negative levels
when it is raised, just as if it had been hit by an energy-draining creature. If the subject is 1st
level, it takes 2 points of Constitution drain instead (if this would reduce its Con to 0 or less,
it can't be raised). A character who died with spells prepared has a 50% chance of losing any given
spell upon being raised. A spellcasting creature that doesn't prepare spells (such as a sorcerer)
has a 50% chance of losing any given unused spell slot as if it had been used to cast a spell.

A raised creature has a number of hit points equal to its current HD. Any ability scores damaged to
0 are raised to 1. Normal poison and normal disease are cured in the process of raising the subject,
but magical diseases and curses are not undone. While the spell closes mortal wounds and repairs
lethal damage of most kinds, the body of the creature to be raised must be whole. Otherwise, missing
parts are still missing when the creature is brought back to life. None of the dead creature's
equipment or possessions are affected in any way by this spell.

A creature who has been turned into an undead creature or killed by a death effect can't be raised
by this spell. Constructs, elementals, outsiders, and undead creatures can't be raised. The spell
cannot bring back a creature that has died of old age.

### Raise Animal Companion

**Sources:** Ultimate Magic pg 233

This spell functions as [raise dead](ref/spell/raise-dead), but it only affects an animal companion,
familiar, or paladin's bonded mount.
