+++
id = "ref/spell/spellcrash-greater"
kind = "spell"
title = "Greater Spellcrash"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellcrash_greater", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates; see text
Spell resistance: yes
Target: one creature
:::

## Lesser Spellcrash

**Sources:** Advanced Class Guide pg 194

You create a discordant blast of energy that disrupts the target's available magic each round at the
start of its turn.

If the target prepares spells, it must choose one of its prepared 3rd-level spells, which is
immediately lost; if the target has no 3rd-level spells prepared, it must lose a 2nd-level spell it
has prepared (progressing down to 1st-level spell if it has no 2nd-level spells prepared).

If the target is a spontaneous spellcaster, it loses one of its available 3rd-level spell slots; if
the target has no available 3rd-level spell slots, it must lose a 2nd-level spell slot (progressing
down to 1st-level spell if it has no 2nd-level spell slots available).

There is no initial saving throw for this spell, but the target can attempt a Will saving throw each
round at the end of its turn.

If the target has more than one spellcasting class, choose one at random to be affected. This spell
has no effect on [spell-like abilities](ref/umr/spell-like-abilities).

Any spell or spell slot lost because of this spell is treated as if the caster had failed a
[concentration](ref/rule/concentration) check while trying to cast it - the spell or spell slot is
wasted and has no effect, but is recovered normally the next time the character prepares spells or
regains spell slots.

### Spellcrash

**Sources:** Advanced Class Guide pg 193

This spell functions as lesser spellcrash, except that it affects 5th-level or lower prepared spells
or spell slots.

### Greater Spellcrash

**Sources:** Advanced Class Guide pg 194

This spell functions as lesser spellcrash, except that it affects 7th-level or lower prepared spells
or spell slots.
