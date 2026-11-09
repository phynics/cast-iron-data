+++
id = "ref/spell/forbid-action"
kind = "spell"
title = "Forbid Action"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forbid_action", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "220"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Cleric, Inquisitor, Mesmerist, Occultist, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

You forbid the target a single course of action, which it avoids to the best of its ability. You may
demand the target not take actions that fall into one of the following options.

_Attack:_ The target cannot take any action that involves an attack roll, or uses a spell or ability
that targets a foe or an area that includes a foe.

_Cast:_ Target cannot cast spells or use [spell-like abilities](ref/umr/spell-like-abilities).

_Communicate:_ The target cannot take any actions that allow it to communicate with anyone. This
includes such acts as speaking, Bluff checks to pass secret messages, writing, and using telepathy.
It does not prevent verbalizations made for purposes other than communication, such as command words
or the verbal component of spellcasting.

_Draw:_ Target cannot ready or prepare any item, weapon, component, or equipment.

_Move:_ The target can take no act that would cause it to end up in a different location. The target
does not resist being moved by others (and thus can be picked up or dragged, or can float along on a
raft), but does not consciously attempt to move (including not directing a mount to move).

The target is free to take any actions not forbidden by the caster. For example, a target affected
by this spell's demand to not move is still free to cast spells, make attacks, or shout for help.
