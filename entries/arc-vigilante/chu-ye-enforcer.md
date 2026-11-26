+++
id = "ref/arc-vigilante/chu-ye-enforcer"
kind = "archetype"
title = "Chu Ye Enforcer"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Chu%20Ye%20Enforcer"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chu_ye_enforcer", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "yokai-heart" },
  { anchor = "oni-mask", level = 1 },
  { anchor = "steel-dictate", level = 1 },
  { anchor = "deceitful-form", level = 4 },
  { anchor = "deadly-horns", level = 6 },
  { anchor = "third-eye", level = 12 },
]
trades = [
  { replaces = "Social talent gained at 1st level", feature = "social-talent", levels = [1], by = ["steel-dictate"] },
  { replaces = "Vigilante talents gained at 4th, 14th, and 18th levels", feature = "vigilante-talent", levels = [4, 14, 18], by = ["deceitful-form"] },
  { replaces = "Vigilante talent gained at 6th level", feature = "vigilante-talent", levels = [6], by = ["deadly-horns"] },
  { replaces = "Vigilante talent gained at 12th level", feature = "vigilante-talent", levels = [12], by = ["third-eye"] },
  { alters = "Dual identity", feature = "dual-identity", by = ["oni-mask"] },
]
+++

In the despotic nation of Chu Ye, merciless [oni](ref/family/oni) oppress the human populace. Some
[humans](ref/race/human) and [tieflings](ref/race/tiefling) with oni blood use the power of the oni
for their own ambitions. Donning terrifying masks, these vigilantes forsake their humanity to become
more like the evil beings they mimic.

## Yokai Heart (Su) {#yokai-heart}

A Chu Ye enforcer seeks to transmute himself into a destructive spirit and terrorize his enemies.
His vigilante identity alignment must be non-good. While in his vigilante identity, the Chu Ye
enforcer gains [darkvision](ref/rule/darkvision) with a range of 60 feet and
[low-light vision](ref/rule/low-light-vision), and he counts as both a native
[outsider](ref/type/outsider) with the [oni](ref/subtype/oni) subtype and his original type for any
effect related to type, whichever is worse for him.

## Oni Mask (Ex) {#oni-mask}

A Chu Ye enforcer gains a grotesque horned mask that he must wear when assuming his vigilante
identity. The mask has 10 hit points per vigilante level he has and [hardness](ref/umr/hardness) 5.
While wearing the mask, the Chu Ye enforcer gains a bonus to Intimidate equal to 1/2 his level
(minimum +1). Without this mask, a Chu Ye enforcer can't assume his vigilante identity. A Chu Ye
enforcer who loses his mask can replace it after 1 day through a specialized ritual that takes 8
hours to complete and costs 200 gp per vigilante level he has.

This alters dual identity.

## Steel Dictate (Ex) {#steel-dictate}

A Chu Ye enforcer gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat,
and when he hits with his unarmed strike, he gains a bonus on damage rolls equal to
[half](ref/misc/fractions-and-rounding) his vigilante level (minimum +1, maximum of +5).

This replaces the social talent gained at 1st level.

## Deceitful Form (Sp) {#deceitful-form}

At 4th level, a Chu Ye enforcer gains the [shapechanger](ref/subtype/shapechanger) subtype and the
ability to change his form, as per _[alter self](ref/spell/alter-self)_, for a number of minutes per
day equal to his vigilante level. These minutes do not need to be consecutive, but they must be
spent in 1-minute increments. At 14th level, he can instead use this ability as per
_[giant form I](ref/spell/giant-form-1)_. At 18th level, he can use this ability as per
_[giant form II](ref/spell/giant-form-2)_.

This replaces the vigilante talents gained at 4th, 14th, and 18th levels.

## Deadly Horns (Ex) {#deadly-horns}

At 6th level, while in his vigilante identity, a Chu Ye enforcer gains a gore attack. This is a
primary [natural attack](ref/umr/natural-attacks) that deals 1d6 points of piercing damage.

This replaces the vigilante talent gained at 6th level.

## Third Eye (Su) {#third-eye}

At 12th level, a Chu Ye enforcer's mask manifests a third eye. As a swift action a number of times
per day equal to his vigilante level, he can launch a beam of fire from the eye as a ranged touch
attack with a range of 180 feet. On a hit, the beam deals 4d6 points of fire damage. At 18th level,
the beam damage increases to 8d6 points of fire damage.

This replaces the vigilante talent gained at 12th level.
