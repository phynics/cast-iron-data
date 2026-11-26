+++
id = "ref/arc-bloodrager/hag-riven"
kind = "archetype"
title = "Hag-Riven"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Hag-Riven"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hag_riven", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-influence" },
  { anchor = "claws-of-the-hag", level = 1 },
  { anchor = "sorcerous-claws", level = 5 },
  { anchor = "scarred-hide", level = 7 },
  { anchor = "hexing-claws", level = 10 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["claws-of-the-hag"] },
  { replaces = "uncanny dodge", feature = "uncanny-dodge", by = ["claws-of-the-hag"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["sorcerous-claws"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["hexing-claws"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies", by = ["arcane-influence"] },
]
+++

All [changelings](ref/race/changeling) have the potential to transform into [hags](ref/family/hag),
but the process is a slow one, requiring several nights to complete. When left incomplete—by virtue
of a wily changeling's escape or her mother's death—the creature is scarred and saturated in
[arcane](ref/blrgbloodline/arcane) power. Though she remains in possession of her own faculties, the
seeds of [hag](ref/blrgbloodline/hag) hatred sprout within her. These hag-riven wield powerful magic
interlaced with more powerful emotions.

The painful rituals that create a [hag](ref/blrgbloodline/hag)-riven can work for any creatures
tenacious enough to endure them, and the art has sprung up as a defense against the devastating
power of [hags](ref/family/hag) in various remote communities.

## Arcane Influence {#arcane-influence}

A hag-riven bloodrager does not gain proficiency with martial weapons and must choose from one of
the following bloodrager bloodlines: arcane, destined, elemental, fey, or hag (see below).

This alters the bloodrager's weapon and armor proficiencies.

## Claws of the Hag (Ex) {#claws-of-the-hag}

A hag-riven grows a pair of vicious claws that are treated as
[natural weapons](ref/rule/natural-attacks). These claws are primary attacks and deal 1d4 points of
damage each (1d3 for a Small creature) plus the hag-riven's Strength modifier. At 2nd level, these
claws are considered magic weapons for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). At 5th level, the damage increases to 1d6 points (1d4
for a Small creature). At 13th level, the hag-riven's claws threaten a critical hit on a natural
roll of 19–20. At 16th level, the damage increases again to 1d8 points (1d6 for a Small creature).

This replaces fast movement and uncanny dodge.

## Sorcerous Claws (Su) {#sorcerous-claws}

At 5th level, a hag-riven can expend one of her daily spell slots as a swift action to grant her
claws an enhancement bonus equal to the level of the spell slot sacrificed. This bonus lasts for 1
minute and stacks with existing enhancement bonuses (such as those provided by
_[magic fang](ref/spell/magic-fang)_ or magic items) to a maximum of +5. Multiple uses of this
ability do not stack with themselves.

Beginning at 7th level, the hag-riven can also expend some or all of the bonus provided by her
sorcerous claws to add any of the following weapon properties to her claws for 1 minute:
_[flaming](ref/magic-enh/flaming)_, _[flaming burst](ref/magic-enh/flaming-burst)_,
_[frost](ref/magic-enh/frost)_, _[icy burst](ref/magic-enh/icy-burst)_,
_[keen](ref/magic-enh/keen)_, _[nullifying](ref/magic-enh/nullifying)_,
_[seaborne](ref/magic-enh/seaborne)_, _[spellstealing](ref/magic-enh/spellstealing)_,
_[shock](ref/magic-enh/shock)_, _[shocking burst](ref/magic-enh/shocking-burst)_, or
_[wounding](ref/magic-enh/wounding)_. Her claws must have a minimum enhancement bonus of +1 before
any special abilities can be added.

This replaces improved uncanny dodge.

## Scarred Hide (Ex) {#scarred-hide}

At 7th level, a hag-riven's scarred flesh becomes thick and leathery. She gains a +1 natural armor
bonus to AC. At 10th, 13th, 16th, and 19th levels, this bonus increases by 1.

## Hexing Claws (Su) {#hexing-claws}

At 10th level, a hag-riven gains [Critical Focus](ref/feat/critical-focus) as a bonus feat, but she
can apply its benefits only to her claw attacks. Each morning, she can select a single feat with
Critical Focus as a prerequisite and apply its benefits to her claw attacks. She must meet all other
prerequisites for any feat she wishes to apply with this ability.

This replaces [damage reduction](ref/rule/damage-reduction).
