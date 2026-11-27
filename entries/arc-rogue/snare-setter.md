+++
id = "ref/arc-rogue/snare-setter"
kind = "archetype"
title = "Snare Setter"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Snare%20Setter"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "snare_setter", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "kobolds-of-golarion"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "trapper", level = 1 },
  { anchor = "trapsmithing", level = 1 },
  { anchor = "deadly-traps", level = 3 },
  { anchor = "sneak-attack", level = 5 },
  { anchor = "master-snare-setter", level = 20 },
]
trades = [
  { replaces = "Sneak attack (but see below)", feature = "sneak-attack", by = ["trapper"] },
  { replaces = "Trapfinding", feature = "trapfinding", by = ["trapsmithing"] },
  { replaces = "Master strike", feature = "master-strike", by = ["master-snare-setter"] },
]
+++

Deep in darkness, the snare setter constructs his deadly traps and brutal mechanisms to confound and
destroy any who try to invade his domain.

## Trapper (Ex) {#trapper}

At 1st level, a snare setter gains [Learn Ranger Trap](ref/feat/learn-ranger-trap) (see page 24) as
a bonus feat. In addition to the trap granted by this feat, he learns how to construct the
[tripwire](ref/rangertrap/tripwire) trap for free. For the purposes of this feat, he's considered a
ranger of his snare setter level, and uses his Intelligence in place of Wisdom to determine uses per
day and the DC of his ranger traps. Whenever the snare setter could learn a new rogue trick, he may
instead learn a new ranger trap.

This ability replaces sneak attack (but see below).

## Trapsmithing (Ex) {#trapsmithing}

A snare setter gains a bonus on Perception skill checks to detect traps and on Craft (traps) checks
equal to 1/2 his snare setter level. He can use Craft (traps) in place of Disable Device to disarm
traps, including magical traps.

This ability replaces trapfinding.

## Deadly Traps (Ex) {#deadly-traps}

At 3rd level, the snare setter's traps deal an additional 1d6 points of damage on the first round
they're activated. This damage is of the same type the trap normally deals. Traps that don't deal
damage are unaffected by this ability. This additional damage increases by 1d6 points every 4 levels
beyond 3rd (7th, 11th, 15th, and 19th).

## Sneak Attack (Su) {#sneak-attack}

At 5th level, the snare setter gains [sneak attack](ref/ability/sneak-attack) +1d6. This functions
as the rogue ability of the same name, but the damage increases by 1d6 every 4 levels after 5th
(9th, 13th, and 17th).

## Master Snare Setter (Ex) {#master-snare-setter}

At 20th level, the snare setter can attach one of a rogue's master strike effects to a trap he
creates. When the trap is triggered, the subject makes an additional Fortitude save at the same DC
as the trap to avoid this effect. A snare setter can have only one trap affected by this ability
active at any time. He may remove this ability from a trap at any range as a free action.

This ability replaces master strike.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the snare setter archetype: camouflage, cunning trigger, fast
stealth, sniper's eye.
