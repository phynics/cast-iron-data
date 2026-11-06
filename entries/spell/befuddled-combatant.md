+++
id = "ref/spell/befuddled-combatant"
kind = "spell"
title = "Befuddled Combatant"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "befuddled_combatant", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (cooked noodles)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Arcanist, Bard, Mesmerist, Psychic, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (cooked noodles)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: curse, mind-affecting
:::

**Sources:** Healer's Handbook pg 17

As a way to befuddle your target, you fill its mind with all manner of swirling images as well as
baffling and incoherent thoughts, making the target an ineffective combatant and rendering its
spellcasting and other such abilities much more feeble.

For the spell's duration, the DCs of all of the target's spells,
[spell-like abilities](ref/umr/spell-like-abilities), supernatural abilities, and extraordinary
abilities are reduced by 4. Any of its attacks that would deal hit point damage, including its melee
and ranged physical attacks, deal minimum damage for the duration of this spell.

This curse applies only to effects created by the creature while this spell is actively affecting
the target; applying or removing this curse doesn't alter the ongoing damage of effects previously
created by the target (such as an incendiary cloud spell that was cast before the target became
affected by this spell).
