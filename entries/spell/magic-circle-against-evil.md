+++
id = "ref/spell/magic-circle-against-evil"
kind = "spell"
title = "Magic Circle Against Evil"
aon = "SpellDisplay.aspx?ItemName=Magic%20Circle%20against%20Evil"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_circle_against_evil", path = "json/spells6.json" },
]
[[sources]]
publication = "core-rulebook"
page = "308"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a 3-ft.-diameter circle of powdered silver)"
range = "touch"
effects = [
  { label = "Area", value = "10-ft.-radius emanation from touched creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no; see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Cleric, Inquisitor, Medium, Occultist, Oracle, Paladin, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a 3-ft.-diameter circle of powdered silver)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no; see text
Area: 10-ft.-radius emanation from touched creature
Descriptors: good
:::

All creatures within the area gain the effects of a
[protection from evil](ref/spell/protection-from-evil) spell, and evil summoned creatures cannot
enter the area either. Creatures in the area, or who later enter the area, receive only one attempt
to suppress effects that are controlling them. If successful, such effects are suppressed as long as
they remain in the area. Creatures that leave the area and come back are not protected. You must
overcome a creature's [spell resistance](ref/rule/spell-resistance) in order to keep it at bay (as
in the third function of protection from evil), but the deflection and resistance bonuses and the
protection from mental control apply regardless of enemies' spell resistance.

This spell has an alternative version that you may choose when casting it. A _magic circle against
evil_ can be focused inward rather than outward. When focused inward, the spell binds a nongood
called creature (such as those called by the
[lesser planar binding](ref/spell/planar-binding-lesser),
[planar binding](ref/spell/planar-binding), and
[greater planar binding](ref/spell/planar-binding-greater) spells) for a maximum of 24 hours per
caster level, provided that you cast the spell that calls the creature within 1 round of casting the
_[magic circle](ref/spell/magic-circle)._ The creature cannot cross the circle's boundaries. If a
creature too large to fit into the spell's area is the subject of the spell, the spell acts as a
normal protection from evil spell for that creature only.

A _[magic circle](ref/spell/magic-circle)_ leaves much to be desired as a trap. If the circle of
powdered silver laid down in the process of spellcasting is broken, the effect immediately ends. The
trapped creature can do nothing that disturbs the circle, directly or indirectly, but other
creatures can. If the called creature has [spell resistance](ref/rule/spell-resistance), it can test
the trap once a day. If you fail to overcome its spell resistance, the creature breaks free,
destroying the circle. A creature capable of any form of dimensional travel (astral projection,
blink, dimension door, etherealness, gate, plane shift, shadow walk, teleport, and similar
abilities) can simply leave the circle through such means. You can prevent the creature's
extradimensional escape by casting a dimensional anchor spell on it, but you must cast the spell
before the creature acts. If you are successful, the anchor effect lasts as long as the
_[magic circle](ref/spell/magic-circle)_ does. The creature cannot reach across the
_[magic circle](ref/spell/magic-circle),_ but its ranged attacks (ranged weapons, spells, magical
abilities, and the like) can. The creature can attack any target it can reach with its ranged
attacks except for the circle itself.

You can add a special diagram (a two-dimensional bounded figure with no gaps along its
circumference, augmented with various magical sigils) to make the
_[magic circle](ref/spell/magic-circle)_ more secure. Drawing the diagram by hand takes 10 minutes
and requires a DC 20 Spellcraft check. You do not know the result of this check. If the check fails,
the diagram is ineffective. You can take 10 when drawing the diagram if you are under no particular
time pressure to complete the task. This task also takes 10 full minutes. If time is no factor at
all, and you devote 3 hours and 20 minutes to the task, you can take 20.

A successful diagram allows you to cast a dimensional anchor spell on the
_[magic circle](ref/spell/magic-circle)_ during the round before casting any summoning spell. The
anchor holds any called creatures in the _[magic circle](ref/spell/magic-circle)_ for 24 hours per
caster level. A creature cannot use its [spell resistance](ref/rule/spell-resistance) against a
_[magic circle](ref/spell/magic-circle)_ prepared with a diagram, and none of its abilities or
attacks can cross the diagram. If the creature tries a Charisma check to break free of the trap (see
the _[lesser planar binding](ref/spell/planar-binding-lesser)_ spell), the DC increases by 5. The
creature is immediately released if anything disturbs the diagram - even a straw laid across it. The
creature itself cannot disturb the diagram either directly or indirectly, as noted above.

This spell is not cumulative with [protection from evil](ref/spell/protection-from-evil) and vice
versa.
