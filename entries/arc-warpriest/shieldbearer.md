+++
id = "ref/arc-warpriest/shieldbearer"
kind = "archetype"
title = "Shieldbearer"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Shieldbearer"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shieldbearer", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "shield-adept", level = 1 },
  { anchor = "sacred-weapon" },
  { anchor = "sacred-shield", level = 4 },
  { anchor = "channel-energy" },
]
trades = [
  { replaces = "Focus weapon", feature = "focus-weapon", by = ["shield-adept"] },
  { alters = "Sacred weapon and also replaces sacred armor", feature = "sacred-weapon", by = ["sacred-weapon"] },
]
+++

Shieldbearers are divine warriors who stand on the front lines of battle, shoulder to shoulder with
the soldiers of their people. The shieldbearer tradition has long been a strong legacy among the
dwarves of the Five Kings Mountains, while many young women throughout the Lands of the Linnorm
Kings and Realm of the Mammoth Lords become shieldbearers known as shield maidens. Shieldbearers
among the Shoanti are often advisors as well as combatants, while in the Mwangi Expanse
shieldbearers are known for defending entire villages from the Gorilla King's minions.

## Shield Adept (Ex) {#shield-adept}

At 1st level, a shieldbearer receives [Improved Shield Bash](ref/feat/improved-shield-bash) as a
bonus feat. When carrying a shield, the shieldbearer adds his shield bonus on
[concentration](ref/rule/concentration) checks to cast defensively.

This ability replaces focus weapon.

## Sacred Weapon (Su) {#sacred-weapon}

A shieldbearer treats shields as sacred weapons (instead of his god's favored weapon), though the
shieldbearer can still designate additional weapons as sacred weapons by selecting them with the
[Weapon Focus](ref/feat/weapon-focus) feat. The shieldbearer's sacred weapon damage applies only to
attacks made with shields. The shieldbearer does not gain the ability to enhance sacred weapons
until 7th level. For every 3 warpriest levels beyond 7th, this bonus increases by 1 (to a maximum of
+5 at 19th level).

This ability alters sacred weapon and also replaces sacred armor.

## Sacred Shield (Su) {#sacred-shield}

At 4th level, a shieldbearer gains the ability to enhance his shield with divine power as a swift
action. This ability functions as the sacred armor ability, except as follows. This power grants the
shield a +1 enhancement bonus (this bonus does not act as an attack or damage bonus when the shield
is used in a shield bash). For every 4 warpriest levels beyond 4th, this bonus increases by 1 (to a
maximum of +5 at 20th level). The shieldbearer can enhance a shield with any of the following armor
special abilities (instead of those listed for sacred armor):
_[arrow deflection](ref/magic-enh/arrow-deflection)_, _[blinding](ref/magic-enh/blinding)_,
_[fortification](ref/magic-enh/fortification)_ (heavy, light, or moderate),
_[reflecting](ref/magic-enh/reflecting)_, and _[spell resistance](ref/magic-enh/spell-resistance)_
(13, 15, 17, and 19).

## Channel Energy (Su) {#channel-energy}

The shieldbearer can channel energy only when carrying a shield, and the ability manifests as a
30-foot-cone burst, rather than as a radius.

This ability modifies channel energy.
