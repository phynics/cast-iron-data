+++
id = "ref/spell/oath-of-justice"
kind = "spell"
title = "Oath of Justice"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oath_of_justice", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "two creatures touched" },
]
duration = "permanent (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Paladin\
3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: permanent (see text)
Saving throw: none
Spell resistance: no
Target: two creatures touched
:::

**Sources:** Dwarves of Golarion pg 22

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of
> [Kols](ref/faith/kols). For 24 hours after the ritual, the caster may prepare spells of the
> requested deity. The caster may only attune himself to one additional deity at a time._

This spell seals a solemn vow between two creatures. When this spell is cast, the targets must clasp
hands and swear their oath in Kols's name. The spell functions like mark of justice, except as noted
above and rather than being cursed, the oath-breaker gains a mark on the face indicating to all
dwarves who see it that the target has broken a sacred oath, which gives the oath-breaker a -4
penalty to influence dwarves. The mark can be removed as described in the mark of justice spell, or
the other target can forgive the oathbreaker, which causes the mark to vanish.
