+++
id = "ref/arc-cleric/divine-scourge"
kind = "archetype"
title = "Divine Scourge"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Divine%20Scourge"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_scourge", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "23"

[fields]
kind = "archetype"
replaces = ["Channel energy"]
alters = ["Domains"]
replaces_features = ["channel-energy"]
alters_features = ["domains"]
+++

Some divine servants take on the role of dealing out unique punishments on behalf of their deities,
taking pleasure in carrying out their sacrosanct duties. Such divine scourges are most common among
worshipers of [Abadar](ref/faith/abadar) (meting out punishment to lawbreakers in concert with local
courts), [Calistria](ref/faith/calistria) (punishing those truly deserving of vengeance), and
[Zon-Kuthon](ref/faith/zon-kuthon) (seeing punishment as an applied form of pain and suffering).
Divine scourges make a point of inflicting long-lasting maladies and curses on those deserving of
such fates under the tenets of the scourges' religions.

**Curser (Ex)**

**Ability:** A divine scourge must take the [Curse](ref/domain/luck) subdomain as a domain,
regardless of the actual domains offered by her deity. The divine scourge does not receive a second
domain.

**Alters:** Domains

**Divine Hexes**

**At 11th Level:** She can select a hex from the list above, or instead select from the following
list of major hexes: [agony](ref/hex/agony), [hoarfrost](ref/hex/hoarfrost),
[infected wounds](ref/hex/infected-wounds), [nightmares](ref/hex/nightmares), and
[retribution](ref/hex/retribution).

**At 15th Level:** She selects another hex or major hex.

**At 19th Level:** She selects a fifth hex or major hex.

**At 3rd Level:** A divine scourge can select one of the following hexes from the witch class hex
list: [blight](ref/hex/blight), [cursed wound](ref/hex/cursed-wound), [evil eye](ref/hex/evil-eye),
[misfortune](ref/hex/misfortune), [scar](ref/hex/scar), [slumber](ref/hex/slumber), and
[unnerve beasts](ref/hex/unnerve-beasts).

**At 7th Level:** She selects a second hex from the list above.

**Replaces:** Channel energy

**Special:** The divine scourge uses her Wisdom modifier instead of her Intelligence modifier to
determine the save DCs of her hexes. Any hex that refers to using her Intelligence modifier to
determine its duration or effect instead uses her Charisma modifier for that purpose.
