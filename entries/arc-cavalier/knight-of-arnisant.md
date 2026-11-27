+++
id = "ref/arc-cavalier/knight-of-arnisant"
kind = "archetype"
title = "Knight of Arnisant"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Knight%20of%20Arnisant"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "knight_of_arnisant", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "shield-expertise", level = 1 },
  { anchor = "deflective-shield", level = 4 },
  { anchor = "heraldic-banner", level = 5 },
  { anchor = "soul-shield", level = 9 },
  { anchor = "defensive-challenge", level = 12 },
  { anchor = "heart-shield", level = 17 },
]
trades = [
  { replaces = "Tactician", feature = "tactician", by = ["shield-expertise"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["deflective-shield"] },
  { replaces = "Greater tactician", feature = "greater-tactician", by = ["soul-shield", "heart-shield"] },
  { replaces = "Demanding challenge", feature = "demanding-challenge", by = ["defensive-challenge"] },
  { alters = "Banner", feature = "banner", by = ["heraldic-banner"] },
]
+++

The cavaliers known as knights of Arnisant revere the famous general who was crucial in the defeat
of [the Whispering Tyrant](ref/monster/the-whispering-tyrant), the powerful wizard-king. Knights of
Arnisant call upon Arnisant to grant them protection from evil magic, just as the Shield of Aroden
protected him. Many of these cavaliers further emulate him by joining the
[order of the shield](ref/order/order-of-the-shield). Most knights of Arnisant serve at Lastwall,
where the movement originated, but they can be found everywhere from the general's homeland of
Taldor to the front lines of the Worldwound.

## Shield Expertise {#shield-expertise}

At 1st level, a knight of Arnisant gains the [Shield Focus](ref/feat/shield-focus) feat as a bonus
feat. His cavalier levels count as fighter levels for the purpose of qualifying for all feats that
list the Shield Focus feat as a prerequisite.

This ability replaces tactician.

## Deflective Shield (Ex) {#deflective-shield}

At 4th level, a knight of Arnisant specializes in using his shield to deflect attacks. He adds a
bonus equal to his shield bonus to AC to his touch AC and his CMD, up to a maximum of
[half](ref/misc/fractions-and-rounding) his cavalier level. He does not include any enhancement
bonus he has from a magic shield in this calculation.

This ability replaces expert trainer.

## Heraldic Banner (Ex) {#heraldic-banner}

At 5th level, a knight of Arnisant uses his shield as a banner, though its benefits apply only to
allies within 30 feet.

This ability alters banner.

## Soul Shield (Su) {#soul-shield}

At 9th level, when carrying a shield, a knight of Arnisant adds a bonus equal to his shield bonus to
AC on all saving throws against curse spells and effects, up to a maximum of half his cavalier
level. He does not include any enhancement bonus from a magic shield in this calculation.

This ability replaces greater tactician.

## Defensive Challenge (Ex) {#defensive-challenge}

At 12th level, whenever a knight of Arnisant declares a challenge, his target must pay particular
attention to him. As long as the target is within the threatened area of the cavalier, it takes a -2
penalty on attack rolls against anyone other than the knight of Arnisant.

This ability replaces demanding challenge.

## Heart Shield (Su) {#heart-shield}

At 17th level, when carrying a shield, a knight of Arnisant adds a bonus equal to his shield bonus
to AC on saving throws against death spells and magical death effects, up to a maximum of half his
cavalier level. He does not include any enhancement bonus from a magic shield in this calculation.

This ability replaces greater tactician.
