+++
id = "ref/spell/spellsteal"
kind = "spell"
title = "Spellsteal"
aon = "SpellDisplay.aspx?ItemName=Spellsteal"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellsteal", path = "json/spells9.json" },
]
[[sources]]
publication = "monster-codex"
page = "200"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous and see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous and see text
Saving throw: Will negates
Spell resistance: yes
Target: one creature
:::

You create a discordant blast of energy that disrupts the target's available magic and transfers
knowledge of that magic to you.

If the target prepares spells, it must choose one of its prepared 3rd-level spells, which is
immediately lost. If the target has no 3rd-level spells prepared, it loses a 2nd-level spell it has
prepared. This progresses down to a 1st-level spell if the target has no 2nd-level spells prepared,
and this spell has no effect if the target also has no 1st-level spells prepared. If the spell is on
your spell list, you can cast this lost spell (using your caster level) on your next turn.

If the target is a spontaneous spellcaster, it loses one of its available 3rd-level spell slots. If
the target has no available 3rd-level spell slots, it must lose a 2nd-level spell slot (progressing
as above). Randomly select one of the target's spells known of that spell level; if that spell is on
your spell list, you can cast it (using your caster level) on your next turn.

You must provide any focus or material components to cast the stolen spell.

If the target has more than one spellcasting class, choose one at random to be affected. This spell
has no effect on [spell-like abilities](ref/umr/spell-like-abilities).

Any spell or spell slot lost because of this spell is treated as if the caster had failed a
[concentration](ref/rule/concentration) check while trying to cast - the spell or spell slot is
wasted and has no effect, but it is recovered normally the next time the character prepares spells
or regains spell slots.
