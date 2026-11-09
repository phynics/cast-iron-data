+++
id = "ref/spell/mages-faithful-hound"
kind = "spell"
title = "Mage's Faithful Hound"
aon = "SpellDisplay.aspx?ItemName=Mage%27s%20Faithful%20Hound"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mages_faithful_hound", path = "json/spells6.json" },
]
[[sources]]
publication = "core-rulebook"
page = "306"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a tiny silver whistle, a piece of bone, and a thread)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "phantom watchdog" },
]
duration = "1 hour/caster level or until discharged, then 1 round/caster level; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Summoner\
5: Arcanist, Sorcerer, Spiritualist, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a tiny silver whistle, a piece of bone, and a thread)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/caster level or until discharged, then 1 round/caster level; see text
Saving throw: none
Spell resistance: no
Effect: phantom watchdog
Subschool: Creation
:::

You conjure up a phantom watchdog that is invisible to everyone but yourself. It then guards the
area where it was conjured (it does not move). The hound immediately starts barking loudly if any
Small or larger creature approaches within 30 feet of it. (Those within 30 feet of the hound when it
is conjured may move about in the area, but if they leave and return, they activate the barking.)
The hound sees invisible and ethereal creatures. It does not react to figments, but it does react to
shadow illusions.

If an intruder approaches to within 5 feet of the hound, the dog stops barking and delivers a
vicious bite (+10 attack bonus, 2d6+3 points of piercing damage) once per round. The dog also gets
the bonuses appropriate to an invisible creature (see [invisibility](ref/rule/invisibility)).

The dog is considered ready to bite intruders, so it delivers its first bite on the intruder's turn.
Its bite is the equivalent of a magic weapon for the purpose of
[damage reduction](ref/rule/damage-reduction). The hound cannot be attacked, but it can be
dispelled.

The spell lasts for 1 hour per caster level, but once the hound begins barking, it lasts only 1
round per caster level. If you are ever more than 100 feet distant from the hound, the spell ends.
