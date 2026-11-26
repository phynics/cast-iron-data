+++
id = "ref/arc-medium/fiend-keeper"
kind = "archetype"
title = "Fiend Keeper"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Fiend%20Keeper"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fiend_keeper", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "evil-spirit" },
  { anchor = "dark-communion", level = 3 },
]
trades = [
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["dark-communion"] },
  { replaces = "location channel", feature = "location-channel", by = ["dark-communion"] },
  { replaces = "connection channel", feature = "connection-channel", by = ["dark-communion"] },
  { replaces = "ask the spirits", feature = "ask-the-spirits", by = ["dark-communion"] },
  { alters = "Spirit", feature = "spirit", by = ["evil-spirit"] },
]
+++

Among the most sacred roles a grippli can play is that of fiend keeper, a vessel to contain one of
the world's evil spirits so that it cannot inflict further harm. As the host performs goodly acts,
he slowly cleanses the spirit, continuing this process over many generations, until the entity's
vileness is no more. In turn, the spirit tempts the fiend keeper with blasphemous power that a
cautious medium can direct toward righteous ends. Many tribes boast a resident fiend keeper who
bears this local burden and trains replacements who might take over when their mentor dies.

## Alignment {#alignment}

A fiend keeper must choose a nonevil alignment.

## Evil Spirit (Su) {#evil-spirit}

A fiend keeper serves as the vessel for a powerful evil spirit that fights and bargains for
dominance. The legends a fiend keeper channels are all aspects of this evil presence. Willingly
performing an evil act automatically grants the evil spirit 1 point of influence over him.
_[Protection from evil](ref/spell/protection-from-evil)_ temporarily suppresses all the spirit's
benefits while the fiend keeper is under the spell's effects. When the spirit gains at least 3
points of influence over the fiend keeper, in addition to the penalties associated with each legend,
he gains an evil aura as per a [cleric](ref/class/cleric) of his level and treats his alignment as
evil for the purposes of resisting or being vulnerable to spells and abilities (such as
_[unholy blight](ref/spell/unholy-blight)_ or a paladin's smite evil class ability).

This ability modifies spirit.

## Dark Communion (Su) {#dark-communion}

At 3rd level, a fiend keeper can entice the evil spirit to lend him its knowledge or its power as a
full-round action a number of times per day equal to his class level. If the fiend keeper seeks
knowledge, this behaves as _[contact other plane](ref/spell/contact-other-plane)_ using his medium
level as his caster level, but if he fails the Intelligence or Charisma check, his spirit gains 1
point of influence over him instead of reducing his ability scores. Treat the spirit as an entity
from the Astral Plane for this ability. Its knowledge is equivalent to that of a demigod at 5th
level, a lesser deity at 7th level, and an intermediate deity at 13th level.

If the fiend keeper requests power, he must instead succeed at an Intelligence or Charisma check (DC
10 at 3rd level, DC 12 at 7th level, or DC 14 at 13th level or higher), or his spirit gains 1 point
of influence over him. Regardless of the outcome, he gains one of the following powers for 1 minute.
At 5th level, he also gains a number of [temporary hit points](ref/rule/temporary-hit-points) equal
to his medium level for 1 minute. At 7th level, he selects two powers.

### Dark Power {#dark-power}

The fiend keeper gains a +1 profane bonus on attack and damage rolls, and a +1 profane bonus to AC.
At 13th level, these bonuses increase to +2.

### Fiendish Form {#fiendish-form}

The fiend keeper gains [darkvision](ref/rule/darkvision) 60 feet. At 7th level, he grows fiendish
wings and gains a fly speed equal to his base speed (average maneuverability). At 13th level, his
fly speed instead equals double his base speed (good maneuverability).

### Natural Attacks {#natural-attacks}

The fiend keeper gains two claw attacks and a bite attack. These are
[primary attacks](ref/umr/natural-attacks) that each deal 1d4 points of damage (1d6 if the fiend
keeper is Medium). At 13th level, the damage increases to 1d6 (1d8 if Medium).

### Spirit Power {#spirit-power}

The fiend keeper's spirit bonus increases by 1. At 13th level, the spirit bonus instead increases
by 2.

### Unholy Resilience {#unholy-resilience}

The fiend keeper gains [resistance](ref/umr/resistance) 5 to two of the following energy types:
acid, cold, electricity, fire, or sonic. The resistance increases to 10 at 7th level and 20 at 13th
level.

This ability replaces haunt channeler, location channel, connection channel, and ask the spirits.

## Ex-Fiend Keepers {#ex-fiend-keepers}

A fiend keeper who becomes permanently evil loses control of the spirit after 1d4+1 days, at which
point he becomes an NPC under the GM's full control. Seeking an _[atonement](ref/spell/atonement)_
spell before then can change the medium's alignment. This effect also can be undone with a
_[limited wish](ref/spell/limited-wish)_, _[miracle](ref/spell/miracle)_, or
_[wish](ref/spell/wish)_ spell.
