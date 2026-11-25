+++
id = "ref/spell/secret-vault"
kind = "spell"
title = "Secret Vault"
aon = "SpellDisplay.aspx?ItemName=Secret%20Vault"
source_ids = ["black-markets", "heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secret_vault", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/secret-chest" },
]
[[sources]]
publication = "black-markets"
page = "31"
[[sources]]
publication = "heroes-of-the-streets"
page = "31"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "10 minutes"
components = "V, S, F (the chest and its replica)"
range = "see text"
effects = [
  { label = "Target", value = "one chamber and up to 10 cu. ft. of goods/caster level" },
]
duration = "60 days or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 8: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (the chest and its replica)
Range: see text
Duration: 60 days or until discharged
Saving throw: none
Spell resistance: no
Target: one chamber and up to 10 cu. ft. of goods/caster level
Subschool: Summoning
:::

### Secret Vault

This spell functions like [secret chest](ref/spell/secret-chest), except it affects a small
structure, vault, or oversized chest. Living creatures within a secret vault don't cause the spell
to fail. While the vault is stored on the Ethereal Plane, living creatures within the vault don't
need to eat, drink, or breathe, but they can't leave the vault except via magic such as plane shift.
The vault used as a focus for secret vault must cost at least 25,000 gp, and its replica costs 250
gp. A secret vault has only a 1% cumulative chance per day of becoming irretrievably lost after 360
days.
