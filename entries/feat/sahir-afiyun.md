+++
id = "ref/feat/sahir-afiyun"
kind = "feat"
title = "Sahir-Afiyun"
aon = "FeatDisplay.aspx?ItemName=Sahir-Afiyun"
source_ids = ["black-markets", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sahir_afiyun", path = "json/feat13.json" },
]
[[sources]]
publication = "black-markets"
page = "18"
[[sources]]
publication = "dark-markets-a-guide-to-katapesh"
page = "56"

[fields]
kind = "feat"
prerequisites = "Spell Focus (any), ability to cast 2nd-level spells."
prerequisite_feats = ["ref/feat/spell-focus"]
benefit = "When you consume pesh, you take 1 fewer point of Constitution or Wisdom damage (your choice). In addition, you add spells below to your own class spell list or list of spells known. You can add one spell from the highest level you can cast; you can instead add two spells to your list of spells known, but both of these spells must be at least 1 level lower than the highest-level spell you can cast for that class. If you have more than one spellcasting class, choose one and add the sahir-afiyun spell or spells to that class's spell list or list of spells known."
special = "You can gain this feat multiple times. Its effects do not stack. Each time you take the feat, add one or more sahir-afiyun spells to your spell list."
+++

You have intertwined your familiarities with pesh and magic to unlock strange powers.\
**Prerequisites:** [Spell Focus](ref/feat/spell-focus) (any), ability to cast 2nd-level spells.\
**Benefit:** When you consume [pesh](ref/drug/pesh), you take 1 fewer point of Constitution or
Wisdom damage (your choice). In addition, you add spells below to your own class spell list or list
of spells known. You can add one spell from the highest level you can cast; you can instead add two
spells to your list of spells known, but both of these spells must be at least 1 level lower than
the highest-level spell you can cast for that class. If you have more than one spellcasting class,
choose one and add the sahir-afiyun spell or spells to that class's spell list or list of spells
known.

All sahir-afiyun spells require 1 dose of pesh as a material component, either replacing the
existing material component, or as part of the material component if the existing component costs
more.

|Spell|Level|School|Description|
| --- | --- | --- | --- |
|[Alleviate Addiction](ref/spell/alleviate-addiction)|1|conjuration (healing)|Ignore the effects of addictions.|
|[Confusion, Lesser](ref/spell/confusion-lesser)|1|enchantment (compulsion) \[mind-affecting\]|One creature is confused for 1 round.|
|[Night Blindness](ref/spell/night-blindness)|1|necromancy \[curse\]|Impair target's vision as if it were darker.|
|[Pesh Vigor](ref/spell/pesh-vigor)|1|transmutation|Increase target's strength with consumption of pesh.|
|[Ray of Sickening](ref/spell/ray-of-sickening)|1|necromancy|Ray makes subject sickened.|
|[Remove Fear](ref/spell/remove-fear)|1|abjuration|Suppresses fear or gives +4 on saves against fear for one subject + one per four levels.|
|[Sleep](ref/spell/sleep)|1|enchantment (compulsion) \[mind-affecting\]|Puts 4 HD of creatures into magical slumber.|
|[Augury](ref/spell/augury)|2|divination|Learns whether an action will be good or bad.|
|[Calm Emotions](ref/spell/calm-emotions)|2|enchantment (compulsion) \[emotion, mind-affecting\]|Calms creatures, negating emotion effects.|
|[Euphoric Cloud](ref/spell/euphoric-cloud)|2|conjuration (creation) \[poison\]|Fog obscures vision and fascinates living creatures.|
|Suffocation, Slow|2|necromancy \[death\]|Overdose someone with pesh, causing them to slowly suffocate.|
|[Contact High](ref/spell/contact-high)|3|transmutation|Duplicate a drug's effects on others.|
|[Deep Slumber](ref/spell/deep-slumber)|3|enchantment (compulsion) \[mind-affecting\]|Puts 10 HD of creatures to sleep.|
|[Imbue With Addiction](ref/spell/imbue-with-addiction)|3|transmutation|Target becomes addicted to a drug.|
|Pesh Addiction, Lesser|3|necromancy|Force someone to use pesh.|
|[Absorbing Inhalation](ref/spell/absorbing-inhalation)|4|transmutation \[air\]|Completely inhale a cloud-like effect, keeping it stored harmlessly in your body.|
|[Confusion](ref/spell/confusion)|4|enchantment (compulsion) \[mind-affecting\]|Subjects behave oddly for 1 round/level.|
|[Divination](ref/spell/divination)|4|divination|Provides useful advice for specific proposed actions.|
|Pesh Addiction|5|necromancy|As Pesh Addiction, Lesser except it has no HD limit and does not allow a saving throw.|
|Suffocation, Instant|5|necromancy \[death\]|Slay someone through pesh suffocation.|
|[Symbol of Sleep](ref/spell/symbol-of-sleep)|5|enchantment (compulsion) \[mind-affecting\]|Triggered rune puts nearby creatures into catatonic slumber.|

> ### Pesh Addiction
>
> **Sources:** Dark Markets - A Guide to Katapesh pg 57\
> **School** [necromancy](ref/spelldef/necromancy); **Level** sahir-afiyun 5\
> **Casting Time** 10 minutes\
> **Components** V, M (a dose of pesh)\
> **Range** close (25 ft. + 5 ft./2 levels)\
> **Target** one living creature\
> **Duration** 1 day/level or until discharged (D)\
> **Saving Throw** none; **Spell Resistance** yes
>
> This spell functions like [geas/quest](ref/spell/geas-quest), except the only allowed command is
> "use [pesh](ref/drug/pesh) or refined pesh."
>
> ### Pesh Addiction, Lesser
>
> **Sources:** Dark Markets - A Guide to Katapesh pg 57\
> **School** [necromancy](ref/spelldef/necromancy); **Level** sahir-afiyun 3\
> **Casting Time** 1 round\
> **Components** V, M (a dose of pesh whey)\
> **Range** close (25 ft. + 5 ft./2 levels)\
> **Target** one living creature with 7 HD or less\
> **Duration** 1 day/level or until discharged (D)\
> **Saving Throw** Will negates; **Spell Resistance** yes
>
> This spell functions like [lesser geas](ref/spell/geas-lesser), except the only allowed command is
> "use [pesh](ref/drug/pesh) or refined pesh."
>
> ### Suffocation, Instant
>
> **Sources:** Dark Markets - A Guide to Katapesh pg 57\
> **School** [necromancy](ref/spelldef/necromancy) \[[death](ref/spelldef/death)\]; **Level**
> sahir-afiyun 5\
> **Casting Time** 1 standard action\
> **Components** V, S\
> **Range** touch\
> **Target** living creature touched\
> **Duration** instantaneous\
> **Saving Throw** Fortitude partial; **Spell Resistance** yes
>
> This spell functions like [slay living](ref/spell/slay-living), and kills by immediate
> suffocation. Creatures that do not need to breathe are immune to this spell. The target is
> considered to have taken a dose of [pesh](ref/drug/pesh) for the purpose of addiction and
> withdrawal effects.
>
> ### Suffocation, Slow
>
> **Sources:** Dark Markets - A Guide to Katapesh pg 57\
> **School** [necromancy](ref/spelldef/necromancy) \[[death](ref/spelldef/death)\]; **Level**
> sahir-afiyun 2\
> **Casting Time** 1 standard action\
> **Components** V, S\
> **Range** touch\
> **Target** living creature touched\
> **Duration** 1 minute/level\
> **Saving Throw** Fortitude negates; **Spell Resistance** yes
>
> The target is unable to breathe and is treated as if she is holding her breath (see the
> [rules for suffocation](ref/rule/suffocation)). Strong stimulants, effects that increase the
> target's Constitution, or physical trauma (such as taking 10 or more points of damage from a
> single attack) negate the spell immediately. Creatures that do not need to breathe are immune to
> this spell. The target is considered to have taken a dose of [pesh](ref/drug/pesh) for the purpose
> of addiction and withdrawal effects. Canny sahir use this spell to subtly kill enemies, as the
> spell mimics a pesh overdose.

**Special:** You can gain this feat multiple times. Its effects do not stack. Each time you take the
feat, add one or more sahir-afiyun spells to your spell list.
