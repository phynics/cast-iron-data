+++
id = "ref/spell/puzzle-box"
kind = "spell"
title = "Puzzle Box"
aon = "SpellDisplay.aspx?ItemName=Puzzle%20Box"
source_ids = ["inner-sea-monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "puzzle_box", path = "json/spells15.json" },
]
[[sources]]
publication = "inner-sea-monster-codex"
page = "41"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or one object up to 5 lbs./level" },
]
duration = "1 round/level or permanent; see text"
saving_throw = "Will negates or none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Skald\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or permanent; see text
Saving throw: Will negates or none
Spell resistance: yes
Target: one creature or one object up to 5 lbs./level
Subschool: Compulsion
Descriptors: curse, mind-affecting
:::

This spell causes even commonly used objects to become conundrums. When cast on a creature, the
target loses all weapon and shield proficiencies. The target also forgets how to use all
[spell-completion](ref/misc/spell-completion), [spell-trigger](ref/misc/spell-trigger), and
use-activated magic items, as well as any mundane items used as part of a skill check, imposing a -5
penalty on all ability and skill checks attempted with such items. These effects last for 1 round
per level. As a move action, the target can attempt a skill check to negate the effects of this
spell for one object. Weapons, shields, and mundane objects require a successful Craft skill check
of the type required to craft the item in question, with a DC equal to the spell's save DC. Magic
items require a successful Spellcraft or Use Magic Device skill check against the spell's save DC.

Alternatively, this spell can be cast on a single touched object that weighs up to 5 pounds per the
caster's level. Use of this object becomes a puzzle even to those previously familiar with it. Any
creature attempting to use an item affected in this way is treated as though the creature was the
target of puzzle box for that item only. When cast on an object, the duration of this spell is
permanent.
