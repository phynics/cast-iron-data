+++
id = "ref/spell/secret-vault"
kind = "spell"
title = "Secret Vault"
source_ids = ["core-rulebook", "black-markets", "heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secret_vault", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, F (the chest and its replica)"
range = "see text"
effects = [
  { label = "Target", value = "one chest and up to 1 cu. ft. of goods/caster level" },
]
duration = "60 days or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Mesmerist, Occultist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (the chest and its replica)
Range: see text
Duration: 60 days or until discharged
Saving throw: none
Spell resistance: no
Target: one chest and up to 1 cu. ft. of goods/caster level
Subschool: Summoning
:::

## Secret Chest

**Sources:** PRPG Core Rulebook pg 338

You hide a chest on the Ethereal Plane for as long as 60 days and can retrieve it at will. The chest
can contain up to 1 cubic foot of material per caster level (regardless of the chest's actual size,
which is about 3 feet by 2 feet by 2 feet). If any living creatures are in the chest, there is a 75%
chance that the spell simply fails. Once the chest is hidden, you can retrieve it by concentrating
(a standard action), and it appears next to you.

The chest must be exceptionally well crafted and expensive, constructed for you by master crafters.
The cost of such a chest is never less than 5,000 gp. Once it is constructed, you must make a tiny
replica (of the same materials and perfect in every detail) so that the miniature of the chest
appears to be a perfect copy. (The replica costs 50 gp.) The chests are nonmagical and can be fitted
with locks, wards, and so on, just as any normal chest can be.

To hide the chest, you cast the spell while touching both the chest and the replica. The chest
vanishes into the Ethereal Plane. You need the replica to recall the chest. After 60 days, there is
a cumulative chance of 5% per day that the chest is irretrievably lost. If the miniature of the
chest is lost or destroyed, there is no way, even with a wish spell, that the large chest can be
summoned back, although an extraplanar expedition might be mounted to find it.

Living things in the chest eat, sleep, and age normally, and they die if they run out of food, air,
water, or whatever they need to survive.

### Secret Coffer

**Sources:** Black Markets pg 31, Heroes of the Streets pg 31

This spell functions like secret chest, except the coffer is only 1 foot square and can contain only
1 cubic foot of goods, and the container can remain safely hidden on the Ethereal Plane for only 14
days before it risks becoming lost. The spell automatically fails if a living creature enters the
coffer. The coffer used as a focus for secret coffer must cost at least 500 gp, and its replica
costs 5 gp.

### Secret Vault

**Sources:** Black Markets pg 31

This spell functions like secret chest, except it affects a small structure, vault, or oversized
chest. Living creatures within a secret vault don't cause the spell to fail. While the vault is
stored on the Ethereal Plane, living creatures within the vault don't need to eat, drink, or
breathe, but they can't leave the vault except via magic such as plane shift. The vault used as a
focus for secret vault must cost at least 25,000 gp, and its replica costs 250 gp. A secret vault
has only a 1% cumulative chance per day of becoming irretrievably lost after 360 days.

> _Note: The original source does not mention a change in duration from
> *[secret chest](ref/spell/secret-chest)*, but the text implies a 360-day duration._
