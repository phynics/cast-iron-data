+++
id = "ref/spell/glyph-of-warding"
kind = "spell"
title = "Glyph of Warding"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "glyph_of_warding", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered diamond worth 200 gp)"
range = "touch"
effects = [
  { label = "Target or Area", value = "object touched or up to 5 sq. ft./level" },
]
duration = "permanent until discharged (D)"
saving_throw = "see text"
spell_resistance = "no (object) and yes; see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Cleric, Inquisitor, Oracle, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, M (powdered diamond worth 200 gp)
Range: touch
Duration: permanent until discharged (D)
Saving throw: see text
Spell resistance: no (object) and yes; see text
Target or Area: object touched or up to 5 sq. ft./level
:::

**Sources:** PRPG Core Rulebook pg 290

This powerful inscription harms those who enter, pass, or open the warded area or object. A glyph of
warding can guard a bridge or passage, ward a portal, trap a chest or box, and so on.

You set all of the conditions of the ward. Typically, any creature entering the warded area or
opening the warded object without speaking a password (which you set when casting the spell) is
subject to the magic it stores. Alternatively or in addition to a password trigger, glyphs can be
set according to physical characteristics (such as height or weight) or creature type, subtype, or
kind. Glyphs can also be set with respect to good, evil, law, or chaos, or to pass those of your
religion. They cannot be set according to class, HD, or level. Glyphs respond to invisible creatures
normally but are not triggered by those who travel past them ethereally. Multiple glyphs cannot be
cast on the same area. However, if a cabinet has three different drawers, each can be separately
warded.

When casting the spell, you weave a tracery of faintly glowing lines around the warding sigil. A
glyph can be placed to conform to any shape up to the limitations of your total square footage. When
the spell is completed, the glyph and tracery become nearly invisible.

Glyphs cannot be affected or bypassed by such means as physical or magical probing, though they can
be dispelled. [Mislead](ref/spell/mislead), [polymorph](ref/spell/polymorph), and
[nondetection](ref/spell/nondetection) (and similar magical effects) can fool a glyph, though
nonmagical disguises and the like can't. [Read magic](ref/spell/read-magic) allows you to identify a
glyph of warding with a DC 13 Knowledge (arcana) check. Identifying the glyph does not discharge it
and allows you to know the basic nature of the glyph (version, type of damage caused, what spell is
stored).

_Note:_ Magic traps such as glyph of warding are hard to detect and disable. While any character can
use Perception to find a glyph, only a character with the trapfinding class feature can use Disable
Device to disarm it. The DC in each case is 25 + spell level, or 28 for glyph of warding.

Depending on the version selected, a glyph either blasts the intruder or activates a spell.

_Blast Glyph:_ A blast glyph deals 1d8 points of damage per two caster levels (maximum 5d8) to the
intruder and to all within 5 feet of him or her. This damage is acid, cold, fire, electricity, or
sonic (caster's choice, made at time of casting). Each creature affected can attempt a Reflex save
to take half damage. [Spell resistance](ref/rule/spell-resistance) applies against this effect.

_Spell Glyph:_ You can store any harmful spell of 3rd level or lower that you know. All
level-dependent features of the spell are based on your caster level at the time of casting the
glyph. If the spell has a target, it targets the intruder. If the spell has an area or an amorphous
effect, the area or effect is centered on the intruder. If the spell summons creatures, they appear
as close as possible to the intruder and attack. Saving throws and
[spell resistance](ref/rule/spell-resistance) operate as normal, except that the DC is based on the
level of the spell stored in the glyph.
