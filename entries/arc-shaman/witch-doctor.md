+++
id = "ref/arc-shaman/witch-doctor"
kind = "archetype"
title = "Witch Doctor"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Witch%20Doctor"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "witch_doctor", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "advanced-class-guide"
page = "113"

[fields]
kind = "archetype"
features = [
  { anchor = "channel-energy", level = 4 },
  { anchor = "counter-curse", level = 8 },
  { anchor = "countering-hex", level = 10 },
]
trades = [
  { replaces = "Hexes gained at 4th and 12th levels", feature = "hex", levels = [4, 12], by = ["channel-energy"] },
  { replaces = "Hex gained at 8th level", feature = "hex", levels = [8], by = ["counter-curse"] },
  { replaces = "Hex gained at 10th level", feature = "hex", levels = [10], by = ["countering-hex"] },
]
+++

The witch doctor is a healer who specializes in afflictions of the soul. Often misunderstood, she
protects her tribe with healing powers, powerful defensive magic, and her own divine "witchcraft."

**Prerequisites:** Nonevil alignment

## Alignment {#alignment}

A witch doctor cannot be of evil alignment.

## Channel Energy (Su) {#channel-energy}

At 4th level, the witch doctor can draw transcendental energies to her location, flooding it with
positive energy as the cleric class feature. This is a separate pool of channel energy that does not
stack with the [life](ref/shamanspirit/life) spirit's channel spirit ability. The witch doctor uses
her shaman level - 3 as her effective cleric level, and can channel energy a number of times per day
equal to 3 + her Charisma modifier. This ability replaces the hexes gained at 4th and 12th levels.

## Counter Curse (Su) {#counter-curse}

At 8th level, the witch doctor can choose to lose any prepared spirit magic spell that is 3rd level
or higher in order to spontaneously cast _[dispel magic](ref/spell/dispel-magic)_ or
_[remove curse](ref/spell/remove-curse)_. This ability can only target a spell effect that is on an
ally (including herself). If she forfeits a spirit magic spell higher than 3rd level, she gains a +2
sacred bonus on her caster level check to dispel the spell or to remove the curse for every spell
level higher than 3rd that she sacrifices. This ability replaces the hex gained at 8th level.

## Countering Hex (Su) {#countering-hex}

At 10th level, the witch doctor can use her hex magic to [counterspell](ref/rule/counterspells) as a
[readied action](ref/rule/ready) as _dispel magic_ instead. She must succeed at a dispel check
(1d20 + her shaman level) with a DC equal to 11 + the spell's caster level. If countering hex
succeeds, the spell fizzles away and is lost. Failure means the spell is not countered. In either
case, the witch doctor cannot attempt to use this hex against any of that caster's spells again for
24 hours. The witch doctor cannot use countering hex on an ongoing effect, a magic item, or a hex.
This ability replaces the hex gained at 10th level.
