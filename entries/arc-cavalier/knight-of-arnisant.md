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
replaces = ["Tactician", "Expert trainer", "Greater tactician", "Demanding challenge", "Greater tactician"]
alters = ["Banner"]
replaces_features = ["tactician", "expert-trainer", "greater-tactician", "demanding-challenge", "greater-tactician"]
alters_features = ["banner"]
+++

The cavaliers known as knights of Arnisant revere the famous general who was crucial in the defeat
of [the Whispering Tyrant](ref/monster/the-whispering-tyrant), the powerful wizard-king. Knights of
Arnisant call upon Arnisant to grant them protection from evil magic, just as the Shield of Aroden
protected him. Many of these cavaliers further emulate him by joining the
[order of the shield](ref/order/order-of-the-shield). Most knights of Arnisant serve at Lastwall,
where the movement originated, but they can be found everywhere from the general's homeland of
Taldor to the front lines of the Worldwound.

**Shield Expertise**

**Ability:** A knight of Arnisant gains the [Shield Focus](ref/feat/shield-focus) feat as a bonus
feat. His cavalier levels count as fighter levels for the purpose of qualifying for all feats that
list the Shield Focus feat as a prerequisite.

**Gained:** At 1st Level

**Replaces:** Tactician

**Deflective Shield (Ex)**

**Flavor:** A knight of Arnisant specializes in using his shield to deflect attacks.

**Gained:** At 4th Level

**Passive:** He adds a bonus equal to his shield bonus to AC to his touch AC and his CMD, up to a
maximum of [half](ref/misc/fractions-and-rounding) his cavalier level. He does not include any
enhancement bonus he has from a magic shield in this calculation.

**Replaces:** Expert trainer

**Heraldic Banner (Ex)**

**Ability:** A knight of Arnisant uses his shield as a _banner,_ though its benefits apply only to
allies within 30 feet.

**Alters:** Banner

**Gained:** At 5th Level

**Soul Shield (Su)**

**Gained:** At 9th Level

**Passive:** When carrying a shield, a knight of Arnisant adds a bonus equal to his shield bonus to
AC on all saving throws against curse spells and effects, up to a maximum of half his cavalier
level. He does not include any enhancement bonus from a magic shield in this calculation.

**Replaces:** Greater tactician

**Defensive Challenge (Ex)**

**Gained:** At 12th Level

**Passive:** Whenever a knight of Arnisant declares a _challenge,_ his target must pay particular
attention to him. As long as the target is within the threatened area of the cavalier, it takes a -2
penalty on attack rolls against anyone other than the knight of Arnisant.

**Replaces:** Demanding challenge

**Heart Shield (Su)**

**Gained:** At 17th Level

**Passive:** When carrying a shield, a knight of Arnisant adds a bonus equal to his shield bonus to
AC on saving throws against death spells and magical death effects, up to a maximum of half his
cavalier level. He does not include any enhancement bonus from a magic shield in this calculation.

**Replaces:** Greater tactician
