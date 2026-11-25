+++
id = "ref/arc-paladin/scion-of-talmandor"
kind = "archetype"
title = "Scion of Talmandor"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Scion%20of%20Talmandor"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scion_of_talmandor", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "adventurers-guide"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "scion-s-faith" },
  { anchor = "egalitarian", level = 2 },
  { anchor = "bonded-eagle", level = 5 },
  { anchor = "consensus", level = 8 },
  { anchor = "talmandor-s-gift", level = 11 },
]
trades = [
  { replaces = "Divine bond", feature = "divine-bond", by = ["bonded-eagle"] },
  { replaces = "Aura of resolve", feature = "aura-of-resolve", by = ["consensus"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["talmandor-s-gift"] },
  { alters = "Divine grace", feature = "divine-grace", by = ["egalitarian"] },
]
+++

While all Steel Falcons are peerless proponents of the rights of the downtrodden, those who endeavor
to make the spread of liberty as peaceful as possible often become scions of Talmandor, honoring the
powerful avoral agathion who serves as the patron of the Steel Falcons. Talmandor is reluctant to
act directly on behalf of the [Eagle Knights](ref/rule/aff-vangard) and even more unwilling to
accept their worship, preferring to lend assistance primarily by being a voice of reason and
dispensing wise counsel when it is most needed. A scion of Talmandor attempts to exemplify this
selfless altruism, offering assistance to the oppressed and facilitating the peaceful transfer of
power from the few to the many.

Scions of Talmandor look to the brutality of the revolution in Galt, Andoran's neighbor, as a
cautionary tale and an unfortunate blemish on populism's short history. They also reject the
Nirmathi notion of freedom, thinking it too individualistic; instead, they strive to build strong
communities both at home and abroad. Wherever possible, a scion of Talmandor opts for peaceful,
grassroots solutions to problems facing the many oppressed peoples of the Inner Sea region,
encouraging them to take a central role in bettering their lot in life.

## Scion's Faith (Ex) {#scion-s-faith}

A scion of Talmandor must worship a lawful good deity, and she gains Fly as a class skill instead of
Ride.

This alters class skills.

## Egalitarian (Su) {#egalitarian}

At 2nd level, once per day as a swift action, a scion of Talmandor can halve her bonus on saving
throws from divine grace (minimum +1) to grant the resulting bonus to herself and to all allies
within 30 feet. This shared bonus lasts for a number of rounds equal to the scion's Charisma
modifier, after which her divine grace is suppressed for 1 hour before returning to normal.

This ability alters divine grace.

## Bonded Eagle (Sp) {#bonded-eagle}

At 5th level, a scion of Talmandor forms a bond with an [eagle](ref/companion/bird) using the
statistics for a bird [animal companion](ref/sidekick/animal-companion). The eagle is a loyal
companion that accompanies the scion on her adventures. When the scion activates smite evil, she can
expend an additional use of smite evil to grant her eagle the bonuses granted from smite evil as
well. This ability functions like the druid animal companion ability, using the scion's paladin
level as her effective druid level.

This ability replaces divine bond.

## Consensus (Ex) {#consensus}

At 8th level, twice per day as a swift action during the first full round of combat, a scion of
Talmandor can take a vote from a number of allies equal to or less than 3 + the scion's Charisma
modifier, all of whom must be within 30 feet of the scion of Talmandor. In initiative order, each
ally can vote for Freedom, Justice, or Responsibility. Allies who vote receive a +2 sacred bonus
either on attack rolls (if Justice wins), on saving throws (if Freedom wins), or to Armor Class (if
Responsibility wins) until the end of combat. The scion of Talmandor votes last, and in the case of
a tie, her vote breaks the tie.

This ability replaces aura of resolve.

## Talmandor's Gift (Sp) {#talmandor-s-gift}

At 11th level, a scion of Talmandor can summon an [avoral agathion](ref/monster/agathion-avoral) as
if via _[summon monster VII](ref/spell/summon-monster-7)_ (caster level equals the scion's character
level).

This ability replaces aura of justice.
