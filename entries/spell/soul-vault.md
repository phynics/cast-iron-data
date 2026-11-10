+++
id = "ref/spell/soul-vault"
kind = "spell"
title = "Soul Vault"
aon = "SpellDisplay.aspx?ItemName=Soul%20Vault"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_vault", path = "json/spells9.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "33"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Spiritualist\
3: Cleric, Inquisitor, Oracle, Warpriest\
4: Arcanist, Druid, Hunter, Shaman, Sorcerer, Witch, Wizard\
5: Psychic
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: creature touched
:::

This spell protects the target's soul by briefly enveloping the target in an ethereal vault. The
target gains a +4 bonus on saving throws against spells and effects that would trap or redirect its
soul (such as magic jar, soul bind, and trap the soul) and effects that would transform the target
into an undead creature. The target is granted a save to negate such effects even if one is not
normally allowed. If it's cast on a living creature that then dies, the target's body and spirit are
protected by the spell for its duration. If it's cast on a corpse within 1 round of death, the
target's body and soul are both protected. Otherwise, only the body receives the protection.

Any spellcaster that worships Abadar may learn and cast soul vault as a 4th level spell, if it isn't
normally on her class spell list. Soul vault can be made permanent with the
[permanency](ref/spell/permanency) spell at a cost of 7,500 gp and a minimum caster level of 11th.
