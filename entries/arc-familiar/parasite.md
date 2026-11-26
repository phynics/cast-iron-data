+++
id = "ref/arc-familiar/parasite"
kind = "archetype"
title = "Parasite"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "parasite", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "wilderness-origins"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "infest" },
  { anchor = "puppeteer", level = 3 },
]
trades = [
  { replaces = "Improved evasion", by = ["infest"] },
  { replaces = "share spells", by = ["infest"] },
  { replaces = "Deliver touch spells", by = ["puppeteer"] },
  { replaces = "speak with animals of its kind", by = ["puppeteer"] },
  { replaces = "spell resistance", by = ["puppeteer"] },
  { replaces = "scry on familiar", by = ["puppeteer"] },
]
+++

Most familiars are still something akin to normal animals, conduits for power rather than powers
themselves. The parasite is one of the more disturbing exceptions.

## Infest (Su) {#infest}

As a full-round action, a parasite can infest a willing or helpless target at least two size
categories larger than the parasite. This deals 1d6 points of
[Constitution damage](ref/rule/ability-damage-drain) as the parasite burrows through viscera before
attaching itself to the target's brain or spinal cord (or equivalent). There, the parasite curls up,
with no ability to see or hear anything itself, but with access to its host's senses.

Despite the gaping wound, this process is curiously painless. Assuming that the location of the
wound and the resultant blood is not obvious (most parasites infest from the back for this reason),
the victim must succeed at a Heal or Sense Motive check opposed by the familiar's Bluff check to
notice that something is amiss.

Removing a parasite requires a successful Heal check opposed by the familiar's Stealth check, or a
successful casting of _[break enchantment](ref/spell/break-enchantment)_ against a DC of 11 + the
parasite's level. If successful, the parasite is destroyed. The parasite can leave the host
willingly as a full-round action.

If the host is killed, the parasite must succeed at a DC 20 Fortitude save or be killed as well.

This replaces improved evasion and share spells.

## Puppeteer (Sp) {#puppeteer}

Beginning at 3rd level, the parasite can attempt to control its host once per day. This functions as
_[suggestion](ref/spell/suggestion)_. At 7th level, the parasite can use this ability to replicate
_[dominate person](ref/spell/dominate-person)_ instead. At 15th level, the parasite can replicate
_[dominate monster](ref/spell/dominate-monster)_. The DC for this ability is calculated as if the
parasite's master had cast the spell (defaulting to Charisma if the owner has no spellcasting
ability).

This replaces deliver touch spells, speak with animals of its kind,
[spell resistance](ref/rule/spell-resistance), and scry on familiar.
