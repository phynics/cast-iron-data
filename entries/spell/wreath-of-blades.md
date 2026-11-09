+++
id = "ref/spell/wreath-of-blades"
kind = "spell"
title = "Wreath of Blades"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wreath_of_blades", path = "json/spells16.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "249"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (four mithral daggers, each worth at least 502 gp each)"
range = "personal"
effects = [
  { label = "Area", value = "5-foot-radius emanation centered on you" },
]
duration = "1 round/level"
saving_throw = "Reflex half (special, see below)"
spell_resistance = "no (special, see below)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Bloodrager, Magus, Occultist\
5: Arcanist, Psychic, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (four mithral daggers, each worth at least 502 gp each)
Range: personal
Duration: 1 round/level
Saving throw: Reflex half (special, see below)
Spell resistance: no (special, see below)
Area: 5-foot-radius emanation centered on you
:::

The daggers serving as focus of this spell take on a deadly sharpness as they animate and spin
around you, creating a 5-foot-radius emanation of spinning mithral blades that moves with you. Any
creature that starts its turn within the area of the spinning blades takes 1d4 points of damage for
every two caster levels (maximum 10d4 at 20th level) and the damage bypasses DR/silver.

Furthermore, the daggers ward off some attacks, in a way similar to the
[warding weapon](ref/spell/warding-weapon) spell. While subject to this spell, you do not provoke
attacks of opportunity for casting spells, even from creatures with the
[Disruptive](ref/feat/disruptive) feat. Creatures with the [Spellbreaker](ref/feat/spellbreaker)
feat can easily bypass this defensive property, though they still take damage from the spell. Your
casting (even failing to cast defensively) still provokes attacks of opportunity from creatures with
that feat.

Lastly, the blades that serve as the focus for this spell can be enchanted for greater effect. When
all of the blades share the same enhancement bonus and special weapon qualities, a creature that is
damaged by this spell is also treated as if hit by one of these weapons. For example, if a
12th-level magus casts this spell using four +1 [frost](ref/magic-enh/frost)
[mithral](ref/eq-material/mithral) daggers as focus, the damage dealt by the blades would be 6d4+1
plus 1d6 cold damage, as long as the daggers were commanded to be sheathed in ice. No matter the
modifications made to the focus weapons, they must always be mithral daggers. No other type of
weapons can serve as a focus for this spell.
