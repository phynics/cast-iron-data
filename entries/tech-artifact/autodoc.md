+++
id = "ref/tech-artifact/autodoc"
kind = "item"
title = "Autodoc"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "autodoc", path = "json/equipment_tech_artifacts.json" },
]

[fields]
kind = "item"
weight = "1,200 lbs."
slot = "none"
+++

**Sources:** Technology Guide pg 60\
**Slot** none; **Weight** 1,200 lbs.\
**Capacity** 120; **Usage** see text

An autodoc is a large, cumbersome device that consists of a comfortable, plastic-framed reclining
chair inside a transparent pod, within which is affixed a dizzying array of multi-jointed arms and
extendable devices. An equally dizzying assortment of buttons, lights, and touch-sensitive screens
adorn the device, both on the inside and outside of the pod.

An autodoc can heal wounds, set broken bones, cure disease, treat burns, implant cybertech, remove
poison, and more. An autodoc can be programmed to perform any number of surgical procedures upon the
person lying within the pod - the dozens of arms and devices work with precision and great speed.
The operator need only enter in the proper diagnosis or desired operation on the screens at the foot
of the bed with a successful [Heal](ref/skill/heal) check; this requires the
[Technologist](ref/feat/technologist) feat to attempt. The DC is based on the operation, detailed
below. An autodoc will not activate until it has been properly programmed. Programming an operation
takes 2d6 rounds of work. An autodoc has some capacity to error-check and auto-complete the correct
programming for an operation before undertaking it by running instantaneous simulations on one of
its many screens, granting the user a +5 circumstance bonus on these Heal checks.

An autodoc consumes 1 charge per hour while idle (including time needed to program an operation),
and 1 charge per round while operating. As an autodoc can only hold a maximum of 120 charges at a
time, for lengthy operations it must be recharged during use or be attached to a standing power
supply such as a [generator or reactor](ref/rule/tech-artifacts). While functioning, an autodoc is
closed tight - a successful DC 25 Strength check is required to wrench the door open. A patient who
leaves or is forcibly removed from an autodoc before an operation finishes (or who is being operated
on when the autodoc runs out of charges) must succeed a DC 15 Reflex save or take 3d6+10 points of
damage from the cutting lasers, surgical tools, and needles moving at high speed. Needless to say,
exiting the autodoc before an operation completes negates any of the benefits that would have been
otherwise granted by the device.

The various operations an autodoc can perform are as follows; additional operations can be devised
as needed.

- **Minor Surgery (DC 15):** The patient heals 1d8+1 points of damage. _Operation Time:_ 1 minute.
- **Moderate Surgery (DC 20):** The patient heals 2d8+3 points of damage and 1d4+1 points of ability
  damage to a selected ability score. _Operation Time:_ 2 minutes.
- **Major Surgery (DC 25):** The patient heals 3d8+5 points of damage and is cured of blindness and
  deafness. _Operation Time:_ 3 minutes.
- **Critical Surgery (DC 30):** The patient heals 4d8+7 points of damage and either all ability
  damage to all ability scores or all ability drain to one ability score. _Operation Time:_ 4
  minutes.
- **Back from the Brink (DC 35):** A dead patient whose body is relatively intact is restored to
  life at 1 hit point per Hit Die, as if by [raise dead](ref/spell/raise-dead) (including time
  restrictions and negative levels). _Operation Time:_ 1 hour.
- **Total Molecular Reconstruction (DC 45):** As long as at least a small amount of a patient's DNA
  is available, an autodoc can reconstruct a patient's body completely. At the end of the
  reconstruction process, the new body is considered to be a blank clone of the patient, and until
  the patient's memories and personality are implanted into the clone via a
  [neurocam](ref/tech-misc/neurocam), the body remains alive but inert. _Operation Time:_ 24 hours.
- **Install Cybertech (DC = the cybertech install DC):** Cybernetic equipment is installed safely.
  _Operation Time:_ 10 minutes per point of implantation of the cybertech being installed.
- **Treat Toxin (DC = 10 + the save DC of disease or poison):** The patient has one disease or
  poison currently afflicting him removed. _Operation Time:_ 10 minutes.
