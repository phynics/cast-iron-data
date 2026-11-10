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
replaces = ["Hexes gained at 4th and 12th levels", "Hex gained at 8th level", "Hex gained at 10th level"]
+++

The witch doctor is a healer who specializes in afflictions of the soul. Often misunderstood, she
protects her tribe with healing powers, powerful defensive magic, and her own divine "witchcraft."

**Prerequisites:** Nonevil alignment

**Channel Energy (Su)**

**Ability:** The witch doctor can draw transcendental energies to her location, flooding it with
positive energy as the cleric class feature. The witch doctor uses her shaman level - 3 as her
effective cleric level. This is a separate pool of _channel energy_ that does not stack with the
[life](ref/shamanspirit/life) spirit's _channel spirit_ ability.

**Gained:** At 4th Level

**Replaces:** Hexes gained at 4th and 12th levels

**Usage:** Charisma3 modifier times/day

**Counter Curse (Su)**

**Ability:** The witch doctor can choose to lose any prepared _spirit magic_ spell that is 3rd level
or higher in order to spontaneously cast [dispel magic](ref/spell/dispel-magic) or
[remove curse](ref/spell/remove-curse). This ability can only target a spell effect that is on an
ally (including herself).

**Gained:** At 8th Level

**Replaces:** Hex gained at 8th level

**Special:** If she forfeits a _spirit magic_ spell higher than 3rd level, she gains a +2 sacred
bonus on her caster level check to dispel the spell or to remove the curse for every spell level
higher than 3rd that she sacrifices.

**Countering Hex (Su)**

**Ability:** The witch doctor can use her hex magic to [counterspell](ref/rule/counterspells) as a
[readied action](ref/rule/ready) as dispel magic instead. She must succeed at a dispel check (1d20 +
her shaman level) with a DC equal to 11 + the spell's caster level. If _countering hex_ succeeds,
the spell fizzles away and is lost. Failure means the spell is not countered. In either case, the
witch doctor cannot attempt to use this hex against any of that caster's spells again for 24 hours.

**Gained:** At 10th Level

**Replaces:** Hex gained at 10th level

**Special:** The witch doctor cannot use _countering hex_ on an ongoing effect, a magic item, or a
hex.
