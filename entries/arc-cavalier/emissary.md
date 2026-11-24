+++
id = "ref/arc-cavalier/emissary"
kind = "archetype"
title = "Emissary"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Emissary"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "emissary", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-combat"
page = "36"

[fields]
kind = "archetype"
features = [
  { anchor = "armor-proficiency" },
  { anchor = "in-or-out-of-the-saddle", level = 1 },
  { anchor = "battlefield-agility", level = 5 },
  { anchor = "mounted-acrobatics", level = 9 },
  { anchor = "mounted-dervish", level = 14 },
  { anchor = "erratic-charge", level = 20 },
]
trades = [
  { replaces = "Tactician", feature = "tactician", by = ["in-or-out-of-the-saddle"] },
  { replaces = "Banner", feature = "banner", by = ["battlefield-agility"] },
  { replaces = "Greater tactician", feature = "greater-tactician", by = ["mounted-acrobatics"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["mounted-dervish"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["erratic-charge"] },
]
+++

Cavaliers serve many roles on the battlefield, from bold leaders and shock troops to dashing knights
and mounted juggernauts. Some cavaliers, however, focus more on speed and mobility than they do on
the raw power of the mounted charge. On foot or in the saddle, the emissary is usually first to meet
the enemy, with a pointed lance, a drawn sword, or terms for surrender.

## Armor Proficiency {#armor-proficiency}

An emissary does not gain proficiency with heavy armor.

## Bonus Feats {#bonus-feats}

An emissary can select [Endurance](ref/feat/endurance), [Fleet](ref/feat/fleet), or
[Run](ref/feat/run) in addition to the list of combat feats whenever he gains a bonus feat.

## In or Out of the Saddle (Ex) {#in-or-out-of-the-saddle}

At 1st level, an emissary gains [Mounted Combat](ref/feat/mounted-combat) as a bonus feat. In
addition, he can move at normal speed when wearing medium armor. This ability replaces tactician.

## Battlefield Agility (Ex) {#battlefield-agility}

At 5th level, an emissary learns to be more aware of the threats that surround him in combat, and
shares this awareness with his loyal steed. Both the emissary and his mount gain
[Mobility](ref/feat/mobility) as a bonus feat. This ability replaces banner.

## Mounted Acrobatics (Ex) {#mounted-acrobatics}

At 9th level, an emissary is even more adept at hopping on and off his steed, and even dropping
alongside its flanks mid-gallop. He gains [Trick Riding](ref/feat/trick-riding) as a bonus feat,
even if he does not meet the prerequisites. The emissary can employ this feat even when wearing
medium armor. This ability replaces greater tactician.

## Mounted Dervish (Ex) {#mounted-dervish}

At 14th level, an emissary becomes a fearsome, mobile foe on the battlefield. He gains
[Mounted Skirmisher](ref/feat/mounted-skirmisher) as a bonus feat, even if he does not meet the
prerequisites. In addition, whenever the emissary is mounted and takes the [charge](ref/rule/charge)
action, he adds 10 feet to his mount's speed. This ability replaces greater banner.

## Erratic Charge (Ex) {#erratic-charge}

At 20th level, an emissary learns to ride through the thick of combat, striking and then moving away
with blinding speed. Whenever the emissary is mounted and takes the [charge](ref/rule/charge)
action, he can first move 10 feet and make a melee attack. This first attack is not a charge, but a
regular melee attack, and the movement counts toward the total allowed movement for the round. After
making this attack, the emissary must still move in a straight line to reach the target of his
charge, and he takes a -5 penalty on the attack roll for the attack at the end of his charge. This
ability replaces supreme charge.
